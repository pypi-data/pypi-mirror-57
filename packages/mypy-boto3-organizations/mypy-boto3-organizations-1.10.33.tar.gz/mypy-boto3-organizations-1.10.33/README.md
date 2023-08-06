# mypy-boto3-organizations

Mypy-friendly auto-generated type annotations for `boto3 organizations 1.10.33` service.
More information can be found [here](https://github.com/vemel/mypy_boto3).

- [mypy-boto3-organizations](#mypy-boto3-organizations)
  - [How to use](#how-to-use)
    - [Type checking](#type-checking)
    - [Code auto-complete](#code-auto-complete)
  - [How it works](#how-it-works)

## How to use

### Type checking

Make sure you have [mypy](https://github.com/python/mypy) installed and activated in your IDE.

Install `boto3-stubs` for `organizations` service.

```bash
pip install boto3-stubs[mypy-boto3-organizations]
```

Use `boto3` with `mypy_boto3` in your project and enjoy type checking.

```python
import boto3

from mypy_boto3 import organizations
# alternative import if you do not want to install mypy_boto3 package
# import mypy_boto3_organizations as organizations

# Use this client as usual, now mypy can check if your code is valid.
client: organizations.Client = boto3.client("organizations")

# works for session as well
session = boto3.session.Session(region="us-west-1")
session_client: organizations.Client = session.client("organizations")


# Paginators need type annotation on creation
list_aws_service_access_for_organization_paginator: organizations.ListAWSServiceAccessForOrganizationPaginator = client.get_paginator("list_aws_service_access_for_organization")
list_accounts_paginator: organizations.ListAccountsPaginator = client.get_paginator("list_accounts")
list_accounts_for_parent_paginator: organizations.ListAccountsForParentPaginator = client.get_paginator("list_accounts_for_parent")
list_children_paginator: organizations.ListChildrenPaginator = client.get_paginator("list_children")
list_create_account_status_paginator: organizations.ListCreateAccountStatusPaginator = client.get_paginator("list_create_account_status")
list_handshakes_for_account_paginator: organizations.ListHandshakesForAccountPaginator = client.get_paginator("list_handshakes_for_account")
list_handshakes_for_organization_paginator: organizations.ListHandshakesForOrganizationPaginator = client.get_paginator("list_handshakes_for_organization")
list_organizational_units_for_parent_paginator: organizations.ListOrganizationalUnitsForParentPaginator = client.get_paginator("list_organizational_units_for_parent")
list_parents_paginator: organizations.ListParentsPaginator = client.get_paginator("list_parents")
list_policies_paginator: organizations.ListPoliciesPaginator = client.get_paginator("list_policies")
list_policies_for_target_paginator: organizations.ListPoliciesForTargetPaginator = client.get_paginator("list_policies_for_target")
list_roots_paginator: organizations.ListRootsPaginator = client.get_paginator("list_roots")
list_tags_for_resource_paginator: organizations.ListTagsForResourcePaginator = client.get_paginator("list_tags_for_resource")
list_targets_for_policy_paginator: organizations.ListTargetsForPolicyPaginator = client.get_paginator("list_targets_for_policy")
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