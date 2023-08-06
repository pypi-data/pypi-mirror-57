"Main interface for groundstation service Paginators"
from __future__ import annotations

from datetime import datetime
import sys
from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_groundstation.type_defs import (
    ListConfigsResponseTypeDef,
    ListContactsResponseTypeDef,
    ListDataflowEndpointGroupsResponseTypeDef,
    ListGroundStationsResponseTypeDef,
    ListMissionProfilesResponseTypeDef,
    ListSatellitesResponseTypeDef,
    PaginatorConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ListConfigsPaginator",
    "ListContactsPaginator",
    "ListDataflowEndpointGroupsPaginator",
    "ListGroundStationsPaginator",
    "ListMissionProfilesPaginator",
    "ListSatellitesPaginator",
)


class ListConfigsPaginator(Boto3Paginator):
    """
    [Paginator.ListConfigs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/groundstation.html#GroundStation.Paginator.ListConfigs)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListConfigsResponseTypeDef:
        """
        [ListConfigs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/groundstation.html#GroundStation.Paginator.ListConfigs.paginate)
        """


class ListContactsPaginator(Boto3Paginator):
    """
    [Paginator.ListContacts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/groundstation.html#GroundStation.Paginator.ListContacts)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        endTime: datetime,
        startTime: datetime,
        statusList: List[
            Literal[
                "AVAILABLE",
                "AWS_CANCELLED",
                "CANCELLED",
                "COMPLETED",
                "FAILED",
                "FAILED_TO_SCHEDULE",
                "PASS",
                "POSTPASS",
                "PREPASS",
                "SCHEDULED",
                "SCHEDULING",
            ]
        ],
        groundStation: str = None,
        missionProfileArn: str = None,
        satelliteArn: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> ListContactsResponseTypeDef:
        """
        [ListContacts.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/groundstation.html#GroundStation.Paginator.ListContacts.paginate)
        """


class ListDataflowEndpointGroupsPaginator(Boto3Paginator):
    """
    [Paginator.ListDataflowEndpointGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/groundstation.html#GroundStation.Paginator.ListDataflowEndpointGroups)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListDataflowEndpointGroupsResponseTypeDef:
        """
        [ListDataflowEndpointGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/groundstation.html#GroundStation.Paginator.ListDataflowEndpointGroups.paginate)
        """


class ListGroundStationsPaginator(Boto3Paginator):
    """
    [Paginator.ListGroundStations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/groundstation.html#GroundStation.Paginator.ListGroundStations)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListGroundStationsResponseTypeDef:
        """
        [ListGroundStations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/groundstation.html#GroundStation.Paginator.ListGroundStations.paginate)
        """


class ListMissionProfilesPaginator(Boto3Paginator):
    """
    [Paginator.ListMissionProfiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/groundstation.html#GroundStation.Paginator.ListMissionProfiles)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListMissionProfilesResponseTypeDef:
        """
        [ListMissionProfiles.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/groundstation.html#GroundStation.Paginator.ListMissionProfiles.paginate)
        """


class ListSatellitesPaginator(Boto3Paginator):
    """
    [Paginator.ListSatellites documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/groundstation.html#GroundStation.Paginator.ListSatellites)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListSatellitesResponseTypeDef:
        """
        [ListSatellites.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/groundstation.html#GroundStation.Paginator.ListSatellites.paginate)
        """
