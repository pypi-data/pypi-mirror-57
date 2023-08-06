"Main interface for personalize service Paginators"
from __future__ import annotations

import sys
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_personalize.type_defs import (
    ListBatchInferenceJobsResponseTypeDef,
    ListCampaignsResponseTypeDef,
    ListDatasetGroupsResponseTypeDef,
    ListDatasetImportJobsResponseTypeDef,
    ListDatasetsResponseTypeDef,
    ListEventTrackersResponseTypeDef,
    ListRecipesResponseTypeDef,
    ListSchemasResponseTypeDef,
    ListSolutionVersionsResponseTypeDef,
    ListSolutionsResponseTypeDef,
    PaginatorConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ListBatchInferenceJobsPaginator",
    "ListCampaignsPaginator",
    "ListDatasetGroupsPaginator",
    "ListDatasetImportJobsPaginator",
    "ListDatasetsPaginator",
    "ListEventTrackersPaginator",
    "ListRecipesPaginator",
    "ListSchemasPaginator",
    "ListSolutionVersionsPaginator",
    "ListSolutionsPaginator",
)


class ListBatchInferenceJobsPaginator(Boto3Paginator):
    """
    [Paginator.ListBatchInferenceJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/personalize.html#Personalize.Paginator.ListBatchInferenceJobs)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, solutionVersionArn: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListBatchInferenceJobsResponseTypeDef:
        """
        [ListBatchInferenceJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/personalize.html#Personalize.Paginator.ListBatchInferenceJobs.paginate)
        """


class ListCampaignsPaginator(Boto3Paginator):
    """
    [Paginator.ListCampaigns documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/personalize.html#Personalize.Paginator.ListCampaigns)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, solutionArn: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListCampaignsResponseTypeDef:
        """
        [ListCampaigns.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/personalize.html#Personalize.Paginator.ListCampaigns.paginate)
        """


class ListDatasetGroupsPaginator(Boto3Paginator):
    """
    [Paginator.ListDatasetGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/personalize.html#Personalize.Paginator.ListDatasetGroups)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListDatasetGroupsResponseTypeDef:
        """
        [ListDatasetGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/personalize.html#Personalize.Paginator.ListDatasetGroups.paginate)
        """


class ListDatasetImportJobsPaginator(Boto3Paginator):
    """
    [Paginator.ListDatasetImportJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/personalize.html#Personalize.Paginator.ListDatasetImportJobs)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, datasetArn: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListDatasetImportJobsResponseTypeDef:
        """
        [ListDatasetImportJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/personalize.html#Personalize.Paginator.ListDatasetImportJobs.paginate)
        """


class ListDatasetsPaginator(Boto3Paginator):
    """
    [Paginator.ListDatasets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/personalize.html#Personalize.Paginator.ListDatasets)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, datasetGroupArn: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListDatasetsResponseTypeDef:
        """
        [ListDatasets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/personalize.html#Personalize.Paginator.ListDatasets.paginate)
        """


class ListEventTrackersPaginator(Boto3Paginator):
    """
    [Paginator.ListEventTrackers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/personalize.html#Personalize.Paginator.ListEventTrackers)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, datasetGroupArn: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListEventTrackersResponseTypeDef:
        """
        [ListEventTrackers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/personalize.html#Personalize.Paginator.ListEventTrackers.paginate)
        """


class ListRecipesPaginator(Boto3Paginator):
    """
    [Paginator.ListRecipes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/personalize.html#Personalize.Paginator.ListRecipes)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        recipeProvider: Literal["SERVICE"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> ListRecipesResponseTypeDef:
        """
        [ListRecipes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/personalize.html#Personalize.Paginator.ListRecipes.paginate)
        """


class ListSchemasPaginator(Boto3Paginator):
    """
    [Paginator.ListSchemas documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/personalize.html#Personalize.Paginator.ListSchemas)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListSchemasResponseTypeDef:
        """
        [ListSchemas.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/personalize.html#Personalize.Paginator.ListSchemas.paginate)
        """


class ListSolutionVersionsPaginator(Boto3Paginator):
    """
    [Paginator.ListSolutionVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/personalize.html#Personalize.Paginator.ListSolutionVersions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, solutionArn: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListSolutionVersionsResponseTypeDef:
        """
        [ListSolutionVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/personalize.html#Personalize.Paginator.ListSolutionVersions.paginate)
        """


class ListSolutionsPaginator(Boto3Paginator):
    """
    [Paginator.ListSolutions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/personalize.html#Personalize.Paginator.ListSolutions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, datasetGroupArn: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListSolutionsResponseTypeDef:
        """
        [ListSolutions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/personalize.html#Personalize.Paginator.ListSolutions.paginate)
        """
