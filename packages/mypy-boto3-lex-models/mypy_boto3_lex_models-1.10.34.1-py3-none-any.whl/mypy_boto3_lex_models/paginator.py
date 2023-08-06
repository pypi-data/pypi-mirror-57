"Main interface for lex-models service Paginators"
from __future__ import annotations

import sys
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_lex_models.type_defs import (
    GetBotAliasesResponseTypeDef,
    GetBotChannelAssociationsResponseTypeDef,
    GetBotVersionsResponseTypeDef,
    GetBotsResponseTypeDef,
    GetBuiltinIntentsResponseTypeDef,
    GetBuiltinSlotTypesResponseTypeDef,
    GetIntentVersionsResponseTypeDef,
    GetIntentsResponseTypeDef,
    GetSlotTypeVersionsResponseTypeDef,
    GetSlotTypesResponseTypeDef,
    PaginatorConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "GetBotAliasesPaginator",
    "GetBotChannelAssociationsPaginator",
    "GetBotVersionsPaginator",
    "GetBotsPaginator",
    "GetBuiltinIntentsPaginator",
    "GetBuiltinSlotTypesPaginator",
    "GetIntentVersionsPaginator",
    "GetIntentsPaginator",
    "GetSlotTypeVersionsPaginator",
    "GetSlotTypesPaginator",
)


class GetBotAliasesPaginator(Boto3Paginator):
    """
    [Paginator.GetBotAliases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBotAliases)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        botName: str,
        nameContains: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> GetBotAliasesResponseTypeDef:
        """
        [GetBotAliases.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBotAliases.paginate)
        """


class GetBotChannelAssociationsPaginator(Boto3Paginator):
    """
    [Paginator.GetBotChannelAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBotChannelAssociations)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        botName: str,
        botAlias: str,
        nameContains: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> GetBotChannelAssociationsResponseTypeDef:
        """
        [GetBotChannelAssociations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBotChannelAssociations.paginate)
        """


class GetBotVersionsPaginator(Boto3Paginator):
    """
    [Paginator.GetBotVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBotVersions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, name: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> GetBotVersionsResponseTypeDef:
        """
        [GetBotVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBotVersions.paginate)
        """


class GetBotsPaginator(Boto3Paginator):
    """
    [Paginator.GetBots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBots)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, nameContains: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> GetBotsResponseTypeDef:
        """
        [GetBots.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBots.paginate)
        """


class GetBuiltinIntentsPaginator(Boto3Paginator):
    """
    [Paginator.GetBuiltinIntents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBuiltinIntents)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        locale: Literal["en-US", "en-GB", "de-DE"] = None,
        signatureContains: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> GetBuiltinIntentsResponseTypeDef:
        """
        [GetBuiltinIntents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBuiltinIntents.paginate)
        """


class GetBuiltinSlotTypesPaginator(Boto3Paginator):
    """
    [Paginator.GetBuiltinSlotTypes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBuiltinSlotTypes)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        locale: Literal["en-US", "en-GB", "de-DE"] = None,
        signatureContains: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> GetBuiltinSlotTypesResponseTypeDef:
        """
        [GetBuiltinSlotTypes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBuiltinSlotTypes.paginate)
        """


class GetIntentVersionsPaginator(Boto3Paginator):
    """
    [Paginator.GetIntentVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetIntentVersions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, name: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> GetIntentVersionsResponseTypeDef:
        """
        [GetIntentVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetIntentVersions.paginate)
        """


class GetIntentsPaginator(Boto3Paginator):
    """
    [Paginator.GetIntents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetIntents)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, nameContains: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> GetIntentsResponseTypeDef:
        """
        [GetIntents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetIntents.paginate)
        """


class GetSlotTypeVersionsPaginator(Boto3Paginator):
    """
    [Paginator.GetSlotTypeVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetSlotTypeVersions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, name: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> GetSlotTypeVersionsResponseTypeDef:
        """
        [GetSlotTypeVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetSlotTypeVersions.paginate)
        """


class GetSlotTypesPaginator(Boto3Paginator):
    """
    [Paginator.GetSlotTypes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetSlotTypes)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, nameContains: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> GetSlotTypesResponseTypeDef:
        """
        [GetSlotTypes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetSlotTypes.paginate)
        """
