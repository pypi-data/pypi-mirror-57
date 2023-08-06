# mypy-boto3-elastictranscoder

Mypy-friendly auto-generated type annotations for `boto3 elastictranscoder 1.10.33` service.
More information can be found [here](https://github.com/vemel/mypy_boto3).

- [mypy-boto3-elastictranscoder](#mypy-boto3-elastictranscoder)
  - [How to use](#how-to-use)
    - [Type checking](#type-checking)
    - [Code auto-complete](#code-auto-complete)
  - [How it works](#how-it-works)

## How to use

### Type checking

Make sure you have [mypy](https://github.com/python/mypy) installed and activated in your IDE.

Install `boto3-stubs` for `elastictranscoder` service.

```bash
pip install boto3-stubs[mypy-boto3-elastictranscoder]
```

Use `boto3` with `mypy_boto3` in your project and enjoy type checking.

```python
import boto3

from mypy_boto3 import elastictranscoder
# alternative import if you do not want to install mypy_boto3 package
# import mypy_boto3_elastictranscoder as elastictranscoder

# Use this client as usual, now mypy can check if your code is valid.
client: elastictranscoder.Client = boto3.client("elastictranscoder")

# works for session as well
session = boto3.session.Session(region="us-west-1")
session_client: elastictranscoder.Client = session.client("elastictranscoder")


# Waiters need type annotation on creation
job_complete_waiter: elastictranscoder.JobCompleteWaiter = client.get_waiter("job_complete")

# Paginators need type annotation on creation
list_jobs_by_pipeline_paginator: elastictranscoder.ListJobsByPipelinePaginator = client.get_paginator("list_jobs_by_pipeline")
list_jobs_by_status_paginator: elastictranscoder.ListJobsByStatusPaginator = client.get_paginator("list_jobs_by_status")
list_pipelines_paginator: elastictranscoder.ListPipelinesPaginator = client.get_paginator("list_pipelines")
list_presets_paginator: elastictranscoder.ListPresetsPaginator = client.get_paginator("list_presets")
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