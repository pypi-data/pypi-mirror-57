# mypy-boto3-s3

Mypy-friendly auto-generated type annotations for `boto3 s3 1.10.33` service.
More information can be found [here](https://github.com/vemel/mypy_boto3).

- [mypy-boto3-s3](#mypy-boto3-s3)
  - [How to use](#how-to-use)
    - [Type checking](#type-checking)
    - [Code auto-complete](#code-auto-complete)
  - [How it works](#how-it-works)

## How to use

### Type checking

Make sure you have [mypy](https://github.com/python/mypy) installed and activated in your IDE.

Install `boto3-stubs` for `s3` service.

```bash
pip install boto3-stubs[mypy-boto3-s3]
```

Use `boto3` with `mypy_boto3` in your project and enjoy type checking.

```python
import boto3

from mypy_boto3 import s3
# alternative import if you do not want to install mypy_boto3 package
# import mypy_boto3_s3 as s3

# Use this client as usual, now mypy can check if your code is valid.
client: s3.Client = boto3.client("s3")

# works for session as well
session = boto3.session.Session(region="us-west-1")
session_client: s3.Client = session.client("s3")

# Do you prefer resource approach? We've got you covered!
resource: s3.ServiceResource = boto3.resource("s3")

# Waiters need type annotation on creation
bucket_exists_waiter: s3.BucketExistsWaiter = client.get_waiter("bucket_exists")
bucket_not_exists_waiter: s3.BucketNotExistsWaiter = client.get_waiter("bucket_not_exists")
object_exists_waiter: s3.ObjectExistsWaiter = client.get_waiter("object_exists")
object_not_exists_waiter: s3.ObjectNotExistsWaiter = client.get_waiter("object_not_exists")

# Paginators need type annotation on creation
list_multipart_uploads_paginator: s3.ListMultipartUploadsPaginator = client.get_paginator("list_multipart_uploads")
list_object_versions_paginator: s3.ListObjectVersionsPaginator = client.get_paginator("list_object_versions")
list_objects_paginator: s3.ListObjectsPaginator = client.get_paginator("list_objects")
list_objects_v2_paginator: s3.ListObjectsV2Paginator = client.get_paginator("list_objects_v2")
list_parts_paginator: s3.ListPartsPaginator = client.get_paginator("list_parts")
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