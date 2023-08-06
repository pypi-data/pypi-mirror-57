# mypy-boto3-sns

Mypy-friendly auto-generated type annotations for `boto3 sns 1.10.33` service.
More information can be found [here](https://github.com/vemel/mypy_boto3).

- [mypy-boto3-sns](#mypy-boto3-sns)
  - [How to use](#how-to-use)
    - [Type checking](#type-checking)
    - [Code auto-complete](#code-auto-complete)
  - [How it works](#how-it-works)

## How to use

### Type checking

Make sure you have [mypy](https://github.com/python/mypy) installed and activated in your IDE.

Install `boto3-stubs` for `sns` service.

```bash
pip install boto3-stubs[mypy-boto3-sns]
```

Use `boto3` with `mypy_boto3` in your project and enjoy type checking.

```python
import boto3

from mypy_boto3 import sns
# alternative import if you do not want to install mypy_boto3 package
# import mypy_boto3_sns as sns

# Use this client as usual, now mypy can check if your code is valid.
client: sns.Client = boto3.client("sns")

# works for session as well
session = boto3.session.Session(region="us-west-1")
session_client: sns.Client = session.client("sns")

# Do you prefer resource approach? We've got you covered!
resource: sns.ServiceResource = boto3.resource("sns")

# Paginators need type annotation on creation
list_endpoints_by_platform_application_paginator: sns.ListEndpointsByPlatformApplicationPaginator = client.get_paginator("list_endpoints_by_platform_application")
list_phone_numbers_opted_out_paginator: sns.ListPhoneNumbersOptedOutPaginator = client.get_paginator("list_phone_numbers_opted_out")
list_platform_applications_paginator: sns.ListPlatformApplicationsPaginator = client.get_paginator("list_platform_applications")
list_subscriptions_paginator: sns.ListSubscriptionsPaginator = client.get_paginator("list_subscriptions")
list_subscriptions_by_topic_paginator: sns.ListSubscriptionsByTopicPaginator = client.get_paginator("list_subscriptions_by_topic")
list_topics_paginator: sns.ListTopicsPaginator = client.get_paginator("list_topics")
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