# mypy-boto3-medialive

Mypy-friendly auto-generated type annotations for `boto3 medialive 1.10.33` service.
More information can be found [here](https://github.com/vemel/mypy_boto3).

- [mypy-boto3-medialive](#mypy-boto3-medialive)
  - [How to use](#how-to-use)
    - [Type checking](#type-checking)
    - [Code auto-complete](#code-auto-complete)
  - [How it works](#how-it-works)

## How to use

### Type checking

Make sure you have [mypy](https://github.com/python/mypy) installed and activated in your IDE.

Install `boto3-stubs` for `medialive` service.

```bash
pip install boto3-stubs[mypy-boto3-medialive]
```

Use `boto3` with `mypy_boto3` in your project and enjoy type checking.

```python
import boto3

from mypy_boto3 import medialive
# alternative import if you do not want to install mypy_boto3 package
# import mypy_boto3_medialive as medialive

# Use this client as usual, now mypy can check if your code is valid.
client: medialive.Client = boto3.client("medialive")

# works for session as well
session = boto3.session.Session(region="us-west-1")
session_client: medialive.Client = session.client("medialive")


# Waiters need type annotation on creation
channel_created_waiter: medialive.ChannelCreatedWaiter = client.get_waiter("channel_created")
channel_deleted_waiter: medialive.ChannelDeletedWaiter = client.get_waiter("channel_deleted")
channel_running_waiter: medialive.ChannelRunningWaiter = client.get_waiter("channel_running")
channel_stopped_waiter: medialive.ChannelStoppedWaiter = client.get_waiter("channel_stopped")
multiplex_created_waiter: medialive.MultiplexCreatedWaiter = client.get_waiter("multiplex_created")
multiplex_deleted_waiter: medialive.MultiplexDeletedWaiter = client.get_waiter("multiplex_deleted")
multiplex_running_waiter: medialive.MultiplexRunningWaiter = client.get_waiter("multiplex_running")
multiplex_stopped_waiter: medialive.MultiplexStoppedWaiter = client.get_waiter("multiplex_stopped")

# Paginators need type annotation on creation
describe_schedule_paginator: medialive.DescribeSchedulePaginator = client.get_paginator("describe_schedule")
list_channels_paginator: medialive.ListChannelsPaginator = client.get_paginator("list_channels")
list_input_security_groups_paginator: medialive.ListInputSecurityGroupsPaginator = client.get_paginator("list_input_security_groups")
list_inputs_paginator: medialive.ListInputsPaginator = client.get_paginator("list_inputs")
list_multiplex_programs_paginator: medialive.ListMultiplexProgramsPaginator = client.get_paginator("list_multiplex_programs")
list_multiplexes_paginator: medialive.ListMultiplexesPaginator = client.get_paginator("list_multiplexes")
list_offerings_paginator: medialive.ListOfferingsPaginator = client.get_paginator("list_offerings")
list_reservations_paginator: medialive.ListReservationsPaginator = client.get_paginator("list_reservations")
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