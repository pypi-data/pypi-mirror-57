# mypy-boto3-workdocs

Mypy-friendly auto-generated type annotations for `boto3 workdocs 1.10.33` service.
More information can be found [here](https://github.com/vemel/mypy_boto3).

- [mypy-boto3-workdocs](#mypy-boto3-workdocs)
  - [How to use](#how-to-use)
    - [Type checking](#type-checking)
    - [Code auto-complete](#code-auto-complete)
  - [How it works](#how-it-works)

## How to use

### Type checking

Make sure you have [mypy](https://github.com/python/mypy) installed and activated in your IDE.

Install `boto3-stubs` for `workdocs` service.

```bash
pip install boto3-stubs[mypy-boto3-workdocs]
```

Use `boto3` with `mypy_boto3` in your project and enjoy type checking.

```python
import boto3

from mypy_boto3 import workdocs
# alternative import if you do not want to install mypy_boto3 package
# import mypy_boto3_workdocs as workdocs

# Use this client as usual, now mypy can check if your code is valid.
client: workdocs.Client = boto3.client("workdocs")

# works for session as well
session = boto3.session.Session(region="us-west-1")
session_client: workdocs.Client = session.client("workdocs")


# Paginators need type annotation on creation
describe_activities_paginator: workdocs.DescribeActivitiesPaginator = client.get_paginator("describe_activities")
describe_comments_paginator: workdocs.DescribeCommentsPaginator = client.get_paginator("describe_comments")
describe_document_versions_paginator: workdocs.DescribeDocumentVersionsPaginator = client.get_paginator("describe_document_versions")
describe_folder_contents_paginator: workdocs.DescribeFolderContentsPaginator = client.get_paginator("describe_folder_contents")
describe_groups_paginator: workdocs.DescribeGroupsPaginator = client.get_paginator("describe_groups")
describe_notification_subscriptions_paginator: workdocs.DescribeNotificationSubscriptionsPaginator = client.get_paginator("describe_notification_subscriptions")
describe_resource_permissions_paginator: workdocs.DescribeResourcePermissionsPaginator = client.get_paginator("describe_resource_permissions")
describe_root_folders_paginator: workdocs.DescribeRootFoldersPaginator = client.get_paginator("describe_root_folders")
describe_users_paginator: workdocs.DescribeUsersPaginator = client.get_paginator("describe_users")
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