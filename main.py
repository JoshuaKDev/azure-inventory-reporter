import os

from src.auth import get_credential
from src.inventory import get_resource_groups, get_virtual_machines
from src.exporters import export_to_json, export_vms_to_csv


SUBSCRIPTION_ID = ""


def main():
    credential = get_credential()

    resource_groups = get_resource_groups(
        credential,
        SUBSCRIPTION_ID
    )

    virtual_machines = get_virtual_machines(
        credential,
        SUBSCRIPTION_ID
    )

    inventory = {
        "resource_groups": resource_groups,
        "virtual_machines": virtual_machines
    }

    export_to_json(
        inventory,
        "output/inventory.json"
    )

    export_vms_to_csv(
        virtual_machines,
        "output/virtual_machines.csv"
    )

    print("\nResource Groups\n")

    for rg in resource_groups:
        print(
            f"{rg['name']} ({rg['location']})"
        )

    print("\nVirtual Machines\n")

    for vm in virtual_machines:
        print(vm)

    print("\nReports Generated\n")
    print("JSON: output/inventory.json")
    print("CSV: output/virtual_machines.csv")


if __name__ == "__main__":
    main()