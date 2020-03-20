from azure.common.client_factory import get_client_from_cli_profile as azprofile
from azure.cli.core import get_default_cli as azcli
from azure.mgmt.keyvault import KeyVaultManagementClient
import sys
import time

print('Listing all Azure accounts below...')
azcli().invoke(['account', 'list'])


def new_vault(resource_group_name, vault_name, location):
    keyvault = azprofile(KeyVaultManagementClient)

    print('Pick an object ID and tenant id from the output above...')
    time.sleep(4)

    keyvault.vaults.create_or_update(
        resource_group_name,
        vault_name,
        {
            'location': location,
            'properties': {
                'sku': {
                    'name': 'standard'
                }
            },
            'access_policies': [{
                'object_id': input(str('Input subscription ID: ')),
                'tenant_id': input(str('Input tenant ID: ')),
                'permissions': {
                    'keys': ['all'],
                    'secrets': ['all']
                }
            }]
        }
    )


resource_group_name = sys.argv[1]
vault_name = sys.argv[2]
location = sys.argv[3]

new_vault(resource_group_name, vault_name, location)