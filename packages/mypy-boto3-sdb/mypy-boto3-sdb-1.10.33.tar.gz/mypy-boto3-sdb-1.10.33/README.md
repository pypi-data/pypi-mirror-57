# mypy-boto3-sdb

Mypy-friendly auto-generated type annotations for `boto3 sdb 1.10.33` service.
More information can be found [here](https://github.com/vemel/mypy_boto3).

- [mypy-boto3-sdb](#mypy-boto3-sdb)
  - [How to use](#how-to-use)
    - [Type checking](#type-checking)
    - [Code auto-complete](#code-auto-complete)
  - [How it works](#how-it-works)

## How to use

### Type checking

Make sure you have [mypy](https://github.com/python/mypy) installed and activated in your IDE.

Install `boto3-stubs` for `sdb` service.

```bash
pip install boto3-stubs[mypy-boto3-sdb]
```

Use `boto3` with `mypy_boto3` in your project and enjoy type checking.

```python
import boto3

from mypy_boto3 import sdb
# alternative import if you do not want to install mypy_boto3 package
# import mypy_boto3_sdb as sdb

# Use this client as usual, now mypy can check if your code is valid.
client: sdb.Client = boto3.client("sdb")

# works for session as well
session = boto3.session.Session(region="us-west-1")
session_client: sdb.Client = session.client("sdb")


# Paginators need type annotation on creation
list_domains_paginator: sdb.ListDomainsPaginator = client.get_paginator("list_domains")
select_paginator: sdb.SelectPaginator = client.get_paginator("select")
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