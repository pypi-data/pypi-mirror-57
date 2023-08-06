# mypy-boto3-storagegateway

Mypy-friendly auto-generated type annotations for `boto3 storagegateway 1.10.33` service.
More information can be found [here](https://github.com/vemel/mypy_boto3).

- [mypy-boto3-storagegateway](#mypy-boto3-storagegateway)
  - [How to use](#how-to-use)
    - [Type checking](#type-checking)
    - [Code auto-complete](#code-auto-complete)
  - [How it works](#how-it-works)

## How to use

### Type checking

Make sure you have [mypy](https://github.com/python/mypy) installed and activated in your IDE.

Install `boto3-stubs` for `storagegateway` service.

```bash
pip install boto3-stubs[mypy-boto3-storagegateway]
```

Use `boto3` with `mypy_boto3` in your project and enjoy type checking.

```python
import boto3

from mypy_boto3 import storagegateway
# alternative import if you do not want to install mypy_boto3 package
# import mypy_boto3_storagegateway as storagegateway

# Use this client as usual, now mypy can check if your code is valid.
client: storagegateway.Client = boto3.client("storagegateway")

# works for session as well
session = boto3.session.Session(region="us-west-1")
session_client: storagegateway.Client = session.client("storagegateway")


# Paginators need type annotation on creation
describe_tape_archives_paginator: storagegateway.DescribeTapeArchivesPaginator = client.get_paginator("describe_tape_archives")
describe_tape_recovery_points_paginator: storagegateway.DescribeTapeRecoveryPointsPaginator = client.get_paginator("describe_tape_recovery_points")
describe_tapes_paginator: storagegateway.DescribeTapesPaginator = client.get_paginator("describe_tapes")
describe_vtl_devices_paginator: storagegateway.DescribeVTLDevicesPaginator = client.get_paginator("describe_vtl_devices")
list_file_shares_paginator: storagegateway.ListFileSharesPaginator = client.get_paginator("list_file_shares")
list_gateways_paginator: storagegateway.ListGatewaysPaginator = client.get_paginator("list_gateways")
list_tags_for_resource_paginator: storagegateway.ListTagsForResourcePaginator = client.get_paginator("list_tags_for_resource")
list_tapes_paginator: storagegateway.ListTapesPaginator = client.get_paginator("list_tapes")
list_volumes_paginator: storagegateway.ListVolumesPaginator = client.get_paginator("list_volumes")
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