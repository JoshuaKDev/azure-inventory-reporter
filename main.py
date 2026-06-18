import os

from src.auth import get_credential
from src.inventory import get_resource_groups


SUBSCRIPTION_ID = "YOUR_SUBSCRIPTION_ID"


def main():
    credential = get_credential()

    resource_groups = get_resource_groups(
        credential,
        SUBSCRIPTION_ID
    )

    print("\nResource Groups\n")

    for rg in resource_groups:
        print(
            f"{rg['name']} ({rg['location']})"
        )


if __name__ == "__main__":
    main()