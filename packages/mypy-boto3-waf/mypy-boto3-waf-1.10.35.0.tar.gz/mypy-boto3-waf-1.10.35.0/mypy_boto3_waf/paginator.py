"Main interface for waf service Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_waf.type_defs import (
    GetRateBasedRuleManagedKeysResponseTypeDef,
    ListActivatedRulesInRuleGroupResponseTypeDef,
    ListByteMatchSetsResponseTypeDef,
    ListGeoMatchSetsResponseTypeDef,
    ListIPSetsResponseTypeDef,
    ListLoggingConfigurationsResponseTypeDef,
    ListRateBasedRulesResponseTypeDef,
    ListRegexMatchSetsResponseTypeDef,
    ListRegexPatternSetsResponseTypeDef,
    ListRuleGroupsResponseTypeDef,
    ListRulesResponseTypeDef,
    ListSizeConstraintSetsResponseTypeDef,
    ListSqlInjectionMatchSetsResponseTypeDef,
    ListSubscribedRuleGroupsResponseTypeDef,
    ListWebACLsResponseTypeDef,
    ListXssMatchSetsResponseTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = (
    "GetRateBasedRuleManagedKeysPaginator",
    "ListActivatedRulesInRuleGroupPaginator",
    "ListByteMatchSetsPaginator",
    "ListGeoMatchSetsPaginator",
    "ListIPSetsPaginator",
    "ListLoggingConfigurationsPaginator",
    "ListRateBasedRulesPaginator",
    "ListRegexMatchSetsPaginator",
    "ListRegexPatternSetsPaginator",
    "ListRuleGroupsPaginator",
    "ListRulesPaginator",
    "ListSizeConstraintSetsPaginator",
    "ListSqlInjectionMatchSetsPaginator",
    "ListSubscribedRuleGroupsPaginator",
    "ListWebACLsPaginator",
    "ListXssMatchSetsPaginator",
)


class GetRateBasedRuleManagedKeysPaginator(Boto3Paginator):
    """
    [Paginator.GetRateBasedRuleManagedKeys documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.35/reference/services/waf.html#WAF.Paginator.GetRateBasedRuleManagedKeys)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, RuleId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> GetRateBasedRuleManagedKeysResponseTypeDef:
        """
        [GetRateBasedRuleManagedKeys.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.35/reference/services/waf.html#WAF.Paginator.GetRateBasedRuleManagedKeys.paginate)
        """


class ListActivatedRulesInRuleGroupPaginator(Boto3Paginator):
    """
    [Paginator.ListActivatedRulesInRuleGroup documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.35/reference/services/waf.html#WAF.Paginator.ListActivatedRulesInRuleGroup)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, RuleGroupId: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListActivatedRulesInRuleGroupResponseTypeDef:
        """
        [ListActivatedRulesInRuleGroup.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.35/reference/services/waf.html#WAF.Paginator.ListActivatedRulesInRuleGroup.paginate)
        """


class ListByteMatchSetsPaginator(Boto3Paginator):
    """
    [Paginator.ListByteMatchSets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.35/reference/services/waf.html#WAF.Paginator.ListByteMatchSets)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListByteMatchSetsResponseTypeDef:
        """
        [ListByteMatchSets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.35/reference/services/waf.html#WAF.Paginator.ListByteMatchSets.paginate)
        """


class ListGeoMatchSetsPaginator(Boto3Paginator):
    """
    [Paginator.ListGeoMatchSets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.35/reference/services/waf.html#WAF.Paginator.ListGeoMatchSets)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListGeoMatchSetsResponseTypeDef:
        """
        [ListGeoMatchSets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.35/reference/services/waf.html#WAF.Paginator.ListGeoMatchSets.paginate)
        """


class ListIPSetsPaginator(Boto3Paginator):
    """
    [Paginator.ListIPSets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.35/reference/services/waf.html#WAF.Paginator.ListIPSets)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListIPSetsResponseTypeDef:
        """
        [ListIPSets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.35/reference/services/waf.html#WAF.Paginator.ListIPSets.paginate)
        """


class ListLoggingConfigurationsPaginator(Boto3Paginator):
    """
    [Paginator.ListLoggingConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.35/reference/services/waf.html#WAF.Paginator.ListLoggingConfigurations)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListLoggingConfigurationsResponseTypeDef:
        """
        [ListLoggingConfigurations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.35/reference/services/waf.html#WAF.Paginator.ListLoggingConfigurations.paginate)
        """


class ListRateBasedRulesPaginator(Boto3Paginator):
    """
    [Paginator.ListRateBasedRules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.35/reference/services/waf.html#WAF.Paginator.ListRateBasedRules)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListRateBasedRulesResponseTypeDef:
        """
        [ListRateBasedRules.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.35/reference/services/waf.html#WAF.Paginator.ListRateBasedRules.paginate)
        """


class ListRegexMatchSetsPaginator(Boto3Paginator):
    """
    [Paginator.ListRegexMatchSets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.35/reference/services/waf.html#WAF.Paginator.ListRegexMatchSets)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListRegexMatchSetsResponseTypeDef:
        """
        [ListRegexMatchSets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.35/reference/services/waf.html#WAF.Paginator.ListRegexMatchSets.paginate)
        """


class ListRegexPatternSetsPaginator(Boto3Paginator):
    """
    [Paginator.ListRegexPatternSets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.35/reference/services/waf.html#WAF.Paginator.ListRegexPatternSets)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListRegexPatternSetsResponseTypeDef:
        """
        [ListRegexPatternSets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.35/reference/services/waf.html#WAF.Paginator.ListRegexPatternSets.paginate)
        """


class ListRuleGroupsPaginator(Boto3Paginator):
    """
    [Paginator.ListRuleGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.35/reference/services/waf.html#WAF.Paginator.ListRuleGroups)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListRuleGroupsResponseTypeDef:
        """
        [ListRuleGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.35/reference/services/waf.html#WAF.Paginator.ListRuleGroups.paginate)
        """


class ListRulesPaginator(Boto3Paginator):
    """
    [Paginator.ListRules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.35/reference/services/waf.html#WAF.Paginator.ListRules)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(self, PaginationConfig: PaginatorConfigTypeDef = None) -> ListRulesResponseTypeDef:
        """
        [ListRules.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.35/reference/services/waf.html#WAF.Paginator.ListRules.paginate)
        """


class ListSizeConstraintSetsPaginator(Boto3Paginator):
    """
    [Paginator.ListSizeConstraintSets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.35/reference/services/waf.html#WAF.Paginator.ListSizeConstraintSets)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListSizeConstraintSetsResponseTypeDef:
        """
        [ListSizeConstraintSets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.35/reference/services/waf.html#WAF.Paginator.ListSizeConstraintSets.paginate)
        """


class ListSqlInjectionMatchSetsPaginator(Boto3Paginator):
    """
    [Paginator.ListSqlInjectionMatchSets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.35/reference/services/waf.html#WAF.Paginator.ListSqlInjectionMatchSets)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListSqlInjectionMatchSetsResponseTypeDef:
        """
        [ListSqlInjectionMatchSets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.35/reference/services/waf.html#WAF.Paginator.ListSqlInjectionMatchSets.paginate)
        """


class ListSubscribedRuleGroupsPaginator(Boto3Paginator):
    """
    [Paginator.ListSubscribedRuleGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.35/reference/services/waf.html#WAF.Paginator.ListSubscribedRuleGroups)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListSubscribedRuleGroupsResponseTypeDef:
        """
        [ListSubscribedRuleGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.35/reference/services/waf.html#WAF.Paginator.ListSubscribedRuleGroups.paginate)
        """


class ListWebACLsPaginator(Boto3Paginator):
    """
    [Paginator.ListWebACLs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.35/reference/services/waf.html#WAF.Paginator.ListWebACLs)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListWebACLsResponseTypeDef:
        """
        [ListWebACLs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.35/reference/services/waf.html#WAF.Paginator.ListWebACLs.paginate)
        """


class ListXssMatchSetsPaginator(Boto3Paginator):
    """
    [Paginator.ListXssMatchSets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.35/reference/services/waf.html#WAF.Paginator.ListXssMatchSets)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListXssMatchSetsResponseTypeDef:
        """
        [ListXssMatchSets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.35/reference/services/waf.html#WAF.Paginator.ListXssMatchSets.paginate)
        """
