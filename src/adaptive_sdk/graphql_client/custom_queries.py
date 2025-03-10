from typing import Any, Dict, Optional
from . import CompletionGroupBy
from .custom_fields import (
    AbcampaignFields,
    CompletionConnectionFields,
    CompletionFields,
    CompletionGroupDataConnectionFields,
    ComputePoolFields,
    DatasetFields,
    EvaluationJobFields,
    MetaObjectFields,
    MetricFields,
    ModelFields,
    PartitionFields,
    RoleFields,
    SystemPromptTemplateFields,
    TeamFields,
    TrainingJobFields,
    UseCaseFields,
    UserFields,
)
from .custom_typing_fields import GraphQLField
from .input_types import (
    AbCampaignFilter,
    CursorPageInput,
    FeedbackFilterInput,
    ListCompletionsFilterInput,
    ModelFilter,
    OrderPair,
    UseCaseFilter,
)


class Query:
    """@private"""

    @classmethod
    def ab_campaigns(cls, filter: AbCampaignFilter) -> AbcampaignFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "filter": {"type": "AbCampaignFilter!", "value": filter}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return AbcampaignFields(field_name="abCampaigns", arguments=cleared_arguments)

    @classmethod
    def ab_campaign(cls, id_or_key: str) -> AbcampaignFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "idOrKey": {"type": "IdOrKey!", "value": id_or_key}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return AbcampaignFields(field_name="abCampaign", arguments=cleared_arguments)

    @classmethod
    def datasets(cls, use_case: str) -> DatasetFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "useCase": {"type": "IdOrKey!", "value": use_case}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return DatasetFields(field_name="datasets", arguments=cleared_arguments)

    @classmethod
    def dataset(cls, id_or_key: str) -> DatasetFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "idOrKey": {"type": "IdOrKey!", "value": id_or_key}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return DatasetFields(field_name="dataset", arguments=cleared_arguments)

    @classmethod
    def evaluation_jobs(cls) -> EvaluationJobFields:
        return EvaluationJobFields(field_name="evaluationJobs")

    @classmethod
    def evaluation_job(cls, id: Any) -> EvaluationJobFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "UUID!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return EvaluationJobFields(
            field_name="evaluationJob", arguments=cleared_arguments
        )

    @classmethod
    def completions(
        cls, filter: ListCompletionsFilterInput, page: CursorPageInput, order: OrderPair
    ) -> CompletionConnectionFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "filter": {"type": "ListCompletionsFilterInput!", "value": filter},
            "page": {"type": "CursorPageInput!", "value": page},
            "order": {"type": "OrderPair!", "value": order},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return CompletionConnectionFields(
            field_name="completions", arguments=cleared_arguments
        )

    @classmethod
    def completions_grouped(
        cls,
        filter: ListCompletionsFilterInput,
        feedback_filter: FeedbackFilterInput,
        group_by: CompletionGroupBy,
        page: CursorPageInput,
        order: OrderPair,
    ) -> CompletionGroupDataConnectionFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "filter": {"type": "ListCompletionsFilterInput!", "value": filter},
            "feedbackFilter": {
                "type": "FeedbackFilterInput!",
                "value": feedback_filter,
            },
            "groupBy": {"type": "CompletionGroupBy!", "value": group_by},
            "page": {"type": "CursorPageInput!", "value": page},
            "order": {"type": "OrderPair!", "value": order},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return CompletionGroupDataConnectionFields(
            field_name="completionsGrouped", arguments=cleared_arguments
        )

    @classmethod
    def completion(cls, use_case: str, id: Any) -> CompletionFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "useCase": {"type": "IdOrKey!", "value": use_case},
            "id": {"type": "UUID!", "value": id},
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return CompletionFields(field_name="completion", arguments=cleared_arguments)

    @classmethod
    def completion_download_url(
        cls, filter: ListCompletionsFilterInput
    ) -> GraphQLField:
        arguments: Dict[str, Dict[str, Any]] = {
            "filter": {"type": "ListCompletionsFilterInput!", "value": filter}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return GraphQLField(
            field_name="completionDownloadUrl", arguments=cleared_arguments
        )

    @classmethod
    def system_prompt_templates(cls) -> SystemPromptTemplateFields:
        return SystemPromptTemplateFields(field_name="systemPromptTemplates")

    @classmethod
    def metrics(cls) -> MetricFields:
        return MetricFields(field_name="metrics")

    @classmethod
    def metric(cls, id_or_key: str) -> MetricFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "idOrKey": {"type": "IdOrKey!", "value": id_or_key}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return MetricFields(field_name="metric", arguments=cleared_arguments)

    @classmethod
    def models(cls, filter: ModelFilter) -> ModelFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "filter": {"type": "ModelFilter!", "value": filter}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return ModelFields(field_name="models", arguments=cleared_arguments)

    @classmethod
    def model(cls, id_or_key: str) -> ModelFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "idOrKey": {"type": "IdOrKey!", "value": id_or_key}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return ModelFields(field_name="model", arguments=cleared_arguments)

    @classmethod
    def partitions(cls) -> PartitionFields:
        return PartitionFields(field_name="partitions")

    @classmethod
    def compute_pools(cls) -> ComputePoolFields:
        return ComputePoolFields(field_name="computePools")

    @classmethod
    def training_jobs(cls) -> TrainingJobFields:
        return TrainingJobFields(field_name="trainingJobs")

    @classmethod
    def training_job(cls, id: Any) -> TrainingJobFields:
        arguments: Dict[str, Dict[str, Any]] = {"id": {"type": "UUID!", "value": id}}
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return TrainingJobFields(field_name="trainingJob", arguments=cleared_arguments)

    @classmethod
    def use_cases(cls, filter: UseCaseFilter) -> UseCaseFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "filter": {"type": "UseCaseFilter!", "value": filter}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return UseCaseFields(field_name="useCases", arguments=cleared_arguments)

    @classmethod
    def use_case(cls, id_or_key: str) -> UseCaseFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "idOrKey": {"type": "IdOrKey!", "value": id_or_key}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return UseCaseFields(field_name="useCase", arguments=cleared_arguments)

    @classmethod
    def me(cls) -> UserFields:
        return UserFields(field_name="me")

    @classmethod
    def users(cls) -> UserFields:
        return UserFields(field_name="users")

    @classmethod
    def roles(cls) -> RoleFields:
        return RoleFields(field_name="roles")

    @classmethod
    def permissions(cls) -> GraphQLField:
        return GraphQLField(field_name="permissions")

    @classmethod
    def teams(cls) -> TeamFields:
        return TeamFields(field_name="teams")

    @classmethod
    def meta(cls) -> MetaObjectFields:
        return MetaObjectFields(field_name="meta")
