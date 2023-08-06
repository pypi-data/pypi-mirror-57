# mypy-boto3-datapipeline

Mypy-friendly auto-generated type annotations for `boto3 datapipeline 1.10.34` service.
More information can be found [here](https://github.com/vemel/mypy_boto3).

- [mypy-boto3-datapipeline](#mypy-boto3-datapipeline)
  - [How to use](#how-to-use)
    - [Type checking](#type-checking)
    - [Code auto-complete](#code-auto-complete)
  - [How it works](#how-it-works)

## How to use

### Type checking

Make sure you have [mypy](https://github.com/python/mypy) installed and activated in your IDE.

Install `boto3-stubs` for `datapipeline` service.

```bash
pip install boto3-stubs[mypy-boto3-datapipeline]
```

Use `boto3` with `mypy_boto3` in your project and enjoy type checking.

```python
import boto3

from mypy_boto3 import datapipeline
# alternative import if you do not want to install mypy_boto3 package
# import mypy_boto3_datapipeline as datapipeline

# Use this client as usual, now mypy can check if your code is valid.
client: datapipeline.Client = boto3.client("datapipeline")

# works for session as well
session = boto3.session.Session(region="us-west-1")
session_client: datapipeline.Client = session.client("datapipeline")


# Paginators need type annotation on creation
describe_objects_paginator: datapipeline.DescribeObjectsPaginator = client.get_paginator("describe_objects")
list_pipelines_paginator: datapipeline.ListPipelinesPaginator = client.get_paginator("list_pipelines")
query_objects_paginator: datapipeline.QueryObjectsPaginator = client.get_paginator("query_objects")
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