# mypy-boto3-elbv2

Mypy-friendly auto-generated type annotations for `boto3 elbv2 1.10.33` service.
More information can be found [here](https://github.com/vemel/mypy_boto3).

- [mypy-boto3-elbv2](#mypy-boto3-elbv2)
  - [How to use](#how-to-use)
    - [Type checking](#type-checking)
    - [Code auto-complete](#code-auto-complete)
  - [How it works](#how-it-works)

## How to use

### Type checking

Make sure you have [mypy](https://github.com/python/mypy) installed and activated in your IDE.

Install `boto3-stubs` for `elbv2` service.

```bash
pip install boto3-stubs[mypy-boto3-elbv2]
```

Use `boto3` with `mypy_boto3` in your project and enjoy type checking.

```python
import boto3

from mypy_boto3 import elbv2
# alternative import if you do not want to install mypy_boto3 package
# import mypy_boto3_elbv2 as elbv2

# Use this client as usual, now mypy can check if your code is valid.
client: elbv2.Client = boto3.client("elbv2")

# works for session as well
session = boto3.session.Session(region="us-west-1")
session_client: elbv2.Client = session.client("elbv2")


# Waiters need type annotation on creation
load_balancer_available_waiter: elbv2.LoadBalancerAvailableWaiter = client.get_waiter("load_balancer_available")
load_balancer_exists_waiter: elbv2.LoadBalancerExistsWaiter = client.get_waiter("load_balancer_exists")
load_balancers_deleted_waiter: elbv2.LoadBalancersDeletedWaiter = client.get_waiter("load_balancers_deleted")
target_deregistered_waiter: elbv2.TargetDeregisteredWaiter = client.get_waiter("target_deregistered")
target_in_service_waiter: elbv2.TargetInServiceWaiter = client.get_waiter("target_in_service")

# Paginators need type annotation on creation
describe_account_limits_paginator: elbv2.DescribeAccountLimitsPaginator = client.get_paginator("describe_account_limits")
describe_listener_certificates_paginator: elbv2.DescribeListenerCertificatesPaginator = client.get_paginator("describe_listener_certificates")
describe_listeners_paginator: elbv2.DescribeListenersPaginator = client.get_paginator("describe_listeners")
describe_load_balancers_paginator: elbv2.DescribeLoadBalancersPaginator = client.get_paginator("describe_load_balancers")
describe_rules_paginator: elbv2.DescribeRulesPaginator = client.get_paginator("describe_rules")
describe_ssl_policies_paginator: elbv2.DescribeSSLPoliciesPaginator = client.get_paginator("describe_ssl_policies")
describe_target_groups_paginator: elbv2.DescribeTargetGroupsPaginator = client.get_paginator("describe_target_groups")
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