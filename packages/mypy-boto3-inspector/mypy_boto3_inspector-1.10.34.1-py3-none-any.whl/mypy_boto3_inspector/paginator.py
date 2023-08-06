"Main interface for inspector service Paginators"
from __future__ import annotations

from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_inspector.type_defs import (
    AgentFilterTypeDef,
    AssessmentRunFilterTypeDef,
    AssessmentTargetFilterTypeDef,
    AssessmentTemplateFilterTypeDef,
    FindingFilterTypeDef,
    ListAssessmentRunAgentsResponseTypeDef,
    ListAssessmentRunsResponseTypeDef,
    ListAssessmentTargetsResponseTypeDef,
    ListAssessmentTemplatesResponseTypeDef,
    ListEventSubscriptionsResponseTypeDef,
    ListExclusionsResponseTypeDef,
    ListFindingsResponseTypeDef,
    ListRulesPackagesResponseTypeDef,
    PaginatorConfigTypeDef,
    PreviewAgentsResponseTypeDef,
)


__all__ = (
    "ListAssessmentRunAgentsPaginator",
    "ListAssessmentRunsPaginator",
    "ListAssessmentTargetsPaginator",
    "ListAssessmentTemplatesPaginator",
    "ListEventSubscriptionsPaginator",
    "ListExclusionsPaginator",
    "ListFindingsPaginator",
    "ListRulesPackagesPaginator",
    "PreviewAgentsPaginator",
)


class ListAssessmentRunAgentsPaginator(Boto3Paginator):
    """
    [Paginator.ListAssessmentRunAgents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/inspector.html#Inspector.Paginator.ListAssessmentRunAgents)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        assessmentRunArn: str,
        filter: AgentFilterTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> ListAssessmentRunAgentsResponseTypeDef:
        """
        [ListAssessmentRunAgents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/inspector.html#Inspector.Paginator.ListAssessmentRunAgents.paginate)
        """


class ListAssessmentRunsPaginator(Boto3Paginator):
    """
    [Paginator.ListAssessmentRuns documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/inspector.html#Inspector.Paginator.ListAssessmentRuns)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        assessmentTemplateArns: List[str] = None,
        filter: AssessmentRunFilterTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> ListAssessmentRunsResponseTypeDef:
        """
        [ListAssessmentRuns.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/inspector.html#Inspector.Paginator.ListAssessmentRuns.paginate)
        """


class ListAssessmentTargetsPaginator(Boto3Paginator):
    """
    [Paginator.ListAssessmentTargets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/inspector.html#Inspector.Paginator.ListAssessmentTargets)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        filter: AssessmentTargetFilterTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> ListAssessmentTargetsResponseTypeDef:
        """
        [ListAssessmentTargets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/inspector.html#Inspector.Paginator.ListAssessmentTargets.paginate)
        """


class ListAssessmentTemplatesPaginator(Boto3Paginator):
    """
    [Paginator.ListAssessmentTemplates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/inspector.html#Inspector.Paginator.ListAssessmentTemplates)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        assessmentTargetArns: List[str] = None,
        filter: AssessmentTemplateFilterTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> ListAssessmentTemplatesResponseTypeDef:
        """
        [ListAssessmentTemplates.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/inspector.html#Inspector.Paginator.ListAssessmentTemplates.paginate)
        """


class ListEventSubscriptionsPaginator(Boto3Paginator):
    """
    [Paginator.ListEventSubscriptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/inspector.html#Inspector.Paginator.ListEventSubscriptions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, resourceArn: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListEventSubscriptionsResponseTypeDef:
        """
        [ListEventSubscriptions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/inspector.html#Inspector.Paginator.ListEventSubscriptions.paginate)
        """


class ListExclusionsPaginator(Boto3Paginator):
    """
    [Paginator.ListExclusions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/inspector.html#Inspector.Paginator.ListExclusions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, assessmentRunArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListExclusionsResponseTypeDef:
        """
        [ListExclusions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/inspector.html#Inspector.Paginator.ListExclusions.paginate)
        """


class ListFindingsPaginator(Boto3Paginator):
    """
    [Paginator.ListFindings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/inspector.html#Inspector.Paginator.ListFindings)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        assessmentRunArns: List[str] = None,
        filter: FindingFilterTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> ListFindingsResponseTypeDef:
        """
        [ListFindings.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/inspector.html#Inspector.Paginator.ListFindings.paginate)
        """


class ListRulesPackagesPaginator(Boto3Paginator):
    """
    [Paginator.ListRulesPackages documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/inspector.html#Inspector.Paginator.ListRulesPackages)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListRulesPackagesResponseTypeDef:
        """
        [ListRulesPackages.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/inspector.html#Inspector.Paginator.ListRulesPackages.paginate)
        """


class PreviewAgentsPaginator(Boto3Paginator):
    """
    [Paginator.PreviewAgents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/inspector.html#Inspector.Paginator.PreviewAgents)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, previewAgentsArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> PreviewAgentsResponseTypeDef:
        """
        [PreviewAgents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/inspector.html#Inspector.Paginator.PreviewAgents.paginate)
        """
