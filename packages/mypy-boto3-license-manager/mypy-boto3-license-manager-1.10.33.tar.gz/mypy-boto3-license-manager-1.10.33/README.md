# mypy-boto3-license-manager

Mypy-friendly auto-generated type annotations for `boto3 license-manager 1.10.33` service.
More information can be found [here](https://github.com/vemel/mypy_boto3).

- [mypy-boto3-license-manager](#mypy-boto3-license-manager)
  - [How to use](#how-to-use)
    - [Type checking](#type-checking)
    - [Code auto-complete](#code-auto-complete)
  - [How it works](#how-it-works)

## How to use

### Type checking

Make sure you have [mypy](https://github.com/python/mypy) installed and activated in your IDE.

Install `boto3-stubs` for `license-manager` service.

```bash
pip install boto3-stubs[mypy-boto3-license-manager]
```

Use `boto3` with `mypy_boto3` in your project and enjoy type checking.

```python
import boto3

from mypy_boto3 import license_manager
# alternative import if you do not want to install mypy_boto3 package
# import mypy_boto3_license_manager as license_manager

# Use this client as usual, now mypy can check if your code is valid.
client: license_manager.Client = boto3.client("license-manager")

# works for session as well
session = boto3.session.Session(region="us-west-1")
session_client: license_manager.Client = session.client("license-manager")


# Paginators need type annotation on creation
list_associations_for_license_configuration_paginator: license_manager.ListAssociationsForLicenseConfigurationPaginator = client.get_paginator("list_associations_for_license_configuration")
list_license_configurations_paginator: license_manager.ListLicenseConfigurationsPaginator = client.get_paginator("list_license_configurations")
list_license_specifications_for_resource_paginator: license_manager.ListLicenseSpecificationsForResourcePaginator = client.get_paginator("list_license_specifications_for_resource")
list_resource_inventory_paginator: license_manager.ListResourceInventoryPaginator = client.get_paginator("list_resource_inventory")
list_usage_for_license_configuration_paginator: license_manager.ListUsageForLicenseConfigurationPaginator = client.get_paginator("list_usage_for_license_configuration")
```

## How it works

Fully automated [builder](https://github.com/vemel/mypy_boto3) carefully generates
type annotations for each service, patiently waiting for `boto3` updates. It delivers
a drop-in type annotations for you and makes sure that:

- Latest version of `boto3` is used.
- Each public class and method of every `boto3` service gets valid type annotations
  extracted from latest documentation (blame `botocore` docs if types are incorrect).
- Type annotations include up-to-date documentation.
- Code is processed by [black](https://github.com/psf/black) for readability.

## Submodules

- `master` - Install `mypy-boto3` package.