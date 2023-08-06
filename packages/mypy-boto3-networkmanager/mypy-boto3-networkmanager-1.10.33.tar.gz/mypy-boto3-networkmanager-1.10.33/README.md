# mypy-boto3-networkmanager

Mypy-friendly auto-generated type annotations for `boto3 networkmanager 1.10.33` service.
More information can be found [here](https://github.com/vemel/mypy_boto3).

- [mypy-boto3-networkmanager](#mypy-boto3-networkmanager)
  - [How to use](#how-to-use)
    - [Type checking](#type-checking)
    - [Code auto-complete](#code-auto-complete)
  - [How it works](#how-it-works)

## How to use

### Type checking

Make sure you have [mypy](https://github.com/python/mypy) installed and activated in your IDE.

Install `boto3-stubs` for `networkmanager` service.

```bash
pip install boto3-stubs[mypy-boto3-networkmanager]
```

Use `boto3` with `mypy_boto3` in your project and enjoy type checking.

```python
import boto3

from mypy_boto3 import networkmanager
# alternative import if you do not want to install mypy_boto3 package
# import mypy_boto3_networkmanager as networkmanager

# Use this client as usual, now mypy can check if your code is valid.
client: networkmanager.Client = boto3.client("networkmanager")

# works for session as well
session = boto3.session.Session(region="us-west-1")
session_client: networkmanager.Client = session.client("networkmanager")


# Paginators need type annotation on creation
describe_global_networks_paginator: networkmanager.DescribeGlobalNetworksPaginator = client.get_paginator("describe_global_networks")
get_customer_gateway_associations_paginator: networkmanager.GetCustomerGatewayAssociationsPaginator = client.get_paginator("get_customer_gateway_associations")
get_devices_paginator: networkmanager.GetDevicesPaginator = client.get_paginator("get_devices")
get_link_associations_paginator: networkmanager.GetLinkAssociationsPaginator = client.get_paginator("get_link_associations")
get_links_paginator: networkmanager.GetLinksPaginator = client.get_paginator("get_links")
get_sites_paginator: networkmanager.GetSitesPaginator = client.get_paginator("get_sites")
get_transit_gateway_registrations_paginator: networkmanager.GetTransitGatewayRegistrationsPaginator = client.get_paginator("get_transit_gateway_registrations")
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