# mypy-boto3-workmail

Mypy-friendly auto-generated type annotations for `boto3 workmail 1.10.33` service.
More information can be found [here](https://github.com/vemel/mypy_boto3).

- [mypy-boto3-workmail](#mypy-boto3-workmail)
  - [How to use](#how-to-use)
    - [Type checking](#type-checking)
    - [Code auto-complete](#code-auto-complete)
  - [How it works](#how-it-works)

## How to use

### Type checking

Make sure you have [mypy](https://github.com/python/mypy) installed and activated in your IDE.

Install `boto3-stubs` for `workmail` service.

```bash
pip install boto3-stubs[mypy-boto3-workmail]
```

Use `boto3` with `mypy_boto3` in your project and enjoy type checking.

```python
import boto3

from mypy_boto3 import workmail
# alternative import if you do not want to install mypy_boto3 package
# import mypy_boto3_workmail as workmail

# Use this client as usual, now mypy can check if your code is valid.
client: workmail.Client = boto3.client("workmail")

# works for session as well
session = boto3.session.Session(region="us-west-1")
session_client: workmail.Client = session.client("workmail")


# Paginators need type annotation on creation
list_aliases_paginator: workmail.ListAliasesPaginator = client.get_paginator("list_aliases")
list_group_members_paginator: workmail.ListGroupMembersPaginator = client.get_paginator("list_group_members")
list_groups_paginator: workmail.ListGroupsPaginator = client.get_paginator("list_groups")
list_mailbox_permissions_paginator: workmail.ListMailboxPermissionsPaginator = client.get_paginator("list_mailbox_permissions")
list_organizations_paginator: workmail.ListOrganizationsPaginator = client.get_paginator("list_organizations")
list_resource_delegates_paginator: workmail.ListResourceDelegatesPaginator = client.get_paginator("list_resource_delegates")
list_resources_paginator: workmail.ListResourcesPaginator = client.get_paginator("list_resources")
list_users_paginator: workmail.ListUsersPaginator = client.get_paginator("list_users")
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