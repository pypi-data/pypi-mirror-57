# mypy-boto3-ram

Mypy-friendly auto-generated type annotations for `boto3 ram 1.10.40` service.
More information can be found [here](https://github.com/vemel/mypy_boto3).

- [mypy-boto3-ram](#mypy-boto3-ram)
  - [How to use](#how-to-use)
    - [Type checking](#type-checking)
    - [Code auto-complete](#code-auto-complete)
  - [How it works](#how-it-works)

## How to use

### Type checking

Make sure you have [mypy](https://github.com/python/mypy) installed and activated in your IDE.

Install `boto3-stubs` for `ram` service.

```bash
python -m pip install boto3-stubs[mypy-boto3-ram]
```

Use `boto3` with `mypy_boto3` in your project and enjoy type checking.

```python
import boto3

from mypy_boto3 import ram
# alternative import if you do not want to install mypy_boto3 package
# import mypy_boto3_ram as ram

# Use this client as usual, now mypy can check if your code is valid.
# Check if your IDE supports function overloads,
# you probably do not need explicit type annotations
# client = boto3.client("ram")
client: ram.RAMClient = boto3.client("ram")

# works for session as well
session = boto3.session.Session(region="us-west-1")
session_client: ram.RAMClient = session.client("ram")


# Paginators need type annotation on creation
get_resource_policies_paginator: ram.GetResourcePoliciesPaginator = client.get_paginator("get_resource_policies")
get_resource_share_associations_paginator: ram.GetResourceShareAssociationsPaginator = client.get_paginator("get_resource_share_associations")
get_resource_share_invitations_paginator: ram.GetResourceShareInvitationsPaginator = client.get_paginator("get_resource_share_invitations")
get_resource_shares_paginator: ram.GetResourceSharesPaginator = client.get_paginator("get_resource_shares")
list_principals_paginator: ram.ListPrincipalsPaginator = client.get_paginator("list_principals")
list_resources_paginator: ram.ListResourcesPaginator = client.get_paginator("list_resources")
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