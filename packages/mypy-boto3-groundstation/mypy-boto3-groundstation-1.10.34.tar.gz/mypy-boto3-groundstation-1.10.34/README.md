# mypy-boto3-groundstation

Mypy-friendly auto-generated type annotations for `boto3 groundstation 1.10.34` service.
More information can be found [here](https://github.com/vemel/mypy_boto3).

- [mypy-boto3-groundstation](#mypy-boto3-groundstation)
  - [How to use](#how-to-use)
    - [Type checking](#type-checking)
    - [Code auto-complete](#code-auto-complete)
  - [How it works](#how-it-works)

## How to use

### Type checking

Make sure you have [mypy](https://github.com/python/mypy) installed and activated in your IDE.

Install `boto3-stubs` for `groundstation` service.

```bash
pip install boto3-stubs[mypy-boto3-groundstation]
```

Use `boto3` with `mypy_boto3` in your project and enjoy type checking.

```python
import boto3

from mypy_boto3 import groundstation
# alternative import if you do not want to install mypy_boto3 package
# import mypy_boto3_groundstation as groundstation

# Use this client as usual, now mypy can check if your code is valid.
client: groundstation.Client = boto3.client("groundstation")

# works for session as well
session = boto3.session.Session(region="us-west-1")
session_client: groundstation.Client = session.client("groundstation")


# Paginators need type annotation on creation
list_configs_paginator: groundstation.ListConfigsPaginator = client.get_paginator("list_configs")
list_contacts_paginator: groundstation.ListContactsPaginator = client.get_paginator("list_contacts")
list_dataflow_endpoint_groups_paginator: groundstation.ListDataflowEndpointGroupsPaginator = client.get_paginator("list_dataflow_endpoint_groups")
list_ground_stations_paginator: groundstation.ListGroundStationsPaginator = client.get_paginator("list_ground_stations")
list_mission_profiles_paginator: groundstation.ListMissionProfilesPaginator = client.get_paginator("list_mission_profiles")
list_satellites_paginator: groundstation.ListSatellitesPaginator = client.get_paginator("list_satellites")
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