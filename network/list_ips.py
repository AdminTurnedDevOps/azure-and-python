from azure.mgmt.network import NetworkManagementClient
from azure.common.client_factory import get_client_from_cli_profile as azcliprofile

network_client = azcliprofile(NetworkManagementClient)
pubips = network_client.public_ip_addresses

ips = pubips.list_all()
for ip in ips:
    print(
        "Name: {} \nMethod: {} \nIPAddress: {}".format(ip.name, ip.public_ip_allocation_method, ip.ip_address)
    )