"Main interface for appstream service Paginators"
from __future__ import annotations

import sys
from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_appstream.type_defs import (
    DescribeDirectoryConfigsResultTypeDef,
    DescribeFleetsResultTypeDef,
    DescribeImageBuildersResultTypeDef,
    DescribeImagesResultTypeDef,
    DescribeSessionsResultTypeDef,
    DescribeStacksResultTypeDef,
    DescribeUserStackAssociationsResultTypeDef,
    DescribeUsersResultTypeDef,
    ListAssociatedFleetsResultTypeDef,
    ListAssociatedStacksResultTypeDef,
    PaginatorConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "DescribeDirectoryConfigsPaginator",
    "DescribeFleetsPaginator",
    "DescribeImageBuildersPaginator",
    "DescribeImagesPaginator",
    "DescribeSessionsPaginator",
    "DescribeStacksPaginator",
    "DescribeUserStackAssociationsPaginator",
    "DescribeUsersPaginator",
    "ListAssociatedFleetsPaginator",
    "ListAssociatedStacksPaginator",
)


class DescribeDirectoryConfigsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeDirectoryConfigs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/appstream.html#AppStream.Paginator.DescribeDirectoryConfigs)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, DirectoryNames: List[str] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> DescribeDirectoryConfigsResultTypeDef:
        """
        [DescribeDirectoryConfigs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/appstream.html#AppStream.Paginator.DescribeDirectoryConfigs.paginate)
        """


class DescribeFleetsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeFleets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/appstream.html#AppStream.Paginator.DescribeFleets)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, Names: List[str] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> DescribeFleetsResultTypeDef:
        """
        [DescribeFleets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/appstream.html#AppStream.Paginator.DescribeFleets.paginate)
        """


class DescribeImageBuildersPaginator(Boto3Paginator):
    """
    [Paginator.DescribeImageBuilders documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/appstream.html#AppStream.Paginator.DescribeImageBuilders)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, Names: List[str] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> DescribeImageBuildersResultTypeDef:
        """
        [DescribeImageBuilders.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/appstream.html#AppStream.Paginator.DescribeImageBuilders.paginate)
        """


class DescribeImagesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeImages documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/appstream.html#AppStream.Paginator.DescribeImages)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Names: List[str] = None,
        Arns: List[str] = None,
        Type: Literal["PUBLIC", "PRIVATE", "SHARED"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> DescribeImagesResultTypeDef:
        """
        [DescribeImages.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/appstream.html#AppStream.Paginator.DescribeImages.paginate)
        """


class DescribeSessionsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeSessions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/appstream.html#AppStream.Paginator.DescribeSessions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        StackName: str,
        FleetName: str,
        UserId: str = None,
        AuthenticationType: Literal["API", "SAML", "USERPOOL"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> DescribeSessionsResultTypeDef:
        """
        [DescribeSessions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/appstream.html#AppStream.Paginator.DescribeSessions.paginate)
        """


class DescribeStacksPaginator(Boto3Paginator):
    """
    [Paginator.DescribeStacks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/appstream.html#AppStream.Paginator.DescribeStacks)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, Names: List[str] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> DescribeStacksResultTypeDef:
        """
        [DescribeStacks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/appstream.html#AppStream.Paginator.DescribeStacks.paginate)
        """


class DescribeUserStackAssociationsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeUserStackAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/appstream.html#AppStream.Paginator.DescribeUserStackAssociations)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        StackName: str = None,
        UserName: str = None,
        AuthenticationType: Literal["API", "SAML", "USERPOOL"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> DescribeUserStackAssociationsResultTypeDef:
        """
        [DescribeUserStackAssociations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/appstream.html#AppStream.Paginator.DescribeUserStackAssociations.paginate)
        """


class DescribeUsersPaginator(Boto3Paginator):
    """
    [Paginator.DescribeUsers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/appstream.html#AppStream.Paginator.DescribeUsers)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        AuthenticationType: Literal["API", "SAML", "USERPOOL"],
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> DescribeUsersResultTypeDef:
        """
        [DescribeUsers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/appstream.html#AppStream.Paginator.DescribeUsers.paginate)
        """


class ListAssociatedFleetsPaginator(Boto3Paginator):
    """
    [Paginator.ListAssociatedFleets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/appstream.html#AppStream.Paginator.ListAssociatedFleets)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, StackName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListAssociatedFleetsResultTypeDef:
        """
        [ListAssociatedFleets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/appstream.html#AppStream.Paginator.ListAssociatedFleets.paginate)
        """


class ListAssociatedStacksPaginator(Boto3Paginator):
    """
    [Paginator.ListAssociatedStacks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/appstream.html#AppStream.Paginator.ListAssociatedStacks)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, FleetName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListAssociatedStacksResultTypeDef:
        """
        [ListAssociatedStacks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/appstream.html#AppStream.Paginator.ListAssociatedStacks.paginate)
        """
