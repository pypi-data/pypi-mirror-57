# mypy-boto3-personalize

Mypy-friendly auto-generated type annotations for `boto3 personalize 1.10.33` service.
More information can be found [here](https://github.com/vemel/mypy_boto3).

- [mypy-boto3-personalize](#mypy-boto3-personalize)
  - [How to use](#how-to-use)
    - [Type checking](#type-checking)
    - [Code auto-complete](#code-auto-complete)
  - [How it works](#how-it-works)

## How to use

### Type checking

Make sure you have [mypy](https://github.com/python/mypy) installed and activated in your IDE.

Install `boto3-stubs` for `personalize` service.

```bash
pip install boto3-stubs[mypy-boto3-personalize]
```

Use `boto3` with `mypy_boto3` in your project and enjoy type checking.

```python
import boto3

from mypy_boto3 import personalize
# alternative import if you do not want to install mypy_boto3 package
# import mypy_boto3_personalize as personalize

# Use this client as usual, now mypy can check if your code is valid.
client: personalize.Client = boto3.client("personalize")

# works for session as well
session = boto3.session.Session(region="us-west-1")
session_client: personalize.Client = session.client("personalize")


# Paginators need type annotation on creation
list_batch_inference_jobs_paginator: personalize.ListBatchInferenceJobsPaginator = client.get_paginator("list_batch_inference_jobs")
list_campaigns_paginator: personalize.ListCampaignsPaginator = client.get_paginator("list_campaigns")
list_dataset_groups_paginator: personalize.ListDatasetGroupsPaginator = client.get_paginator("list_dataset_groups")
list_dataset_import_jobs_paginator: personalize.ListDatasetImportJobsPaginator = client.get_paginator("list_dataset_import_jobs")
list_datasets_paginator: personalize.ListDatasetsPaginator = client.get_paginator("list_datasets")
list_event_trackers_paginator: personalize.ListEventTrackersPaginator = client.get_paginator("list_event_trackers")
list_recipes_paginator: personalize.ListRecipesPaginator = client.get_paginator("list_recipes")
list_schemas_paginator: personalize.ListSchemasPaginator = client.get_paginator("list_schemas")
list_solution_versions_paginator: personalize.ListSolutionVersionsPaginator = client.get_paginator("list_solution_versions")
list_solutions_paginator: personalize.ListSolutionsPaginator = client.get_paginator("list_solutions")
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