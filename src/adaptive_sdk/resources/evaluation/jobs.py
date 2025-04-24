from __future__ import annotations
from copy import deepcopy
from typing import List, Literal, TYPE_CHECKING
from adaptive_sdk.graphql_client import (
    ListEvaluationJobsEvaluationJobs,
    DescribeEvaluationJobEvaluationJob,
    EvaluationCreate,
    EvaluationKind,
    AijudgeEvaluation,
    EvaluationRecipeInput,
    EvaluationJobData,
    SampleConfigInput,
)
from adaptive_sdk import input_types
from ..base_resource import SyncAPIResource, AsyncAPIResource, UseCaseResource
from typing_extensions import override

if TYPE_CHECKING:
    from adaptive_sdk.client import Adaptive, AsyncAdaptive


class EvalJobs(SyncAPIResource, UseCaseResource):  # type: ignore[misc]
    """
    Resource to interact with evaluation jobs.
    """

    @override
    def __init__(self, client: Adaptive) -> None:
        SyncAPIResource.__init__(self, client)
        UseCaseResource.__init__(self, client)
        self.client = client

    def create(
        self,
        data_config: input_types.SampleConfigInput,
        models: List[str],
        judge_model: str,
        method: Literal[
            "custom", "answer_relevancy", "context_relevancy", "faithfulness"
        ],
        custom_eval_config: input_types.CustomRecipe | None = None,
        name: str | None = None,
        use_case: str | None = None,
        compute_pool: str | None = None,
    ) -> EvaluationJobData:
        """
        Create a new evaluation job.

        Args:
            data_config: Input data configuration.
            models: Models to evaluate.
            judge_model: Model key of judge.
            method: Eval method (built in method, or custom eval).
            custom_eval_config: Only required if method=="custom".
            name: Optional name for evaluation job.
        """
        if data_config.get("datasource", {}).get("completions"):
            data_config["datasource"]["completions"]["filter"] = (  # type: ignore
                {} if not data_config["datasource"]["completions"].get("filter") else deepcopy(data_config["datasource"]["completions"]["filter"])  # type: ignore
            )
            data_config["datasource"]["completions"]["filter"].update({"useCase": self.use_case_key(use_case)})  # type: ignore

        ds_input = SampleConfigInput.model_validate(data_config)
        if method == "custom":
            assert custom_eval_config, "Custom eval requires custom_eval_config"
            metric_register_mode = (
                "existing"
                if self.client.feedback.get_key(custom_eval_config["feedback_key"])
                else "new"
            )
            recipe_dict = {
                "custom": {
                    "guidelines": custom_eval_config["guidelines"],
                    "metric": {
                        metric_register_mode: custom_eval_config["feedback_key"]
                    },
                }
            }

        else:
            recipe_dict = {method: {}}
        recipe_input = EvaluationRecipeInput.model_validate(recipe_dict)
        input = EvaluationCreate(
            useCase=self.use_case_key(use_case),
            kind=EvaluationKind(
                aijudge=AijudgeEvaluation(
                    sampleConfig=ds_input, judge=judge_model, recipe=recipe_input
                )
            ),
            modelServices=models,
            name=name,
            computePool=compute_pool,
        )
        return self._gql_client.create_evaluation_job(input=input).create_evaluation_job

    def cancel(self, job_id: str) -> str:
        return self._gql_client.cancel_evaluation_job(id=job_id).cancel_evaluation_job

    def list(self) -> List[ListEvaluationJobsEvaluationJobs]:
        return self._gql_client.list_evaluation_jobs().evaluation_jobs

    def get(self, job_id: str) -> DescribeEvaluationJobEvaluationJob | None:
        return self._gql_client.describe_evaluation_job(id=job_id).evaluation_job


class AsyncEvalJobs(AsyncAPIResource, UseCaseResource):  # type: ignore[misc]
    def __init__(self, client: AsyncAdaptive) -> None:
        AsyncAPIResource.__init__(self, client)
        UseCaseResource.__init__(self, client)
        self.client = client

    async def create(
        self,
        data_config: input_types.SampleConfigInput,
        models: List[str],
        judge_model: str,
        method: Literal[
            "custom", "answer_relevancy", "context_relevancy", "faithfulness"
        ],
        custom_eval_config: input_types.CustomRecipe | None = None,
        name: str | None = None,
        use_case: str | None = None,
        compute_pool: str | None = None,
    ) -> EvaluationJobData:
        """
        Create a new evaluation job.

        Args:
            data_config: Input data configuration.
            models: Models to evaluate.
            judge_model: Model key of judge.
            method: Eval method (built in method, or custom eval).
            custom_eval_config: Configuration for custom eval. Only required if method=="custom".
            name: Optional name for evaluation job.
        """
        if data_config.get("datasource", {}).get("completions"):
            data_config["datasource"]["completions"]["filter"] = (  # type: ignore
                {} if not data_config["datasource"]["completions"].get("filter") else deepcopy(data_config["datasource"]["completions"]["filter"])  # type: ignore
            )
            data_config["datasource"]["completions"]["filter"].update({"useCase": self.use_case_key(use_case)})  # type: ignore

        ds_input = SampleConfigInput.model_validate(data_config)
        if method == "custom":
            assert custom_eval_config, "Custom eval requires custom_eval_config"
            metric_register_mode = (
                "existing"
                if (
                    await self.client.feedback.get_key(
                        custom_eval_config["feedback_key"]
                    )
                )
                else "new"
            )
            recipe_dict = {
                "custom": {
                    "guidelines": custom_eval_config["guidelines"],
                    "metric": {
                        metric_register_mode: custom_eval_config["feedback_key"]
                    },
                }
            }

        else:
            recipe_dict = {method: {}}
        recipe_input = EvaluationRecipeInput.model_validate(recipe_dict)
        input = EvaluationCreate(
            useCase=self.use_case_key(use_case),
            kind=EvaluationKind(
                aijudge=AijudgeEvaluation(
                    sampleConfig=ds_input, judge=judge_model, recipe=recipe_input
                )
            ),
            modelServices=models,
            name=name,
            computePool=compute_pool,
        )
        result = await self._gql_client.create_evaluation_job(input=input)
        return result.create_evaluation_job

    async def cancel(self, job_id: str) -> str:
        return (
            await self._gql_client.cancel_evaluation_job(id=job_id)
        ).cancel_evaluation_job

    async def list(self) -> List[ListEvaluationJobsEvaluationJobs]:
        result = await self._gql_client.list_evaluation_jobs()
        return result.evaluation_jobs

    async def get(self, job_id: str) -> DescribeEvaluationJobEvaluationJob | None:
        result = await self._gql_client.describe_evaluation_job(id=job_id)
        return result.evaluation_job
