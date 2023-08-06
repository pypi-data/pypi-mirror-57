# mypy-boto3-codepipeline

Mypy-friendly auto-generated type annotations for `boto3 codepipeline 1.10.37` service.
More information can be found [here](https://github.com/vemel/mypy_boto3).

- [mypy-boto3-codepipeline](#mypy-boto3-codepipeline)
  - [How to use](#how-to-use)
    - [Type checking](#type-checking)
    - [Code auto-complete](#code-auto-complete)
  - [How it works](#how-it-works)

## How to use

### Type checking

Make sure you have [mypy](https://github.com/python/mypy) installed and activated in your IDE.

Install `boto3-stubs` for `codepipeline` service.

```bash
python -m pip install boto3-stubs[mypy-boto3-codepipeline]

# build service index. You should execute this command everytime
# you install or remove service packages
python -m mypy_boto3
```

Use `boto3` with `mypy_boto3` in your project and enjoy type checking.

```python
import boto3

from mypy_boto3 import codepipeline
# alternative import if you do not want to install mypy_boto3 package
# import mypy_boto3_codepipeline as codepipeline

# Use this client as usual, now mypy can check if your code is valid.
# Check if your IDE supports function overloads,
# you probably do not need explicit type annotations
# client = boto3.client("codepipeline")
client: codepipeline.CodePipelineClient = boto3.client("codepipeline")

# works for session as well
session = boto3.session.Session(region="us-west-1")
session_client: codepipeline.CodePipelineClient = session.client("codepipeline")


# Paginators need type annotation on creation
list_action_executions_paginator: codepipeline.ListActionExecutionsPaginator = client.get_paginator("list_action_executions")
list_action_types_paginator: codepipeline.ListActionTypesPaginator = client.get_paginator("list_action_types")
list_pipeline_executions_paginator: codepipeline.ListPipelineExecutionsPaginator = client.get_paginator("list_pipeline_executions")
list_pipelines_paginator: codepipeline.ListPipelinesPaginator = client.get_paginator("list_pipelines")
list_tags_for_resource_paginator: codepipeline.ListTagsForResourcePaginator = client.get_paginator("list_tags_for_resource")
list_webhooks_paginator: codepipeline.ListWebhooksPaginator = client.get_paginator("list_webhooks")
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