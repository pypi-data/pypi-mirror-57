# mypy-boto3-machinelearning

Mypy-friendly auto-generated type annotations for `boto3 machinelearning 1.10.33` service.
More information can be found [here](https://github.com/vemel/mypy_boto3).

- [mypy-boto3-machinelearning](#mypy-boto3-machinelearning)
  - [How to use](#how-to-use)
    - [Type checking](#type-checking)
    - [Code auto-complete](#code-auto-complete)
  - [How it works](#how-it-works)

## How to use

### Type checking

Make sure you have [mypy](https://github.com/python/mypy) installed and activated in your IDE.

Install `boto3-stubs` for `machinelearning` service.

```bash
pip install boto3-stubs[mypy-boto3-machinelearning]
```

Use `boto3` with `mypy_boto3` in your project and enjoy type checking.

```python
import boto3

from mypy_boto3 import machinelearning
# alternative import if you do not want to install mypy_boto3 package
# import mypy_boto3_machinelearning as machinelearning

# Use this client as usual, now mypy can check if your code is valid.
client: machinelearning.Client = boto3.client("machinelearning")

# works for session as well
session = boto3.session.Session(region="us-west-1")
session_client: machinelearning.Client = session.client("machinelearning")


# Waiters need type annotation on creation
batch_prediction_available_waiter: machinelearning.BatchPredictionAvailableWaiter = client.get_waiter("batch_prediction_available")
data_source_available_waiter: machinelearning.DataSourceAvailableWaiter = client.get_waiter("data_source_available")
evaluation_available_waiter: machinelearning.EvaluationAvailableWaiter = client.get_waiter("evaluation_available")
ml_model_available_waiter: machinelearning.MLModelAvailableWaiter = client.get_waiter("ml_model_available")

# Paginators need type annotation on creation
describe_batch_predictions_paginator: machinelearning.DescribeBatchPredictionsPaginator = client.get_paginator("describe_batch_predictions")
describe_data_sources_paginator: machinelearning.DescribeDataSourcesPaginator = client.get_paginator("describe_data_sources")
describe_evaluations_paginator: machinelearning.DescribeEvaluationsPaginator = client.get_paginator("describe_evaluations")
describe_ml_models_paginator: machinelearning.DescribeMLModelsPaginator = client.get_paginator("describe_ml_models")
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