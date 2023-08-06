# mypy-boto3-iot1click-projects

Mypy-friendly auto-generated type annotations for `boto3 iot1click-projects 1.10.33` service.
More information can be found [here](https://github.com/vemel/mypy_boto3).

- [mypy-boto3-iot1click-projects](#mypy-boto3-iot1click-projects)
  - [How to use](#how-to-use)
    - [Type checking](#type-checking)
    - [Code auto-complete](#code-auto-complete)
  - [How it works](#how-it-works)

## How to use

### Type checking

Make sure you have [mypy](https://github.com/python/mypy) installed and activated in your IDE.

Install `boto3-stubs` for `iot1click-projects` service.

```bash
pip install boto3-stubs[mypy-boto3-iot1click-projects]
```

Use `boto3` with `mypy_boto3` in your project and enjoy type checking.

```python
import boto3

from mypy_boto3 import iot1click_projects
# alternative import if you do not want to install mypy_boto3 package
# import mypy_boto3_iot1click_projects as iot1click_projects

# Use this client as usual, now mypy can check if your code is valid.
client: iot1click_projects.Client = boto3.client("iot1click-projects")

# works for session as well
session = boto3.session.Session(region="us-west-1")
session_client: iot1click_projects.Client = session.client("iot1click-projects")


# Paginators need type annotation on creation
list_placements_paginator: iot1click_projects.ListPlacementsPaginator = client.get_paginator("list_placements")
list_projects_paginator: iot1click_projects.ListProjectsPaginator = client.get_paginator("list_projects")
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