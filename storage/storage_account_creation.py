from azure.common.client_factory import get_client_from_cli_profile
from azure.mgmt.storage import StorageManagementClient
import logging
import sys

try:
    storage_client = get_client_from_cli_profile(StorageManagementClient)
except Exception as e:
    logging.error(msg='Check to ensure your existing Azure CLI profile exists...')
    print(e)

def storage_account_name_check(name):
    print(f'Checking to see if {name} is an allowed storage account name')
    avail = storage_client.storage_accounts.check_name_availability(name)
    print(avail)

name = sys.argv[1]

storage_account_name_check(name)