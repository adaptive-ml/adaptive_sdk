import asyncio
import time
import os
import pprint
from typing import Sequence

from adaptive_sdk import AsyncAdaptive
from adaptive_sdk import rest as rest_types
from adaptive_sdk.graphql_client import ModelData

from .utils import log_function_name
import logging


class AsyncTests:
    def __init__(
        self,
        client: AsyncAdaptive,
        async_prefix: str,
        use_case: str,
        other_team_use_case: str,
        feedback_key: str,
        model: str,
        user_email: str,
        team: str,
        other_team: str,
        role: str,
        open_ai_key: str,
        google_key: str,
        azure_key: str,
        azure_endpoint: str,
        azure_deployment_name: str,
        open_ai_model_name: str,
        google_model_name: str,
        azure_model_name: str,
        ab_test: str,
    ) -> None:

        self.client = client
        self.use_case = use_case
        self.client.set_default_use_case(self.use_case)
        self.async_prefix = async_prefix
        self.other_team_use_case = other_team_use_case
        self.feedback_key = feedback_key
        self.model = model
        self.user_email = user_email
        self.team = team
        self.other_team = other_team
        self.role = role
        self.open_ai_key = open_ai_key
        self.google_key = google_key
        self.azure_key = azure_key
        self.azure_endpoint = azure_endpoint
        self.azure_deployment_name = azure_deployment_name
        self.open_ai_model_name = open_ai_model_name
        self.google_model_name = google_model_name
        self.azure_model_name = azure_model_name
        self.ab_test = ab_test

    @log_function_name
    def check_inputs(self):
        assert self.open_ai_key
        assert self.google_key
        assert self.azure_key
        assert self.azure_endpoint

    @log_function_name
    async def test_teams(self):
        _ = await self.client.teams.create(key=self.other_team, name=self.other_team)
        teams_list = await self.client.teams.list()
        assert any([team.key == self.other_team for team in teams_list])

    @log_function_name
    async def test_roles(self):
        _ = await self.client.permissions.list()
        _ = await self.client.roles.create(key=self.role, name=self.role, permissions=["use_case:read"])
        roles_list = await self.client.roles.list()
        assert any([role.key == self.role for role in roles_list])

    @log_function_name
    async def test_users(self):
        assert await self.client.users.me()
        _ = await self.client.users.list()
        # TODO: when we allow platform_admins to add themselves to any team
        # update_user = self.client.users.update(email=self.user_email, team=self.team, role="admin")

    @log_function_name
    async def test_use_cases(self):
        use_case_create = await self.client.use_cases.create(
            key=self.use_case,
            name=self.use_case,
            description="A use case for sync tests",
            team=self.team,
        )

        assert await self.client.use_cases.get(use_case_create.key)
        assert await self.client.use_cases.get(use_case_create.id)

        _ = await self.client.use_cases.list()

    @log_function_name
    async def test_feedback_admin(self):
        feedback_key_register = await self.client.feedback.register_key(
            key=self.feedback_key,
            name=self.feedback_key,
            kind="scalar",
            scoring_type="higher_is_better",
            description="A scaler feedback for sync tests",
        )
        assert await self.client.feedback.get_key(feedback_key_register.key)
        assert await self.client.feedback.get_key(feedback_key_register.id)

        _ = await self.client.feedback.list_keys()
        _ = await self.client.feedback.link(feedback_key=self.feedback_key)
        _ = await self.client.feedback.unlink(feedback_key=self.feedback_key)
        _ = await self.client.feedback.link(feedback_key=self.feedback_key)

    @log_function_name
    async def test_models_admin(self):
        models_list = await self.client.models.list()
        assert await self.client.models.get(models_list[0].key)
        assert await self.client.models.get(models_list[0].id)

        open_ai_model = await self.client.models.add_external(
            provider="open_ai",
            external_model_id="GPT4O_MINI",
            name=self.open_ai_model_name,
            api_key=self.open_ai_key,
        )

        azure_model = await self.client.models.add_external(
            provider="azure",
            external_model_id=self.azure_deployment_name,
            name=self.azure_model_name,
            api_key=self.azure_key,
            endpoint=self.azure_endpoint,
        )

        google_model = await self.client.models.add_external(
            provider="google",
            external_model_id="gemini-1.5-flash-8b",
            name=self.google_model_name,
            api_key=self.google_key,
        )

        for model in [open_ai_model, azure_model, google_model]:
            _ = await self.client.models.attach(model=model.id)

        _ = await self.client.models.attach(model=self.model, wait=True, make_default=True)
        # _ = await self.client.models.terminate(model=self.model, force=True)
        # _ = await self.client.models.detach(model=self.model)
        # _ = await self.client.models.deploy(model=self.model, wait=True)
        # _ = await self.client.models.attach(model=self.model, wait=True, make_default=True)

        # _ = await self.client.models.update(model=self.model, is_default=False, desired_online=False)
        # _ = await self.client.models.update(model=self.model, is_default=True, desired_online=True)

        while True:
            if (await self.client.models.get(self.model)).online.value == "ONLINE":  # type: ignore
                break
            logging.warning(f"waiting for model '{self.model}' to be online")
            time.sleep(3)

        return (open_ai_model, azure_model, google_model)

    @log_function_name
    async def test_inference(self, ext_models: Sequence[ModelData]) -> rest_types.ChatResponse:
        for ext in ext_models:
            _ = await self.client.chat.create(
                model=ext.key,
                messages=[{"role": "user", "content": "Hey there."}],
                max_tokens=200,
                temperature=0,
                labels={"test": "ext"},
            )

        completions = await self.client.chat.create(
            model=self.model,
            messages=[{"role": "user", "content": "Hey there."}],
            max_tokens=200,
            temperature=0,
            n=2,
            labels={"test": "local"},
        )
        assert len(completions.choices) == 2
        return completions

    @log_function_name
    async def test_feedback_logging(self, completions: rest_types.ChatResponse):
        _ = await self.client.feedback.log_metric(
            completion_id=completions.choices[0].completion_id,
            value=1,
            feedback_key=self.feedback_key,
            details="Text feedback",
        )

        _ = await self.client.feedback.log_preference(
            feedback_key=self.feedback_key,
            preferred_completion=completions.choices[0].completion_id,
            other_completion=completions.choices[1].completion_id,
        )

    @log_function_name
    async def test_interactions(self, completions: rest_types.ChatResponse):
        metric_logged_completion = await self.client.interactions.get(completions.choices[0].completion_id)
        assert metric_logged_completion
        assert len(metric_logged_completion.direct_feedbacks) == 1
        assert len(metric_logged_completion.comparison_feedbacks) == 1

        _ = await self.client.interactions.create(
            completion="completion", messages=[{"role": "user", "content": "prompt"}]
        )
        _ = await self.client.interactions.create(
            model=self.model,
            completion="completion",
            messages=[{"role": "user", "content": "prompt"}],
        )

        ungrouped_interactions = await self.client.interactions.list(
            filters={"labels": [{"key": "test", "value": ["local"]}]}
        )
        assert ungrouped_interactions.total_count == 2
        grouped_interactions = await self.client.interactions.list(
            filters={"labels": [{"key": "test", "value": ["local"]}]}, group_by="prompt"
        )
        assert grouped_interactions.total_count == 1

    async def test_ab_tests(self, ext_models: Sequence[ModelData]):
        ab_test = await self.client.ab_tests.create(
            ab_test_key=self.ab_test,
            feedback_key=self.feedback_key,
            models=[self.model, ext_models[0].key],
        )
        assert await self.client.ab_tests.get(ab_test.key)
        assert await self.client.ab_tests.get(ab_test.id)
        assert len(await self.client.ab_tests.list(active=True)) == 1

        _ = await self.client.ab_tests.cancel(ab_test.key)

    @log_function_name
    async def test_datasets(self):
        integration_data_dir = "tests/integration_data"
        dataset_files = os.listdir(integration_data_dir)

        for filename in dataset_files:
            # TODO: fix duplicate key bug for same key datasets in different use cases
            new_ds = await self.client.datasets.upload(
                file_path=f"{integration_data_dir}/{filename}",
                dataset_key=self.async_prefix + filename.replace(".jsonl", ""),
            )
            assert await self.client.datasets.get(new_ds.key)
            assert await self.client.datasets.get(new_ds.id)

        assert len(await self.client.datasets.list()) == len(dataset_files)

    @log_function_name
    async def test_evals(self, ext_models: Sequence[ModelData]):
        context_relevancy_job = await self.client.evaluation.jobs.create(
            models=[self.model],
            judge_model=ext_models[0].key,
            method="context_relevancy",
            data_source="DATASET",
            data_config={"dataset": self.async_prefix + "relevancy"},
        )
        answer_relevancy_job = await self.client.evaluation.jobs.create(
            models=[self.model],
            judge_model=ext_models[0].key,
            method="answer_relevancy",
            data_source="DATASET",
            data_config={"dataset": self.async_prefix + "relevancy"},
        )

        while True:
            cr_job_status = (await self.client.evaluation.jobs.get(context_relevancy_job.id)).status  # type: ignore
            ar_job_status = (await self.client.evaluation.jobs.get(answer_relevancy_job.id)).status  # type: ignore
            if cr_job_status == "COMPLETED" and ar_job_status == "COMPLETED":
                break
            elif cr_job_status == "FAILED" or ar_job_status == "FAILED":
                cr_job_str = pprint.pformat(context_relevancy_job.model_dump())
                ar_job_str = pprint.pformat(answer_relevancy_job.model_dump())
                raise RuntimeError(f"One of the evaluation jobs failed:\n\n{cr_job_str}\n\n{ar_job_str}")

    @log_function_name
    async def test_judges(self, ext_models: Sequence[ModelData]):
        judge_key = f"e2e-judge-{int(time.time()*1000)}"
        # prebuilt_key = f"{judge_key}-prebuilt"

        # Create a custom judge
        created = await self.client.judges.create(
            key=judge_key,
            name=judge_key,
            criteria="The answer must be helpful and relevant.",
            judge_model=ext_models[0].key,
            examples=[
                {
                    "input": [{"role": "user", "content": "Hello"}],
                    "output": "Hi",
                    "passes": True,
                    "reasoning": "Basic greeting passes.",
                }
            ],
            feedback_key=self.feedback_key,
        )
        assert created.key == judge_key

        # Read operations
        assert await self.client.judges.get(key=judge_key)
        assert any(j.key == judge_key for j in await self.client.judges.list())

        # Update to create a new version
        updated = await self.client.judges.update(key=judge_key, criteria="Updated criteria for the judge.")
        assert updated.criteria
        assert updated.criteria.startswith("Updated")
        assert len(await self.client.judges.list_versions(key=judge_key)) >= 2

        # Pre-built judge
        # prebuilt = await self.client.judges.create_prebuilt(
        #     key=prebuilt_key,
        #     name=prebuilt_key,
        #     judge_model=ext_models[0].key,
        #     prebuilt_criteria="ANSWER_RELEVANCY",
        # )
        # assert prebuilt.key == prebuilt_key

        # Clean-up
        assert await self.client.judges.delete(key=judge_key)
        # assert awaitself.client.judges.delete(key=prebuilt_key)

    async def run_all_tests(self):
        self.check_inputs()
        await self.test_teams()
        await self.test_roles()
        await self.test_users()
        await self.test_use_cases()
        await self.test_feedback_admin()
        ext_models = await self.test_models_admin()
        completions = await self.test_inference(ext_models)
        await self.test_feedback_logging(completions)
        await self.test_interactions(completions)
        await self.test_ab_tests(ext_models)
        await self.test_datasets()
        await self.test_evals(ext_models)
        await self.test_judges(ext_models)
        # TODO:
        #   * test_evals_from_interactions, using generations from the previous step
        #   * test training, both with judge feedback provided above, and RLAIF
        # self.test_evals_from_interactions(ext_models)


def test_async():
    base_url = os.getenv("TESTING_ADAPTIVE_BASE_URL")
    api_key = os.getenv("TESTING_ADAPTIVE_API_KEY")
    open_ai_key = os.getenv("TESTING_OPENAI_API_KEY")
    google_key = os.getenv("TESTING_GOOGLE_API_KEY")
    azure_key = os.getenv("TESTING_AZURE_API_KEY")
    azure_endpoint = os.getenv("TESTING_AZURE_ENDPOINT")
    cf_access_client_id = os.getenv("CF_ACCESS_CLIENT_ID")
    cf_access_client_secret = os.getenv("CF_ACCESS_CLIENT_SECRET")

    # individual asserts so we can pinpoint exactly what's missing in test logs
    assert base_url
    assert api_key

    suffix = os.getenv("GITHUB_RUN_ID", "")
    use_case = f"e2e-usecase{suffix}"
    other_team_use_case = f"e2e-other-team-usecase{suffix}"
    team = "default"
    other_team = "test-team"
    feedback_key = "feedback-key"
    model = "qwen_25_500M"
    user_email = "user"
    role = "test-role"
    azure_deployment_name = "gpt-4o-mini"
    open_ai_model_name = "adaptive-gpt"
    google_model_name = "adaptive-gemini"
    azure_model_name = "adaptive-azure-gpt"
    ab_test = "ab-test"

    assert api_key
    assert base_url

    assert open_ai_key
    assert google_key
    assert azure_key
    assert azure_endpoint
    async_client = AsyncAdaptive(
        base_url=base_url,
        api_key=api_key,
        default_headers=(
            {
                "CF-Access-Client-Id": cf_access_client_id,
                "CF-Access-Client-Secret": cf_access_client_secret,
            }
            if cf_access_client_id and cf_access_client_secret
            else None
        ),
    )

    async_prefix = "async-"
    asyncio.run(
        AsyncTests(
            client=async_client,
            use_case=async_prefix + use_case,
            async_prefix=async_prefix,
            other_team_use_case=async_prefix + other_team_use_case,
            feedback_key=async_prefix + feedback_key,
            model=model,
            user_email=user_email,
            team=team,
            other_team=async_prefix + other_team,
            role=async_prefix + role,
            open_ai_key=open_ai_key,
            google_key=google_key,
            azure_key=azure_key,
            azure_endpoint=azure_endpoint,
            azure_deployment_name=azure_deployment_name,
            open_ai_model_name=async_prefix + open_ai_model_name,
            google_model_name=async_prefix + google_model_name,
            azure_model_name=async_prefix + azure_model_name,
            ab_test=async_prefix + ab_test,
        ).run_all_tests()
    )
