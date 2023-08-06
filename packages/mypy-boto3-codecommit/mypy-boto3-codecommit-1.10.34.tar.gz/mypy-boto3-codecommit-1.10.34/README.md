# mypy-boto3-codecommit

Mypy-friendly auto-generated type annotations for `boto3 codecommit 1.10.34` service.
More information can be found [here](https://github.com/vemel/mypy_boto3).

- [mypy-boto3-codecommit](#mypy-boto3-codecommit)
  - [How to use](#how-to-use)
    - [Type checking](#type-checking)
    - [Code auto-complete](#code-auto-complete)
  - [How it works](#how-it-works)

## How to use

### Type checking

Make sure you have [mypy](https://github.com/python/mypy) installed and activated in your IDE.

Install `boto3-stubs` for `codecommit` service.

```bash
pip install boto3-stubs[mypy-boto3-codecommit]
```

Use `boto3` with `mypy_boto3` in your project and enjoy type checking.

```python
import boto3

from mypy_boto3 import codecommit
# alternative import if you do not want to install mypy_boto3 package
# import mypy_boto3_codecommit as codecommit

# Use this client as usual, now mypy can check if your code is valid.
client: codecommit.Client = boto3.client("codecommit")

# works for session as well
session = boto3.session.Session(region="us-west-1")
session_client: codecommit.Client = session.client("codecommit")


# Paginators need type annotation on creation
describe_pull_request_events_paginator: codecommit.DescribePullRequestEventsPaginator = client.get_paginator("describe_pull_request_events")
get_comments_for_compared_commit_paginator: codecommit.GetCommentsForComparedCommitPaginator = client.get_paginator("get_comments_for_compared_commit")
get_comments_for_pull_request_paginator: codecommit.GetCommentsForPullRequestPaginator = client.get_paginator("get_comments_for_pull_request")
get_differences_paginator: codecommit.GetDifferencesPaginator = client.get_paginator("get_differences")
list_branches_paginator: codecommit.ListBranchesPaginator = client.get_paginator("list_branches")
list_pull_requests_paginator: codecommit.ListPullRequestsPaginator = client.get_paginator("list_pull_requests")
list_repositories_paginator: codecommit.ListRepositoriesPaginator = client.get_paginator("list_repositories")
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