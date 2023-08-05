"Main interface for config service Paginators"
from __future__ import annotations

from datetime import datetime
from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3.type_defs import Literal
from mypy_boto3_config.type_defs import (
    DescribeAggregateComplianceByConfigRulesPaginateFiltersTypeDef,
    DescribeAggregateComplianceByConfigRulesPaginatePaginationConfigTypeDef,
    DescribeAggregateComplianceByConfigRulesPaginateResponseTypeDef,
    DescribeAggregationAuthorizationsPaginatePaginationConfigTypeDef,
    DescribeAggregationAuthorizationsPaginateResponseTypeDef,
    DescribeComplianceByConfigRulePaginatePaginationConfigTypeDef,
    DescribeComplianceByConfigRulePaginateResponseTypeDef,
    DescribeComplianceByResourcePaginatePaginationConfigTypeDef,
    DescribeComplianceByResourcePaginateResponseTypeDef,
    DescribeConfigRuleEvaluationStatusPaginatePaginationConfigTypeDef,
    DescribeConfigRuleEvaluationStatusPaginateResponseTypeDef,
    DescribeConfigRulesPaginatePaginationConfigTypeDef,
    DescribeConfigRulesPaginateResponseTypeDef,
    DescribeConfigurationAggregatorSourcesStatusPaginatePaginationConfigTypeDef,
    DescribeConfigurationAggregatorSourcesStatusPaginateResponseTypeDef,
    DescribeConfigurationAggregatorsPaginatePaginationConfigTypeDef,
    DescribeConfigurationAggregatorsPaginateResponseTypeDef,
    DescribePendingAggregationRequestsPaginatePaginationConfigTypeDef,
    DescribePendingAggregationRequestsPaginateResponseTypeDef,
    DescribeRemediationExecutionStatusPaginatePaginationConfigTypeDef,
    DescribeRemediationExecutionStatusPaginateResourceKeysTypeDef,
    DescribeRemediationExecutionStatusPaginateResponseTypeDef,
    DescribeRetentionConfigurationsPaginatePaginationConfigTypeDef,
    DescribeRetentionConfigurationsPaginateResponseTypeDef,
    GetAggregateComplianceDetailsByConfigRulePaginatePaginationConfigTypeDef,
    GetAggregateComplianceDetailsByConfigRulePaginateResponseTypeDef,
    GetComplianceDetailsByConfigRulePaginatePaginationConfigTypeDef,
    GetComplianceDetailsByConfigRulePaginateResponseTypeDef,
    GetComplianceDetailsByResourcePaginatePaginationConfigTypeDef,
    GetComplianceDetailsByResourcePaginateResponseTypeDef,
    GetResourceConfigHistoryPaginatePaginationConfigTypeDef,
    GetResourceConfigHistoryPaginateResponseTypeDef,
    ListAggregateDiscoveredResourcesPaginateFiltersTypeDef,
    ListAggregateDiscoveredResourcesPaginatePaginationConfigTypeDef,
    ListAggregateDiscoveredResourcesPaginateResponseTypeDef,
    ListDiscoveredResourcesPaginatePaginationConfigTypeDef,
    ListDiscoveredResourcesPaginateResponseTypeDef,
)


__all__ = (
    "DescribeAggregateComplianceByConfigRulesPaginator",
    "DescribeAggregationAuthorizationsPaginator",
    "DescribeComplianceByConfigRulePaginator",
    "DescribeComplianceByResourcePaginator",
    "DescribeConfigRuleEvaluationStatusPaginator",
    "DescribeConfigRulesPaginator",
    "DescribeConfigurationAggregatorSourcesStatusPaginator",
    "DescribeConfigurationAggregatorsPaginator",
    "DescribePendingAggregationRequestsPaginator",
    "DescribeRemediationExecutionStatusPaginator",
    "DescribeRetentionConfigurationsPaginator",
    "GetAggregateComplianceDetailsByConfigRulePaginator",
    "GetComplianceDetailsByConfigRulePaginator",
    "GetComplianceDetailsByResourcePaginator",
    "GetResourceConfigHistoryPaginator",
    "ListAggregateDiscoveredResourcesPaginator",
    "ListDiscoveredResourcesPaginator",
)


class DescribeAggregateComplianceByConfigRulesPaginator(Boto3Paginator):
    """
    Paginator for `describe_aggregate_compliance_by_config_rules`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ConfigurationAggregatorName: str,
        Filters: DescribeAggregateComplianceByConfigRulesPaginateFiltersTypeDef = None,
        PaginationConfig: DescribeAggregateComplianceByConfigRulesPaginatePaginationConfigTypeDef = None,
    ) -> DescribeAggregateComplianceByConfigRulesPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`ConfigService.Client.describe_aggregate_compliance_by_config_rules`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/DescribeAggregateComplianceByConfigRules>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              ConfigurationAggregatorName='string',
              Filters={
                  'ConfigRuleName': 'string',
                  'ComplianceType':
                  'COMPLIANT'|'NON_COMPLIANT'|'NOT_APPLICABLE'|'INSUFFICIENT_DATA',
                  'AccountId': 'string',
                  'AwsRegion': 'string'
              },
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type ConfigurationAggregatorName: string
        :param ConfigurationAggregatorName: **[REQUIRED]**

          The name of the configuration aggregator.

        :type Filters: dict
        :param Filters:

          Filters the results by ConfigRuleComplianceFilters object.

          - **ConfigRuleName** *(string) --*

            The name of the AWS Config rule.

          - **ComplianceType** *(string) --*

            The rule compliance status.

            For the ``ConfigRuleComplianceFilters`` data type, AWS Config supports only
            ``COMPLIANT`` and ``NON_COMPLIANT`` . AWS Config does not support the ``NOT_APPLICABLE``
            and the ``INSUFFICIENT_DATA`` values.

          - **AccountId** *(string) --*

            The 12-digit account ID of the source account.

          - **AwsRegion** *(string) --*

            The source region where the data is aggregated.

        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than
            the value specified in max-items then a ``NextToken`` will be provided in the output
            that you can use to resume pagination.

          - **PageSize** *(integer) --*

            The size of each page.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'AggregateComplianceByConfigRules': [
                    {
                        'ConfigRuleName': 'string',
                        'Compliance': {
                            'ComplianceType':
                            'COMPLIANT'|'NON_COMPLIANT'|'NOT_APPLICABLE'
                            |'INSUFFICIENT_DATA',
                            'ComplianceContributorCount': {
                                'CappedCount': 123,
                                'CapExceeded': True|False
                            }
                        },
                        'AccountId': 'string',
                        'AwsRegion': 'string'
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **AggregateComplianceByConfigRules** *(list) --*

              Returns a list of AggregateComplianceByConfigRule object.

              - *(dict) --*

                Indicates whether an AWS Config rule is compliant based on account ID, region,
                compliance, and rule name.

                A rule is compliant if all of the resources that the rule evaluated comply with it.
                It is noncompliant if any of these resources do not comply.

                - **ConfigRuleName** *(string) --*

                  The name of the AWS Config rule.

                - **Compliance** *(dict) --*

                  Indicates whether an AWS resource or AWS Config rule is compliant and provides the
                  number of contributors that affect the compliance.

                  - **ComplianceType** *(string) --*

                    Indicates whether an AWS resource or AWS Config rule is compliant.

                    A resource is compliant if it complies with all of the AWS Config rules that
                    evaluate it. A resource is noncompliant if it does not comply with one or more
                    of these rules.

                    A rule is compliant if all of the resources that the rule evaluates comply with
                    it. A rule is noncompliant if any of these resources do not comply.

                    AWS Config returns the ``INSUFFICIENT_DATA`` value when no evaluation results
                    are available for the AWS resource or AWS Config rule.

                    For the ``Compliance`` data type, AWS Config supports only ``COMPLIANT`` ,
                    ``NON_COMPLIANT`` , and ``INSUFFICIENT_DATA`` values. AWS Config does not
                    support the ``NOT_APPLICABLE`` value for the ``Compliance`` data type.

                  - **ComplianceContributorCount** *(dict) --*

                    The number of AWS resources or AWS Config rules that cause a result of
                    ``NON_COMPLIANT`` , up to a maximum number.

                    - **CappedCount** *(integer) --*

                      The number of AWS resources or AWS Config rules responsible for the current
                      compliance of the item.

                    - **CapExceeded** *(boolean) --*

                      Indicates whether the maximum count is reached.

                - **AccountId** *(string) --*

                  The 12-digit account ID of the source account.

                - **AwsRegion** *(string) --*

                  The source region from where the data is aggregated.
        """


class DescribeAggregationAuthorizationsPaginator(Boto3Paginator):
    """
    Paginator for `describe_aggregation_authorizations`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        PaginationConfig: DescribeAggregationAuthorizationsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeAggregationAuthorizationsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`ConfigService.Client.describe_aggregation_authorizations`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/DescribeAggregationAuthorizations>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than
            the value specified in max-items then a ``NextToken`` will be provided in the output
            that you can use to resume pagination.

          - **PageSize** *(integer) --*

            The size of each page.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'AggregationAuthorizations': [
                    {
                        'AggregationAuthorizationArn': 'string',
                        'AuthorizedAccountId': 'string',
                        'AuthorizedAwsRegion': 'string',
                        'CreationTime': datetime(2015, 1, 1)
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **AggregationAuthorizations** *(list) --*

              Returns a list of authorizations granted to various aggregator accounts and regions.

              - *(dict) --*

                An object that represents the authorizations granted to aggregator accounts and
                regions.

                - **AggregationAuthorizationArn** *(string) --*

                  The Amazon Resource Name (ARN) of the aggregation object.

                - **AuthorizedAccountId** *(string) --*

                  The 12-digit account ID of the account authorized to aggregate data.

                - **AuthorizedAwsRegion** *(string) --*

                  The region authorized to collect aggregated data.

                - **CreationTime** *(datetime) --*

                  The time stamp when the aggregation authorization was created.
        """


class DescribeComplianceByConfigRulePaginator(Boto3Paginator):
    """
    Paginator for `describe_compliance_by_config_rule`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ConfigRuleNames: List[str] = None,
        ComplianceTypes: List[
            Literal["COMPLIANT", "NON_COMPLIANT", "NOT_APPLICABLE", "INSUFFICIENT_DATA"]
        ] = None,
        PaginationConfig: DescribeComplianceByConfigRulePaginatePaginationConfigTypeDef = None,
    ) -> DescribeComplianceByConfigRulePaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`ConfigService.Client.describe_compliance_by_config_rule`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/DescribeComplianceByConfigRule>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              ConfigRuleNames=[
                  'string',
              ],
              ComplianceTypes=[
                  'COMPLIANT'|'NON_COMPLIANT'|'NOT_APPLICABLE'|'INSUFFICIENT_DATA',
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'StartingToken': 'string'
              }
          )
        :type ConfigRuleNames: list
        :param ConfigRuleNames:

          Specify one or more AWS Config rule names to filter the results by rule.

          - *(string) --*

        :type ComplianceTypes: list
        :param ComplianceTypes:

          Filters the results by compliance.

          The allowed values are ``COMPLIANT`` and ``NON_COMPLIANT`` .

          - *(string) --*

        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than
            the value specified in max-items then a ``NextToken`` will be provided in the output
            that you can use to resume pagination.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ComplianceByConfigRules': [
                    {
                        'ConfigRuleName': 'string',
                        'Compliance': {
                            'ComplianceType':
                            'COMPLIANT'|'NON_COMPLIANT'|'NOT_APPLICABLE'
                            |'INSUFFICIENT_DATA',
                            'ComplianceContributorCount': {
                                'CappedCount': 123,
                                'CapExceeded': True|False
                            }
                        }
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **ComplianceByConfigRules** *(list) --*

              Indicates whether each of the specified AWS Config rules is compliant.

              - *(dict) --*

                Indicates whether an AWS Config rule is compliant. A rule is compliant if all of the
                resources that the rule evaluated comply with it. A rule is noncompliant if any of
                these resources do not comply.

                - **ConfigRuleName** *(string) --*

                  The name of the AWS Config rule.

                - **Compliance** *(dict) --*

                  Indicates whether the AWS Config rule is compliant.

                  - **ComplianceType** *(string) --*

                    Indicates whether an AWS resource or AWS Config rule is compliant.

                    A resource is compliant if it complies with all of the AWS Config rules that
                    evaluate it. A resource is noncompliant if it does not comply with one or more
                    of these rules.

                    A rule is compliant if all of the resources that the rule evaluates comply with
                    it. A rule is noncompliant if any of these resources do not comply.

                    AWS Config returns the ``INSUFFICIENT_DATA`` value when no evaluation results
                    are available for the AWS resource or AWS Config rule.

                    For the ``Compliance`` data type, AWS Config supports only ``COMPLIANT`` ,
                    ``NON_COMPLIANT`` , and ``INSUFFICIENT_DATA`` values. AWS Config does not
                    support the ``NOT_APPLICABLE`` value for the ``Compliance`` data type.

                  - **ComplianceContributorCount** *(dict) --*

                    The number of AWS resources or AWS Config rules that cause a result of
                    ``NON_COMPLIANT`` , up to a maximum number.

                    - **CappedCount** *(integer) --*

                      The number of AWS resources or AWS Config rules responsible for the current
                      compliance of the item.

                    - **CapExceeded** *(boolean) --*

                      Indicates whether the maximum count is reached.
        """


class DescribeComplianceByResourcePaginator(Boto3Paginator):
    """
    Paginator for `describe_compliance_by_resource`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ResourceType: str = None,
        ResourceId: str = None,
        ComplianceTypes: List[
            Literal["COMPLIANT", "NON_COMPLIANT", "NOT_APPLICABLE", "INSUFFICIENT_DATA"]
        ] = None,
        Limit: int = None,
        PaginationConfig: DescribeComplianceByResourcePaginatePaginationConfigTypeDef = None,
    ) -> DescribeComplianceByResourcePaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`ConfigService.Client.describe_compliance_by_resource`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/DescribeComplianceByResource>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              ResourceType='string',
              ResourceId='string',
              ComplianceTypes=[
                  'COMPLIANT'|'NON_COMPLIANT'|'NOT_APPLICABLE'|'INSUFFICIENT_DATA',
              ],
              Limit=123,
              PaginationConfig={
                  'MaxItems': 123,
                  'StartingToken': 'string'
              }
          )
        :type ResourceType: string
        :param ResourceType:

          The types of AWS resources for which you want compliance information (for example,
          ``AWS::EC2::Instance`` ). For this action, you can specify that the resource type is an
          AWS account by specifying ``AWS::::Account`` .

        :type ResourceId: string
        :param ResourceId:

          The ID of the AWS resource for which you want compliance information. You can specify only
          one resource ID. If you specify a resource ID, you must also specify a type for
          ``ResourceType`` .

        :type ComplianceTypes: list
        :param ComplianceTypes:

          Filters the results by compliance.

          The allowed values are ``COMPLIANT`` , ``NON_COMPLIANT`` , and ``INSUFFICIENT_DATA`` .

          - *(string) --*

        :type Limit: integer
        :param Limit:

          The maximum number of evaluation results returned on each page. The default is 10. You
          cannot specify a number greater than 100. If you specify 0, AWS Config uses the default.

        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than
            the value specified in max-items then a ``NextToken`` will be provided in the output
            that you can use to resume pagination.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ComplianceByResources': [
                    {
                        'ResourceType': 'string',
                        'ResourceId': 'string',
                        'Compliance': {
                            'ComplianceType':
                            'COMPLIANT'|'NON_COMPLIANT'|'NOT_APPLICABLE'
                            |'INSUFFICIENT_DATA',
                            'ComplianceContributorCount': {
                                'CappedCount': 123,
                                'CapExceeded': True|False
                            }
                        }
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **ComplianceByResources** *(list) --*

              Indicates whether the specified AWS resource complies with all of the AWS Config rules
              that evaluate it.

              - *(dict) --*

                Indicates whether an AWS resource that is evaluated according to one or more AWS
                Config rules is compliant. A resource is compliant if it complies with all of the
                rules that evaluate it. A resource is noncompliant if it does not comply with one or
                more of these rules.

                - **ResourceType** *(string) --*

                  The type of the AWS resource that was evaluated.

                - **ResourceId** *(string) --*

                  The ID of the AWS resource that was evaluated.

                - **Compliance** *(dict) --*

                  Indicates whether the AWS resource complies with all of the AWS Config rules that
                  evaluated it.

                  - **ComplianceType** *(string) --*

                    Indicates whether an AWS resource or AWS Config rule is compliant.

                    A resource is compliant if it complies with all of the AWS Config rules that
                    evaluate it. A resource is noncompliant if it does not comply with one or more
                    of these rules.

                    A rule is compliant if all of the resources that the rule evaluates comply with
                    it. A rule is noncompliant if any of these resources do not comply.

                    AWS Config returns the ``INSUFFICIENT_DATA`` value when no evaluation results
                    are available for the AWS resource or AWS Config rule.

                    For the ``Compliance`` data type, AWS Config supports only ``COMPLIANT`` ,
                    ``NON_COMPLIANT`` , and ``INSUFFICIENT_DATA`` values. AWS Config does not
                    support the ``NOT_APPLICABLE`` value for the ``Compliance`` data type.

                  - **ComplianceContributorCount** *(dict) --*

                    The number of AWS resources or AWS Config rules that cause a result of
                    ``NON_COMPLIANT`` , up to a maximum number.

                    - **CappedCount** *(integer) --*

                      The number of AWS resources or AWS Config rules responsible for the current
                      compliance of the item.

                    - **CapExceeded** *(boolean) --*

                      Indicates whether the maximum count is reached.
        """


class DescribeConfigRuleEvaluationStatusPaginator(Boto3Paginator):
    """
    Paginator for `describe_config_rule_evaluation_status`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ConfigRuleNames: List[str] = None,
        PaginationConfig: DescribeConfigRuleEvaluationStatusPaginatePaginationConfigTypeDef = None,
    ) -> DescribeConfigRuleEvaluationStatusPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`ConfigService.Client.describe_config_rule_evaluation_status`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/DescribeConfigRuleEvaluationStatus>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              ConfigRuleNames=[
                  'string',
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type ConfigRuleNames: list
        :param ConfigRuleNames:

          The name of the AWS managed Config rules for which you want status information. If you do
          not specify any names, AWS Config returns status information for all AWS managed Config
          rules that you use.

          - *(string) --*

        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than
            the value specified in max-items then a ``NextToken`` will be provided in the output
            that you can use to resume pagination.

          - **PageSize** *(integer) --*

            The size of each page.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ConfigRulesEvaluationStatus': [
                    {
                        'ConfigRuleName': 'string',
                        'ConfigRuleArn': 'string',
                        'ConfigRuleId': 'string',
                        'LastSuccessfulInvocationTime': datetime(2015, 1, 1),
                        'LastFailedInvocationTime': datetime(2015, 1, 1),
                        'LastSuccessfulEvaluationTime': datetime(2015, 1, 1),
                        'LastFailedEvaluationTime': datetime(2015, 1, 1),
                        'FirstActivatedTime': datetime(2015, 1, 1),
                        'LastErrorCode': 'string',
                        'LastErrorMessage': 'string',
                        'FirstEvaluationStarted': True|False
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **ConfigRulesEvaluationStatus** *(list) --*

              Status information about your AWS managed Config rules.

              - *(dict) --*

                Status information for your AWS managed Config rules. The status includes
                information such as the last time the rule ran, the last time it failed, and the
                related error for the last failure.

                This action does not return status information about custom AWS Config rules.

                - **ConfigRuleName** *(string) --*

                  The name of the AWS Config rule.

                - **ConfigRuleArn** *(string) --*

                  The Amazon Resource Name (ARN) of the AWS Config rule.

                - **ConfigRuleId** *(string) --*

                  The ID of the AWS Config rule.

                - **LastSuccessfulInvocationTime** *(datetime) --*

                  The time that AWS Config last successfully invoked the AWS Config rule to evaluate
                  your AWS resources.

                - **LastFailedInvocationTime** *(datetime) --*

                  The time that AWS Config last failed to invoke the AWS Config rule to evaluate
                  your AWS resources.

                - **LastSuccessfulEvaluationTime** *(datetime) --*

                  The time that AWS Config last successfully evaluated your AWS resources against
                  the rule.

                - **LastFailedEvaluationTime** *(datetime) --*

                  The time that AWS Config last failed to evaluate your AWS resources against the
                  rule.

                - **FirstActivatedTime** *(datetime) --*

                  The time that you first activated the AWS Config rule.

                - **LastErrorCode** *(string) --*

                  The error code that AWS Config returned when the rule last failed.

                - **LastErrorMessage** *(string) --*

                  The error message that AWS Config returned when the rule last failed.

                - **FirstEvaluationStarted** *(boolean) --*

                  Indicates whether AWS Config has evaluated your resources against the rule at
                  least once.

                  * ``true`` - AWS Config has evaluated your AWS resources against the rule at least
                  once.

                  * ``false`` - AWS Config has not once finished evaluating your AWS resources
                  against the rule.
        """


class DescribeConfigRulesPaginator(Boto3Paginator):
    """
    Paginator for `describe_config_rules`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ConfigRuleNames: List[str] = None,
        PaginationConfig: DescribeConfigRulesPaginatePaginationConfigTypeDef = None,
    ) -> DescribeConfigRulesPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`ConfigService.Client.describe_config_rules`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/DescribeConfigRules>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              ConfigRuleNames=[
                  'string',
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'StartingToken': 'string'
              }
          )
        :type ConfigRuleNames: list
        :param ConfigRuleNames:

          The names of the AWS Config rules for which you want details. If you do not specify any
          names, AWS Config returns details for all your rules.

          - *(string) --*

        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than
            the value specified in max-items then a ``NextToken`` will be provided in the output
            that you can use to resume pagination.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ConfigRules': [
                    {
                        'ConfigRuleName': 'string',
                        'ConfigRuleArn': 'string',
                        'ConfigRuleId': 'string',
                        'Description': 'string',
                        'Scope': {
                            'ComplianceResourceTypes': [
                                'string',
                            ],
                            'TagKey': 'string',
                            'TagValue': 'string',
                            'ComplianceResourceId': 'string'
                        },
                        'Source': {
                            'Owner': 'CUSTOM_LAMBDA'|'AWS',
                            'SourceIdentifier': 'string',
                            'SourceDetails': [
                                {
                                    'EventSource': 'aws.config',
                                    'MessageType':
                                    'ConfigurationItemChangeNotification'|'ConfigurationSnapshotDeliveryCompleted'|'ScheduledNotification'
                                    |'OversizedConfigurationItemChangeNotification',
                                    'MaximumExecutionFrequency':
                                    'One_Hour'|'Three_Hours'|'Six_Hours'
                                    |'Twelve_Hours'|'TwentyFour_Hours'
                                },
                            ]
                        },
                        'InputParameters': 'string',
                        'MaximumExecutionFrequency':
                        'One_Hour'|'Three_Hours'|'Six_Hours'|'Twelve_Hours'
                        |'TwentyFour_Hours',
                        'ConfigRuleState': 'ACTIVE'|'DELETING'|'DELETING_RESULTS'|'EVALUATING',
                        'CreatedBy': 'string'
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **ConfigRules** *(list) --*

              The details about your AWS Config rules.

              - *(dict) --*

                An AWS Config rule represents an AWS Lambda function that you create for a custom
                rule or a predefined function for an AWS managed rule. The function evaluates
                configuration items to assess whether your AWS resources comply with your desired
                configurations. This function can run when AWS Config detects a configuration change
                to an AWS resource and at a periodic frequency that you choose (for example, every
                24 hours).

                .. note::

                  You can use the AWS CLI and AWS SDKs if you want to create a rule that triggers
                  evaluations for your resources when AWS Config delivers the configuration
                  snapshot. For more information, see  ConfigSnapshotDeliveryProperties .

                For more information about developing and using AWS Config rules, see `Evaluating
                AWS Resource Configurations with AWS Config
                <https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config.html>`__
                in the *AWS Config Developer Guide* .

                - **ConfigRuleName** *(string) --*

                  The name that you assign to the AWS Config rule. The name is required if you are
                  adding a new rule.

                - **ConfigRuleArn** *(string) --*

                  The Amazon Resource Name (ARN) of the AWS Config rule.

                - **ConfigRuleId** *(string) --*

                  The ID of the AWS Config rule.

                - **Description** *(string) --*

                  The description that you provide for the AWS Config rule.

                - **Scope** *(dict) --*

                  Defines which resources can trigger an evaluation for the rule. The scope can
                  include one or more resource types, a combination of one resource type and one
                  resource ID, or a combination of a tag key and value. Specify a scope to constrain
                  the resources that can trigger an evaluation for the rule. If you do not specify a
                  scope, evaluations are triggered when any resource in the recording group changes.

                  - **ComplianceResourceTypes** *(list) --*

                    The resource types of only those AWS resources that you want to trigger an
                    evaluation for the rule. You can only specify one type if you also specify a
                    resource ID for ``ComplianceResourceId`` .

                    - *(string) --*

                  - **TagKey** *(string) --*

                    The tag key that is applied to only those AWS resources that you want to trigger
                    an evaluation for the rule.

                  - **TagValue** *(string) --*

                    The tag value applied to only those AWS resources that you want to trigger an
                    evaluation for the rule. If you specify a value for ``TagValue`` , you must also
                    specify a value for ``TagKey`` .

                  - **ComplianceResourceId** *(string) --*

                    The ID of the only AWS resource that you want to trigger an evaluation for the
                    rule. If you specify a resource ID, you must specify one resource type for
                    ``ComplianceResourceTypes`` .

                - **Source** *(dict) --*

                  Provides the rule owner (AWS or customer), the rule identifier, and the
                  notifications that cause the function to evaluate your AWS resources.

                  - **Owner** *(string) --*

                    Indicates whether AWS or the customer owns and manages the AWS Config rule.

                  - **SourceIdentifier** *(string) --*

                    For AWS Config managed rules, a predefined identifier from a list. For example,
                    ``IAM_PASSWORD_POLICY`` is a managed rule. To reference a managed rule, see
                    `Using AWS Managed Config Rules
                    <https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_use-managed-rules.html>`__
                    .

                    For custom rules, the identifier is the Amazon Resource Name (ARN) of the rule's
                    AWS Lambda function, such as
                    ``arn:aws:lambda:us-east-2:123456789012:function:custom_rule_name`` .

                  - **SourceDetails** *(list) --*

                    Provides the source and type of the event that causes AWS Config to evaluate
                    your AWS resources.

                    - *(dict) --*

                      Provides the source and the message types that trigger AWS Config to evaluate
                      your AWS resources against a rule. It also provides the frequency with which
                      you want AWS Config to run evaluations for the rule if the trigger type is
                      periodic. You can specify the parameter values for ``SourceDetail`` only for
                      custom rules.

                      - **EventSource** *(string) --*

                        The source of the event, such as an AWS service, that triggers AWS Config to
                        evaluate your AWS resources.

                      - **MessageType** *(string) --*

                        The type of notification that triggers AWS Config to run an evaluation for a
                        rule. You can specify the following notification types:

                        * ``ConfigurationItemChangeNotification`` - Triggers an evaluation when AWS
                        Config delivers a configuration item as a result of a resource change.

                        * ``OversizedConfigurationItemChangeNotification`` - Triggers an evaluation
                        when AWS Config delivers an oversized configuration item. AWS Config may
                        generate this notification type when a resource changes and the notification
                        exceeds the maximum size allowed by Amazon SNS.

                        * ``ScheduledNotification`` - Triggers a periodic evaluation at the
                        frequency specified for ``MaximumExecutionFrequency`` .

                        * ``ConfigurationSnapshotDeliveryCompleted`` - Triggers a periodic
                        evaluation when AWS Config delivers a configuration snapshot.

                        If you want your custom rule to be triggered by configuration changes,
                        specify two SourceDetail objects, one for
                        ``ConfigurationItemChangeNotification`` and one for
                        ``OversizedConfigurationItemChangeNotification`` .

                      - **MaximumExecutionFrequency** *(string) --*

                        The frequency at which you want AWS Config to run evaluations for a custom
                        rule with a periodic trigger. If you specify a value for
                        ``MaximumExecutionFrequency`` , then ``MessageType`` must use the
                        ``ScheduledNotification`` value.

                        .. note::

                          By default, rules with a periodic trigger are evaluated every 24 hours. To
                          change the frequency, specify a valid value for the
                          ``MaximumExecutionFrequency`` parameter.

                          Based on the valid value you choose, AWS Config runs evaluations once for
                          each valid value. For example, if you choose ``Three_Hours`` , AWS Config
                          runs evaluations once every three hours. In this case, ``Three_Hours`` is
                          the frequency of this rule.

                - **InputParameters** *(string) --*

                  A string, in JSON format, that is passed to the AWS Config rule Lambda function.

                - **MaximumExecutionFrequency** *(string) --*

                  The maximum frequency with which AWS Config runs evaluations for a rule. You can
                  specify a value for ``MaximumExecutionFrequency`` when:

                  * You are using an AWS managed rule that is triggered at a periodic frequency.

                  * Your custom rule is triggered when AWS Config delivers the configuration
                  snapshot. For more information, see  ConfigSnapshotDeliveryProperties .

                  .. note::

                    By default, rules with a periodic trigger are evaluated every 24 hours. To
                    change the frequency, specify a valid value for the
                    ``MaximumExecutionFrequency`` parameter.

                - **ConfigRuleState** *(string) --*

                  Indicates whether the AWS Config rule is active or is currently being deleted by
                  AWS Config. It can also indicate the evaluation status for the AWS Config rule.

                  AWS Config sets the state of the rule to ``EVALUATING`` temporarily after you use
                  the ``StartConfigRulesEvaluation`` request to evaluate your resources against the
                  AWS Config rule.

                  AWS Config sets the state of the rule to ``DELETING_RESULTS`` temporarily after
                  you use the ``DeleteEvaluationResults`` request to delete the current evaluation
                  results for the AWS Config rule.

                  AWS Config temporarily sets the state of a rule to ``DELETING`` after you use the
                  ``DeleteConfigRule`` request to delete the rule. After AWS Config deletes the
                  rule, the rule and all of its evaluations are erased and are no longer available.

                - **CreatedBy** *(string) --*

                  Service principal name of the service that created the rule.

                  .. note::

                    The field is populated only if the service linked rule is created by a service.
                    The field is empty if you create your own rule.
        """


class DescribeConfigurationAggregatorSourcesStatusPaginator(Boto3Paginator):
    """
    Paginator for `describe_configuration_aggregator_sources_status`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ConfigurationAggregatorName: str,
        UpdateStatus: List[Literal["FAILED", "SUCCEEDED", "OUTDATED"]] = None,
        PaginationConfig: DescribeConfigurationAggregatorSourcesStatusPaginatePaginationConfigTypeDef = None,
    ) -> DescribeConfigurationAggregatorSourcesStatusPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`ConfigService.Client.describe_configuration_aggregator_sources_status`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/DescribeConfigurationAggregatorSourcesStatus>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              ConfigurationAggregatorName='string',
              UpdateStatus=[
                  'FAILED'|'SUCCEEDED'|'OUTDATED',
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type ConfigurationAggregatorName: string
        :param ConfigurationAggregatorName: **[REQUIRED]**

          The name of the configuration aggregator.

        :type UpdateStatus: list
        :param UpdateStatus:

          Filters the status type.

          * Valid value FAILED indicates errors while moving data.

          * Valid value SUCCEEDED indicates the data was successfully moved.

          * Valid value OUTDATED indicates the data is not the most recent.

          - *(string) --*

        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than
            the value specified in max-items then a ``NextToken`` will be provided in the output
            that you can use to resume pagination.

          - **PageSize** *(integer) --*

            The size of each page.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'AggregatedSourceStatusList': [
                    {
                        'SourceId': 'string',
                        'SourceType': 'ACCOUNT'|'ORGANIZATION',
                        'AwsRegion': 'string',
                        'LastUpdateStatus': 'FAILED'|'SUCCEEDED'|'OUTDATED',
                        'LastUpdateTime': datetime(2015, 1, 1),
                        'LastErrorCode': 'string',
                        'LastErrorMessage': 'string'
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **AggregatedSourceStatusList** *(list) --*

              Returns an AggregatedSourceStatus object.

              - *(dict) --*

                The current sync status between the source and the aggregator account.

                - **SourceId** *(string) --*

                  The source account ID or an organization.

                - **SourceType** *(string) --*

                  The source account or an organization.

                - **AwsRegion** *(string) --*

                  The region authorized to collect aggregated data.

                - **LastUpdateStatus** *(string) --*

                  Filters the last updated status type.

                  * Valid value FAILED indicates errors while moving data.

                  * Valid value SUCCEEDED indicates the data was successfully moved.

                  * Valid value OUTDATED indicates the data is not the most recent.

                - **LastUpdateTime** *(datetime) --*

                  The time of the last update.

                - **LastErrorCode** *(string) --*

                  The error code that AWS Config returned when the source account aggregation last
                  failed.

                - **LastErrorMessage** *(string) --*

                  The message indicating that the source account aggregation failed due to an error.
        """


class DescribeConfigurationAggregatorsPaginator(Boto3Paginator):
    """
    Paginator for `describe_configuration_aggregators`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ConfigurationAggregatorNames: List[str] = None,
        PaginationConfig: DescribeConfigurationAggregatorsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeConfigurationAggregatorsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`ConfigService.Client.describe_configuration_aggregators`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/DescribeConfigurationAggregators>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              ConfigurationAggregatorNames=[
                  'string',
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type ConfigurationAggregatorNames: list
        :param ConfigurationAggregatorNames:

          The name of the configuration aggregators.

          - *(string) --*

        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than
            the value specified in max-items then a ``NextToken`` will be provided in the output
            that you can use to resume pagination.

          - **PageSize** *(integer) --*

            The size of each page.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ConfigurationAggregators': [
                    {
                        'ConfigurationAggregatorName': 'string',
                        'ConfigurationAggregatorArn': 'string',
                        'AccountAggregationSources': [
                            {
                                'AccountIds': [
                                    'string',
                                ],
                                'AllAwsRegions': True|False,
                                'AwsRegions': [
                                    'string',
                                ]
                            },
                        ],
                        'OrganizationAggregationSource': {
                            'RoleArn': 'string',
                            'AwsRegions': [
                                'string',
                            ],
                            'AllAwsRegions': True|False
                        },
                        'CreationTime': datetime(2015, 1, 1),
                        'LastUpdatedTime': datetime(2015, 1, 1)
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **ConfigurationAggregators** *(list) --*

              Returns a ConfigurationAggregators object.

              - *(dict) --*

                The details about the configuration aggregator, including information about source
                accounts, regions, and metadata of the aggregator.

                - **ConfigurationAggregatorName** *(string) --*

                  The name of the aggregator.

                - **ConfigurationAggregatorArn** *(string) --*

                  The Amazon Resource Name (ARN) of the aggregator.

                - **AccountAggregationSources** *(list) --*

                  Provides a list of source accounts and regions to be aggregated.

                  - *(dict) --*

                    A collection of accounts and regions.

                    - **AccountIds** *(list) --*

                      The 12-digit account ID of the account being aggregated.

                      - *(string) --*

                    - **AllAwsRegions** *(boolean) --*

                      If true, aggregate existing AWS Config regions and future regions.

                    - **AwsRegions** *(list) --*

                      The source regions being aggregated.

                      - *(string) --*

                - **OrganizationAggregationSource** *(dict) --*

                  Provides an organization and list of regions to be aggregated.

                  - **RoleArn** *(string) --*

                    ARN of the IAM role used to retrieve AWS Organization details associated with
                    the aggregator account.

                  - **AwsRegions** *(list) --*

                    The source regions being aggregated.

                    - *(string) --*

                  - **AllAwsRegions** *(boolean) --*

                    If true, aggregate existing AWS Config regions and future regions.

                - **CreationTime** *(datetime) --*

                  The time stamp when the configuration aggregator was created.

                - **LastUpdatedTime** *(datetime) --*

                  The time of the last update.
        """


class DescribePendingAggregationRequestsPaginator(Boto3Paginator):
    """
    Paginator for `describe_pending_aggregation_requests`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        PaginationConfig: DescribePendingAggregationRequestsPaginatePaginationConfigTypeDef = None,
    ) -> DescribePendingAggregationRequestsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`ConfigService.Client.describe_pending_aggregation_requests`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/DescribePendingAggregationRequests>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than
            the value specified in max-items then a ``NextToken`` will be provided in the output
            that you can use to resume pagination.

          - **PageSize** *(integer) --*

            The size of each page.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'PendingAggregationRequests': [
                    {
                        'RequesterAccountId': 'string',
                        'RequesterAwsRegion': 'string'
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **PendingAggregationRequests** *(list) --*

              Returns a PendingAggregationRequests object.

              - *(dict) --*

                An object that represents the account ID and region of an aggregator account that is
                requesting authorization but is not yet authorized.

                - **RequesterAccountId** *(string) --*

                  The 12-digit account ID of the account requesting to aggregate data.

                - **RequesterAwsRegion** *(string) --*

                  The region requesting to aggregate data.
        """


class DescribeRemediationExecutionStatusPaginator(Boto3Paginator):
    """
    Paginator for `describe_remediation_execution_status`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ConfigRuleName: str,
        ResourceKeys: List[DescribeRemediationExecutionStatusPaginateResourceKeysTypeDef] = None,
        PaginationConfig: DescribeRemediationExecutionStatusPaginatePaginationConfigTypeDef = None,
    ) -> DescribeRemediationExecutionStatusPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`ConfigService.Client.describe_remediation_execution_status`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/DescribeRemediationExecutionStatus>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              ConfigRuleName='string',
              ResourceKeys=[
                  {
                      'resourceType':
                      'AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'
                      |'AWS::EC2::Instance'|'AWS::EC2::InternetGateway'
                      |'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'
                      |'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'
                      |'AWS::EC2::Subnet'|'AWS::CloudTrail::Trail'|'AWS::EC2::Volume'
                      |'AWS::EC2::VPC'|'AWS::EC2::VPNConnection'
                      |'AWS::EC2::VPNGateway'|'AWS::EC2::RegisteredHAInstance'
                      |'AWS::EC2::NatGateway'|'AWS::EC2::EgressOnlyInternetGateway'
                      |'AWS::EC2::VPCEndpoint'|'AWS::EC2::VPCEndpointService'
                      |'AWS::EC2::FlowLog'|'AWS::EC2::VPCPeeringConnection'
                      |'AWS::IAM::Group'|'AWS::IAM::Policy'|'AWS::IAM::Role'
                      |'AWS::IAM::User'|'AWS::ElasticLoadBalancingV2::LoadBalancer'
                      |'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'
                      |'AWS::RDS::DBParameterGroup'|'AWS::RDS::DBOptionGroup'
                      |'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'
                      |'AWS::RDS::DBSnapshot'|'AWS::RDS::DBCluster'
                      |'AWS::RDS::DBClusterParameterGroup'
                      |'AWS::RDS::DBClusterSnapshot'|'AWS::RDS::EventSubscription'
                      |'AWS::S3::Bucket'|'AWS::S3::AccountPublicAccessBlock'
                      |'AWS::Redshift::Cluster'|'AWS::Redshift::ClusterSnapshot'
                      |'AWS::Redshift::ClusterParameterGroup'
                      |'AWS::Redshift::ClusterSecurityGroup'
                      |'AWS::Redshift::ClusterSubnetGroup'
                      |'AWS::Redshift::EventSubscription'
                      |'AWS::SSM::ManagedInstanceInventory'|'AWS::CloudWatch::Alarm'
                      |'AWS::CloudFormation::Stack'
                      |'AWS::ElasticLoadBalancing::LoadBalancer'
                      |'AWS::AutoScaling::AutoScalingGroup'
                      |'AWS::AutoScaling::LaunchConfiguration'
                      |'AWS::AutoScaling::ScalingPolicy'
                      |'AWS::AutoScaling::ScheduledAction'|'AWS::DynamoDB::Table'
                      |'AWS::CodeBuild::Project'|'AWS::WAF::RateBasedRule'
                      |'AWS::WAF::Rule'|'AWS::WAF::RuleGroup'|'AWS::WAF::WebACL'
                      |'AWS::WAFRegional::RateBasedRule'|'AWS::WAFRegional::Rule'
                      |'AWS::WAFRegional::RuleGroup'|'AWS::WAFRegional::WebACL'
                      |'AWS::CloudFront::Distribution'
                      |'AWS::CloudFront::StreamingDistribution'|'AWS::Lambda::Alias'
                      |'AWS::Lambda::Function'|'AWS::ElasticBeanstalk::Application'
                      |'AWS::ElasticBeanstalk::ApplicationVersion'
                      |'AWS::ElasticBeanstalk::Environment'|'AWS::MobileHub::Project'
                      |'AWS::XRay::EncryptionConfig'|'AWS::SSM::AssociationCompliance'
                      |'AWS::SSM::PatchCompliance'|'AWS::Shield::Protection'
                      |'AWS::ShieldRegional::Protection'
                      |'AWS::Config::ResourceCompliance'
                      |'AWS::LicenseManager::LicenseConfiguration'
                      |'AWS::ApiGateway::DomainName'|'AWS::ApiGateway::Method'
                      |'AWS::ApiGateway::Stage'|'AWS::ApiGateway::RestApi'
                      |'AWS::ApiGatewayV2::DomainName'|'AWS::ApiGatewayV2::Stage'
                      |'AWS::ApiGatewayV2::Api'|'AWS::CodePipeline::Pipeline'
                      |'AWS::ServiceCatalog::CloudFormationProvisionedProduct'
                      |'AWS::ServiceCatalog::CloudFormationProduct'
                      |'AWS::ServiceCatalog::Portfolio',
                      'resourceId': 'string'
                  },
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type ConfigRuleName: string
        :param ConfigRuleName: **[REQUIRED]**

          A list of AWS Config rule names.

        :type ResourceKeys: list
        :param ResourceKeys:

          A list of resource keys to be processed with the current request. Each element in the list
          consists of the resource type and resource ID.

          - *(dict) --*

            The details that identify a resource within AWS Config, including the resource type and
            resource ID.

            - **resourceType** *(string) --* **[REQUIRED]**

              The resource type.

            - **resourceId** *(string) --* **[REQUIRED]**

              The ID of the resource (for example., sg-xxxxxx).

        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than
            the value specified in max-items then a ``NextToken`` will be provided in the output
            that you can use to resume pagination.

          - **PageSize** *(integer) --*

            The size of each page.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'RemediationExecutionStatuses': [
                    {
                        'ResourceKey': {
                            'resourceType':
                            'AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'
                            |'AWS::EC2::Host'|'AWS::EC2::Instance'
                            |'AWS::EC2::InternetGateway'|'AWS::EC2::NetworkAcl'
                            |'AWS::EC2::NetworkInterface'|'AWS::EC2::RouteTable'
                            |'AWS::EC2::SecurityGroup'|'AWS::EC2::Subnet'
                            |'AWS::CloudTrail::Trail'|'AWS::EC2::Volume'
                            |'AWS::EC2::VPC'|'AWS::EC2::VPNConnection'
                            |'AWS::EC2::VPNGateway'
                            |'AWS::EC2::RegisteredHAInstance'
                            |'AWS::EC2::NatGateway'
                            |'AWS::EC2::EgressOnlyInternetGateway'
                            |'AWS::EC2::VPCEndpoint'
                            |'AWS::EC2::VPCEndpointService'|'AWS::EC2::FlowLog'
                            |'AWS::EC2::VPCPeeringConnection'|'AWS::IAM::Group'
                            |'AWS::IAM::Policy'|'AWS::IAM::Role'
                            |'AWS::IAM::User'
                            |'AWS::ElasticLoadBalancingV2::LoadBalancer'
                            |'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'
                            |'AWS::RDS::DBParameterGroup'
                            |'AWS::RDS::DBOptionGroup'|'AWS::RDS::DBSubnetGroup'
                            |'AWS::RDS::DBSecurityGroup'|'AWS::RDS::DBSnapshot'
                            |'AWS::RDS::DBCluster'
                            |'AWS::RDS::DBClusterParameterGroup'
                            |'AWS::RDS::DBClusterSnapshot'
                            |'AWS::RDS::EventSubscription'|'AWS::S3::Bucket'
                            |'AWS::S3::AccountPublicAccessBlock'
                            |'AWS::Redshift::Cluster'
                            |'AWS::Redshift::ClusterSnapshot'
                            |'AWS::Redshift::ClusterParameterGroup'
                            |'AWS::Redshift::ClusterSecurityGroup'
                            |'AWS::Redshift::ClusterSubnetGroup'
                            |'AWS::Redshift::EventSubscription'
                            |'AWS::SSM::ManagedInstanceInventory'
                            |'AWS::CloudWatch::Alarm'
                            |'AWS::CloudFormation::Stack'
                            |'AWS::ElasticLoadBalancing::LoadBalancer'
                            |'AWS::AutoScaling::AutoScalingGroup'
                            |'AWS::AutoScaling::LaunchConfiguration'
                            |'AWS::AutoScaling::ScalingPolicy'
                            |'AWS::AutoScaling::ScheduledAction'
                            |'AWS::DynamoDB::Table'|'AWS::CodeBuild::Project'
                            |'AWS::WAF::RateBasedRule'|'AWS::WAF::Rule'
                            |'AWS::WAF::RuleGroup'|'AWS::WAF::WebACL'
                            |'AWS::WAFRegional::RateBasedRule'
                            |'AWS::WAFRegional::Rule'
                            |'AWS::WAFRegional::RuleGroup'
                            |'AWS::WAFRegional::WebACL'
                            |'AWS::CloudFront::Distribution'
                            |'AWS::CloudFront::StreamingDistribution'
                            |'AWS::Lambda::Alias'|'AWS::Lambda::Function'
                            |'AWS::ElasticBeanstalk::Application'
                            |'AWS::ElasticBeanstalk::ApplicationVersion'
                            |'AWS::ElasticBeanstalk::Environment'
                            |'AWS::MobileHub::Project'
                            |'AWS::XRay::EncryptionConfig'
                            |'AWS::SSM::AssociationCompliance'
                            |'AWS::SSM::PatchCompliance'
                            |'AWS::Shield::Protection'
                            |'AWS::ShieldRegional::Protection'
                            |'AWS::Config::ResourceCompliance'
                            |'AWS::LicenseManager::LicenseConfiguration'
                            |'AWS::ApiGateway::DomainName'
                            |'AWS::ApiGateway::Method'|'AWS::ApiGateway::Stage'
                            |'AWS::ApiGateway::RestApi'
                            |'AWS::ApiGatewayV2::DomainName'
                            |'AWS::ApiGatewayV2::Stage'|'AWS::ApiGatewayV2::Api'
                            |'AWS::CodePipeline::Pipeline'
                            |'AWS::ServiceCatalog::CloudFormationProvisionedProduct'|'AWS::ServiceCatalog::CloudFormationProduct'
                            |'AWS::ServiceCatalog::Portfolio',
                            'resourceId': 'string'
                        },
                        'State': 'QUEUED'|'IN_PROGRESS'|'SUCCEEDED'|'FAILED',
                        'StepDetails': [
                            {
                                'Name': 'string',
                                'State': 'SUCCEEDED'|'PENDING'|'FAILED',
                                'ErrorMessage': 'string',
                                'StartTime': datetime(2015, 1, 1),
                                'StopTime': datetime(2015, 1, 1)
                            },
                        ],
                        'InvocationTime': datetime(2015, 1, 1),
                        'LastUpdatedTime': datetime(2015, 1, 1)
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **RemediationExecutionStatuses** *(list) --*

              Returns a list of remediation execution statuses objects.

              - *(dict) --*

                Provides details of the current status of the invoked remediation action for that
                resource.

                - **ResourceKey** *(dict) --*

                  The details that identify a resource within AWS Config, including the resource
                  type and resource ID.

                  - **resourceType** *(string) --*

                    The resource type.

                  - **resourceId** *(string) --*

                    The ID of the resource (for example., sg-xxxxxx).

                - **State** *(string) --*

                  ENUM of the values.

                - **StepDetails** *(list) --*

                  Details of every step.

                  - *(dict) --*

                    Name of the step from the SSM document.

                    - **Name** *(string) --*

                      The details of the step.

                    - **State** *(string) --*

                      The valid status of the step.

                    - **ErrorMessage** *(string) --*

                      An error message if the step was interrupted during execution.

                    - **StartTime** *(datetime) --*

                      The time when the step started.

                    - **StopTime** *(datetime) --*

                      The time when the step stopped.

                - **InvocationTime** *(datetime) --*

                  Start time when the remediation was executed.

                - **LastUpdatedTime** *(datetime) --*

                  The time when the remediation execution was last updated.
        """


class DescribeRetentionConfigurationsPaginator(Boto3Paginator):
    """
    Paginator for `describe_retention_configurations`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        RetentionConfigurationNames: List[str] = None,
        PaginationConfig: DescribeRetentionConfigurationsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeRetentionConfigurationsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`ConfigService.Client.describe_retention_configurations`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/DescribeRetentionConfigurations>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              RetentionConfigurationNames=[
                  'string',
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'StartingToken': 'string'
              }
          )
        :type RetentionConfigurationNames: list
        :param RetentionConfigurationNames:

          A list of names of retention configurations for which you want details. If you do not
          specify a name, AWS Config returns details for all the retention configurations for that
          account.

          .. note::

            Currently, AWS Config supports only one retention configuration per region in your
            account.

          - *(string) --*

        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than
            the value specified in max-items then a ``NextToken`` will be provided in the output
            that you can use to resume pagination.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'RetentionConfigurations': [
                    {
                        'Name': 'string',
                        'RetentionPeriodInDays': 123
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **RetentionConfigurations** *(list) --*

              Returns a retention configuration object.

              - *(dict) --*

                An object with the name of the retention configuration and the retention period in
                days. The object stores the configuration for data retention in AWS Config.

                - **Name** *(string) --*

                  The name of the retention configuration object.

                - **RetentionPeriodInDays** *(integer) --*

                  Number of days AWS Config stores your historical information.

                  .. note::

                    Currently, only applicable to the configuration item history.
        """


class GetAggregateComplianceDetailsByConfigRulePaginator(Boto3Paginator):
    """
    Paginator for `get_aggregate_compliance_details_by_config_rule`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ConfigurationAggregatorName: str,
        ConfigRuleName: str,
        AccountId: str,
        AwsRegion: str,
        ComplianceType: Literal[
            "COMPLIANT", "NON_COMPLIANT", "NOT_APPLICABLE", "INSUFFICIENT_DATA"
        ] = None,
        PaginationConfig: GetAggregateComplianceDetailsByConfigRulePaginatePaginationConfigTypeDef = None,
    ) -> GetAggregateComplianceDetailsByConfigRulePaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`ConfigService.Client.get_aggregate_compliance_details_by_config_rule`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/GetAggregateComplianceDetailsByConfigRule>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              ConfigurationAggregatorName='string',
              ConfigRuleName='string',
              AccountId='string',
              AwsRegion='string',
              ComplianceType='COMPLIANT'|'NON_COMPLIANT'|'NOT_APPLICABLE'|'INSUFFICIENT_DATA',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type ConfigurationAggregatorName: string
        :param ConfigurationAggregatorName: **[REQUIRED]**

          The name of the configuration aggregator.

        :type ConfigRuleName: string
        :param ConfigRuleName: **[REQUIRED]**

          The name of the AWS Config rule for which you want compliance information.

        :type AccountId: string
        :param AccountId: **[REQUIRED]**

          The 12-digit account ID of the source account.

        :type AwsRegion: string
        :param AwsRegion: **[REQUIRED]**

          The source region from where the data is aggregated.

        :type ComplianceType: string
        :param ComplianceType:

          The resource compliance status.

          .. note::

            For the ``GetAggregateComplianceDetailsByConfigRuleRequest`` data type, AWS Config
            supports only the ``COMPLIANT`` and ``NON_COMPLIANT`` . AWS Config does not support the
            ``NOT_APPLICABLE`` and ``INSUFFICIENT_DATA`` values.

        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than
            the value specified in max-items then a ``NextToken`` will be provided in the output
            that you can use to resume pagination.

          - **PageSize** *(integer) --*

            The size of each page.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'AggregateEvaluationResults': [
                    {
                        'EvaluationResultIdentifier': {
                            'EvaluationResultQualifier': {
                                'ConfigRuleName': 'string',
                                'ResourceType': 'string',
                                'ResourceId': 'string'
                            },
                            'OrderingTimestamp': datetime(2015, 1, 1)
                        },
                        'ComplianceType':
                        'COMPLIANT'|'NON_COMPLIANT'|'NOT_APPLICABLE'
                        |'INSUFFICIENT_DATA',
                        'ResultRecordedTime': datetime(2015, 1, 1),
                        'ConfigRuleInvokedTime': datetime(2015, 1, 1),
                        'Annotation': 'string',
                        'AccountId': 'string',
                        'AwsRegion': 'string'
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **AggregateEvaluationResults** *(list) --*

              Returns an AggregateEvaluationResults object.

              - *(dict) --*

                The details of an AWS Config evaluation for an account ID and region in an
                aggregator. Provides the AWS resource that was evaluated, the compliance of the
                resource, related time stamps, and supplementary information.

                - **EvaluationResultIdentifier** *(dict) --*

                  Uniquely identifies the evaluation result.

                  - **EvaluationResultQualifier** *(dict) --*

                    Identifies an AWS Config rule used to evaluate an AWS resource, and provides the
                    type and ID of the evaluated resource.

                    - **ConfigRuleName** *(string) --*

                      The name of the AWS Config rule that was used in the evaluation.

                    - **ResourceType** *(string) --*

                      The type of AWS resource that was evaluated.

                    - **ResourceId** *(string) --*

                      The ID of the evaluated AWS resource.

                  - **OrderingTimestamp** *(datetime) --*

                    The time of the event that triggered the evaluation of your AWS resources. The
                    time can indicate when AWS Config delivered a configuration item change
                    notification, or it can indicate when AWS Config delivered the configuration
                    snapshot, depending on which event triggered the evaluation.

                - **ComplianceType** *(string) --*

                  The resource compliance status.

                  For the ``AggregationEvaluationResult`` data type, AWS Config supports only the
                  ``COMPLIANT`` and ``NON_COMPLIANT`` . AWS Config does not support the
                  ``NOT_APPLICABLE`` and ``INSUFFICIENT_DATA`` value.

                - **ResultRecordedTime** *(datetime) --*

                  The time when AWS Config recorded the aggregate evaluation result.

                - **ConfigRuleInvokedTime** *(datetime) --*

                  The time when the AWS Config rule evaluated the AWS resource.

                - **Annotation** *(string) --*

                  Supplementary information about how the agrregate evaluation determined the
                  compliance.

                - **AccountId** *(string) --*

                  The 12-digit account ID of the source account.

                - **AwsRegion** *(string) --*

                  The source region from where the data is aggregated.
        """


class GetComplianceDetailsByConfigRulePaginator(Boto3Paginator):
    """
    Paginator for `get_compliance_details_by_config_rule`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ConfigRuleName: str,
        ComplianceTypes: List[
            Literal["COMPLIANT", "NON_COMPLIANT", "NOT_APPLICABLE", "INSUFFICIENT_DATA"]
        ] = None,
        Limit: int = None,
        PaginationConfig: GetComplianceDetailsByConfigRulePaginatePaginationConfigTypeDef = None,
    ) -> GetComplianceDetailsByConfigRulePaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`ConfigService.Client.get_compliance_details_by_config_rule`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/GetComplianceDetailsByConfigRule>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              ConfigRuleName='string',
              ComplianceTypes=[
                  'COMPLIANT'|'NON_COMPLIANT'|'NOT_APPLICABLE'|'INSUFFICIENT_DATA',
              ],
              Limit=123,
              PaginationConfig={
                  'MaxItems': 123,
                  'StartingToken': 'string'
              }
          )
        :type ConfigRuleName: string
        :param ConfigRuleName: **[REQUIRED]**

          The name of the AWS Config rule for which you want compliance information.

        :type ComplianceTypes: list
        :param ComplianceTypes:

          Filters the results by compliance.

          The allowed values are ``COMPLIANT`` , ``NON_COMPLIANT`` , and ``NOT_APPLICABLE`` .

          - *(string) --*

        :type Limit: integer
        :param Limit:

          The maximum number of evaluation results returned on each page. The default is 10. You
          cannot specify a number greater than 100. If you specify 0, AWS Config uses the default.

        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than
            the value specified in max-items then a ``NextToken`` will be provided in the output
            that you can use to resume pagination.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'EvaluationResults': [
                    {
                        'EvaluationResultIdentifier': {
                            'EvaluationResultQualifier': {
                                'ConfigRuleName': 'string',
                                'ResourceType': 'string',
                                'ResourceId': 'string'
                            },
                            'OrderingTimestamp': datetime(2015, 1, 1)
                        },
                        'ComplianceType':
                        'COMPLIANT'|'NON_COMPLIANT'|'NOT_APPLICABLE'
                        |'INSUFFICIENT_DATA',
                        'ResultRecordedTime': datetime(2015, 1, 1),
                        'ConfigRuleInvokedTime': datetime(2015, 1, 1),
                        'Annotation': 'string',
                        'ResultToken': 'string'
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **EvaluationResults** *(list) --*

              Indicates whether the AWS resource complies with the specified AWS Config rule.

              - *(dict) --*

                The details of an AWS Config evaluation. Provides the AWS resource that was
                evaluated, the compliance of the resource, related time stamps, and supplementary
                information.

                - **EvaluationResultIdentifier** *(dict) --*

                  Uniquely identifies the evaluation result.

                  - **EvaluationResultQualifier** *(dict) --*

                    Identifies an AWS Config rule used to evaluate an AWS resource, and provides the
                    type and ID of the evaluated resource.

                    - **ConfigRuleName** *(string) --*

                      The name of the AWS Config rule that was used in the evaluation.

                    - **ResourceType** *(string) --*

                      The type of AWS resource that was evaluated.

                    - **ResourceId** *(string) --*

                      The ID of the evaluated AWS resource.

                  - **OrderingTimestamp** *(datetime) --*

                    The time of the event that triggered the evaluation of your AWS resources. The
                    time can indicate when AWS Config delivered a configuration item change
                    notification, or it can indicate when AWS Config delivered the configuration
                    snapshot, depending on which event triggered the evaluation.

                - **ComplianceType** *(string) --*

                  Indicates whether the AWS resource complies with the AWS Config rule that
                  evaluated it.

                  For the ``EvaluationResult`` data type, AWS Config supports only the ``COMPLIANT``
                  , ``NON_COMPLIANT`` , and ``NOT_APPLICABLE`` values. AWS Config does not support
                  the ``INSUFFICIENT_DATA`` value for the ``EvaluationResult`` data type.

                - **ResultRecordedTime** *(datetime) --*

                  The time when AWS Config recorded the evaluation result.

                - **ConfigRuleInvokedTime** *(datetime) --*

                  The time when the AWS Config rule evaluated the AWS resource.

                - **Annotation** *(string) --*

                  Supplementary information about how the evaluation determined the compliance.

                - **ResultToken** *(string) --*

                  An encrypted token that associates an evaluation with an AWS Config rule. The
                  token identifies the rule, the AWS resource being evaluated, and the event that
                  triggered the evaluation.
        """


class GetComplianceDetailsByResourcePaginator(Boto3Paginator):
    """
    Paginator for `get_compliance_details_by_resource`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ResourceType: str,
        ResourceId: str,
        ComplianceTypes: List[
            Literal["COMPLIANT", "NON_COMPLIANT", "NOT_APPLICABLE", "INSUFFICIENT_DATA"]
        ] = None,
        PaginationConfig: GetComplianceDetailsByResourcePaginatePaginationConfigTypeDef = None,
    ) -> GetComplianceDetailsByResourcePaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`ConfigService.Client.get_compliance_details_by_resource`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/GetComplianceDetailsByResource>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              ResourceType='string',
              ResourceId='string',
              ComplianceTypes=[
                  'COMPLIANT'|'NON_COMPLIANT'|'NOT_APPLICABLE'|'INSUFFICIENT_DATA',
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'StartingToken': 'string'
              }
          )
        :type ResourceType: string
        :param ResourceType: **[REQUIRED]**

          The type of the AWS resource for which you want compliance information.

        :type ResourceId: string
        :param ResourceId: **[REQUIRED]**

          The ID of the AWS resource for which you want compliance information.

        :type ComplianceTypes: list
        :param ComplianceTypes:

          Filters the results by compliance.

          The allowed values are ``COMPLIANT`` , ``NON_COMPLIANT`` , and ``NOT_APPLICABLE`` .

          - *(string) --*

        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than
            the value specified in max-items then a ``NextToken`` will be provided in the output
            that you can use to resume pagination.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'EvaluationResults': [
                    {
                        'EvaluationResultIdentifier': {
                            'EvaluationResultQualifier': {
                                'ConfigRuleName': 'string',
                                'ResourceType': 'string',
                                'ResourceId': 'string'
                            },
                            'OrderingTimestamp': datetime(2015, 1, 1)
                        },
                        'ComplianceType':
                        'COMPLIANT'|'NON_COMPLIANT'|'NOT_APPLICABLE'
                        |'INSUFFICIENT_DATA',
                        'ResultRecordedTime': datetime(2015, 1, 1),
                        'ConfigRuleInvokedTime': datetime(2015, 1, 1),
                        'Annotation': 'string',
                        'ResultToken': 'string'
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **EvaluationResults** *(list) --*

              Indicates whether the specified AWS resource complies each AWS Config rule.

              - *(dict) --*

                The details of an AWS Config evaluation. Provides the AWS resource that was
                evaluated, the compliance of the resource, related time stamps, and supplementary
                information.

                - **EvaluationResultIdentifier** *(dict) --*

                  Uniquely identifies the evaluation result.

                  - **EvaluationResultQualifier** *(dict) --*

                    Identifies an AWS Config rule used to evaluate an AWS resource, and provides the
                    type and ID of the evaluated resource.

                    - **ConfigRuleName** *(string) --*

                      The name of the AWS Config rule that was used in the evaluation.

                    - **ResourceType** *(string) --*

                      The type of AWS resource that was evaluated.

                    - **ResourceId** *(string) --*

                      The ID of the evaluated AWS resource.

                  - **OrderingTimestamp** *(datetime) --*

                    The time of the event that triggered the evaluation of your AWS resources. The
                    time can indicate when AWS Config delivered a configuration item change
                    notification, or it can indicate when AWS Config delivered the configuration
                    snapshot, depending on which event triggered the evaluation.

                - **ComplianceType** *(string) --*

                  Indicates whether the AWS resource complies with the AWS Config rule that
                  evaluated it.

                  For the ``EvaluationResult`` data type, AWS Config supports only the ``COMPLIANT``
                  , ``NON_COMPLIANT`` , and ``NOT_APPLICABLE`` values. AWS Config does not support
                  the ``INSUFFICIENT_DATA`` value for the ``EvaluationResult`` data type.

                - **ResultRecordedTime** *(datetime) --*

                  The time when AWS Config recorded the evaluation result.

                - **ConfigRuleInvokedTime** *(datetime) --*

                  The time when the AWS Config rule evaluated the AWS resource.

                - **Annotation** *(string) --*

                  Supplementary information about how the evaluation determined the compliance.

                - **ResultToken** *(string) --*

                  An encrypted token that associates an evaluation with an AWS Config rule. The
                  token identifies the rule, the AWS resource being evaluated, and the event that
                  triggered the evaluation.
        """


class GetResourceConfigHistoryPaginator(Boto3Paginator):
    """
    Paginator for `get_resource_config_history`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        resourceType: Literal[
            "AWS::EC2::CustomerGateway",
            "AWS::EC2::EIP",
            "AWS::EC2::Host",
            "AWS::EC2::Instance",
            "AWS::EC2::InternetGateway",
            "AWS::EC2::NetworkAcl",
            "AWS::EC2::NetworkInterface",
            "AWS::EC2::RouteTable",
            "AWS::EC2::SecurityGroup",
            "AWS::EC2::Subnet",
            "AWS::CloudTrail::Trail",
            "AWS::EC2::Volume",
            "AWS::EC2::VPC",
            "AWS::EC2::VPNConnection",
            "AWS::EC2::VPNGateway",
            "AWS::EC2::RegisteredHAInstance",
            "AWS::EC2::NatGateway",
            "AWS::EC2::EgressOnlyInternetGateway",
            "AWS::EC2::VPCEndpoint",
            "AWS::EC2::VPCEndpointService",
            "AWS::EC2::FlowLog",
            "AWS::EC2::VPCPeeringConnection",
            "AWS::IAM::Group",
            "AWS::IAM::Policy",
            "AWS::IAM::Role",
            "AWS::IAM::User",
            "AWS::ElasticLoadBalancingV2::LoadBalancer",
            "AWS::ACM::Certificate",
            "AWS::RDS::DBInstance",
            "AWS::RDS::DBParameterGroup",
            "AWS::RDS::DBOptionGroup",
            "AWS::RDS::DBSubnetGroup",
            "AWS::RDS::DBSecurityGroup",
            "AWS::RDS::DBSnapshot",
            "AWS::RDS::DBCluster",
            "AWS::RDS::DBClusterParameterGroup",
            "AWS::RDS::DBClusterSnapshot",
            "AWS::RDS::EventSubscription",
            "AWS::S3::Bucket",
            "AWS::S3::AccountPublicAccessBlock",
            "AWS::Redshift::Cluster",
            "AWS::Redshift::ClusterSnapshot",
            "AWS::Redshift::ClusterParameterGroup",
            "AWS::Redshift::ClusterSecurityGroup",
            "AWS::Redshift::ClusterSubnetGroup",
            "AWS::Redshift::EventSubscription",
            "AWS::SSM::ManagedInstanceInventory",
            "AWS::CloudWatch::Alarm",
            "AWS::CloudFormation::Stack",
            "AWS::ElasticLoadBalancing::LoadBalancer",
            "AWS::AutoScaling::AutoScalingGroup",
            "AWS::AutoScaling::LaunchConfiguration",
            "AWS::AutoScaling::ScalingPolicy",
            "AWS::AutoScaling::ScheduledAction",
            "AWS::DynamoDB::Table",
            "AWS::CodeBuild::Project",
            "AWS::WAF::RateBasedRule",
            "AWS::WAF::Rule",
            "AWS::WAF::RuleGroup",
            "AWS::WAF::WebACL",
            "AWS::WAFRegional::RateBasedRule",
            "AWS::WAFRegional::Rule",
            "AWS::WAFRegional::RuleGroup",
            "AWS::WAFRegional::WebACL",
            "AWS::CloudFront::Distribution",
            "AWS::CloudFront::StreamingDistribution",
            "AWS::Lambda::Alias",
            "AWS::Lambda::Function",
            "AWS::ElasticBeanstalk::Application",
            "AWS::ElasticBeanstalk::ApplicationVersion",
            "AWS::ElasticBeanstalk::Environment",
            "AWS::MobileHub::Project",
            "AWS::XRay::EncryptionConfig",
            "AWS::SSM::AssociationCompliance",
            "AWS::SSM::PatchCompliance",
            "AWS::Shield::Protection",
            "AWS::ShieldRegional::Protection",
            "AWS::Config::ResourceCompliance",
            "AWS::LicenseManager::LicenseConfiguration",
            "AWS::ApiGateway::DomainName",
            "AWS::ApiGateway::Method",
            "AWS::ApiGateway::Stage",
            "AWS::ApiGateway::RestApi",
            "AWS::ApiGatewayV2::DomainName",
            "AWS::ApiGatewayV2::Stage",
            "AWS::ApiGatewayV2::Api",
            "AWS::CodePipeline::Pipeline",
            "AWS::ServiceCatalog::CloudFormationProvisionedProduct",
            "AWS::ServiceCatalog::CloudFormationProduct",
            "AWS::ServiceCatalog::Portfolio",
        ],
        resourceId: str,
        laterTime: datetime = None,
        earlierTime: datetime = None,
        chronologicalOrder: Literal["Reverse", "Forward"] = None,
        PaginationConfig: GetResourceConfigHistoryPaginatePaginationConfigTypeDef = None,
    ) -> GetResourceConfigHistoryPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`ConfigService.Client.get_resource_config_history`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/GetResourceConfigHistory>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              resourceType=
                  'AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'|'AWS::EC2::Instance'
                  |'AWS::EC2::InternetGateway'|'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'
                  |'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'|'AWS::EC2::Subnet'
                  |'AWS::CloudTrail::Trail'|'AWS::EC2::Volume'|'AWS::EC2::VPC'
                  |'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'|'AWS::EC2::RegisteredHAInstance'
                  |'AWS::EC2::NatGateway'|'AWS::EC2::EgressOnlyInternetGateway'
                  |'AWS::EC2::VPCEndpoint'|'AWS::EC2::VPCEndpointService'|'AWS::EC2::FlowLog'
                  |'AWS::EC2::VPCPeeringConnection'|'AWS::IAM::Group'|'AWS::IAM::Policy'
                  |'AWS::IAM::Role'|'AWS::IAM::User'|'AWS::ElasticLoadBalancingV2::LoadBalancer'
                  |'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'|'AWS::RDS::DBParameterGroup'
                  |'AWS::RDS::DBOptionGroup'|'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'
                  |'AWS::RDS::DBSnapshot'|'AWS::RDS::DBCluster'|'AWS::RDS::DBClusterParameterGroup'
                  |'AWS::RDS::DBClusterSnapshot'|'AWS::RDS::EventSubscription'|'AWS::S3::Bucket'
                  |'AWS::S3::AccountPublicAccessBlock'|'AWS::Redshift::Cluster'
                  |'AWS::Redshift::ClusterSnapshot'|'AWS::Redshift::ClusterParameterGroup'
                  |'AWS::Redshift::ClusterSecurityGroup'|'AWS::Redshift::ClusterSubnetGroup'
                  |'AWS::Redshift::EventSubscription'|'AWS::SSM::ManagedInstanceInventory'
                  |'AWS::CloudWatch::Alarm'|'AWS::CloudFormation::Stack'
                  |'AWS::ElasticLoadBalancing::LoadBalancer'|'AWS::AutoScaling::AutoScalingGroup'
                  |'AWS::AutoScaling::LaunchConfiguration'|'AWS::AutoScaling::ScalingPolicy'
                  |'AWS::AutoScaling::ScheduledAction'|'AWS::DynamoDB::Table'
                  |'AWS::CodeBuild::Project'|'AWS::WAF::RateBasedRule'|'AWS::WAF::Rule'
                  |'AWS::WAF::RuleGroup'|'AWS::WAF::WebACL'|'AWS::WAFRegional::RateBasedRule'
                  |'AWS::WAFRegional::Rule'|'AWS::WAFRegional::RuleGroup'|'AWS::WAFRegional::WebACL'
                  |'AWS::CloudFront::Distribution'|'AWS::CloudFront::StreamingDistribution'
                  |'AWS::Lambda::Alias'|'AWS::Lambda::Function'|'AWS::ElasticBeanstalk::Application'
                  |'AWS::ElasticBeanstalk::ApplicationVersion'|'AWS::ElasticBeanstalk::Environment'
                  |'AWS::MobileHub::Project'|'AWS::XRay::EncryptionConfig'
                  |'AWS::SSM::AssociationCompliance'|'AWS::SSM::PatchCompliance'
                  |'AWS::Shield::Protection'|'AWS::ShieldRegional::Protection'
                  |'AWS::Config::ResourceCompliance'|'AWS::LicenseManager::LicenseConfiguration'
                  |'AWS::ApiGateway::DomainName'|'AWS::ApiGateway::Method'|'AWS::ApiGateway::Stage'
                  |'AWS::ApiGateway::RestApi'|'AWS::ApiGatewayV2::DomainName'
                  |'AWS::ApiGatewayV2::Stage'|'AWS::ApiGatewayV2::Api'|'AWS::CodePipeline::Pipeline'
                  |'AWS::ServiceCatalog::CloudFormationProvisionedProduct'
                  |'AWS::ServiceCatalog::CloudFormationProduct'|'AWS::ServiceCatalog::Portfolio',
              resourceId='string',
              laterTime=datetime(2015, 1, 1),
              earlierTime=datetime(2015, 1, 1),
              chronologicalOrder='Reverse'|'Forward',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type resourceType: string
        :param resourceType: **[REQUIRED]**

          The resource type.

        :type resourceId: string
        :param resourceId: **[REQUIRED]**

          The ID of the resource (for example., ``sg-xxxxxx`` ).

        :type laterTime: datetime
        :param laterTime:

          The time stamp that indicates a later time. If not specified, current time is taken.

        :type earlierTime: datetime
        :param earlierTime:

          The time stamp that indicates an earlier time. If not specified, the action returns
          paginated results that contain configuration items that start when the first configuration
          item was recorded.

        :type chronologicalOrder: string
        :param chronologicalOrder:

          The chronological order for configuration items listed. By default, the results are listed
          in reverse chronological order.

        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than
            the value specified in max-items then a ``NextToken`` will be provided in the output
            that you can use to resume pagination.

          - **PageSize** *(integer) --*

            The size of each page.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'configurationItems': [
                    {
                        'version': 'string',
                        'accountId': 'string',
                        'configurationItemCaptureTime': datetime(2015, 1, 1),
                        'configurationItemStatus':
                        'OK'|'ResourceDiscovered'|'ResourceNotRecorded'
                        |'ResourceDeleted'|'ResourceDeletedNotRecorded',
                        'configurationStateId': 'string',
                        'configurationItemMD5Hash': 'string',
                        'arn': 'string',
                        'resourceType':
                        'AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'
                        |'AWS::EC2::Instance'|'AWS::EC2::InternetGateway'
                        |'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'
                        |'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'
                        |'AWS::EC2::Subnet'|'AWS::CloudTrail::Trail'
                        |'AWS::EC2::Volume'|'AWS::EC2::VPC'
                        |'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'
                        |'AWS::EC2::RegisteredHAInstance'|'AWS::EC2::NatGateway'
                        |'AWS::EC2::EgressOnlyInternetGateway'
                        |'AWS::EC2::VPCEndpoint'|'AWS::EC2::VPCEndpointService'
                        |'AWS::EC2::FlowLog'|'AWS::EC2::VPCPeeringConnection'
                        |'AWS::IAM::Group'|'AWS::IAM::Policy'|'AWS::IAM::Role'
                        |'AWS::IAM::User'
                        |'AWS::ElasticLoadBalancingV2::LoadBalancer'
                        |'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'
                        |'AWS::RDS::DBParameterGroup'|'AWS::RDS::DBOptionGroup'
                        |'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'
                        |'AWS::RDS::DBSnapshot'|'AWS::RDS::DBCluster'
                        |'AWS::RDS::DBClusterParameterGroup'
                        |'AWS::RDS::DBClusterSnapshot'|'AWS::RDS::EventSubscription'
                        |'AWS::S3::Bucket'|'AWS::S3::AccountPublicAccessBlock'
                        |'AWS::Redshift::Cluster'|'AWS::Redshift::ClusterSnapshot'
                        |'AWS::Redshift::ClusterParameterGroup'
                        |'AWS::Redshift::ClusterSecurityGroup'
                        |'AWS::Redshift::ClusterSubnetGroup'
                        |'AWS::Redshift::EventSubscription'
                        |'AWS::SSM::ManagedInstanceInventory'
                        |'AWS::CloudWatch::Alarm'|'AWS::CloudFormation::Stack'
                        |'AWS::ElasticLoadBalancing::LoadBalancer'
                        |'AWS::AutoScaling::AutoScalingGroup'
                        |'AWS::AutoScaling::LaunchConfiguration'
                        |'AWS::AutoScaling::ScalingPolicy'
                        |'AWS::AutoScaling::ScheduledAction'|'AWS::DynamoDB::Table'
                        |'AWS::CodeBuild::Project'|'AWS::WAF::RateBasedRule'
                        |'AWS::WAF::Rule'|'AWS::WAF::RuleGroup'|'AWS::WAF::WebACL'
                        |'AWS::WAFRegional::RateBasedRule'|'AWS::WAFRegional::Rule'
                        |'AWS::WAFRegional::RuleGroup'|'AWS::WAFRegional::WebACL'
                        |'AWS::CloudFront::Distribution'
                        |'AWS::CloudFront::StreamingDistribution'
                        |'AWS::Lambda::Alias'|'AWS::Lambda::Function'
                        |'AWS::ElasticBeanstalk::Application'
                        |'AWS::ElasticBeanstalk::ApplicationVersion'
                        |'AWS::ElasticBeanstalk::Environment'
                        |'AWS::MobileHub::Project'|'AWS::XRay::EncryptionConfig'
                        |'AWS::SSM::AssociationCompliance'
                        |'AWS::SSM::PatchCompliance'|'AWS::Shield::Protection'
                        |'AWS::ShieldRegional::Protection'
                        |'AWS::Config::ResourceCompliance'
                        |'AWS::LicenseManager::LicenseConfiguration'
                        |'AWS::ApiGateway::DomainName'|'AWS::ApiGateway::Method'
                        |'AWS::ApiGateway::Stage'|'AWS::ApiGateway::RestApi'
                        |'AWS::ApiGatewayV2::DomainName'|'AWS::ApiGatewayV2::Stage'
                        |'AWS::ApiGatewayV2::Api'|'AWS::CodePipeline::Pipeline'
                        |'AWS::ServiceCatalog::CloudFormationProvisionedProduct'
                        |'AWS::ServiceCatalog::CloudFormationProduct'
                        |'AWS::ServiceCatalog::Portfolio',
                        'resourceId': 'string',
                        'resourceName': 'string',
                        'awsRegion': 'string',
                        'availabilityZone': 'string',
                        'resourceCreationTime': datetime(2015, 1, 1),
                        'tags': {
                            'string': 'string'
                        },
                        'relatedEvents': [
                            'string',
                        ],
                        'relationships': [
                            {
                                'resourceType':
                                'AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'
                                |'AWS::EC2::Host'|'AWS::EC2::Instance'
                                |'AWS::EC2::InternetGateway'
                                |'AWS::EC2::NetworkAcl'
                                |'AWS::EC2::NetworkInterface'
                                |'AWS::EC2::RouteTable'
                                |'AWS::EC2::SecurityGroup'
                                |'AWS::EC2::Subnet'|'AWS::CloudTrail::Trail'
                                |'AWS::EC2::Volume'|'AWS::EC2::VPC'
                                |'AWS::EC2::VPNConnection'
                                |'AWS::EC2::VPNGateway'
                                |'AWS::EC2::RegisteredHAInstance'
                                |'AWS::EC2::NatGateway'
                                |'AWS::EC2::EgressOnlyInternetGateway'
                                |'AWS::EC2::VPCEndpoint'
                                |'AWS::EC2::VPCEndpointService'
                                |'AWS::EC2::FlowLog'
                                |'AWS::EC2::VPCPeeringConnection'
                                |'AWS::IAM::Group'|'AWS::IAM::Policy'
                                |'AWS::IAM::Role'|'AWS::IAM::User'
                                |'AWS::ElasticLoadBalancingV2::LoadBalancer'
                                |'AWS::ACM::Certificate'
                                |'AWS::RDS::DBInstance'
                                |'AWS::RDS::DBParameterGroup'
                                |'AWS::RDS::DBOptionGroup'
                                |'AWS::RDS::DBSubnetGroup'
                                |'AWS::RDS::DBSecurityGroup'
                                |'AWS::RDS::DBSnapshot'
                                |'AWS::RDS::DBCluster'
                                |'AWS::RDS::DBClusterParameterGroup'
                                |'AWS::RDS::DBClusterSnapshot'
                                |'AWS::RDS::EventSubscription'
                                |'AWS::S3::Bucket'
                                |'AWS::S3::AccountPublicAccessBlock'
                                |'AWS::Redshift::Cluster'
                                |'AWS::Redshift::ClusterSnapshot'
                                |'AWS::Redshift::ClusterParameterGroup'
                                |'AWS::Redshift::ClusterSecurityGroup'
                                |'AWS::Redshift::ClusterSubnetGroup'
                                |'AWS::Redshift::EventSubscription'
                                |'AWS::SSM::ManagedInstanceInventory'
                                |'AWS::CloudWatch::Alarm'
                                |'AWS::CloudFormation::Stack'
                                |'AWS::ElasticLoadBalancing::LoadBalancer'
                                |'AWS::AutoScaling::AutoScalingGroup'
                                |'AWS::AutoScaling::LaunchConfiguration'
                                |'AWS::AutoScaling::ScalingPolicy'
                                |'AWS::AutoScaling::ScheduledAction'
                                |'AWS::DynamoDB::Table'
                                |'AWS::CodeBuild::Project'
                                |'AWS::WAF::RateBasedRule'|'AWS::WAF::Rule'
                                |'AWS::WAF::RuleGroup'|'AWS::WAF::WebACL'
                                |'AWS::WAFRegional::RateBasedRule'
                                |'AWS::WAFRegional::Rule'
                                |'AWS::WAFRegional::RuleGroup'
                                |'AWS::WAFRegional::WebACL'
                                |'AWS::CloudFront::Distribution'
                                |'AWS::CloudFront::StreamingDistribution'
                                |'AWS::Lambda::Alias'
                                |'AWS::Lambda::Function'
                                |'AWS::ElasticBeanstalk::Application'
                                |'AWS::ElasticBeanstalk::ApplicationVersion'
                                |'AWS::ElasticBeanstalk::Environment'
                                |'AWS::MobileHub::Project'
                                |'AWS::XRay::EncryptionConfig'
                                |'AWS::SSM::AssociationCompliance'
                                |'AWS::SSM::PatchCompliance'
                                |'AWS::Shield::Protection'
                                |'AWS::ShieldRegional::Protection'
                                |'AWS::Config::ResourceCompliance'
                                |'AWS::LicenseManager::LicenseConfiguration'
                                |'AWS::ApiGateway::DomainName'
                                |'AWS::ApiGateway::Method'
                                |'AWS::ApiGateway::Stage'
                                |'AWS::ApiGateway::RestApi'
                                |'AWS::ApiGatewayV2::DomainName'
                                |'AWS::ApiGatewayV2::Stage'
                                |'AWS::ApiGatewayV2::Api'
                                |'AWS::CodePipeline::Pipeline'
                                |'AWS::ServiceCatalog::CloudFormationProvisionedProduct'|'AWS::ServiceCatalog::CloudFormationProduct'
                                |'AWS::ServiceCatalog::Portfolio',
                                'resourceId': 'string',
                                'resourceName': 'string',
                                'relationshipName': 'string'
                            },
                        ],
                        'configuration': 'string',
                        'supplementaryConfiguration': {
                            'string': 'string'
                        }
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            The output for the  GetResourceConfigHistory action.

            - **configurationItems** *(list) --*

              A list that contains the configuration history of one or more resources.

              - *(dict) --*

                A list that contains detailed configurations of a specified resource.

                - **version** *(string) --*

                  The version number of the resource configuration.

                - **accountId** *(string) --*

                  The 12-digit AWS account ID associated with the resource.

                - **configurationItemCaptureTime** *(datetime) --*

                  The time when the configuration recording was initiated.

                - **configurationItemStatus** *(string) --*

                  The configuration item status.

                - **configurationStateId** *(string) --*

                  An identifier that indicates the ordering of the configuration items of a
                  resource.

                - **configurationItemMD5Hash** *(string) --*

                  Unique MD5 hash that represents the configuration item's state.

                  You can use MD5 hash to compare the states of two or more configuration items that
                  are associated with the same resource.

                - **arn** *(string) --*

                  accoun

                - **resourceType** *(string) --*

                  The type of AWS resource.

                - **resourceId** *(string) --*

                  The ID of the resource (for example, ``sg-xxxxxx`` ).

                - **resourceName** *(string) --*

                  The custom name of the resource, if available.

                - **awsRegion** *(string) --*

                  The region where the resource resides.

                - **availabilityZone** *(string) --*

                  The Availability Zone associated with the resource.

                - **resourceCreationTime** *(datetime) --*

                  The time stamp when the resource was created.

                - **tags** *(dict) --*

                  A mapping of key value tags associated with the resource.

                  - *(string) --*

                    - *(string) --*

                - **relatedEvents** *(list) --*

                  A list of CloudTrail event IDs.

                  A populated field indicates that the current configuration was initiated by the
                  events recorded in the CloudTrail log. For more information about CloudTrail, see
                  `What Is AWS CloudTrail
                  <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/what_is_cloud_trail_top_level.html>`__
                  .

                  An empty field indicates that the current configuration was not initiated by any
                  event. As of Version 1.3, the relatedEvents field is empty. You can access the
                  `LookupEvents API
                  <https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_LookupEvents.html>`__
                  in the *AWS CloudTrail API Reference* to retrieve the events for the resource.

                  - *(string) --*

                - **relationships** *(list) --*

                  A list of related AWS resources.

                  - *(dict) --*

                    The relationship of the related resource to the main resource.

                    - **resourceType** *(string) --*

                      The resource type of the related resource.

                    - **resourceId** *(string) --*

                      The ID of the related resource (for example, ``sg-xxxxxx`` ).

                    - **resourceName** *(string) --*

                      The custom name of the related resource, if available.

                    - **relationshipName** *(string) --*

                      The type of relationship with the related resource.

                - **configuration** *(string) --*

                  The description of the resource configuration.

                - **supplementaryConfiguration** *(dict) --*

                  Configuration attributes that AWS Config returns for certain resource types to
                  supplement the information returned for the ``configuration`` parameter.

                  - *(string) --*

                    - *(string) --*

            - **NextToken** *(string) --*

              A token to resume pagination.
        """


class ListAggregateDiscoveredResourcesPaginator(Boto3Paginator):
    """
    Paginator for `list_aggregate_discovered_resources`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ConfigurationAggregatorName: str,
        ResourceType: Literal[
            "AWS::EC2::CustomerGateway",
            "AWS::EC2::EIP",
            "AWS::EC2::Host",
            "AWS::EC2::Instance",
            "AWS::EC2::InternetGateway",
            "AWS::EC2::NetworkAcl",
            "AWS::EC2::NetworkInterface",
            "AWS::EC2::RouteTable",
            "AWS::EC2::SecurityGroup",
            "AWS::EC2::Subnet",
            "AWS::CloudTrail::Trail",
            "AWS::EC2::Volume",
            "AWS::EC2::VPC",
            "AWS::EC2::VPNConnection",
            "AWS::EC2::VPNGateway",
            "AWS::EC2::RegisteredHAInstance",
            "AWS::EC2::NatGateway",
            "AWS::EC2::EgressOnlyInternetGateway",
            "AWS::EC2::VPCEndpoint",
            "AWS::EC2::VPCEndpointService",
            "AWS::EC2::FlowLog",
            "AWS::EC2::VPCPeeringConnection",
            "AWS::IAM::Group",
            "AWS::IAM::Policy",
            "AWS::IAM::Role",
            "AWS::IAM::User",
            "AWS::ElasticLoadBalancingV2::LoadBalancer",
            "AWS::ACM::Certificate",
            "AWS::RDS::DBInstance",
            "AWS::RDS::DBParameterGroup",
            "AWS::RDS::DBOptionGroup",
            "AWS::RDS::DBSubnetGroup",
            "AWS::RDS::DBSecurityGroup",
            "AWS::RDS::DBSnapshot",
            "AWS::RDS::DBCluster",
            "AWS::RDS::DBClusterParameterGroup",
            "AWS::RDS::DBClusterSnapshot",
            "AWS::RDS::EventSubscription",
            "AWS::S3::Bucket",
            "AWS::S3::AccountPublicAccessBlock",
            "AWS::Redshift::Cluster",
            "AWS::Redshift::ClusterSnapshot",
            "AWS::Redshift::ClusterParameterGroup",
            "AWS::Redshift::ClusterSecurityGroup",
            "AWS::Redshift::ClusterSubnetGroup",
            "AWS::Redshift::EventSubscription",
            "AWS::SSM::ManagedInstanceInventory",
            "AWS::CloudWatch::Alarm",
            "AWS::CloudFormation::Stack",
            "AWS::ElasticLoadBalancing::LoadBalancer",
            "AWS::AutoScaling::AutoScalingGroup",
            "AWS::AutoScaling::LaunchConfiguration",
            "AWS::AutoScaling::ScalingPolicy",
            "AWS::AutoScaling::ScheduledAction",
            "AWS::DynamoDB::Table",
            "AWS::CodeBuild::Project",
            "AWS::WAF::RateBasedRule",
            "AWS::WAF::Rule",
            "AWS::WAF::RuleGroup",
            "AWS::WAF::WebACL",
            "AWS::WAFRegional::RateBasedRule",
            "AWS::WAFRegional::Rule",
            "AWS::WAFRegional::RuleGroup",
            "AWS::WAFRegional::WebACL",
            "AWS::CloudFront::Distribution",
            "AWS::CloudFront::StreamingDistribution",
            "AWS::Lambda::Alias",
            "AWS::Lambda::Function",
            "AWS::ElasticBeanstalk::Application",
            "AWS::ElasticBeanstalk::ApplicationVersion",
            "AWS::ElasticBeanstalk::Environment",
            "AWS::MobileHub::Project",
            "AWS::XRay::EncryptionConfig",
            "AWS::SSM::AssociationCompliance",
            "AWS::SSM::PatchCompliance",
            "AWS::Shield::Protection",
            "AWS::ShieldRegional::Protection",
            "AWS::Config::ResourceCompliance",
            "AWS::LicenseManager::LicenseConfiguration",
            "AWS::ApiGateway::DomainName",
            "AWS::ApiGateway::Method",
            "AWS::ApiGateway::Stage",
            "AWS::ApiGateway::RestApi",
            "AWS::ApiGatewayV2::DomainName",
            "AWS::ApiGatewayV2::Stage",
            "AWS::ApiGatewayV2::Api",
            "AWS::CodePipeline::Pipeline",
            "AWS::ServiceCatalog::CloudFormationProvisionedProduct",
            "AWS::ServiceCatalog::CloudFormationProduct",
            "AWS::ServiceCatalog::Portfolio",
        ],
        Filters: ListAggregateDiscoveredResourcesPaginateFiltersTypeDef = None,
        PaginationConfig: ListAggregateDiscoveredResourcesPaginatePaginationConfigTypeDef = None,
    ) -> ListAggregateDiscoveredResourcesPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`ConfigService.Client.list_aggregate_discovered_resources`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/ListAggregateDiscoveredResources>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              ConfigurationAggregatorName='string',
              ResourceType=
                  'AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'|'AWS::EC2::Instance'
                  |'AWS::EC2::InternetGateway'|'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'
                  |'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'|'AWS::EC2::Subnet'
                  |'AWS::CloudTrail::Trail'|'AWS::EC2::Volume'|'AWS::EC2::VPC'
                  |'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'|'AWS::EC2::RegisteredHAInstance'
                  |'AWS::EC2::NatGateway'|'AWS::EC2::EgressOnlyInternetGateway'
                  |'AWS::EC2::VPCEndpoint'|'AWS::EC2::VPCEndpointService'|'AWS::EC2::FlowLog'
                  |'AWS::EC2::VPCPeeringConnection'|'AWS::IAM::Group'|'AWS::IAM::Policy'
                  |'AWS::IAM::Role'|'AWS::IAM::User'|'AWS::ElasticLoadBalancingV2::LoadBalancer'
                  |'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'|'AWS::RDS::DBParameterGroup'
                  |'AWS::RDS::DBOptionGroup'|'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'
                  |'AWS::RDS::DBSnapshot'|'AWS::RDS::DBCluster'|'AWS::RDS::DBClusterParameterGroup'
                  |'AWS::RDS::DBClusterSnapshot'|'AWS::RDS::EventSubscription'|'AWS::S3::Bucket'
                  |'AWS::S3::AccountPublicAccessBlock'|'AWS::Redshift::Cluster'
                  |'AWS::Redshift::ClusterSnapshot'|'AWS::Redshift::ClusterParameterGroup'
                  |'AWS::Redshift::ClusterSecurityGroup'|'AWS::Redshift::ClusterSubnetGroup'
                  |'AWS::Redshift::EventSubscription'|'AWS::SSM::ManagedInstanceInventory'
                  |'AWS::CloudWatch::Alarm'|'AWS::CloudFormation::Stack'
                  |'AWS::ElasticLoadBalancing::LoadBalancer'|'AWS::AutoScaling::AutoScalingGroup'
                  |'AWS::AutoScaling::LaunchConfiguration'|'AWS::AutoScaling::ScalingPolicy'
                  |'AWS::AutoScaling::ScheduledAction'|'AWS::DynamoDB::Table'
                  |'AWS::CodeBuild::Project'|'AWS::WAF::RateBasedRule'|'AWS::WAF::Rule'
                  |'AWS::WAF::RuleGroup'|'AWS::WAF::WebACL'|'AWS::WAFRegional::RateBasedRule'
                  |'AWS::WAFRegional::Rule'|'AWS::WAFRegional::RuleGroup'|'AWS::WAFRegional::WebACL'
                  |'AWS::CloudFront::Distribution'|'AWS::CloudFront::StreamingDistribution'
                  |'AWS::Lambda::Alias'|'AWS::Lambda::Function'|'AWS::ElasticBeanstalk::Application'
                  |'AWS::ElasticBeanstalk::ApplicationVersion'|'AWS::ElasticBeanstalk::Environment'
                  |'AWS::MobileHub::Project'|'AWS::XRay::EncryptionConfig'
                  |'AWS::SSM::AssociationCompliance'|'AWS::SSM::PatchCompliance'
                  |'AWS::Shield::Protection'|'AWS::ShieldRegional::Protection'
                  |'AWS::Config::ResourceCompliance'|'AWS::LicenseManager::LicenseConfiguration'
                  |'AWS::ApiGateway::DomainName'|'AWS::ApiGateway::Method'|'AWS::ApiGateway::Stage'
                  |'AWS::ApiGateway::RestApi'|'AWS::ApiGatewayV2::DomainName'
                  |'AWS::ApiGatewayV2::Stage'|'AWS::ApiGatewayV2::Api'|'AWS::CodePipeline::Pipeline'
                  |'AWS::ServiceCatalog::CloudFormationProvisionedProduct'
                  |'AWS::ServiceCatalog::CloudFormationProduct'|'AWS::ServiceCatalog::Portfolio',
              Filters={
                  'AccountId': 'string',
                  'ResourceId': 'string',
                  'ResourceName': 'string',
                  'Region': 'string'
              },
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type ConfigurationAggregatorName: string
        :param ConfigurationAggregatorName: **[REQUIRED]**

          The name of the configuration aggregator.

        :type ResourceType: string
        :param ResourceType: **[REQUIRED]**

          The type of resources that you want AWS Config to list in the response.

        :type Filters: dict
        :param Filters:

          Filters the results based on the ``ResourceFilters`` object.

          - **AccountId** *(string) --*

            The 12-digit source account ID.

          - **ResourceId** *(string) --*

            The ID of the resource.

          - **ResourceName** *(string) --*

            The name of the resource.

          - **Region** *(string) --*

            The source region.

        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than
            the value specified in max-items then a ``NextToken`` will be provided in the output
            that you can use to resume pagination.

          - **PageSize** *(integer) --*

            The size of each page.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ResourceIdentifiers': [
                    {
                        'SourceAccountId': 'string',
                        'SourceRegion': 'string',
                        'ResourceId': 'string',
                        'ResourceType':
                        'AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'
                        |'AWS::EC2::Instance'|'AWS::EC2::InternetGateway'
                        |'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'
                        |'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'
                        |'AWS::EC2::Subnet'|'AWS::CloudTrail::Trail'
                        |'AWS::EC2::Volume'|'AWS::EC2::VPC'
                        |'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'
                        |'AWS::EC2::RegisteredHAInstance'|'AWS::EC2::NatGateway'
                        |'AWS::EC2::EgressOnlyInternetGateway'
                        |'AWS::EC2::VPCEndpoint'|'AWS::EC2::VPCEndpointService'
                        |'AWS::EC2::FlowLog'|'AWS::EC2::VPCPeeringConnection'
                        |'AWS::IAM::Group'|'AWS::IAM::Policy'|'AWS::IAM::Role'
                        |'AWS::IAM::User'
                        |'AWS::ElasticLoadBalancingV2::LoadBalancer'
                        |'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'
                        |'AWS::RDS::DBParameterGroup'|'AWS::RDS::DBOptionGroup'
                        |'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'
                        |'AWS::RDS::DBSnapshot'|'AWS::RDS::DBCluster'
                        |'AWS::RDS::DBClusterParameterGroup'
                        |'AWS::RDS::DBClusterSnapshot'|'AWS::RDS::EventSubscription'
                        |'AWS::S3::Bucket'|'AWS::S3::AccountPublicAccessBlock'
                        |'AWS::Redshift::Cluster'|'AWS::Redshift::ClusterSnapshot'
                        |'AWS::Redshift::ClusterParameterGroup'
                        |'AWS::Redshift::ClusterSecurityGroup'
                        |'AWS::Redshift::ClusterSubnetGroup'
                        |'AWS::Redshift::EventSubscription'
                        |'AWS::SSM::ManagedInstanceInventory'
                        |'AWS::CloudWatch::Alarm'|'AWS::CloudFormation::Stack'
                        |'AWS::ElasticLoadBalancing::LoadBalancer'
                        |'AWS::AutoScaling::AutoScalingGroup'
                        |'AWS::AutoScaling::LaunchConfiguration'
                        |'AWS::AutoScaling::ScalingPolicy'
                        |'AWS::AutoScaling::ScheduledAction'|'AWS::DynamoDB::Table'
                        |'AWS::CodeBuild::Project'|'AWS::WAF::RateBasedRule'
                        |'AWS::WAF::Rule'|'AWS::WAF::RuleGroup'|'AWS::WAF::WebACL'
                        |'AWS::WAFRegional::RateBasedRule'|'AWS::WAFRegional::Rule'
                        |'AWS::WAFRegional::RuleGroup'|'AWS::WAFRegional::WebACL'
                        |'AWS::CloudFront::Distribution'
                        |'AWS::CloudFront::StreamingDistribution'
                        |'AWS::Lambda::Alias'|'AWS::Lambda::Function'
                        |'AWS::ElasticBeanstalk::Application'
                        |'AWS::ElasticBeanstalk::ApplicationVersion'
                        |'AWS::ElasticBeanstalk::Environment'
                        |'AWS::MobileHub::Project'|'AWS::XRay::EncryptionConfig'
                        |'AWS::SSM::AssociationCompliance'
                        |'AWS::SSM::PatchCompliance'|'AWS::Shield::Protection'
                        |'AWS::ShieldRegional::Protection'
                        |'AWS::Config::ResourceCompliance'
                        |'AWS::LicenseManager::LicenseConfiguration'
                        |'AWS::ApiGateway::DomainName'|'AWS::ApiGateway::Method'
                        |'AWS::ApiGateway::Stage'|'AWS::ApiGateway::RestApi'
                        |'AWS::ApiGatewayV2::DomainName'|'AWS::ApiGatewayV2::Stage'
                        |'AWS::ApiGatewayV2::Api'|'AWS::CodePipeline::Pipeline'
                        |'AWS::ServiceCatalog::CloudFormationProvisionedProduct'
                        |'AWS::ServiceCatalog::CloudFormationProduct'
                        |'AWS::ServiceCatalog::Portfolio',
                        'ResourceName': 'string'
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **ResourceIdentifiers** *(list) --*

              Returns a list of ``ResourceIdentifiers`` objects.

              - *(dict) --*

                The details that identify a resource that is collected by AWS Config aggregator,
                including the resource type, ID, (if available) the custom resource name, the source
                account, and source region.

                - **SourceAccountId** *(string) --*

                  The 12-digit account ID of the source account.

                - **SourceRegion** *(string) --*

                  The source region where data is aggregated.

                - **ResourceId** *(string) --*

                  The ID of the AWS resource.

                - **ResourceType** *(string) --*

                  The type of the AWS resource.

                - **ResourceName** *(string) --*

                  The name of the AWS resource.
        """


class ListDiscoveredResourcesPaginator(Boto3Paginator):
    """
    Paginator for `list_discovered_resources`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        resourceType: Literal[
            "AWS::EC2::CustomerGateway",
            "AWS::EC2::EIP",
            "AWS::EC2::Host",
            "AWS::EC2::Instance",
            "AWS::EC2::InternetGateway",
            "AWS::EC2::NetworkAcl",
            "AWS::EC2::NetworkInterface",
            "AWS::EC2::RouteTable",
            "AWS::EC2::SecurityGroup",
            "AWS::EC2::Subnet",
            "AWS::CloudTrail::Trail",
            "AWS::EC2::Volume",
            "AWS::EC2::VPC",
            "AWS::EC2::VPNConnection",
            "AWS::EC2::VPNGateway",
            "AWS::EC2::RegisteredHAInstance",
            "AWS::EC2::NatGateway",
            "AWS::EC2::EgressOnlyInternetGateway",
            "AWS::EC2::VPCEndpoint",
            "AWS::EC2::VPCEndpointService",
            "AWS::EC2::FlowLog",
            "AWS::EC2::VPCPeeringConnection",
            "AWS::IAM::Group",
            "AWS::IAM::Policy",
            "AWS::IAM::Role",
            "AWS::IAM::User",
            "AWS::ElasticLoadBalancingV2::LoadBalancer",
            "AWS::ACM::Certificate",
            "AWS::RDS::DBInstance",
            "AWS::RDS::DBParameterGroup",
            "AWS::RDS::DBOptionGroup",
            "AWS::RDS::DBSubnetGroup",
            "AWS::RDS::DBSecurityGroup",
            "AWS::RDS::DBSnapshot",
            "AWS::RDS::DBCluster",
            "AWS::RDS::DBClusterParameterGroup",
            "AWS::RDS::DBClusterSnapshot",
            "AWS::RDS::EventSubscription",
            "AWS::S3::Bucket",
            "AWS::S3::AccountPublicAccessBlock",
            "AWS::Redshift::Cluster",
            "AWS::Redshift::ClusterSnapshot",
            "AWS::Redshift::ClusterParameterGroup",
            "AWS::Redshift::ClusterSecurityGroup",
            "AWS::Redshift::ClusterSubnetGroup",
            "AWS::Redshift::EventSubscription",
            "AWS::SSM::ManagedInstanceInventory",
            "AWS::CloudWatch::Alarm",
            "AWS::CloudFormation::Stack",
            "AWS::ElasticLoadBalancing::LoadBalancer",
            "AWS::AutoScaling::AutoScalingGroup",
            "AWS::AutoScaling::LaunchConfiguration",
            "AWS::AutoScaling::ScalingPolicy",
            "AWS::AutoScaling::ScheduledAction",
            "AWS::DynamoDB::Table",
            "AWS::CodeBuild::Project",
            "AWS::WAF::RateBasedRule",
            "AWS::WAF::Rule",
            "AWS::WAF::RuleGroup",
            "AWS::WAF::WebACL",
            "AWS::WAFRegional::RateBasedRule",
            "AWS::WAFRegional::Rule",
            "AWS::WAFRegional::RuleGroup",
            "AWS::WAFRegional::WebACL",
            "AWS::CloudFront::Distribution",
            "AWS::CloudFront::StreamingDistribution",
            "AWS::Lambda::Alias",
            "AWS::Lambda::Function",
            "AWS::ElasticBeanstalk::Application",
            "AWS::ElasticBeanstalk::ApplicationVersion",
            "AWS::ElasticBeanstalk::Environment",
            "AWS::MobileHub::Project",
            "AWS::XRay::EncryptionConfig",
            "AWS::SSM::AssociationCompliance",
            "AWS::SSM::PatchCompliance",
            "AWS::Shield::Protection",
            "AWS::ShieldRegional::Protection",
            "AWS::Config::ResourceCompliance",
            "AWS::LicenseManager::LicenseConfiguration",
            "AWS::ApiGateway::DomainName",
            "AWS::ApiGateway::Method",
            "AWS::ApiGateway::Stage",
            "AWS::ApiGateway::RestApi",
            "AWS::ApiGatewayV2::DomainName",
            "AWS::ApiGatewayV2::Stage",
            "AWS::ApiGatewayV2::Api",
            "AWS::CodePipeline::Pipeline",
            "AWS::ServiceCatalog::CloudFormationProvisionedProduct",
            "AWS::ServiceCatalog::CloudFormationProduct",
            "AWS::ServiceCatalog::Portfolio",
        ],
        resourceIds: List[str] = None,
        resourceName: str = None,
        limit: int = None,
        includeDeletedResources: bool = None,
        PaginationConfig: ListDiscoveredResourcesPaginatePaginationConfigTypeDef = None,
    ) -> ListDiscoveredResourcesPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`ConfigService.Client.list_discovered_resources`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/ListDiscoveredResources>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              resourceType=
                  'AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'|'AWS::EC2::Instance'
                  |'AWS::EC2::InternetGateway'|'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'
                  |'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'|'AWS::EC2::Subnet'
                  |'AWS::CloudTrail::Trail'|'AWS::EC2::Volume'|'AWS::EC2::VPC'
                  |'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'|'AWS::EC2::RegisteredHAInstance'
                  |'AWS::EC2::NatGateway'|'AWS::EC2::EgressOnlyInternetGateway'
                  |'AWS::EC2::VPCEndpoint'|'AWS::EC2::VPCEndpointService'|'AWS::EC2::FlowLog'
                  |'AWS::EC2::VPCPeeringConnection'|'AWS::IAM::Group'|'AWS::IAM::Policy'
                  |'AWS::IAM::Role'|'AWS::IAM::User'|'AWS::ElasticLoadBalancingV2::LoadBalancer'
                  |'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'|'AWS::RDS::DBParameterGroup'
                  |'AWS::RDS::DBOptionGroup'|'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'
                  |'AWS::RDS::DBSnapshot'|'AWS::RDS::DBCluster'|'AWS::RDS::DBClusterParameterGroup'
                  |'AWS::RDS::DBClusterSnapshot'|'AWS::RDS::EventSubscription'|'AWS::S3::Bucket'
                  |'AWS::S3::AccountPublicAccessBlock'|'AWS::Redshift::Cluster'
                  |'AWS::Redshift::ClusterSnapshot'|'AWS::Redshift::ClusterParameterGroup'
                  |'AWS::Redshift::ClusterSecurityGroup'|'AWS::Redshift::ClusterSubnetGroup'
                  |'AWS::Redshift::EventSubscription'|'AWS::SSM::ManagedInstanceInventory'
                  |'AWS::CloudWatch::Alarm'|'AWS::CloudFormation::Stack'
                  |'AWS::ElasticLoadBalancing::LoadBalancer'|'AWS::AutoScaling::AutoScalingGroup'
                  |'AWS::AutoScaling::LaunchConfiguration'|'AWS::AutoScaling::ScalingPolicy'
                  |'AWS::AutoScaling::ScheduledAction'|'AWS::DynamoDB::Table'
                  |'AWS::CodeBuild::Project'|'AWS::WAF::RateBasedRule'|'AWS::WAF::Rule'
                  |'AWS::WAF::RuleGroup'|'AWS::WAF::WebACL'|'AWS::WAFRegional::RateBasedRule'
                  |'AWS::WAFRegional::Rule'|'AWS::WAFRegional::RuleGroup'|'AWS::WAFRegional::WebACL'
                  |'AWS::CloudFront::Distribution'|'AWS::CloudFront::StreamingDistribution'
                  |'AWS::Lambda::Alias'|'AWS::Lambda::Function'|'AWS::ElasticBeanstalk::Application'
                  |'AWS::ElasticBeanstalk::ApplicationVersion'|'AWS::ElasticBeanstalk::Environment'
                  |'AWS::MobileHub::Project'|'AWS::XRay::EncryptionConfig'
                  |'AWS::SSM::AssociationCompliance'|'AWS::SSM::PatchCompliance'
                  |'AWS::Shield::Protection'|'AWS::ShieldRegional::Protection'
                  |'AWS::Config::ResourceCompliance'|'AWS::LicenseManager::LicenseConfiguration'
                  |'AWS::ApiGateway::DomainName'|'AWS::ApiGateway::Method'|'AWS::ApiGateway::Stage'
                  |'AWS::ApiGateway::RestApi'|'AWS::ApiGatewayV2::DomainName'
                  |'AWS::ApiGatewayV2::Stage'|'AWS::ApiGatewayV2::Api'|'AWS::CodePipeline::Pipeline'
                  |'AWS::ServiceCatalog::CloudFormationProvisionedProduct'
                  |'AWS::ServiceCatalog::CloudFormationProduct'|'AWS::ServiceCatalog::Portfolio',
              resourceIds=[
                  'string',
              ],
              resourceName='string',
              limit=123,
              includeDeletedResources=True|False,
              PaginationConfig={
                  'MaxItems': 123,
                  'StartingToken': 'string'
              }
          )
        :type resourceType: string
        :param resourceType: **[REQUIRED]**

          The type of resources that you want AWS Config to list in the response.

        :type resourceIds: list
        :param resourceIds:

          The IDs of only those resources that you want AWS Config to list in the response. If you
          do not specify this parameter, AWS Config lists all resources of the specified type that
          it has discovered.

          - *(string) --*

        :type resourceName: string
        :param resourceName:

          The custom name of only those resources that you want AWS Config to list in the response.
          If you do not specify this parameter, AWS Config lists all resources of the specified type
          that it has discovered.

        :type limit: integer
        :param limit:

          The maximum number of resource identifiers returned on each page. The default is 100. You
          cannot specify a number greater than 100. If you specify 0, AWS Config uses the default.

        :type includeDeletedResources: boolean
        :param includeDeletedResources:

          Specifies whether AWS Config includes deleted resources in the results. By default,
          deleted resources are not included.

        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than
            the value specified in max-items then a ``NextToken`` will be provided in the output
            that you can use to resume pagination.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'resourceIdentifiers': [
                    {
                        'resourceType':
                        'AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'
                        |'AWS::EC2::Instance'|'AWS::EC2::InternetGateway'
                        |'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'
                        |'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'
                        |'AWS::EC2::Subnet'|'AWS::CloudTrail::Trail'
                        |'AWS::EC2::Volume'|'AWS::EC2::VPC'
                        |'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'
                        |'AWS::EC2::RegisteredHAInstance'|'AWS::EC2::NatGateway'
                        |'AWS::EC2::EgressOnlyInternetGateway'
                        |'AWS::EC2::VPCEndpoint'|'AWS::EC2::VPCEndpointService'
                        |'AWS::EC2::FlowLog'|'AWS::EC2::VPCPeeringConnection'
                        |'AWS::IAM::Group'|'AWS::IAM::Policy'|'AWS::IAM::Role'
                        |'AWS::IAM::User'
                        |'AWS::ElasticLoadBalancingV2::LoadBalancer'
                        |'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'
                        |'AWS::RDS::DBParameterGroup'|'AWS::RDS::DBOptionGroup'
                        |'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'
                        |'AWS::RDS::DBSnapshot'|'AWS::RDS::DBCluster'
                        |'AWS::RDS::DBClusterParameterGroup'
                        |'AWS::RDS::DBClusterSnapshot'|'AWS::RDS::EventSubscription'
                        |'AWS::S3::Bucket'|'AWS::S3::AccountPublicAccessBlock'
                        |'AWS::Redshift::Cluster'|'AWS::Redshift::ClusterSnapshot'
                        |'AWS::Redshift::ClusterParameterGroup'
                        |'AWS::Redshift::ClusterSecurityGroup'
                        |'AWS::Redshift::ClusterSubnetGroup'
                        |'AWS::Redshift::EventSubscription'
                        |'AWS::SSM::ManagedInstanceInventory'
                        |'AWS::CloudWatch::Alarm'|'AWS::CloudFormation::Stack'
                        |'AWS::ElasticLoadBalancing::LoadBalancer'
                        |'AWS::AutoScaling::AutoScalingGroup'
                        |'AWS::AutoScaling::LaunchConfiguration'
                        |'AWS::AutoScaling::ScalingPolicy'
                        |'AWS::AutoScaling::ScheduledAction'|'AWS::DynamoDB::Table'
                        |'AWS::CodeBuild::Project'|'AWS::WAF::RateBasedRule'
                        |'AWS::WAF::Rule'|'AWS::WAF::RuleGroup'|'AWS::WAF::WebACL'
                        |'AWS::WAFRegional::RateBasedRule'|'AWS::WAFRegional::Rule'
                        |'AWS::WAFRegional::RuleGroup'|'AWS::WAFRegional::WebACL'
                        |'AWS::CloudFront::Distribution'
                        |'AWS::CloudFront::StreamingDistribution'
                        |'AWS::Lambda::Alias'|'AWS::Lambda::Function'
                        |'AWS::ElasticBeanstalk::Application'
                        |'AWS::ElasticBeanstalk::ApplicationVersion'
                        |'AWS::ElasticBeanstalk::Environment'
                        |'AWS::MobileHub::Project'|'AWS::XRay::EncryptionConfig'
                        |'AWS::SSM::AssociationCompliance'
                        |'AWS::SSM::PatchCompliance'|'AWS::Shield::Protection'
                        |'AWS::ShieldRegional::Protection'
                        |'AWS::Config::ResourceCompliance'
                        |'AWS::LicenseManager::LicenseConfiguration'
                        |'AWS::ApiGateway::DomainName'|'AWS::ApiGateway::Method'
                        |'AWS::ApiGateway::Stage'|'AWS::ApiGateway::RestApi'
                        |'AWS::ApiGatewayV2::DomainName'|'AWS::ApiGatewayV2::Stage'
                        |'AWS::ApiGatewayV2::Api'|'AWS::CodePipeline::Pipeline'
                        |'AWS::ServiceCatalog::CloudFormationProvisionedProduct'
                        |'AWS::ServiceCatalog::CloudFormationProduct'
                        |'AWS::ServiceCatalog::Portfolio',
                        'resourceId': 'string',
                        'resourceName': 'string',
                        'resourceDeletionTime': datetime(2015, 1, 1)
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **resourceIdentifiers** *(list) --*

              The details that identify a resource that is discovered by AWS Config, including the
              resource type, ID, and (if available) the custom resource name.

              - *(dict) --*

                The details that identify a resource that is discovered by AWS Config, including the
                resource type, ID, and (if available) the custom resource name.

                - **resourceType** *(string) --*

                  The type of resource.

                - **resourceId** *(string) --*

                  The ID of the resource (for example, ``sg-xxxxxx`` ).

                - **resourceName** *(string) --*

                  The custom name of the resource (if available).

                - **resourceDeletionTime** *(datetime) --*

                  The time that the resource was deleted.

            - **NextToken** *(string) --*

              A token to resume pagination.
        """
