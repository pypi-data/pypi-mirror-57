# mypy-boto3-glue

Mypy-friendly auto-generated type annotations for `boto3 glue 1.10.34` service.
More information can be found [here](https://github.com/vemel/mypy_boto3).

- [mypy-boto3-glue](#mypy-boto3-glue)
  - [How to use](#how-to-use)
    - [Type checking](#type-checking)
    - [Code auto-complete](#code-auto-complete)
  - [How it works](#how-it-works)

## How to use

### Type checking

Make sure you have [mypy](https://github.com/python/mypy) installed and activated in your IDE.

Install `boto3-stubs` for `glue` service.

```bash
pip install boto3-stubs[mypy-boto3-glue]
```

Use `boto3` with `mypy_boto3` in your project and enjoy type checking.

```python
import boto3

from mypy_boto3 import glue
# alternative import if you do not want to install mypy_boto3 package
# import mypy_boto3_glue as glue

# Use this client as usual, now mypy can check if your code is valid.
client: glue.Client = boto3.client("glue")

# works for session as well
session = boto3.session.Session(region="us-west-1")
session_client: glue.Client = session.client("glue")


# Paginators need type annotation on creation
get_classifiers_paginator: glue.GetClassifiersPaginator = client.get_paginator("get_classifiers")
get_connections_paginator: glue.GetConnectionsPaginator = client.get_paginator("get_connections")
get_crawler_metrics_paginator: glue.GetCrawlerMetricsPaginator = client.get_paginator("get_crawler_metrics")
get_crawlers_paginator: glue.GetCrawlersPaginator = client.get_paginator("get_crawlers")
get_databases_paginator: glue.GetDatabasesPaginator = client.get_paginator("get_databases")
get_dev_endpoints_paginator: glue.GetDevEndpointsPaginator = client.get_paginator("get_dev_endpoints")
get_job_runs_paginator: glue.GetJobRunsPaginator = client.get_paginator("get_job_runs")
get_jobs_paginator: glue.GetJobsPaginator = client.get_paginator("get_jobs")
get_partitions_paginator: glue.GetPartitionsPaginator = client.get_paginator("get_partitions")
get_security_configurations_paginator: glue.GetSecurityConfigurationsPaginator = client.get_paginator("get_security_configurations")
get_table_versions_paginator: glue.GetTableVersionsPaginator = client.get_paginator("get_table_versions")
get_tables_paginator: glue.GetTablesPaginator = client.get_paginator("get_tables")
get_triggers_paginator: glue.GetTriggersPaginator = client.get_paginator("get_triggers")
get_user_defined_functions_paginator: glue.GetUserDefinedFunctionsPaginator = client.get_paginator("get_user_defined_functions")
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