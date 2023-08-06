# mypy-boto3-cloudtrail

Mypy-friendly auto-generated type annotations for `boto3 cloudtrail 1.10.35` service.
More information can be found [here](https://github.com/vemel/mypy_boto3).

- [mypy-boto3-cloudtrail](#mypy-boto3-cloudtrail)
  - [How to use](#how-to-use)
    - [Type checking](#type-checking)
    - [Code auto-complete](#code-auto-complete)
  - [How it works](#how-it-works)

## How to use

### Type checking

Make sure you have [mypy](https://github.com/python/mypy) installed and activated in your IDE.

Install `boto3-stubs` for `cloudtrail` service.

```bash
python -m pip install boto3-stubs[mypy-boto3-cloudtrail]

# build service index. You should execute this command everytime
# you update boto3-stubs or install/remove services
python -m python -m mypy_boto3
```

Use `boto3` with `mypy_boto3` in your project and enjoy type checking.

```python
import boto3

from mypy_boto3 import cloudtrail
# alternative import if you do not want to install mypy_boto3 package
# import mypy_boto3_cloudtrail as cloudtrail

# Use this client as usual, now mypy can check if your code is valid.
# Check if your IDE supports function overloads,
# you probably do not need explicit type annotations
# client = boto3.client("cloudtrail")
client: cloudtrail.Client = boto3.client("cloudtrail")

# works for session as well
session = boto3.session.Session(region="us-west-1")
session_client: cloudtrail.Client = session.client("cloudtrail")


# Paginators need type annotation on creation
list_public_keys_paginator: cloudtrail.ListPublicKeysPaginator = client.get_paginator("list_public_keys")
list_tags_paginator: cloudtrail.ListTagsPaginator = client.get_paginator("list_tags")
list_trails_paginator: cloudtrail.ListTrailsPaginator = client.get_paginator("list_trails")
lookup_events_paginator: cloudtrail.LookupEventsPaginator = client.get_paginator("lookup_events")
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