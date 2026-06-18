from azure.mgmt.resource import ResourceManagementClient


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