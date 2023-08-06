# mypy-boto3-kinesis

Mypy-friendly auto-generated type annotations for `boto3 kinesis 1.10.33` service.
More information can be found [here](https://github.com/vemel/mypy_boto3).

- [mypy-boto3-kinesis](#mypy-boto3-kinesis)
  - [How to use](#how-to-use)
    - [Type checking](#type-checking)
    - [Code auto-complete](#code-auto-complete)
  - [How it works](#how-it-works)

## How to use

### Type checking

Make sure you have [mypy](https://github.com/python/mypy) installed and activated in your IDE.

Install `boto3-stubs` for `kinesis` service.

```bash
pip install boto3-stubs[mypy-boto3-kinesis]
```

Use `boto3` with `mypy_boto3` in your project and enjoy type checking.

```python
import boto3

from mypy_boto3 import kinesis
# alternative import if you do not want to install mypy_boto3 package
# import mypy_boto3_kinesis as kinesis

# Use this client as usual, now mypy can check if your code is valid.
client: kinesis.Client = boto3.client("kinesis")

# works for session as well
session = boto3.session.Session(region="us-west-1")
session_client: kinesis.Client = session.client("kinesis")


# Waiters need type annotation on creation
stream_exists_waiter: kinesis.StreamExistsWaiter = client.get_waiter("stream_exists")
stream_not_exists_waiter: kinesis.StreamNotExistsWaiter = client.get_waiter("stream_not_exists")

# Paginators need type annotation on creation
describe_stream_paginator: kinesis.DescribeStreamPaginator = client.get_paginator("describe_stream")
list_shards_paginator: kinesis.ListShardsPaginator = client.get_paginator("list_shards")
list_stream_consumers_paginator: kinesis.ListStreamConsumersPaginator = client.get_paginator("list_stream_consumers")
list_streams_paginator: kinesis.ListStreamsPaginator = client.get_paginator("list_streams")
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