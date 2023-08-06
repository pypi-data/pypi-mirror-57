# mypy-boto3-snowball

Mypy-friendly auto-generated type annotations for `boto3 snowball 1.10.33` service.
More information can be found [here](https://github.com/vemel/mypy_boto3).

- [mypy-boto3-snowball](#mypy-boto3-snowball)
  - [How to use](#how-to-use)
    - [Type checking](#type-checking)
    - [Code auto-complete](#code-auto-complete)
  - [How it works](#how-it-works)

## How to use

### Type checking

Make sure you have [mypy](https://github.com/python/mypy) installed and activated in your IDE.

Install `boto3-stubs` for `snowball` service.

```bash
pip install boto3-stubs[mypy-boto3-snowball]
```

Use `boto3` with `mypy_boto3` in your project and enjoy type checking.

```python
import boto3

from mypy_boto3 import snowball
# alternative import if you do not want to install mypy_boto3 package
# import mypy_boto3_snowball as snowball

# Use this client as usual, now mypy can check if your code is valid.
client: snowball.Client = boto3.client("snowball")

# works for session as well
session = boto3.session.Session(region="us-west-1")
session_client: snowball.Client = session.client("snowball")


# Paginators need type annotation on creation
describe_addresses_paginator: snowball.DescribeAddressesPaginator = client.get_paginator("describe_addresses")
list_cluster_jobs_paginator: snowball.ListClusterJobsPaginator = client.get_paginator("list_cluster_jobs")
list_clusters_paginator: snowball.ListClustersPaginator = client.get_paginator("list_clusters")
list_compatible_images_paginator: snowball.ListCompatibleImagesPaginator = client.get_paginator("list_compatible_images")
list_jobs_paginator: snowball.ListJobsPaginator = client.get_paginator("list_jobs")
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