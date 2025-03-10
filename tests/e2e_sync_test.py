import functools
import time
import os
from typing import Sequence

from adaptive_sdk import Adaptive
from adaptive_sdk import rest as rest_types
from adaptive_sdk.graphql_client import ModelData

from .utils import log_function_name
import logging


class RunnerFixture:
    def __init__(
        self,
        client: Adaptive,
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
    def test_teams(self):
        _ = self.client.teams.create(key=self.other_team, name=self.other_team)
        teams_list = self.client.teams.list()
        assert any([team.key == self.other_team for team in teams_list])

    @log_function_name
    def test_roles(self):
        _ = self.client.permissions.list()
        _ = self.client.roles.create(key=self.role, name=self.role, permissions=["use_case:read"])
        roles_list = self.client.roles.list()
        assert any([role.key == self.role for role in roles_list])

    @log_function_name
    def test_users(self):
        assert self.client.users.me()
        _ = self.client.users.list()
        # TODO: when we allow platform_admins to add themselves to any team
        # update_user = self.client.users.update(email=self.user_email, team=self.team, role="admin")

    @log_function_name
    def test_use_cases(self):
        use_case_create = self.client.use_cases.create(
            key=self.use_case, name=self.use_case, description="A use case for sync tests", team=self.team
        )

        assert self.client.use_cases.get(use_case_create.key)
        assert self.client.use_cases.get(use_case_create.id)

        _ = self.client.use_cases.list()

    @log_function_name
    def test_feedback_admin(self):
        feedback_key_register = self.client.feedback.register_key(
            key=self.feedback_key,
            name=self.feedback_key,
            kind="scalar",
            scoring_type="higher_is_better",
            description="A scaler feedback for sync tests",
        )
        assert self.client.feedback.get_key(feedback_key_register.key)
        assert self.client.feedback.get_key(feedback_key_register.id)

        _ = self.client.feedback.list_keys()
        _ = self.client.feedback.link(feedback_key=self.feedback_key)
        _ = self.client.feedback.unlink(feedback_key=self.feedback_key)
        _ = self.client.feedback.link(feedback_key=self.feedback_key)

    @log_function_name
    def test_models_admin(self):
        models_list = self.client.models.list()
        assert self.client.models.get(models_list[0].key)
        assert self.client.models.get(models_list[0].id)

        open_ai_model = self.client.models.add_external(
            provider="open_ai", external_model_id="GPT4O_MINI", name=self.open_ai_model_name, api_key=self.open_ai_key
        )

        azure_model = self.client.models.add_external(
            provider="azure",
            external_model_id=self.azure_deployment_name,
            name=self.azure_model_name,
            api_key=self.azure_key,
            endpoint=self.azure_endpoint,
        )

        google_model = self.client.models.add_external(
            provider="google",
            external_model_id="gemini-1.5-flash-8b",
            name=self.google_model_name,
            api_key=self.google_key,
        )

        for model in [open_ai_model, azure_model, google_model]:
            _ = self.client.models.attach(model=model.id)

        _ = self.client.models.attach(model=self.model, wait=True, make_default=True)
        _ = self.client.models.terminate(model=self.model, force=True)
        _ = self.client.models.detach(model=self.model)
        _ = self.client.models.deploy(model=self.model, wait=True)
        _ = self.client.models.attach(model=self.model, wait=True, make_default=True)

        _ = self.client.models.update(model=self.model, is_default=False, desired_online=False)
        _ = self.client.models.update(model=self.model, is_default=True, desired_online=True)

        while True:
            if self.client.models.get(self.model).online.value == "ONLINE":  # type: ignore
                break
            logging.warning(f"waiting for model '{self.model}' to be online")
            time.sleep(3)

        return (open_ai_model, azure_model, google_model)

    @log_function_name
    def test_inference(self, ext_models: Sequence[ModelData]) -> rest_types.ChatResponse:
        for ext in ext_models:
            _ = self.client.chat.create(
                model=ext.key,
                messages=[{"role": "user", "content": "Hey there."}],
                max_tokens=200,
                temperature=0,
                labels={"test": "ext"},
            )

        completions = self.client.chat.create(
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
    def test_feedback_logging(self, completions: rest_types.ChatResponse):
        _ = self.client.feedback.log_metric(
            completion_id=completions.choices[0].completion_id,
            value=1,
            feedback_key=self.feedback_key,
            details="Text feedback",
        )

        _ = self.client.feedback.log_preference(
            feedback_key=self.feedback_key,
            preferred_completion=completions.choices[0].completion_id,
            other_completion=completions.choices[1].completion_id,
        )

    @log_function_name
    def test_interactions(self, completions: rest_types.ChatResponse):
        metric_logged_completion = self.client.interactions.get(completions.choices[0].completion_id)
        assert metric_logged_completion
        assert len(metric_logged_completion.direct_feedbacks) == 1
        assert len(metric_logged_completion.comparison_feedbacks) == 1

        _ = self.client.interactions.create(completion="completion", messages=[{"role": "user", "content": "prompt"}])
        _ = self.client.interactions.create(
            model=self.model, completion="completion", messages=[{"role": "user", "content": "prompt"}]
        )

        ungrouped_interactions = self.client.interactions.list(
            filters={"labels": [{"key": "test", "value": ["local"]}]}
        )
        assert ungrouped_interactions.total_count == 2
        grouped_interactions = self.client.interactions.list(
            filters={"labels": [{"key": "test", "value": ["local"]}]}, group_by="prompt"
        )
        assert grouped_interactions.total_count == 1

    @log_function_name
    def test_ab_tests(self, ext_models: Sequence[ModelData]):
        ab_test = self.client.ab_tests.create(
            ab_test_key=self.ab_test, feedback_key=self.feedback_key, models=[self.model, ext_models[0].key]
        )
        assert self.client.ab_tests.get(ab_test.key)
        assert self.client.ab_tests.get(ab_test.id)
        assert len(self.client.ab_tests.list(active=True)) == 1

        _ = self.client.ab_tests.cancel(ab_test.key)

    @log_function_name
    def test_datasets(self):
        integration_data_dir = "tests/integration_data"
        for filename in os.listdir(integration_data_dir):
            new_ds = self.client.datasets.upload(
                file_path=f"{integration_data_dir}/{filename}", dataset_key=filename.replace(".jsonl", "")
            )
            assert self.client.datasets.get(new_ds.key)
            assert self.client.datasets.get(new_ds.id)

        assert len(self.client.datasets.list()) == 4

    def run_all_tests(self):
        self.check_inputs()
        self.test_teams()
        self.test_roles()
        self.test_users()
        self.test_use_cases()
        self.test_feedback_admin()
        ext_models = self.test_models_admin()
        completions = self.test_inference(ext_models)
        self.test_feedback_logging(completions)
        self.test_interactions(completions)
        self.test_ab_tests(ext_models)
        self.test_datasets()
        # TODO:
        #   * test_evals_from_dataset datasets, generating completions in the process
        #   * test_evals_from_interactions, using generations from the previous step
        #   * test training, both with judge feedback provided above, and RLAIF
        # self.test_evals_from_dataset(ext_models)
        # self.test_evals_from_interactions(ext_models)
        # self.test_training(ext_models)


def test_sync():
    base_url = os.getenv("TESTING_ADAPTIVE_BASE_URL")
    api_key = os.getenv("TESTING_ADAPTIVE_API_KEY")
    open_ai_key = os.getenv("TESTING_OPENAI_API_KEY")
    google_key = os.getenv("TESTING_GOOGLE_API_KEY")
    azure_key = os.getenv("TESTING_AZURE_API_KEY")
    azure_endpoint = os.getenv("TESTING_AZURE_ENDPOINT")

    use_case = "use-case"
    other_team_use_case = "other-team-use-case"
    team = "default"
    other_team = "test-team"
    feedback_key = "feedback-key"
    model = "minimal"
    user_email = "user"
    role = "test-role"
    azure_deployment_name = "gpt-4o-mini"
    open_ai_model_name = "adaptive-gpt"
    google_model_name = "adaptive-gemini"
    azure_model_name = "adaptive-azure-gpt"
    ab_test = "ab-test"

    assert api_key
    assert base_url

    sync_client = Adaptive(base_url=base_url, api_key=api_key)

    RunnerFixture(
        client=sync_client,
        use_case=use_case,
        other_team_use_case=other_team_use_case,
        feedback_key=feedback_key,
        model=model,
        user_email=user_email,
        team=team,
        other_team=other_team,
        role=role,
        open_ai_key=open_ai_key,
        google_key=google_key,
        azure_key=azure_key,
        azure_endpoint=azure_endpoint,
        azure_deployment_name=azure_deployment_name,
        open_ai_model_name=open_ai_model_name,
        google_model_name=google_model_name,
        azure_model_name=azure_model_name,
        ab_test=ab_test,
    ).run_all_tests()
