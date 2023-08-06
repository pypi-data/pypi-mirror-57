"Main interface for lambda service Paginators"
from __future__ import annotations

import sys
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_lambda.type_defs import (
    ListAliasesResponseTypeDef,
    ListEventSourceMappingsResponseTypeDef,
    ListFunctionEventInvokeConfigsResponseTypeDef,
    ListFunctionsResponseTypeDef,
    ListLayerVersionsResponseTypeDef,
    ListLayersResponseTypeDef,
    ListProvisionedConcurrencyConfigsResponseTypeDef,
    ListVersionsByFunctionResponseTypeDef,
    PaginatorConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ListAliasesPaginator",
    "ListEventSourceMappingsPaginator",
    "ListFunctionEventInvokeConfigsPaginator",
    "ListFunctionsPaginator",
    "ListLayerVersionsPaginator",
    "ListLayersPaginator",
    "ListProvisionedConcurrencyConfigsPaginator",
    "ListVersionsByFunctionPaginator",
)


class ListAliasesPaginator(Boto3Paginator):
    """
    [Paginator.ListAliases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lambda.html#Lambda.Paginator.ListAliases)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        FunctionName: str,
        FunctionVersion: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> ListAliasesResponseTypeDef:
        """
        [ListAliases.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lambda.html#Lambda.Paginator.ListAliases.paginate)
        """


class ListEventSourceMappingsPaginator(Boto3Paginator):
    """
    [Paginator.ListEventSourceMappings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lambda.html#Lambda.Paginator.ListEventSourceMappings)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        EventSourceArn: str = None,
        FunctionName: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> ListEventSourceMappingsResponseTypeDef:
        """
        [ListEventSourceMappings.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lambda.html#Lambda.Paginator.ListEventSourceMappings.paginate)
        """


class ListFunctionEventInvokeConfigsPaginator(Boto3Paginator):
    """
    [Paginator.ListFunctionEventInvokeConfigs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lambda.html#Lambda.Paginator.ListFunctionEventInvokeConfigs)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, FunctionName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListFunctionEventInvokeConfigsResponseTypeDef:
        """
        [ListFunctionEventInvokeConfigs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lambda.html#Lambda.Paginator.ListFunctionEventInvokeConfigs.paginate)
        """


class ListFunctionsPaginator(Boto3Paginator):
    """
    [Paginator.ListFunctions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lambda.html#Lambda.Paginator.ListFunctions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        MasterRegion: str = None,
        FunctionVersion: Literal["ALL"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> ListFunctionsResponseTypeDef:
        """
        [ListFunctions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lambda.html#Lambda.Paginator.ListFunctions.paginate)
        """


class ListLayerVersionsPaginator(Boto3Paginator):
    """
    [Paginator.ListLayerVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lambda.html#Lambda.Paginator.ListLayerVersions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        LayerName: str,
        CompatibleRuntime: Literal[
            "nodejs",
            "nodejs4.3",
            "nodejs6.10",
            "nodejs8.10",
            "nodejs10.x",
            "nodejs12.x",
            "java8",
            "java11",
            "python2.7",
            "python3.6",
            "python3.7",
            "python3.8",
            "dotnetcore1.0",
            "dotnetcore2.0",
            "dotnetcore2.1",
            "nodejs4.3-edge",
            "go1.x",
            "ruby2.5",
            "provided",
        ] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> ListLayerVersionsResponseTypeDef:
        """
        [ListLayerVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lambda.html#Lambda.Paginator.ListLayerVersions.paginate)
        """


class ListLayersPaginator(Boto3Paginator):
    """
    [Paginator.ListLayers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lambda.html#Lambda.Paginator.ListLayers)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        CompatibleRuntime: Literal[
            "nodejs",
            "nodejs4.3",
            "nodejs6.10",
            "nodejs8.10",
            "nodejs10.x",
            "nodejs12.x",
            "java8",
            "java11",
            "python2.7",
            "python3.6",
            "python3.7",
            "python3.8",
            "dotnetcore1.0",
            "dotnetcore2.0",
            "dotnetcore2.1",
            "nodejs4.3-edge",
            "go1.x",
            "ruby2.5",
            "provided",
        ] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> ListLayersResponseTypeDef:
        """
        [ListLayers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lambda.html#Lambda.Paginator.ListLayers.paginate)
        """


class ListProvisionedConcurrencyConfigsPaginator(Boto3Paginator):
    """
    [Paginator.ListProvisionedConcurrencyConfigs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lambda.html#Lambda.Paginator.ListProvisionedConcurrencyConfigs)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, FunctionName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListProvisionedConcurrencyConfigsResponseTypeDef:
        """
        [ListProvisionedConcurrencyConfigs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lambda.html#Lambda.Paginator.ListProvisionedConcurrencyConfigs.paginate)
        """


class ListVersionsByFunctionPaginator(Boto3Paginator):
    """
    [Paginator.ListVersionsByFunction documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lambda.html#Lambda.Paginator.ListVersionsByFunction)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, FunctionName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListVersionsByFunctionResponseTypeDef:
        """
        [ListVersionsByFunction.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lambda.html#Lambda.Paginator.ListVersionsByFunction.paginate)
        """
