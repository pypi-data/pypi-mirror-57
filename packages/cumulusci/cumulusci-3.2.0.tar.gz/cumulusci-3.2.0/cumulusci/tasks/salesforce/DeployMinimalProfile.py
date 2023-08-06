import os
import xml.etree.ElementTree as ET

from cumulusci.tasks.salesforce import BaseSalesforceApiTask
from cumulusci.tasks.salesforce import Deploy
from cumulusci.tasks.metadata.package import PackageXmlGenerator
from cumulusci.tasks.salesforce.sourcetracking import MetadataType
from cumulusci.utils import elementtree_parse_file
from cumulusci.utils import temporary_dir

OBJECT_PERMS = """<objectPermissions xmlns="http://soap.sforce.com/2006/04/metadata">
    <object>{}</object>
    <allowCreate>false</allowCreate>
    <allowDelete>false</allowDelete>
    <allowEdit>false</allowEdit>
    <allowRead>false</allowRead>
</objectPermissions>"""

USER_PERMS = """<userPermissions xmlns="http://soap.sforce.com/2006/04/metadata">
    <name>{}</name>
    <enabled>false</enabled>
</userPermissions>
"""

APP_VISIBILITIES = """<applicationVisibilities xmlns="http://soap.sforce.com/2006/04/metadata">
    <application>{}</application>
    <default>false</default>
    <visible>false</visible>
</applicationVisibilities>
"""

TAB_VISIBILITIES = """<tabVisibilities xmlns="http://soap.sforce.com/2006/04/metadata">
    <tab>{}</tab>
    <visibility>Hidden</visibility>
</tabVisibilities>
"""


def namespaced_name(entity):
    return (
        f"{entity['NamespacePrefix']}__{entity['DeveloperName']}"
        if entity["NamespacePrefix"]
        else entity["DeveloperName"]
    )


class DeployMinimalProfile(Deploy, BaseSalesforceApiTask):

    namespaces = {"sf": "http://soap.sforce.com/2006/04/metadata"}

    def _get_api(self):
        # Read the profile
        profile_path = self.options["path"]
        profile_filename = os.path.basename(profile_path)
        profile_name, _ = os.path.splitext(profile_filename)
        tree = elementtree_parse_file(profile_path)
        root = tree.getroot()

        # Disable missing object CRUD permissions
        # We use the intersection of:
        # - objects from the SobjectType picklist on ObjectPermissions
        # - objects with the IsEverCreatable flag on EntityDefinition
        objpset_describe = self.sf.ObjectPermissions.describe()
        sobject_type_field = [
            f for f in objpset_describe["fields"] if f["name"] == "SobjectType"
        ][0]
        permissionable_sobjects = set(
            p["value"] for p in sobject_type_field["picklistValues"]
        )
        creatable_sobjects = [
            namespaced_name(entity)
            for entity in self.tooling.query(
                "SELECT DeveloperName, NamespacePrefix, IsEverCreatable FROM EntityDefinition"
            )["records"]
            if entity["IsEverCreatable"]
        ]
        crud_sobjects = permissionable_sobjects.intersection(creatable_sobjects)
        for sobject in crud_sobjects:
            if not tree.findall(
                f".//sf:objectPermissions[sf:name='{sobject}']", self.namespaces
            ):
                root.append(ET.fromstring(OBJECT_PERMS.format(sobject)))

        # XXX Disable FLS

        # Disable missing user permissions
        pset_describe = self.sf.PermissionSet.describe()
        for field in pset_describe["fields"]:
            if not field["name"].startswith("Permissions"):
                continue
            permission_name = field["name"][len("Permissions") :]
            # Skip permissions that can't be disabled for profiles using the default license type
            if permission_name in (
                "ActivitiesAccess",
                "AllowViewKnowledge",
                "ChatterInternalUser",
                "LightningConsoleAllowedForUser",
                "ViewHelpLink",
            ):
                continue
            if not tree.findall(
                f".//sf:userPermissions[sf:name='{permission_name}']", self.namespaces
            ):
                root.append(ET.fromstring(USER_PERMS.format(permission_name)))

        # Disable missing apps
        for app in self.tooling.query(
            "SELECT DeveloperName, NamespacePrefix FROM CustomApplication"
        )["records"]:
            name = namespaced_name(app)
            if name == "standard__Sales":
                # xxx hack to avoid removing default app for now
                continue
            if not tree.findall(
                f".//sf:applicationVisibilities[sf:name='{name}']", self.namespaces
            ):
                root.append(ET.fromstring(APP_VISIBILITIES.format(name)))
        # xxx why is Work.com app missing?

        # Disable missing tabs
        tabs = set(
            tab["Name"]
            for tab in self.tooling.query("SELECT Name FROM TabDefinition")["records"]
        )
        for tab in tabs:
            if not tree.findall(
                f".//sf:tabVisibilities[sf:name='{tab}']", self.namespaces
            ):
                root.append(ET.fromstring(TAB_VISIBILITIES.format(tab)))

        # Construct a metadata package with the modified profile
        with temporary_dir() as path:
            os.mkdir("profiles")
            tree.write(
                os.path.join(path, "profiles", profile_filename),
                "utf-8",
                xml_declaration=True,
                default_namespace=self.namespaces["sf"],
            )
            # with open(os.path.join(path, "profiles", profile_filename), "r") as f:
            #     print(f.read())
            package_xml = PackageXmlGenerator(
                path,
                self.project_config.project__package__api_version,
                types=[MetadataType("Profile", [profile_name])],
            )()
            with open("package.xml", "w") as f:
                f.write(package_xml)

            package_zip = self._get_package_zip(path)
            self.logger.info(f"Deploying {profile_path} minimally")
            return self.api_class(self, package_zip, purge_on_delete=False)
