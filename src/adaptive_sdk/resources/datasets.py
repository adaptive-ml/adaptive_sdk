from pathlib import Path
from typing import List

from adaptive_sdk.base_client import BaseAsyncClient, BaseSyncClient
from adaptive_sdk.graphql_client import (
    DatasetCreate,
    Upload,
    LoadDatasetCreateDataset,
    ListDatasetsDatasets,
    DescribeDatasetDataset,
)

from .base_resource import SyncAPIResource, AsyncAPIResource


class Datasets(SyncAPIResource):
    """
    Resource to interact with file datasets.
    """

    def __init__(self, client: BaseSyncClient, use_case_key: str) -> None:
        super().__init__(client)
        self._use_case_key = use_case_key

    def upload(
        self,
        file_path: str,
        dataset_key: str,
        name: str | None = None,
    ) -> LoadDatasetCreateDataset:
        """
         Upload a dataset from a file. File must be jsonl, where each line should match structure in example below.

        Args:
            file_path: Path to jsonl file.
            dataset_key: New dataset key.
            name: Optional name to render in UI; if `None`, defaults to same as `dataset_key`.

        Example:
        ```
        {"messages": [{"role": "system", "content": "<optional system prompt>"}, {"role": "user", "content": "<user content>"}, {"role": "assistant", "content": "<assistant answer>"}], "completion": "hey"}
        ```
        """
        input = DatasetCreate(useCase=self._use_case_key, name=name if name else dataset_key, key=dataset_key)
        filename = Path(file_path).stem
        with open(file_path, "rb") as f:
            file_upload = Upload(filename=filename, content=f, content_type="application/jsonl")
            return self._gql_client.load_dataset(input=input, file=file_upload).create_dataset

    def list(
        self,
    ) -> List[ListDatasetsDatasets]:
        """
        List previously uploaded datasets.
        """
        return self._gql_client.list_datasets(self._use_case_key).datasets

    def get(self, key: str) -> DescribeDatasetDataset | None:
        """
        Get details for dataset.

        Args:
            key: Dataset key.
        """
        return self._gql_client.describe_dataset(key).dataset


class AsyncDatasets(AsyncAPIResource):
    def __init__(self, client: BaseAsyncClient, use_case_key: str) -> None:
        super().__init__(client)
        self._use_case_key = use_case_key

    async def upload(
        self,
        file_path: str,
        dataset_key: str,
        name: str | None = None,
    ) -> LoadDatasetCreateDataset:
        """
        Upload a dataset from a file. File must be jsonl, where each line should match structure in example below.

        Args:
            file_path: Path to jsonl file.
            dataset_key: New dataset key.
            name: Optional name to render in UI; if `None`, defaults to same as `dataset_key`.

        Example:
        ```
        {"messages": [{"role": "system", "content": "<optional system prompt>"}, {"role": "user", "content": "<user content>"}, {"role": "assistant", "content": "<assistant answer>"}], "completion": "hey"}
        ```
        """
        input = DatasetCreate(useCase=self._use_case_key, name=name if name else dataset_key, key=dataset_key)
        filename = Path(file_path).stem
        with open(file_path, "rb") as f:
            file_upload = Upload(filename=filename, content=f, content_type="application/jsonl")
            upload_result = await self._gql_client.load_dataset(input=input, file=file_upload)
            return upload_result.create_dataset

    async def list(
        self,
    ) -> List[ListDatasetsDatasets]:
        """
        List previously uploaded datasets.
        """
        results = await self._gql_client.list_datasets(self._use_case_key)
        return results.datasets

    async def get(self, key: str) -> DescribeDatasetDataset | None:
        """
        Get details for dataset.

        Args:
            key: Dataset key.
        """
        result = await self._gql_client.describe_dataset(key)
        return result.dataset
