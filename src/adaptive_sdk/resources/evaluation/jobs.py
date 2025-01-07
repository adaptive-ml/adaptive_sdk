from copy import deepcopy
from typing import List, Literal
from adaptive_sdk.base_client import BaseAsyncClient, BaseSyncClient
from adaptive_sdk.graphql_client import (
    ListEvaluationJobsEvaluationJobs,
    DescribeEvaluationJobEvaluationJob,
    EvaluationCreate,
    EvaluationKind,
    AijudgeEvaluation,
    EvaluationRecipeInput,
    EvaluationDatasource,
    CreateEvaluationJobCreateEvaluationJob,
)
from adaptive_sdk import input_types
from ..base_resource import SyncAPIResource, AsyncAPIResource


class EvalJobs(SyncAPIResource):
    """
    Resource to interact with evaluation jobs.
    """

    def __init__(self, client: BaseSyncClient, use_case_key: str) -> None:
        super().__init__(client)
        self._use_case_key = use_case_key

    def create(
        self,
        datasource: input_types.EvaluationDatasource,
        models: List[str],
        judge_model: str,
        method: Literal["faithfulness", "custom"],
        custom_eval_config: input_types.CustomRecipe | None = None,
        name: str | None = None,
    ) -> CreateEvaluationJobCreateEvaluationJob:
        """
        Create a new evaluation job.

        Args:
            datasource: Datasource configuration.
            models: Models to evaluate.
            judge_model: Model key of judge.
            method: Eval method (built in method, or custom eval).
            custom_eval_config: Only required if method=="custom".
            name: Optional name for evaluation job.
        """
        if datasource.get("completions"):
            datasource["completions"]["filter"] = (  # type: ignore
                {} if not datasource["completions"]["filter"] else deepcopy(datasource["completions"]["filter"])  # type: ignore
            )
            datasource["completions"]["filter"].update({"useCase": self._use_case_key})  # type: ignore

        ds_input = EvaluationDatasource.model_validate(datasource)
        if method == "custom":
            assert custom_eval_config, "Custom eval requires custom_eval_config"
            recipe_dict = {
                "custom": {
                    "guidelines": custom_eval_config["guidelines"],
                    "metric": {"existing": custom_eval_config["feedback_key"]},
                }
            }

        else:
            recipe_dict = {"faithfulness": "hey"}
        recipe_input = EvaluationRecipeInput.model_validate(recipe_dict)
        input = EvaluationCreate(
            useCase=self._use_case_key,
            kind=EvaluationKind(aijudge=AijudgeEvaluation(datasource=ds_input, judge=judge_model, recipe=recipe_input)),
            modelServices=models,
            name=name,
        )
        return self._gql_client.create_evaluation_job(input=input).create_evaluation_job

    def list(self) -> List[ListEvaluationJobsEvaluationJobs]:
        return self._gql_client.list_evaluation_jobs().evaluation_jobs

    def get(self, job_id: str) -> DescribeEvaluationJobEvaluationJob | None:
        return self._gql_client.describe_evaluation_job(id=job_id).evaluation_job


class EvalJobsAdmin(SyncAPIResource):
    def list(self) -> List[ListEvaluationJobsEvaluationJobs]:
        return self._gql_client.list_evaluation_jobs().evaluation_jobs

    def get(self, job_id: str) -> DescribeEvaluationJobEvaluationJob | None:
        return self._gql_client.describe_evaluation_job(id=job_id).evaluation_job


class AsyncEvalJobs(AsyncAPIResource):
    def __init__(self, client: BaseAsyncClient, use_case_key: str) -> None:
        super().__init__(client)
        self._use_case_key = use_case_key

    async def create(
        self,
        datasource: input_types.EvaluationDatasource,
        models: List[str],
        judge_model: str,
        method: Literal["faithfulness", "custom"],
        custom_eval_config: input_types.CustomRecipe | None = None,
        name: str | None = None,
    ) -> CreateEvaluationJobCreateEvaluationJob:
        """
        Create a new evaluation job.

        Args:
            datasource: Datasource configuration.
            models: Models to evaluate.
            judge_model: Model key of judge.
            method: Eval method (built in method, or custom eval).
            custom_eval_config: Configuration for custom eval. Only required if method=="custom".
            name: Optional name for evaluation job.
        """
        if datasource.get("completions"):
            datasource["completions"]["filter"] = (  # type: ignore
                {} if not datasource["completions"]["filter"] else deepcopy(datasource["completions"]["filter"])  # type: ignore
            )
            datasource["completions"]["filter"].update({"useCase": self._use_case_key})  # type: ignore

        ds_input = EvaluationDatasource.model_validate(datasource)
        if method == "custom":
            assert custom_eval_config, "Custom eval requires custom_eval_config"
            recipe_dict = {
                "custom": {
                    "guidelines": custom_eval_config["guidelines"],
                    "metric": {"existing": custom_eval_config["feedback_key"]},
                }
            }

        else:
            recipe_dict = {"faithfulness": "hey"}
        recipe_input = EvaluationRecipeInput.model_validate(recipe_dict)
        input = EvaluationCreate(
            useCase=self._use_case_key,
            kind=EvaluationKind(aijudge=AijudgeEvaluation(datasource=ds_input, judge=judge_model, recipe=recipe_input)),
            modelServices=models,
            name=name,
        )
        result = await self._gql_client.create_evaluation_job(input=input)
        return result.create_evaluation_job

    async def list(self) -> List[ListEvaluationJobsEvaluationJobs]:
        result = await self._gql_client.list_evaluation_jobs()
        return result.evaluation_jobs

    async def get(self, job_id: str) -> DescribeEvaluationJobEvaluationJob | None:
        result = await self._gql_client.describe_evaluation_job(id=job_id)
        return result.evaluation_job


class AsyncEvalJobsAdmin(AsyncAPIResource):
    async def list(self) -> List[ListEvaluationJobsEvaluationJobs]:
        result = await self._gql_client.list_evaluation_jobs()
        return result.evaluation_jobs

    async def get(self, job_id: str) -> DescribeEvaluationJobEvaluationJob | None:
        result = await self._gql_client.describe_evaluation_job(id=job_id)
        return result.evaluation_job
