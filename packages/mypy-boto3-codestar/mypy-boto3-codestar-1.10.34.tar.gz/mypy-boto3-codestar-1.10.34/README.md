# mypy-boto3-codestar

Mypy-friendly auto-generated type annotations for `boto3 codestar 1.10.34` service.
More information can be found [here](https://github.com/vemel/mypy_boto3).

- [mypy-boto3-codestar](#mypy-boto3-codestar)
  - [How to use](#how-to-use)
    - [Type checking](#type-checking)
    - [Code auto-complete](#code-auto-complete)
  - [How it works](#how-it-works)

## How to use

### Type checking

Make sure you have [mypy](https://github.com/python/mypy) installed and activated in your IDE.

Install `boto3-stubs` for `codestar` service.

```bash
pip install boto3-stubs[mypy-boto3-codestar]
```

Use `boto3` with `mypy_boto3` in your project and enjoy type checking.

```python
import boto3

from mypy_boto3 import codestar
# alternative import if you do not want to install mypy_boto3 package
# import mypy_boto3_codestar as codestar

# Use this client as usual, now mypy can check if your code is valid.
client: codestar.Client = boto3.client("codestar")

# works for session as well
session = boto3.session.Session(region="us-west-1")
session_client: codestar.Client = session.client("codestar")


# Paginators need type annotation on creation
list_projects_paginator: codestar.ListProjectsPaginator = client.get_paginator("list_projects")
list_resources_paginator: codestar.ListResourcesPaginator = client.get_paginator("list_resources")
list_team_members_paginator: codestar.ListTeamMembersPaginator = client.get_paginator("list_team_members")
list_user_profiles_paginator: codestar.ListUserProfilesPaginator = client.get_paginator("list_user_profiles")
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