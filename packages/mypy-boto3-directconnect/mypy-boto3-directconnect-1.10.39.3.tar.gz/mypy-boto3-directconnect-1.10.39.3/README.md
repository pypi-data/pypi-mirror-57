# mypy-boto3-directconnect

Mypy-friendly auto-generated type annotations for `boto3 directconnect 1.10.39` service.
More information can be found [here](https://github.com/vemel/mypy_boto3).

- [mypy-boto3-directconnect](#mypy-boto3-directconnect)
  - [How to use](#how-to-use)
    - [Type checking](#type-checking)
    - [Code auto-complete](#code-auto-complete)
  - [How it works](#how-it-works)

## How to use

### Type checking

Make sure you have [mypy](https://github.com/python/mypy) installed and activated in your IDE.

Install `boto3-stubs` for `directconnect` service.

```bash
python -m pip install boto3-stubs[mypy-boto3-directconnect]
```

Use `boto3` with `mypy_boto3` in your project and enjoy type checking.

```python
import boto3

from mypy_boto3 import directconnect
# alternative import if you do not want to install mypy_boto3 package
# import mypy_boto3_directconnect as directconnect

# Use this client as usual, now mypy can check if your code is valid.
# Check if your IDE supports function overloads,
# you probably do not need explicit type annotations
# client = boto3.client("directconnect")
client: directconnect.DirectConnectClient = boto3.client("directconnect")

# works for session as well
session = boto3.session.Session(region="us-west-1")
session_client: directconnect.DirectConnectClient = session.client("directconnect")


# Paginators need type annotation on creation
describe_direct_connect_gateway_associations_paginator: directconnect.DescribeDirectConnectGatewayAssociationsPaginator = client.get_paginator("describe_direct_connect_gateway_associations")
describe_direct_connect_gateway_attachments_paginator: directconnect.DescribeDirectConnectGatewayAttachmentsPaginator = client.get_paginator("describe_direct_connect_gateway_attachments")
describe_direct_connect_gateways_paginator: directconnect.DescribeDirectConnectGatewaysPaginator = client.get_paginator("describe_direct_connect_gateways")
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