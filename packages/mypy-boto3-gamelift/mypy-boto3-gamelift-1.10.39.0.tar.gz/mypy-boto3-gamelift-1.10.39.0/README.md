# mypy-boto3-gamelift

Mypy-friendly auto-generated type annotations for `boto3 gamelift 1.10.39` service.
More information can be found [here](https://github.com/vemel/mypy_boto3).

- [mypy-boto3-gamelift](#mypy-boto3-gamelift)
  - [How to use](#how-to-use)
    - [Type checking](#type-checking)
    - [Code auto-complete](#code-auto-complete)
  - [How it works](#how-it-works)

## How to use

### Type checking

Make sure you have [mypy](https://github.com/python/mypy) installed and activated in your IDE.

Install `boto3-stubs` for `gamelift` service.

```bash
python -m pip install boto3-stubs[mypy-boto3-gamelift]

# build service index. You should execute this command everytime
# you install or remove service packages
python -m mypy_boto3
```

Use `boto3` with `mypy_boto3` in your project and enjoy type checking.

```python
import boto3

from mypy_boto3 import gamelift
# alternative import if you do not want to install mypy_boto3 package
# import mypy_boto3_gamelift as gamelift

# Use this client as usual, now mypy can check if your code is valid.
# Check if your IDE supports function overloads,
# you probably do not need explicit type annotations
# client = boto3.client("gamelift")
client: gamelift.GameLiftClient = boto3.client("gamelift")

# works for session as well
session = boto3.session.Session(region="us-west-1")
session_client: gamelift.GameLiftClient = session.client("gamelift")


# Paginators need type annotation on creation
describe_fleet_attributes_paginator: gamelift.DescribeFleetAttributesPaginator = client.get_paginator("describe_fleet_attributes")
describe_fleet_capacity_paginator: gamelift.DescribeFleetCapacityPaginator = client.get_paginator("describe_fleet_capacity")
describe_fleet_events_paginator: gamelift.DescribeFleetEventsPaginator = client.get_paginator("describe_fleet_events")
describe_fleet_utilization_paginator: gamelift.DescribeFleetUtilizationPaginator = client.get_paginator("describe_fleet_utilization")
describe_game_session_details_paginator: gamelift.DescribeGameSessionDetailsPaginator = client.get_paginator("describe_game_session_details")
describe_game_session_queues_paginator: gamelift.DescribeGameSessionQueuesPaginator = client.get_paginator("describe_game_session_queues")
describe_game_sessions_paginator: gamelift.DescribeGameSessionsPaginator = client.get_paginator("describe_game_sessions")
describe_instances_paginator: gamelift.DescribeInstancesPaginator = client.get_paginator("describe_instances")
describe_matchmaking_configurations_paginator: gamelift.DescribeMatchmakingConfigurationsPaginator = client.get_paginator("describe_matchmaking_configurations")
describe_matchmaking_rule_sets_paginator: gamelift.DescribeMatchmakingRuleSetsPaginator = client.get_paginator("describe_matchmaking_rule_sets")
describe_player_sessions_paginator: gamelift.DescribePlayerSessionsPaginator = client.get_paginator("describe_player_sessions")
describe_scaling_policies_paginator: gamelift.DescribeScalingPoliciesPaginator = client.get_paginator("describe_scaling_policies")
list_aliases_paginator: gamelift.ListAliasesPaginator = client.get_paginator("list_aliases")
list_builds_paginator: gamelift.ListBuildsPaginator = client.get_paginator("list_builds")
list_fleets_paginator: gamelift.ListFleetsPaginator = client.get_paginator("list_fleets")
search_game_sessions_paginator: gamelift.SearchGameSessionsPaginator = client.get_paginator("search_game_sessions")
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