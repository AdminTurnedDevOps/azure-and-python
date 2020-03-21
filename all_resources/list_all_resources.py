from azure.mgmt.resource import ResourceManagementClient
from azure.common.client_factory import get_client_from_cli_profile as azprofile
import sys
import logging

resources = azprofile(ResourceManagementClient)


def list_all_resources(resource_group_name):
    all_resources = resources.resources.list_by_resource_group(
        resource_group_name)

    try:
        for resource in all_resources:
            print(
                "ID: {} \nName: {} \nType: {} \n".format(
                    resource.id, resource.name, resource.type)
            )

    except Exception as e:
        logging.error(msg='Please confirm the default Azure profile has access to the resources in resource group {resource_group_name}')
        print(e)


resource_group_name = sys.argv[1]

if __name__ == '__main__':
    print(f'Listing Resources in: {resource_group_name}')
    list_all_resources(resource_group_name)
