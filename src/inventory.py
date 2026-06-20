from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.compute import ComputeManagementClient


def get_resource_groups(credential, subscription_id):
    client = ResourceManagementClient(
        credential,
        subscription_id
    )

    resource_groups = []

    for rg in client.resource_groups.list():
        resource_groups.append({
            "name": rg.name,
            "location": rg.location
        })

    return resource_groups


def get_virtual_machines(credential, subscription_id):
    client = ComputeManagementClient(
        credential,
        subscription_id
    )

    virtual_machines = []

    for vm in client.virtual_machines.list_all():
        virtual_machines.append({
            "name": vm.name,
            "location": vm.location
        })

    return virtual_machines