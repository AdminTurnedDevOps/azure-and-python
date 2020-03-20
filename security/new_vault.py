from azure.common.client_factory import get_client_from_cli_profile as azprofile
from azure.cli.core import get_default_cli as azcli
from azure.mgmt.keyvault import KeyVaultManagementClient
import sys
import time
import logging

print('Listing all Azure accounts below...')
azcli().invoke(['account', 'list'])


def new_vault(resource_group_name, vault_name, location):
    try:
        keyvault = azprofile(KeyVaultManagementClient)
    except Exception as e:
        logging.error(
            msg='Please check the default Azure profile as access to keyvault')
        print(e)

    print('Pick an object ID and tenant id from the output above...')
    time.sleep(4)

    tenant = input('Please enter the tenant ID: ')
    subscription = input('Please enter the subscription ID: ')
    try:
        keyvault.vaults.create_or_update(
            resource_group_name,
            vault_name,
            {
                'location': location,
                'properties': {
                    'sku': {
                        'name': 'standard'
                    },
                    'tenant_id': tenant,
                    'access_policies': [{
                        'object_id': subscription,
                        'tenant_id': tenant,
                        'permissions': {
                            'keys': ['all'],
                            'secrets': ['all']
                        }
                    }]
                }
            }
        )
    except Exception as d:
        logging.error(msg=f'The KeyVault {vault_name} was not created')
        print(d)


resource_group_name = sys.argv[1]
vault_name = sys.argv[2]
location = sys.argv[3]

if __name__ == '__main__':
    new_vault(resource_group_name, vault_name, location)
    print(f'{vault_name}: Created')
