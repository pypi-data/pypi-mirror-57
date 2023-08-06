# mypy-boto3-mturk

Mypy-friendly auto-generated type annotations for `boto3 mturk 1.10.33` service.
More information can be found [here](https://github.com/vemel/mypy_boto3).

- [mypy-boto3-mturk](#mypy-boto3-mturk)
  - [How to use](#how-to-use)
    - [Type checking](#type-checking)
    - [Code auto-complete](#code-auto-complete)
  - [How it works](#how-it-works)

## How to use

### Type checking

Make sure you have [mypy](https://github.com/python/mypy) installed and activated in your IDE.

Install `boto3-stubs` for `mturk` service.

```bash
pip install boto3-stubs[mypy-boto3-mturk]
```

Use `boto3` with `mypy_boto3` in your project and enjoy type checking.

```python
import boto3

from mypy_boto3 import mturk
# alternative import if you do not want to install mypy_boto3 package
# import mypy_boto3_mturk as mturk

# Use this client as usual, now mypy can check if your code is valid.
client: mturk.Client = boto3.client("mturk")

# works for session as well
session = boto3.session.Session(region="us-west-1")
session_client: mturk.Client = session.client("mturk")


# Paginators need type annotation on creation
list_assignments_for_hit_paginator: mturk.ListAssignmentsForHITPaginator = client.get_paginator("list_assignments_for_hit")
list_bonus_payments_paginator: mturk.ListBonusPaymentsPaginator = client.get_paginator("list_bonus_payments")
list_hits_paginator: mturk.ListHITsPaginator = client.get_paginator("list_hits")
list_hits_for_qualification_type_paginator: mturk.ListHITsForQualificationTypePaginator = client.get_paginator("list_hits_for_qualification_type")
list_qualification_requests_paginator: mturk.ListQualificationRequestsPaginator = client.get_paginator("list_qualification_requests")
list_qualification_types_paginator: mturk.ListQualificationTypesPaginator = client.get_paginator("list_qualification_types")
list_reviewable_hits_paginator: mturk.ListReviewableHITsPaginator = client.get_paginator("list_reviewable_hits")
list_worker_blocks_paginator: mturk.ListWorkerBlocksPaginator = client.get_paginator("list_worker_blocks")
list_workers_with_qualification_type_paginator: mturk.ListWorkersWithQualificationTypePaginator = client.get_paginator("list_workers_with_qualification_type")
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