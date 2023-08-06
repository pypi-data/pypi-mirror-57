# mypy-boto3-rekognition

Mypy-friendly auto-generated type annotations for `boto3 rekognition 1.10.33` service.
More information can be found [here](https://github.com/vemel/mypy_boto3).

- [mypy-boto3-rekognition](#mypy-boto3-rekognition)
  - [How to use](#how-to-use)
    - [Type checking](#type-checking)
    - [Code auto-complete](#code-auto-complete)
  - [How it works](#how-it-works)

## How to use

### Type checking

Make sure you have [mypy](https://github.com/python/mypy) installed and activated in your IDE.

Install `boto3-stubs` for `rekognition` service.

```bash
pip install boto3-stubs[mypy-boto3-rekognition]
```

Use `boto3` with `mypy_boto3` in your project and enjoy type checking.

```python
import boto3

from mypy_boto3 import rekognition
# alternative import if you do not want to install mypy_boto3 package
# import mypy_boto3_rekognition as rekognition

# Use this client as usual, now mypy can check if your code is valid.
client: rekognition.Client = boto3.client("rekognition")

# works for session as well
session = boto3.session.Session(region="us-west-1")
session_client: rekognition.Client = session.client("rekognition")


# Waiters need type annotation on creation
project_version_running_waiter: rekognition.ProjectVersionRunningWaiter = client.get_waiter("project_version_running")
project_version_training_completed_waiter: rekognition.ProjectVersionTrainingCompletedWaiter = client.get_waiter("project_version_training_completed")

# Paginators need type annotation on creation
describe_project_versions_paginator: rekognition.DescribeProjectVersionsPaginator = client.get_paginator("describe_project_versions")
describe_projects_paginator: rekognition.DescribeProjectsPaginator = client.get_paginator("describe_projects")
list_collections_paginator: rekognition.ListCollectionsPaginator = client.get_paginator("list_collections")
list_faces_paginator: rekognition.ListFacesPaginator = client.get_paginator("list_faces")
list_stream_processors_paginator: rekognition.ListStreamProcessorsPaginator = client.get_paginator("list_stream_processors")
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