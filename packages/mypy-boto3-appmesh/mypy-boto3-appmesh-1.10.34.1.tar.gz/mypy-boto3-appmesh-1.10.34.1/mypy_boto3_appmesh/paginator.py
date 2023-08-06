"Main interface for appmesh service Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_appmesh.type_defs import (
    ListMeshesOutputTypeDef,
    ListRoutesOutputTypeDef,
    ListTagsForResourceOutputTypeDef,
    ListVirtualNodesOutputTypeDef,
    ListVirtualRoutersOutputTypeDef,
    ListVirtualServicesOutputTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = (
    "ListMeshesPaginator",
    "ListRoutesPaginator",
    "ListTagsForResourcePaginator",
    "ListVirtualNodesPaginator",
    "ListVirtualRoutersPaginator",
    "ListVirtualServicesPaginator",
)


class ListMeshesPaginator(Boto3Paginator):
    """
    [Paginator.ListMeshes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/appmesh.html#AppMesh.Paginator.ListMeshes)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(self, PaginationConfig: PaginatorConfigTypeDef = None) -> ListMeshesOutputTypeDef:
        """
        [ListMeshes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/appmesh.html#AppMesh.Paginator.ListMeshes.paginate)
        """


class ListRoutesPaginator(Boto3Paginator):
    """
    [Paginator.ListRoutes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/appmesh.html#AppMesh.Paginator.ListRoutes)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, meshName: str, virtualRouterName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListRoutesOutputTypeDef:
        """
        [ListRoutes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/appmesh.html#AppMesh.Paginator.ListRoutes.paginate)
        """


class ListTagsForResourcePaginator(Boto3Paginator):
    """
    [Paginator.ListTagsForResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/appmesh.html#AppMesh.Paginator.ListTagsForResource)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, resourceArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListTagsForResourceOutputTypeDef:
        """
        [ListTagsForResource.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/appmesh.html#AppMesh.Paginator.ListTagsForResource.paginate)
        """


class ListVirtualNodesPaginator(Boto3Paginator):
    """
    [Paginator.ListVirtualNodes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/appmesh.html#AppMesh.Paginator.ListVirtualNodes)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, meshName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListVirtualNodesOutputTypeDef:
        """
        [ListVirtualNodes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/appmesh.html#AppMesh.Paginator.ListVirtualNodes.paginate)
        """


class ListVirtualRoutersPaginator(Boto3Paginator):
    """
    [Paginator.ListVirtualRouters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/appmesh.html#AppMesh.Paginator.ListVirtualRouters)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, meshName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListVirtualRoutersOutputTypeDef:
        """
        [ListVirtualRouters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/appmesh.html#AppMesh.Paginator.ListVirtualRouters.paginate)
        """


class ListVirtualServicesPaginator(Boto3Paginator):
    """
    [Paginator.ListVirtualServices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/appmesh.html#AppMesh.Paginator.ListVirtualServices)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, meshName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListVirtualServicesOutputTypeDef:
        """
        [ListVirtualServices.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/appmesh.html#AppMesh.Paginator.ListVirtualServices.paginate)
        """
