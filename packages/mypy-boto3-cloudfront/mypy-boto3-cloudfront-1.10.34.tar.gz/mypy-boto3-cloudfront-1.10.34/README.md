# mypy-boto3-cloudfront

Mypy-friendly auto-generated type annotations for `boto3 cloudfront 1.10.34` service.
More information can be found [here](https://github.com/vemel/mypy_boto3).

- [mypy-boto3-cloudfront](#mypy-boto3-cloudfront)
  - [How to use](#how-to-use)
    - [Type checking](#type-checking)
    - [Code auto-complete](#code-auto-complete)
  - [How it works](#how-it-works)

## How to use

### Type checking

Make sure you have [mypy](https://github.com/python/mypy) installed and activated in your IDE.

Install `boto3-stubs` for `cloudfront` service.

```bash
pip install boto3-stubs[mypy-boto3-cloudfront]
```

Use `boto3` with `mypy_boto3` in your project and enjoy type checking.

```python
import boto3

from mypy_boto3 import cloudfront
# alternative import if you do not want to install mypy_boto3 package
# import mypy_boto3_cloudfront as cloudfront

# Use this client as usual, now mypy can check if your code is valid.
client: cloudfront.Client = boto3.client("cloudfront")

# works for session as well
session = boto3.session.Session(region="us-west-1")
session_client: cloudfront.Client = session.client("cloudfront")


# Waiters need type annotation on creation
distribution_deployed_waiter: cloudfront.DistributionDeployedWaiter = client.get_waiter("distribution_deployed")
invalidation_completed_waiter: cloudfront.InvalidationCompletedWaiter = client.get_waiter("invalidation_completed")
streaming_distribution_deployed_waiter: cloudfront.StreamingDistributionDeployedWaiter = client.get_waiter("streaming_distribution_deployed")

# Paginators need type annotation on creation
list_cloud_front_origin_access_identities_paginator: cloudfront.ListCloudFrontOriginAccessIdentitiesPaginator = client.get_paginator("list_cloud_front_origin_access_identities")
list_distributions_paginator: cloudfront.ListDistributionsPaginator = client.get_paginator("list_distributions")
list_invalidations_paginator: cloudfront.ListInvalidationsPaginator = client.get_paginator("list_invalidations")
list_streaming_distributions_paginator: cloudfront.ListStreamingDistributionsPaginator = client.get_paginator("list_streaming_distributions")
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