# mypy-boto3-config

Mypy-friendly auto-generated type annotations for `boto3 config 1.10.33` service.
More information can be found [here](https://github.com/vemel/mypy_boto3).

- [mypy-boto3-config](#mypy-boto3-config)
  - [How to use](#how-to-use)
    - [Type checking](#type-checking)
    - [Code auto-complete](#code-auto-complete)
  - [How it works](#how-it-works)

## How to use

### Type checking

Make sure you have [mypy](https://github.com/python/mypy) installed and activated in your IDE.

Install `boto3-stubs` for `config` service.

```bash
pip install boto3-stubs[mypy-boto3-config]
```

Use `boto3` with `mypy_boto3` in your project and enjoy type checking.

```python
import boto3

from mypy_boto3 import config
# alternative import if you do not want to install mypy_boto3 package
# import mypy_boto3_config as config

# Use this client as usual, now mypy can check if your code is valid.
client: config.Client = boto3.client("config")

# works for session as well
session = boto3.session.Session(region="us-west-1")
session_client: config.Client = session.client("config")


# Paginators need type annotation on creation
describe_aggregate_compliance_by_config_rules_paginator: config.DescribeAggregateComplianceByConfigRulesPaginator = client.get_paginator("describe_aggregate_compliance_by_config_rules")
describe_aggregation_authorizations_paginator: config.DescribeAggregationAuthorizationsPaginator = client.get_paginator("describe_aggregation_authorizations")
describe_compliance_by_config_rule_paginator: config.DescribeComplianceByConfigRulePaginator = client.get_paginator("describe_compliance_by_config_rule")
describe_compliance_by_resource_paginator: config.DescribeComplianceByResourcePaginator = client.get_paginator("describe_compliance_by_resource")
describe_config_rule_evaluation_status_paginator: config.DescribeConfigRuleEvaluationStatusPaginator = client.get_paginator("describe_config_rule_evaluation_status")
describe_config_rules_paginator: config.DescribeConfigRulesPaginator = client.get_paginator("describe_config_rules")
describe_configuration_aggregator_sources_status_paginator: config.DescribeConfigurationAggregatorSourcesStatusPaginator = client.get_paginator("describe_configuration_aggregator_sources_status")
describe_configuration_aggregators_paginator: config.DescribeConfigurationAggregatorsPaginator = client.get_paginator("describe_configuration_aggregators")
describe_pending_aggregation_requests_paginator: config.DescribePendingAggregationRequestsPaginator = client.get_paginator("describe_pending_aggregation_requests")
describe_remediation_execution_status_paginator: config.DescribeRemediationExecutionStatusPaginator = client.get_paginator("describe_remediation_execution_status")
describe_retention_configurations_paginator: config.DescribeRetentionConfigurationsPaginator = client.get_paginator("describe_retention_configurations")
get_aggregate_compliance_details_by_config_rule_paginator: config.GetAggregateComplianceDetailsByConfigRulePaginator = client.get_paginator("get_aggregate_compliance_details_by_config_rule")
get_compliance_details_by_config_rule_paginator: config.GetComplianceDetailsByConfigRulePaginator = client.get_paginator("get_compliance_details_by_config_rule")
get_compliance_details_by_resource_paginator: config.GetComplianceDetailsByResourcePaginator = client.get_paginator("get_compliance_details_by_resource")
get_resource_config_history_paginator: config.GetResourceConfigHistoryPaginator = client.get_paginator("get_resource_config_history")
list_aggregate_discovered_resources_paginator: config.ListAggregateDiscoveredResourcesPaginator = client.get_paginator("list_aggregate_discovered_resources")
list_discovered_resources_paginator: config.ListDiscoveredResourcesPaginator = client.get_paginator("list_discovered_resources")
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