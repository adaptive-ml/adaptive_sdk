from typing import Any, Dict, Optional
from .base_model import Upload
from .custom_fields import AbcampaignFields, ApiKeyFields, DatasetFields, DirectFeedbackFields, EvaluationJobFields, MetricFields, MetricWithContextFields, ModelFields, ModelServiceFields, SystemPromptTemplateFields, TeamMemberFields, TrainingJobFields, UseCaseFields, UserFields
from .custom_typing_fields import GraphQLField
from .input_types import AbcampaignCreate, AddExternalModelInput, AddHFModelInput, AddModelInput, ApiKeyCreate, AttachModel, DatasetCreate, EvaluationCreate, FeedbackAddInput, FeedbackUpdateInput, MetricCreate, MetricLink, MetricUnlink, ModelServiceDisconnect, SystemPromptTemplateCreate, SystemPromptTemplateUpdate, TeamMemberRemove, TeamMemberSet, TrainingJobInput, UpdateModelService, UseCaseCreate, UseCaseShares, UseCaseUpdate


class Mutation:
    """@private"""

    @classmethod
    def create_ab_campaign(cls, input: AbcampaignCreate) ->AbcampaignFields:
        arguments: Dict[str, Dict[str, Any]] = {'input': {'type':
            'AbcampaignCreate!', 'value': input}}
        cleared_arguments = {key: value for key, value in arguments.items() if
            value['value'] is not None}
        return AbcampaignFields(field_name='createAbCampaign', arguments=
            cleared_arguments)

    @classmethod
    def cancel_ab_campaign(cls, input: str) ->GraphQLField:
        arguments: Dict[str, Dict[str, Any]] = {'input': {'type':
            'IdOrKey!', 'value': input}}
        cleared_arguments = {key: value for key, value in arguments.items() if
            value['value'] is not None}
        return GraphQLField(field_name='cancelAbCampaign', arguments=
            cleared_arguments)

    @classmethod
    def create_dataset(cls, input: DatasetCreate, file: Upload
        ) ->DatasetFields:
        arguments: Dict[str, Dict[str, Any]] = {'input': {'type':
            'DatasetCreate!', 'value': input}, 'file': {'type': 'Upload!',
            'value': file}}
        cleared_arguments = {key: value for key, value in arguments.items() if
            value['value'] is not None}
        return DatasetFields(field_name='createDataset', arguments=
            cleared_arguments)

    @classmethod
    def create_evaluation_job(cls, input: EvaluationCreate
        ) ->EvaluationJobFields:
        arguments: Dict[str, Dict[str, Any]] = {'input': {'type':
            'EvaluationCreate!', 'value': input}}
        cleared_arguments = {key: value for key, value in arguments.items() if
            value['value'] is not None}
        return EvaluationJobFields(field_name='createEvaluationJob',
            arguments=cleared_arguments)

    @classmethod
    def create_system_prompt_template(cls, input: SystemPromptTemplateCreate
        ) ->SystemPromptTemplateFields:
        arguments: Dict[str, Dict[str, Any]] = {'input': {'type':
            'SystemPromptTemplateCreate!', 'value': input}}
        cleared_arguments = {key: value for key, value in arguments.items() if
            value['value'] is not None}
        return SystemPromptTemplateFields(field_name=
            'createSystemPromptTemplate', arguments=cleared_arguments)

    @classmethod
    def derive_system_prompt_template(cls, input: SystemPromptTemplateUpdate
        ) ->SystemPromptTemplateFields:
        arguments: Dict[str, Dict[str, Any]] = {'input': {'type':
            'SystemPromptTemplateUpdate!', 'value': input}}
        cleared_arguments = {key: value for key, value in arguments.items() if
            value['value'] is not None}
        return SystemPromptTemplateFields(field_name=
            'deriveSystemPromptTemplate', arguments=cleared_arguments)

    @classmethod
    def create_metric(cls, input: MetricCreate) ->MetricFields:
        arguments: Dict[str, Dict[str, Any]] = {'input': {'type':
            'MetricCreate!', 'value': input}}
        cleared_arguments = {key: value for key, value in arguments.items() if
            value['value'] is not None}
        return MetricFields(field_name='createMetric', arguments=
            cleared_arguments)

    @classmethod
    def link_metric(cls, input: MetricLink) ->MetricWithContextFields:
        arguments: Dict[str, Dict[str, Any]] = {'input': {'type':
            'MetricLink!', 'value': input}}
        cleared_arguments = {key: value for key, value in arguments.items() if
            value['value'] is not None}
        return MetricWithContextFields(field_name='linkMetric', arguments=
            cleared_arguments)

    @classmethod
    def unlink_metric(cls, input: MetricUnlink) ->GraphQLField:
        arguments: Dict[str, Dict[str, Any]] = {'input': {'type':
            'MetricUnlink!', 'value': input}}
        cleared_arguments = {key: value for key, value in arguments.items() if
            value['value'] is not None}
        return GraphQLField(field_name='unlinkMetric', arguments=
            cleared_arguments)

    @classmethod
    def attach_model(cls, input: AttachModel) ->ModelServiceFields:
        arguments: Dict[str, Dict[str, Any]] = {'input': {'type':
            'AttachModel!', 'value': input}}
        cleared_arguments = {key: value for key, value in arguments.items() if
            value['value'] is not None}
        return ModelServiceFields(field_name='attachModel', arguments=
            cleared_arguments)

    @classmethod
    def disconnect_model(cls, input: ModelServiceDisconnect) ->GraphQLField:
        arguments: Dict[str, Dict[str, Any]] = {'input': {'type':
            'ModelServiceDisconnect!', 'value': input}}
        cleared_arguments = {key: value for key, value in arguments.items() if
            value['value'] is not None}
        return GraphQLField(field_name='disconnectModel', arguments=
            cleared_arguments)

    @classmethod
    def update_model_service(cls, input: UpdateModelService
        ) ->ModelServiceFields:
        arguments: Dict[str, Dict[str, Any]] = {'input': {'type':
            'UpdateModelService!', 'value': input}}
        cleared_arguments = {key: value for key, value in arguments.items() if
            value['value'] is not None}
        return ModelServiceFields(field_name='updateModelService',
            arguments=cleared_arguments)

    @classmethod
    def deploy_model(cls, id_or_key: str, wait: bool) ->GraphQLField:
        arguments: Dict[str, Dict[str, Any]] = {'idOrKey': {'type':
            'IdOrKey!', 'value': id_or_key}, 'wait': {'type': 'Boolean!',
            'value': wait}}
        cleared_arguments = {key: value for key, value in arguments.items() if
            value['value'] is not None}
        return GraphQLField(field_name='deployModel', arguments=
            cleared_arguments)

    @classmethod
    def terminate_model(cls, id_or_key: str, force: bool) ->GraphQLField:
        arguments: Dict[str, Dict[str, Any]] = {'idOrKey': {'type':
            'IdOrKey!', 'value': id_or_key}, 'force': {'type': 'Boolean!',
            'value': force}}
        cleared_arguments = {key: value for key, value in arguments.items() if
            value['value'] is not None}
        return GraphQLField(field_name='terminateModel', arguments=
            cleared_arguments)

    @classmethod
    def add_external_model(cls, input: AddExternalModelInput) ->ModelFields:
        arguments: Dict[str, Dict[str, Any]] = {'input': {'type':
            'AddExternalModelInput!', 'value': input}}
        cleared_arguments = {key: value for key, value in arguments.items() if
            value['value'] is not None}
        return ModelFields(field_name='addExternalModel', arguments=
            cleared_arguments)

    @classmethod
    def add_model(cls, input: AddModelInput) ->ModelFields:
        arguments: Dict[str, Dict[str, Any]] = {'input': {'type':
            'AddModelInput!', 'value': input}}
        cleared_arguments = {key: value for key, value in arguments.items() if
            value['value'] is not None}
        return ModelFields(field_name='addModel', arguments=cleared_arguments)

    @classmethod
    def import_hf_model(cls, input: AddHFModelInput) ->GraphQLField:
        arguments: Dict[str, Dict[str, Any]] = {'input': {'type':
            'AddHFModelInput!', 'value': input}}
        cleared_arguments = {key: value for key, value in arguments.items() if
            value['value'] is not None}
        return GraphQLField(field_name='importHfModel', arguments=
            cleared_arguments)

    @classmethod
    def create_training_job(cls, input: TrainingJobInput) ->TrainingJobFields:
        arguments: Dict[str, Dict[str, Any]] = {'input': {'type':
            'TrainingJobInput!', 'value': input}}
        cleared_arguments = {key: value for key, value in arguments.items() if
            value['value'] is not None}
        return TrainingJobFields(field_name='createTrainingJob', arguments=
            cleared_arguments)

    @classmethod
    def cancel_training_job(cls, id: Any) ->GraphQLField:
        arguments: Dict[str, Dict[str, Any]] = {'id': {'type': 'UUID!',
            'value': id}}
        cleared_arguments = {key: value for key, value in arguments.items() if
            value['value'] is not None}
        return GraphQLField(field_name='cancelTrainingJob', arguments=
            cleared_arguments)

    @classmethod
    def create_use_case(cls, input: UseCaseCreate) ->UseCaseFields:
        arguments: Dict[str, Dict[str, Any]] = {'input': {'type':
            'UseCaseCreate!', 'value': input}}
        cleared_arguments = {key: value for key, value in arguments.items() if
            value['value'] is not None}
        return UseCaseFields(field_name='createUseCase', arguments=
            cleared_arguments)

    @classmethod
    def update_use_case(cls, id_or_key: str, input: UseCaseUpdate
        ) ->UseCaseFields:
        arguments: Dict[str, Dict[str, Any]] = {'idOrKey': {'type':
            'IdOrKey!', 'value': id_or_key}, 'input': {'type':
            'UseCaseUpdate!', 'value': input}}
        cleared_arguments = {key: value for key, value in arguments.items() if
            value['value'] is not None}
        return UseCaseFields(field_name='updateUseCase', arguments=
            cleared_arguments)

    @classmethod
    def share_use_case(cls, id_or_key: str, input: UseCaseShares
        ) ->UseCaseFields:
        arguments: Dict[str, Dict[str, Any]] = {'idOrKey': {'type':
            'IdOrKey!', 'value': id_or_key}, 'input': {'type':
            'UseCaseShares!', 'value': input}}
        cleared_arguments = {key: value for key, value in arguments.items() if
            value['value'] is not None}
        return UseCaseFields(field_name='shareUseCase', arguments=
            cleared_arguments)

    @classmethod
    def create_api_key(cls, input: ApiKeyCreate) ->ApiKeyFields:
        arguments: Dict[str, Dict[str, Any]] = {'input': {'type':
            'ApiKeyCreate!', 'value': input}}
        cleared_arguments = {key: value for key, value in arguments.items() if
            value['value'] is not None}
        return ApiKeyFields(field_name='createApiKey', arguments=
            cleared_arguments)

    @classmethod
    def set_team_member(cls, input: TeamMemberSet) ->TeamMemberFields:
        arguments: Dict[str, Dict[str, Any]] = {'input': {'type':
            'TeamMemberSet!', 'value': input}}
        cleared_arguments = {key: value for key, value in arguments.items() if
            value['value'] is not None}
        return TeamMemberFields(field_name='setTeamMember', arguments=
            cleared_arguments)

    @classmethod
    def remove_team_member(cls, input: TeamMemberRemove) ->UserFields:
        arguments: Dict[str, Dict[str, Any]] = {'input': {'type':
            'TeamMemberRemove!', 'value': input}}
        cleared_arguments = {key: value for key, value in arguments.items() if
            value['value'] is not None}
        return UserFields(field_name='removeTeamMember', arguments=
            cleared_arguments)

    @classmethod
    def update_feedback(cls, id: Any, input: FeedbackUpdateInput
        ) ->DirectFeedbackFields:
        arguments: Dict[str, Dict[str, Any]] = {'id': {'type': 'UUID!',
            'value': id}, 'input': {'type': 'FeedbackUpdateInput!', 'value':
            input}}
        cleared_arguments = {key: value for key, value in arguments.items() if
            value['value'] is not None}
        return DirectFeedbackFields(field_name='updateFeedback', arguments=
            cleared_arguments)

    @classmethod
    def add_direct_feedback(cls, completion_id: Any, metric_id: str, input:
        FeedbackAddInput) ->DirectFeedbackFields:
        arguments: Dict[str, Dict[str, Any]] = {'completionId': {'type':
            'UUID!', 'value': completion_id}, 'metricId': {'type':
            'IdOrKey!', 'value': metric_id}, 'input': {'type':
            'FeedbackAddInput!', 'value': input}}
        cleared_arguments = {key: value for key, value in arguments.items() if
            value['value'] is not None}
        return DirectFeedbackFields(field_name='addDirectFeedback',
            arguments=cleared_arguments)
