from azure.mgmt.resource import ResourceManagementClient
from azure.common.client_factory import get_client_from_cli_profile as azprofile

resources = azprofile(ResourceManagementClient)

list_resources = resources.resource_groups.list()

for i in list_resources:
    print(
        "Name: {} \nLocation: {}".format(i.name, i.location)
    )