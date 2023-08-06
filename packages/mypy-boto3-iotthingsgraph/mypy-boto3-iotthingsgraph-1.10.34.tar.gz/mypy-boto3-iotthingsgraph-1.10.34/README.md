# mypy-boto3-iotthingsgraph

Mypy-friendly auto-generated type annotations for `boto3 iotthingsgraph 1.10.34` service.
More information can be found [here](https://github.com/vemel/mypy_boto3).

- [mypy-boto3-iotthingsgraph](#mypy-boto3-iotthingsgraph)
  - [How to use](#how-to-use)
    - [Type checking](#type-checking)
    - [Code auto-complete](#code-auto-complete)
  - [How it works](#how-it-works)

## How to use

### Type checking

Make sure you have [mypy](https://github.com/python/mypy) installed and activated in your IDE.

Install `boto3-stubs` for `iotthingsgraph` service.

```bash
pip install boto3-stubs[mypy-boto3-iotthingsgraph]
```

Use `boto3` with `mypy_boto3` in your project and enjoy type checking.

```python
import boto3

from mypy_boto3 import iotthingsgraph
# alternative import if you do not want to install mypy_boto3 package
# import mypy_boto3_iotthingsgraph as iotthingsgraph

# Use this client as usual, now mypy can check if your code is valid.
client: iotthingsgraph.Client = boto3.client("iotthingsgraph")

# works for session as well
session = boto3.session.Session(region="us-west-1")
session_client: iotthingsgraph.Client = session.client("iotthingsgraph")


# Paginators need type annotation on creation
get_flow_template_revisions_paginator: iotthingsgraph.GetFlowTemplateRevisionsPaginator = client.get_paginator("get_flow_template_revisions")
get_system_template_revisions_paginator: iotthingsgraph.GetSystemTemplateRevisionsPaginator = client.get_paginator("get_system_template_revisions")
list_flow_execution_messages_paginator: iotthingsgraph.ListFlowExecutionMessagesPaginator = client.get_paginator("list_flow_execution_messages")
list_tags_for_resource_paginator: iotthingsgraph.ListTagsForResourcePaginator = client.get_paginator("list_tags_for_resource")
search_entities_paginator: iotthingsgraph.SearchEntitiesPaginator = client.get_paginator("search_entities")
search_flow_executions_paginator: iotthingsgraph.SearchFlowExecutionsPaginator = client.get_paginator("search_flow_executions")
search_flow_templates_paginator: iotthingsgraph.SearchFlowTemplatesPaginator = client.get_paginator("search_flow_templates")
search_system_instances_paginator: iotthingsgraph.SearchSystemInstancesPaginator = client.get_paginator("search_system_instances")
search_system_templates_paginator: iotthingsgraph.SearchSystemTemplatesPaginator = client.get_paginator("search_system_templates")
search_things_paginator: iotthingsgraph.SearchThingsPaginator = client.get_paginator("search_things")
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