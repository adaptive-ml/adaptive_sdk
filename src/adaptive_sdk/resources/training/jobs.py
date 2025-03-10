from __future__ import annotations
from typing import List, TYPE_CHECKING
import humps

from typing_extensions import override

from adaptive_sdk import input_types
from adaptive_sdk.graphql_client import (
    ListTrainingJobsTrainingJobs,
    DescribeTrainingJobTrainingJob,
    TrainingJobInput,
    AdaptRequestConfigInput,
    CreateTrainingJobCreateTrainingJob,
)

from .defaults import update_training_config_with_defaults
from ..base_resource import SyncAPIResource, AsyncAPIResource, UseCaseResource

if TYPE_CHECKING:
    from adaptive_sdk.client import Adaptive, AsyncAdaptive


class TrainingJobs(SyncAPIResource, UseCaseResource):  # type: ignore[misc]
    """
    Resource to interact with training jobs.
    """

    def __init__(self, client: Adaptive) -> None:
        SyncAPIResource.__init__(self, client)
        UseCaseResource.__init__(self, client)

    def create(
        self,
        model: str,
        config: input_types.AdaptRequestConfigInput,
        name: str | None = None,
        wait: bool = False,
        use_case: str | None = None,
    ) -> CreateTrainingJobCreateTrainingJob:
        """
        Create a new training job.

        Args:
            model: Model to train.
            config: Training config.
            name: Name for training job.
        """
        new_config = update_training_config_with_defaults(config)
        if (
            new_config.get("sample_config", {})
            .get("datasource", {})
            .get("completions", {})
            .get("filter")
            is not None
        ):
            new_config["sample_config"]["datasource"]["completions"][
                "filter"
            ].update(  # type:ignore
                {"useCase": self.use_case_key(use_case)}  # type:ignore
            )
        new_config = humps.camelize(new_config)
        config_input = AdaptRequestConfigInput.model_validate(new_config)
        input = TrainingJobInput(
            model=model,
            useCase=self.use_case_key(use_case),
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


class AsyncTrainingJobs(AsyncAPIResource, UseCaseResource):  # type: ignore[misc]
    """
    Resource to interact with training jobs.
    """

    def __init__(self, client: AsyncAdaptive) -> None:
        AsyncAPIResource.__init__(self, client)
        UseCaseResource.__init__(self, client)

    async def create(
        self,
        model: str,
        config: input_types.AdaptRequestConfigInput,
        name: str | None = None,
        wait: bool = False,
        use_case: str | None = None,
    ) -> CreateTrainingJobCreateTrainingJob:
        """
        Create a new training job.

        Args:
            model: Model to train.
            config: Training config.
            name: Name for training job.
        """
        new_config = update_training_config_with_defaults(config)
        if (
            new_config.get("sample_config", {})
            .get("datasource", {})
            .get("completions", {})
            .get("filter")
        ):
            new_config["sample_config"]["datasource"]["completions"][
                "filter"
            ].update(  # type:ignore
                {"useCase": self.use_case_key(use_case)}  # type:ignore
            )
        new_config = humps.camelize(new_config)
        config_input = AdaptRequestConfigInput.model_validate(new_config)
        input = TrainingJobInput(
            model=model,
            useCase=self.use_case_key(use_case),
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
