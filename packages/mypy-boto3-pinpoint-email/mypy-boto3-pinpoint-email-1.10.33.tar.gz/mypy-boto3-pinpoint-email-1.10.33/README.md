# mypy-boto3-pinpoint-email

Mypy-friendly auto-generated type annotations for `boto3 pinpoint-email 1.10.33` service.
More information can be found [here](https://github.com/vemel/mypy_boto3).

- [mypy-boto3-pinpoint-email](#mypy-boto3-pinpoint-email)
  - [How to use](#how-to-use)
    - [Type checking](#type-checking)
    - [Code auto-complete](#code-auto-complete)
  - [How it works](#how-it-works)

## How to use

### Type checking

Make sure you have [mypy](https://github.com/python/mypy) installed and activated in your IDE.

Install `boto3-stubs` for `pinpoint-email` service.

```bash
pip install boto3-stubs[mypy-boto3-pinpoint-email]
```

Use `boto3` with `mypy_boto3` in your project and enjoy type checking.

```python
import boto3

from mypy_boto3 import pinpoint_email
# alternative import if you do not want to install mypy_boto3 package
# import mypy_boto3_pinpoint_email as pinpoint_email

# Use this client as usual, now mypy can check if your code is valid.
client: pinpoint_email.Client = boto3.client("pinpoint-email")

# works for session as well
session = boto3.session.Session(region="us-west-1")
session_client: pinpoint_email.Client = session.client("pinpoint-email")


# Paginators need type annotation on creation
get_dedicated_ips_paginator: pinpoint_email.GetDedicatedIpsPaginator = client.get_paginator("get_dedicated_ips")
list_configuration_sets_paginator: pinpoint_email.ListConfigurationSetsPaginator = client.get_paginator("list_configuration_sets")
list_dedicated_ip_pools_paginator: pinpoint_email.ListDedicatedIpPoolsPaginator = client.get_paginator("list_dedicated_ip_pools")
list_deliverability_test_reports_paginator: pinpoint_email.ListDeliverabilityTestReportsPaginator = client.get_paginator("list_deliverability_test_reports")
list_email_identities_paginator: pinpoint_email.ListEmailIdentitiesPaginator = client.get_paginator("list_email_identities")
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