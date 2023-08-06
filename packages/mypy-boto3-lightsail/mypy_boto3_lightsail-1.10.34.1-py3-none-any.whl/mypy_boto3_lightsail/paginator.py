"Main interface for lightsail service Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_lightsail.type_defs import (
    GetActiveNamesResultTypeDef,
    GetBlueprintsResultTypeDef,
    GetBundlesResultTypeDef,
    GetCloudFormationStackRecordsResultTypeDef,
    GetDiskSnapshotsResultTypeDef,
    GetDisksResultTypeDef,
    GetDomainsResultTypeDef,
    GetExportSnapshotRecordsResultTypeDef,
    GetInstanceSnapshotsResultTypeDef,
    GetInstancesResultTypeDef,
    GetKeyPairsResultTypeDef,
    GetLoadBalancersResultTypeDef,
    GetOperationsResultTypeDef,
    GetRelationalDatabaseBlueprintsResultTypeDef,
    GetRelationalDatabaseBundlesResultTypeDef,
    GetRelationalDatabaseEventsResultTypeDef,
    GetRelationalDatabaseParametersResultTypeDef,
    GetRelationalDatabaseSnapshotsResultTypeDef,
    GetRelationalDatabasesResultTypeDef,
    GetStaticIpsResultTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = (
    "GetActiveNamesPaginator",
    "GetBlueprintsPaginator",
    "GetBundlesPaginator",
    "GetCloudFormationStackRecordsPaginator",
    "GetDiskSnapshotsPaginator",
    "GetDisksPaginator",
    "GetDomainsPaginator",
    "GetExportSnapshotRecordsPaginator",
    "GetInstanceSnapshotsPaginator",
    "GetInstancesPaginator",
    "GetKeyPairsPaginator",
    "GetLoadBalancersPaginator",
    "GetOperationsPaginator",
    "GetRelationalDatabaseBlueprintsPaginator",
    "GetRelationalDatabaseBundlesPaginator",
    "GetRelationalDatabaseEventsPaginator",
    "GetRelationalDatabaseParametersPaginator",
    "GetRelationalDatabaseSnapshotsPaginator",
    "GetRelationalDatabasesPaginator",
    "GetStaticIpsPaginator",
)


class GetActiveNamesPaginator(Boto3Paginator):
    """
    [Paginator.GetActiveNames documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lightsail.html#Lightsail.Paginator.GetActiveNames)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> GetActiveNamesResultTypeDef:
        """
        [GetActiveNames.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lightsail.html#Lightsail.Paginator.GetActiveNames.paginate)
        """


class GetBlueprintsPaginator(Boto3Paginator):
    """
    [Paginator.GetBlueprints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lightsail.html#Lightsail.Paginator.GetBlueprints)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, includeInactive: bool = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> GetBlueprintsResultTypeDef:
        """
        [GetBlueprints.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lightsail.html#Lightsail.Paginator.GetBlueprints.paginate)
        """


class GetBundlesPaginator(Boto3Paginator):
    """
    [Paginator.GetBundles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lightsail.html#Lightsail.Paginator.GetBundles)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, includeInactive: bool = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> GetBundlesResultTypeDef:
        """
        [GetBundles.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lightsail.html#Lightsail.Paginator.GetBundles.paginate)
        """


class GetCloudFormationStackRecordsPaginator(Boto3Paginator):
    """
    [Paginator.GetCloudFormationStackRecords documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lightsail.html#Lightsail.Paginator.GetCloudFormationStackRecords)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> GetCloudFormationStackRecordsResultTypeDef:
        """
        [GetCloudFormationStackRecords.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lightsail.html#Lightsail.Paginator.GetCloudFormationStackRecords.paginate)
        """


class GetDiskSnapshotsPaginator(Boto3Paginator):
    """
    [Paginator.GetDiskSnapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lightsail.html#Lightsail.Paginator.GetDiskSnapshots)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> GetDiskSnapshotsResultTypeDef:
        """
        [GetDiskSnapshots.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lightsail.html#Lightsail.Paginator.GetDiskSnapshots.paginate)
        """


class GetDisksPaginator(Boto3Paginator):
    """
    [Paginator.GetDisks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lightsail.html#Lightsail.Paginator.GetDisks)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(self, PaginationConfig: PaginatorConfigTypeDef = None) -> GetDisksResultTypeDef:
        """
        [GetDisks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lightsail.html#Lightsail.Paginator.GetDisks.paginate)
        """


class GetDomainsPaginator(Boto3Paginator):
    """
    [Paginator.GetDomains documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lightsail.html#Lightsail.Paginator.GetDomains)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(self, PaginationConfig: PaginatorConfigTypeDef = None) -> GetDomainsResultTypeDef:
        """
        [GetDomains.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lightsail.html#Lightsail.Paginator.GetDomains.paginate)
        """


class GetExportSnapshotRecordsPaginator(Boto3Paginator):
    """
    [Paginator.GetExportSnapshotRecords documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lightsail.html#Lightsail.Paginator.GetExportSnapshotRecords)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> GetExportSnapshotRecordsResultTypeDef:
        """
        [GetExportSnapshotRecords.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lightsail.html#Lightsail.Paginator.GetExportSnapshotRecords.paginate)
        """


class GetInstanceSnapshotsPaginator(Boto3Paginator):
    """
    [Paginator.GetInstanceSnapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lightsail.html#Lightsail.Paginator.GetInstanceSnapshots)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> GetInstanceSnapshotsResultTypeDef:
        """
        [GetInstanceSnapshots.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lightsail.html#Lightsail.Paginator.GetInstanceSnapshots.paginate)
        """


class GetInstancesPaginator(Boto3Paginator):
    """
    [Paginator.GetInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lightsail.html#Lightsail.Paginator.GetInstances)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> GetInstancesResultTypeDef:
        """
        [GetInstances.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lightsail.html#Lightsail.Paginator.GetInstances.paginate)
        """


class GetKeyPairsPaginator(Boto3Paginator):
    """
    [Paginator.GetKeyPairs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lightsail.html#Lightsail.Paginator.GetKeyPairs)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(self, PaginationConfig: PaginatorConfigTypeDef = None) -> GetKeyPairsResultTypeDef:
        """
        [GetKeyPairs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lightsail.html#Lightsail.Paginator.GetKeyPairs.paginate)
        """


class GetLoadBalancersPaginator(Boto3Paginator):
    """
    [Paginator.GetLoadBalancers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lightsail.html#Lightsail.Paginator.GetLoadBalancers)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> GetLoadBalancersResultTypeDef:
        """
        [GetLoadBalancers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lightsail.html#Lightsail.Paginator.GetLoadBalancers.paginate)
        """


class GetOperationsPaginator(Boto3Paginator):
    """
    [Paginator.GetOperations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lightsail.html#Lightsail.Paginator.GetOperations)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> GetOperationsResultTypeDef:
        """
        [GetOperations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lightsail.html#Lightsail.Paginator.GetOperations.paginate)
        """


class GetRelationalDatabaseBlueprintsPaginator(Boto3Paginator):
    """
    [Paginator.GetRelationalDatabaseBlueprints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lightsail.html#Lightsail.Paginator.GetRelationalDatabaseBlueprints)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> GetRelationalDatabaseBlueprintsResultTypeDef:
        """
        [GetRelationalDatabaseBlueprints.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lightsail.html#Lightsail.Paginator.GetRelationalDatabaseBlueprints.paginate)
        """


class GetRelationalDatabaseBundlesPaginator(Boto3Paginator):
    """
    [Paginator.GetRelationalDatabaseBundles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lightsail.html#Lightsail.Paginator.GetRelationalDatabaseBundles)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> GetRelationalDatabaseBundlesResultTypeDef:
        """
        [GetRelationalDatabaseBundles.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lightsail.html#Lightsail.Paginator.GetRelationalDatabaseBundles.paginate)
        """


class GetRelationalDatabaseEventsPaginator(Boto3Paginator):
    """
    [Paginator.GetRelationalDatabaseEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lightsail.html#Lightsail.Paginator.GetRelationalDatabaseEvents)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        relationalDatabaseName: str,
        durationInMinutes: int = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> GetRelationalDatabaseEventsResultTypeDef:
        """
        [GetRelationalDatabaseEvents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lightsail.html#Lightsail.Paginator.GetRelationalDatabaseEvents.paginate)
        """


class GetRelationalDatabaseParametersPaginator(Boto3Paginator):
    """
    [Paginator.GetRelationalDatabaseParameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lightsail.html#Lightsail.Paginator.GetRelationalDatabaseParameters)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, relationalDatabaseName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> GetRelationalDatabaseParametersResultTypeDef:
        """
        [GetRelationalDatabaseParameters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lightsail.html#Lightsail.Paginator.GetRelationalDatabaseParameters.paginate)
        """


class GetRelationalDatabaseSnapshotsPaginator(Boto3Paginator):
    """
    [Paginator.GetRelationalDatabaseSnapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lightsail.html#Lightsail.Paginator.GetRelationalDatabaseSnapshots)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> GetRelationalDatabaseSnapshotsResultTypeDef:
        """
        [GetRelationalDatabaseSnapshots.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lightsail.html#Lightsail.Paginator.GetRelationalDatabaseSnapshots.paginate)
        """


class GetRelationalDatabasesPaginator(Boto3Paginator):
    """
    [Paginator.GetRelationalDatabases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lightsail.html#Lightsail.Paginator.GetRelationalDatabases)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> GetRelationalDatabasesResultTypeDef:
        """
        [GetRelationalDatabases.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lightsail.html#Lightsail.Paginator.GetRelationalDatabases.paginate)
        """


class GetStaticIpsPaginator(Boto3Paginator):
    """
    [Paginator.GetStaticIps documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lightsail.html#Lightsail.Paginator.GetStaticIps)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> GetStaticIpsResultTypeDef:
        """
        [GetStaticIps.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lightsail.html#Lightsail.Paginator.GetStaticIps.paginate)
        """
