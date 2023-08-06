"Main interface for iot service Paginators"
from __future__ import annotations

from datetime import datetime
import sys
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_iot.type_defs import (
    ListActiveViolationsResponseTypeDef,
    ListAttachedPoliciesResponseTypeDef,
    ListAuditFindingsResponseTypeDef,
    ListAuditTasksResponseTypeDef,
    ListAuthorizersResponseTypeDef,
    ListBillingGroupsResponseTypeDef,
    ListCACertificatesResponseTypeDef,
    ListCertificatesByCAResponseTypeDef,
    ListCertificatesResponseTypeDef,
    ListIndicesResponseTypeDef,
    ListJobExecutionsForJobResponseTypeDef,
    ListJobExecutionsForThingResponseTypeDef,
    ListJobsResponseTypeDef,
    ListOTAUpdatesResponseTypeDef,
    ListOutgoingCertificatesResponseTypeDef,
    ListPoliciesResponseTypeDef,
    ListPolicyPrincipalsResponseTypeDef,
    ListPrincipalPoliciesResponseTypeDef,
    ListPrincipalThingsResponseTypeDef,
    ListRoleAliasesResponseTypeDef,
    ListScheduledAuditsResponseTypeDef,
    ListSecurityProfilesForTargetResponseTypeDef,
    ListSecurityProfilesResponseTypeDef,
    ListStreamsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTargetsForPolicyResponseTypeDef,
    ListTargetsForSecurityProfileResponseTypeDef,
    ListThingGroupsForThingResponseTypeDef,
    ListThingGroupsResponseTypeDef,
    ListThingRegistrationTasksResponseTypeDef,
    ListThingTypesResponseTypeDef,
    ListThingsInBillingGroupResponseTypeDef,
    ListThingsInThingGroupResponseTypeDef,
    ListThingsResponseTypeDef,
    ListTopicRulesResponseTypeDef,
    ListV2LoggingLevelsResponseTypeDef,
    ListViolationEventsResponseTypeDef,
    PaginatorConfigTypeDef,
    ResourceIdentifierTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ListActiveViolationsPaginator",
    "ListAttachedPoliciesPaginator",
    "ListAuditFindingsPaginator",
    "ListAuditTasksPaginator",
    "ListAuthorizersPaginator",
    "ListBillingGroupsPaginator",
    "ListCACertificatesPaginator",
    "ListCertificatesPaginator",
    "ListCertificatesByCAPaginator",
    "ListIndicesPaginator",
    "ListJobExecutionsForJobPaginator",
    "ListJobExecutionsForThingPaginator",
    "ListJobsPaginator",
    "ListOTAUpdatesPaginator",
    "ListOutgoingCertificatesPaginator",
    "ListPoliciesPaginator",
    "ListPolicyPrincipalsPaginator",
    "ListPrincipalPoliciesPaginator",
    "ListPrincipalThingsPaginator",
    "ListRoleAliasesPaginator",
    "ListScheduledAuditsPaginator",
    "ListSecurityProfilesPaginator",
    "ListSecurityProfilesForTargetPaginator",
    "ListStreamsPaginator",
    "ListTagsForResourcePaginator",
    "ListTargetsForPolicyPaginator",
    "ListTargetsForSecurityProfilePaginator",
    "ListThingGroupsPaginator",
    "ListThingGroupsForThingPaginator",
    "ListThingRegistrationTasksPaginator",
    "ListThingTypesPaginator",
    "ListThingsPaginator",
    "ListThingsInBillingGroupPaginator",
    "ListThingsInThingGroupPaginator",
    "ListTopicRulesPaginator",
    "ListV2LoggingLevelsPaginator",
    "ListViolationEventsPaginator",
)


class ListActiveViolationsPaginator(Boto3Paginator):
    """
    [Paginator.ListActiveViolations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListActiveViolations)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        thingName: str = None,
        securityProfileName: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> ListActiveViolationsResponseTypeDef:
        """
        [ListActiveViolations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListActiveViolations.paginate)
        """


class ListAttachedPoliciesPaginator(Boto3Paginator):
    """
    [Paginator.ListAttachedPolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListAttachedPolicies)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, target: str, recursive: bool = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListAttachedPoliciesResponseTypeDef:
        """
        [ListAttachedPolicies.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListAttachedPolicies.paginate)
        """


class ListAuditFindingsPaginator(Boto3Paginator):
    """
    [Paginator.ListAuditFindings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListAuditFindings)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        taskId: str = None,
        checkName: str = None,
        resourceIdentifier: ResourceIdentifierTypeDef = None,
        startTime: datetime = None,
        endTime: datetime = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> ListAuditFindingsResponseTypeDef:
        """
        [ListAuditFindings.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListAuditFindings.paginate)
        """


class ListAuditTasksPaginator(Boto3Paginator):
    """
    [Paginator.ListAuditTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListAuditTasks)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        startTime: datetime,
        endTime: datetime,
        taskType: Literal["ON_DEMAND_AUDIT_TASK", "SCHEDULED_AUDIT_TASK"] = None,
        taskStatus: Literal["IN_PROGRESS", "COMPLETED", "FAILED", "CANCELED"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> ListAuditTasksResponseTypeDef:
        """
        [ListAuditTasks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListAuditTasks.paginate)
        """


class ListAuthorizersPaginator(Boto3Paginator):
    """
    [Paginator.ListAuthorizers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListAuthorizers)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ascendingOrder: bool = None,
        status: Literal["ACTIVE", "INACTIVE"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> ListAuthorizersResponseTypeDef:
        """
        [ListAuthorizers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListAuthorizers.paginate)
        """


class ListBillingGroupsPaginator(Boto3Paginator):
    """
    [Paginator.ListBillingGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListBillingGroups)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, namePrefixFilter: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListBillingGroupsResponseTypeDef:
        """
        [ListBillingGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListBillingGroups.paginate)
        """


class ListCACertificatesPaginator(Boto3Paginator):
    """
    [Paginator.ListCACertificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListCACertificates)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, ascendingOrder: bool = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListCACertificatesResponseTypeDef:
        """
        [ListCACertificates.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListCACertificates.paginate)
        """


class ListCertificatesPaginator(Boto3Paginator):
    """
    [Paginator.ListCertificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListCertificates)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, ascendingOrder: bool = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListCertificatesResponseTypeDef:
        """
        [ListCertificates.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListCertificates.paginate)
        """


class ListCertificatesByCAPaginator(Boto3Paginator):
    """
    [Paginator.ListCertificatesByCA documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListCertificatesByCA)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        caCertificateId: str,
        ascendingOrder: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> ListCertificatesByCAResponseTypeDef:
        """
        [ListCertificatesByCA.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListCertificatesByCA.paginate)
        """


class ListIndicesPaginator(Boto3Paginator):
    """
    [Paginator.ListIndices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListIndices)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListIndicesResponseTypeDef:
        """
        [ListIndices.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListIndices.paginate)
        """


class ListJobExecutionsForJobPaginator(Boto3Paginator):
    """
    [Paginator.ListJobExecutionsForJob documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListJobExecutionsForJob)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        jobId: str,
        status: Literal[
            "QUEUED",
            "IN_PROGRESS",
            "SUCCEEDED",
            "FAILED",
            "TIMED_OUT",
            "REJECTED",
            "REMOVED",
            "CANCELED",
        ] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> ListJobExecutionsForJobResponseTypeDef:
        """
        [ListJobExecutionsForJob.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListJobExecutionsForJob.paginate)
        """


class ListJobExecutionsForThingPaginator(Boto3Paginator):
    """
    [Paginator.ListJobExecutionsForThing documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListJobExecutionsForThing)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        thingName: str,
        status: Literal[
            "QUEUED",
            "IN_PROGRESS",
            "SUCCEEDED",
            "FAILED",
            "TIMED_OUT",
            "REJECTED",
            "REMOVED",
            "CANCELED",
        ] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> ListJobExecutionsForThingResponseTypeDef:
        """
        [ListJobExecutionsForThing.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListJobExecutionsForThing.paginate)
        """


class ListJobsPaginator(Boto3Paginator):
    """
    [Paginator.ListJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListJobs)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        status: Literal["IN_PROGRESS", "CANCELED", "COMPLETED", "DELETION_IN_PROGRESS"] = None,
        targetSelection: Literal["CONTINUOUS", "SNAPSHOT"] = None,
        thingGroupName: str = None,
        thingGroupId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> ListJobsResponseTypeDef:
        """
        [ListJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListJobs.paginate)
        """


class ListOTAUpdatesPaginator(Boto3Paginator):
    """
    [Paginator.ListOTAUpdates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListOTAUpdates)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        otaUpdateStatus: Literal[
            "CREATE_PENDING", "CREATE_IN_PROGRESS", "CREATE_COMPLETE", "CREATE_FAILED"
        ] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> ListOTAUpdatesResponseTypeDef:
        """
        [ListOTAUpdates.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListOTAUpdates.paginate)
        """


class ListOutgoingCertificatesPaginator(Boto3Paginator):
    """
    [Paginator.ListOutgoingCertificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListOutgoingCertificates)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, ascendingOrder: bool = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListOutgoingCertificatesResponseTypeDef:
        """
        [ListOutgoingCertificates.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListOutgoingCertificates.paginate)
        """


class ListPoliciesPaginator(Boto3Paginator):
    """
    [Paginator.ListPolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListPolicies)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, ascendingOrder: bool = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListPoliciesResponseTypeDef:
        """
        [ListPolicies.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListPolicies.paginate)
        """


class ListPolicyPrincipalsPaginator(Boto3Paginator):
    """
    [Paginator.ListPolicyPrincipals documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListPolicyPrincipals)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        policyName: str,
        ascendingOrder: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> ListPolicyPrincipalsResponseTypeDef:
        """
        [ListPolicyPrincipals.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListPolicyPrincipals.paginate)
        """


class ListPrincipalPoliciesPaginator(Boto3Paginator):
    """
    [Paginator.ListPrincipalPolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListPrincipalPolicies)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        principal: str,
        ascendingOrder: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> ListPrincipalPoliciesResponseTypeDef:
        """
        [ListPrincipalPolicies.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListPrincipalPolicies.paginate)
        """


class ListPrincipalThingsPaginator(Boto3Paginator):
    """
    [Paginator.ListPrincipalThings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListPrincipalThings)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, principal: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListPrincipalThingsResponseTypeDef:
        """
        [ListPrincipalThings.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListPrincipalThings.paginate)
        """


class ListRoleAliasesPaginator(Boto3Paginator):
    """
    [Paginator.ListRoleAliases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListRoleAliases)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, ascendingOrder: bool = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListRoleAliasesResponseTypeDef:
        """
        [ListRoleAliases.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListRoleAliases.paginate)
        """


class ListScheduledAuditsPaginator(Boto3Paginator):
    """
    [Paginator.ListScheduledAudits documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListScheduledAudits)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListScheduledAuditsResponseTypeDef:
        """
        [ListScheduledAudits.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListScheduledAudits.paginate)
        """


class ListSecurityProfilesPaginator(Boto3Paginator):
    """
    [Paginator.ListSecurityProfiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListSecurityProfiles)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListSecurityProfilesResponseTypeDef:
        """
        [ListSecurityProfiles.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListSecurityProfiles.paginate)
        """


class ListSecurityProfilesForTargetPaginator(Boto3Paginator):
    """
    [Paginator.ListSecurityProfilesForTarget documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListSecurityProfilesForTarget)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        securityProfileTargetArn: str,
        recursive: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> ListSecurityProfilesForTargetResponseTypeDef:
        """
        [ListSecurityProfilesForTarget.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListSecurityProfilesForTarget.paginate)
        """


class ListStreamsPaginator(Boto3Paginator):
    """
    [Paginator.ListStreams documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListStreams)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, ascendingOrder: bool = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListStreamsResponseTypeDef:
        """
        [ListStreams.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListStreams.paginate)
        """


class ListTagsForResourcePaginator(Boto3Paginator):
    """
    [Paginator.ListTagsForResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListTagsForResource)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, resourceArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListTagsForResourceResponseTypeDef:
        """
        [ListTagsForResource.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListTagsForResource.paginate)
        """


class ListTargetsForPolicyPaginator(Boto3Paginator):
    """
    [Paginator.ListTargetsForPolicy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListTargetsForPolicy)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, policyName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListTargetsForPolicyResponseTypeDef:
        """
        [ListTargetsForPolicy.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListTargetsForPolicy.paginate)
        """


class ListTargetsForSecurityProfilePaginator(Boto3Paginator):
    """
    [Paginator.ListTargetsForSecurityProfile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListTargetsForSecurityProfile)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, securityProfileName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListTargetsForSecurityProfileResponseTypeDef:
        """
        [ListTargetsForSecurityProfile.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListTargetsForSecurityProfile.paginate)
        """


class ListThingGroupsPaginator(Boto3Paginator):
    """
    [Paginator.ListThingGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListThingGroups)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        parentGroup: str = None,
        namePrefixFilter: str = None,
        recursive: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> ListThingGroupsResponseTypeDef:
        """
        [ListThingGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListThingGroups.paginate)
        """


class ListThingGroupsForThingPaginator(Boto3Paginator):
    """
    [Paginator.ListThingGroupsForThing documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListThingGroupsForThing)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, thingName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListThingGroupsForThingResponseTypeDef:
        """
        [ListThingGroupsForThing.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListThingGroupsForThing.paginate)
        """


class ListThingRegistrationTasksPaginator(Boto3Paginator):
    """
    [Paginator.ListThingRegistrationTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListThingRegistrationTasks)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        status: Literal["InProgress", "Completed", "Failed", "Cancelled", "Cancelling"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> ListThingRegistrationTasksResponseTypeDef:
        """
        [ListThingRegistrationTasks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListThingRegistrationTasks.paginate)
        """


class ListThingTypesPaginator(Boto3Paginator):
    """
    [Paginator.ListThingTypes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListThingTypes)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, thingTypeName: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListThingTypesResponseTypeDef:
        """
        [ListThingTypes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListThingTypes.paginate)
        """


class ListThingsPaginator(Boto3Paginator):
    """
    [Paginator.ListThings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListThings)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        attributeName: str = None,
        attributeValue: str = None,
        thingTypeName: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> ListThingsResponseTypeDef:
        """
        [ListThings.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListThings.paginate)
        """


class ListThingsInBillingGroupPaginator(Boto3Paginator):
    """
    [Paginator.ListThingsInBillingGroup documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListThingsInBillingGroup)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, billingGroupName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListThingsInBillingGroupResponseTypeDef:
        """
        [ListThingsInBillingGroup.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListThingsInBillingGroup.paginate)
        """


class ListThingsInThingGroupPaginator(Boto3Paginator):
    """
    [Paginator.ListThingsInThingGroup documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListThingsInThingGroup)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        thingGroupName: str,
        recursive: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> ListThingsInThingGroupResponseTypeDef:
        """
        [ListThingsInThingGroup.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListThingsInThingGroup.paginate)
        """


class ListTopicRulesPaginator(Boto3Paginator):
    """
    [Paginator.ListTopicRules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListTopicRules)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        topic: str = None,
        ruleDisabled: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> ListTopicRulesResponseTypeDef:
        """
        [ListTopicRules.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListTopicRules.paginate)
        """


class ListV2LoggingLevelsPaginator(Boto3Paginator):
    """
    [Paginator.ListV2LoggingLevels documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListV2LoggingLevels)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        targetType: Literal["DEFAULT", "THING_GROUP"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> ListV2LoggingLevelsResponseTypeDef:
        """
        [ListV2LoggingLevels.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListV2LoggingLevels.paginate)
        """


class ListViolationEventsPaginator(Boto3Paginator):
    """
    [Paginator.ListViolationEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListViolationEvents)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        startTime: datetime,
        endTime: datetime,
        thingName: str = None,
        securityProfileName: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> ListViolationEventsResponseTypeDef:
        """
        [ListViolationEvents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListViolationEvents.paginate)
        """
