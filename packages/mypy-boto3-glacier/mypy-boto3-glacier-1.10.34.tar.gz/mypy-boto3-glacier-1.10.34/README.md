# mypy-boto3-glacier

Mypy-friendly auto-generated type annotations for `boto3 glacier 1.10.34` service.
More information can be found [here](https://github.com/vemel/mypy_boto3).

- [mypy-boto3-glacier](#mypy-boto3-glacier)
  - [How to use](#how-to-use)
    - [Type checking](#type-checking)
    - [Code auto-complete](#code-auto-complete)
  - [How it works](#how-it-works)

## How to use

### Type checking

Make sure you have [mypy](https://github.com/python/mypy) installed and activated in your IDE.

Install `boto3-stubs` for `glacier` service.

```bash
pip install boto3-stubs[mypy-boto3-glacier]
```

Use `boto3` with `mypy_boto3` in your project and enjoy type checking.

```python
import boto3

from mypy_boto3 import glacier
# alternative import if you do not want to install mypy_boto3 package
# import mypy_boto3_glacier as glacier

# Use this client as usual, now mypy can check if your code is valid.
client: glacier.Client = boto3.client("glacier")

# works for session as well
session = boto3.session.Session(region="us-west-1")
session_client: glacier.Client = session.client("glacier")

# Do you prefer resource approach? We've got you covered!
resource: glacier.ServiceResource = boto3.resource("glacier")

# Waiters need type annotation on creation
vault_exists_waiter: glacier.VaultExistsWaiter = client.get_waiter("vault_exists")
vault_not_exists_waiter: glacier.VaultNotExistsWaiter = client.get_waiter("vault_not_exists")

# Paginators need type annotation on creation
list_jobs_paginator: glacier.ListJobsPaginator = client.get_paginator("list_jobs")
list_multipart_uploads_paginator: glacier.ListMultipartUploadsPaginator = client.get_paginator("list_multipart_uploads")
list_parts_paginator: glacier.ListPartsPaginator = client.get_paginator("list_parts")
list_vaults_paginator: glacier.ListVaultsPaginator = client.get_paginator("list_vaults")
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