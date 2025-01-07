from typing import List
import humps

from adaptive_sdk import input_types
from adaptive_sdk.base_client import BaseAsyncClient, BaseSyncClient
from adaptive_sdk.graphql_client import (
    ListTrainingJobsTrainingJobs,
    DescribeTrainingJobTrainingJob,
    TrainingJobInput,
    AdaptRequestConfigInput,
    CreateTrainingJobCreateTrainingJob,
)

from .defaults import update_training_config_with_defaults
from ..base_resource import SyncAPIResource, AsyncAPIResource


class TrainingJobsAdmin(SyncAPIResource):
    """
    Resource to administrate training jobs.
    """

    def cancel(self, job_id: str) -> str:
        """
        Cancel ongoing training job.
        """
        return self._gql_client.cancel_training_job(job_id).cancel_training_job

    def list(self) -> List[ListTrainingJobsTrainingJobs]:
        """
        List all training jobs.
        """
        return self._gql_client.list_training_jobs().training_jobs

    def get(self, job_id: str) -> DescribeTrainingJobTrainingJob | None:
        """
        Get details for training job.
        """
        return self._gql_client.describe_training_job(id=job_id).training_job


class TrainingJobs(SyncAPIResource):
    """
    Resource to interact with training jobs.
    """

    def __init__(self, client: BaseSyncClient, use_case_key: str) -> None:
        super().__init__(client)
        self._use_case_key = use_case_key

    def create(
        self,
        model: str,
        config: input_types.AdaptRequestConfigInput,
        name: str | None = None,
        wait: bool = False,
    ) -> CreateTrainingJobCreateTrainingJob:
        """
        Create a new training job.

        Args:
            model: Model to train.
            config: Training config.
            name: Name for training job.
        """
        new_config = update_training_config_with_defaults(config)
        if new_config.get("sample_config").get("filter"):  # type:ignore
            new_config["sample_config"]["filter"].update({"useCase": self._use_case_key})  # type:ignore
        new_config = humps.camelize(new_config)
        config_input = AdaptRequestConfigInput.model_validate(new_config)
        input = TrainingJobInput(
            model=model,
            useCase=self._use_case_key,
            name=name,
            config=config_input,
            wait=wait,
        )
        return self._gql_client.create_training_job(input).create_training_job

    def cancel(self, job_id: str) -> str:
        """
        Cancel ongoing training job.
        """
        return self._gql_client.cancel_training_job(job_id).cancel_training_job

    def list(self) -> List[ListTrainingJobsTrainingJobs]:
        """
        List all training jobs.
        """
        return self._gql_client.list_training_jobs().training_jobs

    def get(self, job_id: str) -> DescribeTrainingJobTrainingJob | None:
        """
        Get details for training job.
        """
        return self._gql_client.describe_training_job(id=job_id).training_job


class AsyncTrainingJobsAdmin(AsyncAPIResource):
    """
    Resource to administrate training jobs.
    """

    async def cancel(self, job_id: str) -> str:
        """
        Cancel ongoing training job.
        """
        return (await self._gql_client.cancel_training_job(job_id)).cancel_training_job

    async def list(self) -> List[ListTrainingJobsTrainingJobs]:
        """
        List all training jobs.
        """
        return (await self._gql_client.list_training_jobs()).training_jobs

    async def get(self, job_id: str) -> DescribeTrainingJobTrainingJob | None:
        """
        Get details for training job.
        """
        return (await self._gql_client.describe_training_job(id=job_id)).training_job


class AsyncTrainingJobs(AsyncAPIResource):
    """
    Resource to interact with training jobs.
    """

    def __init__(self, client: BaseAsyncClient, use_case_key: str) -> None:
        super().__init__(client)
        self._use_case_key = use_case_key

    async def create(
        self,
        model: str,
        config: input_types.AdaptRequestConfigInput,
        name: str | None = None,
        wait: bool = False,
    ) -> CreateTrainingJobCreateTrainingJob:
        """
        Create a new training job.

        Args:
            model: Model to train.
            config: Training config.
            name: Name for training job.
        """
        new_config = update_training_config_with_defaults(config)
        if new_config.get("sample_config").get("filter"):  # type:ignore
            new_config["sample_config"]["filter"].update({"useCase": self._use_case_key})  # type:ignore
        new_config = humps.camelize(new_config)
        config_input = AdaptRequestConfigInput.model_validate(new_config)
        input = TrainingJobInput(
            model=model,
            useCase=self._use_case_key,
            name=name,
            config=config_input,
            wait=wait,
        )
        result = await self._gql_client.create_training_job(input)
        return result.create_training_job

    async def cancel(self, job_id: str) -> str:
        """
        Cancel ongoing training job.
        """
        result = await self._gql_client.cancel_training_job(job_id)
        return result.cancel_training_job

    async def list(self) -> List[ListTrainingJobsTrainingJobs]:
        """
        List all training jobs.
        """
        result = await self._gql_client.list_training_jobs()
        return result.training_jobs

    async def get(self, job_id: str) -> DescribeTrainingJobTrainingJob | None:
        """
        Get details for training job.
        """
        result = await self._gql_client.describe_training_job(id=job_id)
        return result.training_job
