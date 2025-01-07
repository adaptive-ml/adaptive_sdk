from .base_operation import GraphQLField


class AbReportGraphQLField(GraphQLField):
    """@private"""

    def alias(self, alias: str) ->'AbReportGraphQLField':
        self._alias = alias
        return self


class AbVariantReportGraphQLField(GraphQLField):
    """@private"""

    def alias(self, alias: str) ->'AbVariantReportGraphQLField':
        self._alias = alias
        return self


class AbVariantReportComparisonGraphQLField(GraphQLField):
    """@private"""

    def alias(self, alias: str) ->'AbVariantReportComparisonGraphQLField':
        self._alias = alias
        return self


class AbcampaignGraphQLField(GraphQLField):
    """@private"""

    def alias(self, alias: str) ->'AbcampaignGraphQLField':
        self._alias = alias
        return self


class ActivityGraphQLField(GraphQLField):
    """@private"""

    def alias(self, alias: str) ->'ActivityGraphQLField':
        self._alias = alias
        return self


class ActivityOutputGraphQLField(GraphQLField):
    """@private"""

    def alias(self, alias: str) ->'ActivityOutputGraphQLField':
        self._alias = alias
        return self


class AdaptRequestConfigOutputGraphQLField(GraphQLField):
    """@private"""

    def alias(self, alias: str) ->'AdaptRequestConfigOutputGraphQLField':
        self._alias = alias
        return self


class ApiKeyGraphQLField(GraphQLField):
    """@private"""

    def alias(self, alias: str) ->'ApiKeyGraphQLField':
        self._alias = alias
        return self


class AuthProviderGraphQLField(GraphQLField):
    """@private"""

    def alias(self, alias: str) ->'AuthProviderGraphQLField':
        self._alias = alias
        return self


class BaseTrainingParamsOutputGraphQLField(GraphQLField):
    """@private"""

    def alias(self, alias: str) ->'BaseTrainingParamsOutputGraphQLField':
        self._alias = alias
        return self


class BatchInferenceJobStageOutputGraphQLField(GraphQLField):
    """@private"""

    def alias(self, alias: str) ->'BatchInferenceJobStageOutputGraphQLField':
        self._alias = alias
        return self


class ChatMessageGraphQLField(GraphQLField):
    """@private"""

    def alias(self, alias: str) ->'ChatMessageGraphQLField':
        self._alias = alias
        return self


class ComparisonFeedbackGraphQLField(GraphQLField):
    """@private"""

    def alias(self, alias: str) ->'ComparisonFeedbackGraphQLField':
        self._alias = alias
        return self


class CompletionGraphQLField(GraphQLField):
    """@private"""

    def alias(self, alias: str) ->'CompletionGraphQLField':
        self._alias = alias
        return self


class CompletionConnectionGraphQLField(GraphQLField):
    """@private"""

    def alias(self, alias: str) ->'CompletionConnectionGraphQLField':
        self._alias = alias
        return self


class CompletionEdgeGraphQLField(GraphQLField):
    """@private"""

    def alias(self, alias: str) ->'CompletionEdgeGraphQLField':
        self._alias = alias
        return self


class CompletionFeedbackFilterOutputGraphQLField(GraphQLField):
    """@private"""

    def alias(self, alias: str) ->'CompletionFeedbackFilterOutputGraphQLField':
        self._alias = alias
        return self


class CompletionGroupDataGraphQLField(GraphQLField):
    """@private"""

    def alias(self, alias: str) ->'CompletionGroupDataGraphQLField':
        self._alias = alias
        return self


class CompletionGroupDataConnectionGraphQLField(GraphQLField):
    """@private"""

    def alias(self, alias: str) ->'CompletionGroupDataConnectionGraphQLField':
        self._alias = alias
        return self


class CompletionGroupDataEdgeGraphQLField(GraphQLField):
    """@private"""

    def alias(self, alias: str) ->'CompletionGroupDataEdgeGraphQLField':
        self._alias = alias
        return self


class CompletionGroupFeedbackStatsGraphQLField(GraphQLField):
    """@private"""

    def alias(self, alias: str) ->'CompletionGroupFeedbackStatsGraphQLField':
        self._alias = alias
        return self


class CompletionHistoryEntryOuputGraphQLField(GraphQLField):
    """@private"""

    def alias(self, alias: str) ->'CompletionHistoryEntryOuputGraphQLField':
        self._alias = alias
        return self


class CompletionLabelGraphQLField(GraphQLField):
    """@private"""

    def alias(self, alias: str) ->'CompletionLabelGraphQLField':
        self._alias = alias
        return self


class CompletionLabelFilterOutputGraphQLField(GraphQLField):
    """@private"""

    def alias(self, alias: str) ->'CompletionLabelFilterOutputGraphQLField':
        self._alias = alias
        return self


class CompletionMetadataGraphQLField(GraphQLField):
    """@private"""

    def alias(self, alias: str) ->'CompletionMetadataGraphQLField':
        self._alias = alias
        return self


class DatasetGraphQLField(GraphQLField):
    """@private"""

    def alias(self, alias: str) ->'DatasetGraphQLField':
        self._alias = alias
        return self


class DirectFeedbackGraphQLField(GraphQLField):
    """@private"""

    def alias(self, alias: str) ->'DirectFeedbackGraphQLField':
        self._alias = alias
        return self


class DpotrainingParamsOutputGraphQLField(GraphQLField):
    """@private"""

    def alias(self, alias: str) ->'DpotrainingParamsOutputGraphQLField':
        self._alias = alias
        return self


class EmojiGraphQLField(GraphQLField):
    """@private"""

    def alias(self, alias: str) ->'EmojiGraphQLField':
        self._alias = alias
        return self


class EvalJobStageOutputGraphQLField(GraphQLField):
    """@private"""

    def alias(self, alias: str) ->'EvalJobStageOutputGraphQLField':
        self._alias = alias
        return self


class EvaluationJobGraphQLField(GraphQLField):
    """@private"""

    def alias(self, alias: str) ->'EvaluationJobGraphQLField':
        self._alias = alias
        return self


class GuidelinesTrainingParamsOutputGraphQLField(GraphQLField):
    """@private"""

    def alias(self, alias: str) ->'GuidelinesTrainingParamsOutputGraphQLField':
        self._alias = alias
        return self


class InteractionOutputGraphQLField(GraphQLField):
    """@private"""

    def alias(self, alias: str) ->'InteractionOutputGraphQLField':
        self._alias = alias
        return self


class IntervalGraphQLField(GraphQLField):
    """@private"""

    def alias(self, alias: str) ->'IntervalGraphQLField':
        self._alias = alias
        return self


class JobStageInfoOutputUnion(GraphQLField):
    """@private"""

    def on(self, type_name: str, *subfields: GraphQLField
        ) ->'JobStageInfoOutputUnion':
        self._inline_fragments[type_name] = subfields
        return self

    def alias(self, alias: str) ->'JobStageInfoOutputUnion':
        self._alias = alias
        return self


class JobStageOutputGraphQLField(GraphQLField):
    """@private"""

    def alias(self, alias: str) ->'JobStageOutputGraphQLField':
        self._alias = alias
        return self


class LabelKeyUsageGraphQLField(GraphQLField):
    """@private"""

    def alias(self, alias: str) ->'LabelKeyUsageGraphQLField':
        self._alias = alias
        return self


class LabelUsageGraphQLField(GraphQLField):
    """@private"""

    def alias(self, alias: str) ->'LabelUsageGraphQLField':
        self._alias = alias
        return self


class LabelValueUsageGraphQLField(GraphQLField):
    """@private"""

    def alias(self, alias: str) ->'LabelValueUsageGraphQLField':
        self._alias = alias
        return self


class ListCompletionsFilterOutputGraphQLField(GraphQLField):
    """@private"""

    def alias(self, alias: str) ->'ListCompletionsFilterOutputGraphQLField':
        self._alias = alias
        return self


class MetaObjectGraphQLField(GraphQLField):
    """@private"""

    def alias(self, alias: str) ->'MetaObjectGraphQLField':
        self._alias = alias
        return self


class MetricGraphQLField(GraphQLField):
    """@private"""

    def alias(self, alias: str) ->'MetricGraphQLField':
        self._alias = alias
        return self


class MetricActivityGraphQLField(GraphQLField):
    """@private"""

    def alias(self, alias: str) ->'MetricActivityGraphQLField':
        self._alias = alias
        return self


class MetricTrainingParamsMetadataOutputUnion(GraphQLField):
    """@private"""

    def on(self, type_name: str, *subfields: GraphQLField
        ) ->'MetricTrainingParamsMetadataOutputUnion':
        self._inline_fragments[type_name] = subfields
        return self

    def alias(self, alias: str) ->'MetricTrainingParamsMetadataOutputUnion':
        self._alias = alias
        return self


class MetricTrainingParamsOutputGraphQLField(GraphQLField):
    """@private"""

    def alias(self, alias: str) ->'MetricTrainingParamsOutputGraphQLField':
        self._alias = alias
        return self


class MetricWithContextGraphQLField(GraphQLField):
    """@private"""

    def alias(self, alias: str) ->'MetricWithContextGraphQLField':
        self._alias = alias
        return self


class ModelGraphQLField(GraphQLField):
    """@private"""

    def alias(self, alias: str) ->'ModelGraphQLField':
        self._alias = alias
        return self


class ModelServiceGraphQLField(GraphQLField):
    """@private"""

    def alias(self, alias: str) ->'ModelServiceGraphQLField':
        self._alias = alias
        return self


class MutationRootGraphQLField(GraphQLField):
    """@private"""

    def alias(self, alias: str) ->'MutationRootGraphQLField':
        self._alias = alias
        return self


class PageInfoGraphQLField(GraphQLField):
    """@private"""

    def alias(self, alias: str) ->'PageInfoGraphQLField':
        self._alias = alias
        return self


class PpotrainingParamsOutputGraphQLField(GraphQLField):
    """@private"""

    def alias(self, alias: str) ->'PpotrainingParamsOutputGraphQLField':
        self._alias = alias
        return self


class ProviderListGraphQLField(GraphQLField):
    """@private"""

    def alias(self, alias: str) ->'ProviderListGraphQLField':
        self._alias = alias
        return self


class QueryRootGraphQLField(GraphQLField):
    """@private"""

    def alias(self, alias: str) ->'QueryRootGraphQLField':
        self._alias = alias
        return self


class RoleGraphQLField(GraphQLField):
    """@private"""

    def alias(self, alias: str) ->'RoleGraphQLField':
        self._alias = alias
        return self


class SampleConfigOutputGraphQLField(GraphQLField):
    """@private"""

    def alias(self, alias: str) ->'SampleConfigOutputGraphQLField':
        self._alias = alias
        return self


class ScalarMetricConfigOutputGraphQLField(GraphQLField):
    """@private"""

    def alias(self, alias: str) ->'ScalarMetricConfigOutputGraphQLField':
        self._alias = alias
        return self


class SessionGraphQLField(GraphQLField):
    """@private"""

    def alias(self, alias: str) ->'SessionGraphQLField':
        self._alias = alias
        return self


class SettingsGraphQLField(GraphQLField):
    """@private"""

    def alias(self, alias: str) ->'SettingsGraphQLField':
        self._alias = alias
        return self


class ShareGraphQLField(GraphQLField):
    """@private"""

    def alias(self, alias: str) ->'ShareGraphQLField':
        self._alias = alias
        return self


class SystemPromptTemplateGraphQLField(GraphQLField):
    """@private"""

    def alias(self, alias: str) ->'SystemPromptTemplateGraphQLField':
        self._alias = alias
        return self


class TeamGraphQLField(GraphQLField):
    """@private"""

    def alias(self, alias: str) ->'TeamGraphQLField':
        self._alias = alias
        return self


class TeamMemberGraphQLField(GraphQLField):
    """@private"""

    def alias(self, alias: str) ->'TeamMemberGraphQLField':
        self._alias = alias
        return self


class TeamWithroleGraphQLField(GraphQLField):
    """@private"""

    def alias(self, alias: str) ->'TeamWithroleGraphQLField':
        self._alias = alias
        return self


class TimeRangeOutputGraphQLField(GraphQLField):
    """@private"""

    def alias(self, alias: str) ->'TimeRangeOutputGraphQLField':
        self._alias = alias
        return self


class TimeseriesGraphQLField(GraphQLField):
    """@private"""

    def alias(self, alias: str) ->'TimeseriesGraphQLField':
        self._alias = alias
        return self


class TrainingConfigOutputGraphQLField(GraphQLField):
    """@private"""

    def alias(self, alias: str) ->'TrainingConfigOutputGraphQLField':
        self._alias = alias
        return self


class TrainingJobGraphQLField(GraphQLField):
    """@private"""

    def alias(self, alias: str) ->'TrainingJobGraphQLField':
        self._alias = alias
        return self


class TrainingJobStageOutputGraphQLField(GraphQLField):
    """@private"""

    def alias(self, alias: str) ->'TrainingJobStageOutputGraphQLField':
        self._alias = alias
        return self


class TrainingMetadataOutputGraphQLField(GraphQLField):
    """@private"""

    def alias(self, alias: str) ->'TrainingMetadataOutputGraphQLField':
        self._alias = alias
        return self


class TrainingMetadataOutputParametersUnion(GraphQLField):
    """@private"""

    def on(self, type_name: str, *subfields: GraphQLField
        ) ->'TrainingMetadataOutputParametersUnion':
        self._inline_fragments[type_name] = subfields
        return self

    def alias(self, alias: str) ->'TrainingMetadataOutputParametersUnion':
        self._alias = alias
        return self


class TrainingObjectiveOutputUnion(GraphQLField):
    """@private"""

    def on(self, type_name: str, *subfields: GraphQLField
        ) ->'TrainingObjectiveOutputUnion':
        self._inline_fragments[type_name] = subfields
        return self

    def alias(self, alias: str) ->'TrainingObjectiveOutputUnion':
        self._alias = alias
        return self


class TrendResultGraphQLField(GraphQLField):
    """@private"""

    def alias(self, alias: str) ->'TrendResultGraphQLField':
        self._alias = alias
        return self


class UnitConfigGraphQLField(GraphQLField):
    """@private"""

    def alias(self, alias: str) ->'UnitConfigGraphQLField':
        self._alias = alias
        return self


class UseCaseGraphQLField(GraphQLField):
    """@private"""

    def alias(self, alias: str) ->'UseCaseGraphQLField':
        self._alias = alias
        return self


class UseCaseMetadataGraphQLField(GraphQLField):
    """@private"""

    def alias(self, alias: str) ->'UseCaseMetadataGraphQLField':
        self._alias = alias
        return self


class UserGraphQLField(GraphQLField):
    """@private"""

    def alias(self, alias: str) ->'UserGraphQLField':
        self._alias = alias
        return self


class WidgetGraphQLField(GraphQLField):
    """@private"""

    def alias(self, alias: str) ->'WidgetGraphQLField':
        self._alias = alias
        return self
