from typing import Annotated, Any, List, Literal, Optional, Union
from pydantic import Field
from .base_model import BaseModel
from .enums import AbcampaignStatus, CompletionSource, CompletionSourceOutput, EvaluationJobStatus, FeedbackType, FeedbackTypeOutput, JobStatusOutput, MetricKind, MetricScoringType, ModelKindFilter, ModelOnline, ProviderName, SelectionTypeOutput, TrainingJobStatus, TrainingMetadataOutputAlignmentMethod, TrainingMetadataOutputTrainingType


class AbCampaignCreateData(BaseModel):
    """@public"""
    id: Any
    key: str
    status: AbcampaignStatus
    begin_date: int = Field(alias='beginDate')


class MetricData(BaseModel):
    """@public"""
    id: Any
    key: str
    name: str
    kind: MetricKind
    description: str
    scoring_type: MetricScoringType = Field(alias='scoringType')
    created_at: int = Field(alias='createdAt')
    has_direct_feedbacks: bool = Field(alias='hasDirectFeedbacks')
    has_comparison_feedbacks: bool = Field(alias='hasComparisonFeedbacks')


class AbCampaignDetailData(AbCampaignCreateData):
    """@public"""
    feedback_type: FeedbackType = Field(alias='feedbackType')
    traffic_split: float = Field(alias='trafficSplit')
    end_date: Optional[int] = Field(alias='endDate')
    metric: Optional['AbCampaignDetailDataMetric']
    use_case: Optional['AbCampaignDetailDataUseCase'] = Field(alias='useCase')
    models: List['AbCampaignDetailDataModels']
    feedbacks: int
    has_enough_feedbacks: bool = Field(alias='hasEnoughFeedbacks')


class AbCampaignDetailDataMetric(MetricData):
    """@public"""
    pass


class AbCampaignDetailDataUseCase(BaseModel):
    """@public"""
    id: Any
    key: str
    name: str


class AbCampaignDetailDataModels(BaseModel):
    """@public"""
    id: Any
    key: str
    name: str


class AbCampaignReportData(BaseModel):
    """@public"""
    p_value: Optional[float] = Field(alias='pValue')
    variants: List['AbCampaignReportDataVariants']


class AbCampaignReportDataVariants(BaseModel):
    """@public"""
    variant: 'AbCampaignReportDataVariantsVariant'
    interval: 'AbCampaignReportDataVariantsInterval'
    feedbacks: int
    comparisons: Optional[List['AbCampaignReportDataVariantsComparisons']]


class AbCampaignReportDataVariantsVariant(BaseModel):
    """@public"""
    id: Any
    key: str
    name: str


class AbCampaignReportDataVariantsInterval(BaseModel):
    """@public"""
    start: float
    middle: float
    end: float


class AbCampaignReportDataVariantsComparisons(BaseModel):
    """@public"""
    feedbacks: int
    wins: int
    losses: int
    ties_good: int = Field(alias='tiesGood')
    ties_bad: int = Field(alias='tiesBad')
    variant: 'AbCampaignReportDataVariantsComparisonsVariant'


class AbCampaignReportDataVariantsComparisonsVariant(BaseModel):
    """@public"""
    id: Any
    key: str
    name: str


class CompletionData(BaseModel):
    """@public"""
    id: Any
    prompt: str
    chat_messages: Optional[List['CompletionDataChatMessages']] = Field(alias
        ='chatMessages')
    completion: Optional[str]
    source: CompletionSource
    model: Optional['CompletionDataModel']
    direct_feedbacks: List['CompletionDataDirectFeedbacks'] = Field(alias=
        'directFeedbacks')
    labels: List['CompletionDataLabels']
    created_at: int = Field(alias='createdAt')


class CompletionDataChatMessages(BaseModel):
    """@public"""
    role: str
    content: str


class CompletionDataModel(BaseModel):
    """@public"""
    id: Any
    key: str
    name: str


class CompletionDataDirectFeedbacks(BaseModel):
    """@public"""
    id: Any
    value: float
    metric: Optional['CompletionDataDirectFeedbacksMetric']
    reason: Optional[str]
    details: Optional[str]
    created_at: int = Field(alias='createdAt')


class CompletionDataDirectFeedbacksMetric(MetricData):
    """@public"""
    pass


class CompletionDataLabels(BaseModel):
    """@public"""
    key: str
    value: str


class DatasetData(BaseModel):
    """@public"""
    id: Any
    key: str
    name: str
    created_at: Any = Field(alias='createdAt')


class ModelData(BaseModel):
    """@public"""
    id: Any
    key: str
    name: str
    online: ModelOnline
    is_external: bool = Field(alias='isExternal')
    provider_name: ProviderName = Field(alias='providerName')
    is_adapter: bool = Field(alias='isAdapter')
    is_training: bool = Field(alias='isTraining')
    created_at: int = Field(alias='createdAt')
    kind: ModelKindFilter


class ModelServiceData(BaseModel):
    """@public"""
    id: Any
    key: str
    name: str
    model: 'ModelServiceDataModel'
    attached: bool
    is_default: bool = Field(alias='isDefault')
    desired_online: bool = Field(alias='desiredOnline')
    created_at: int = Field(alias='createdAt')


class ModelServiceDataModel(ModelData):
    """@public"""
    backbone: Optional['ModelServiceDataModelBackbone']


class ModelServiceDataModelBackbone(ModelData):
    """@public"""
    pass


class JobStageOutputData(BaseModel):
    """@public"""
    name: str
    status: JobStatusOutput
    parent: Optional[str]
    stage_id: int = Field(alias='stageId')
    info: Optional[Annotated[Union[
        'JobStageOutputDataInfoTrainingJobStageOutput',
        'JobStageOutputDataInfoEvalJobStageOutput',
        'JobStageOutputDataInfoBatchInferenceJobStageOutput'], Field(
        discriminator='typename__')]]
    started_at: Optional[int] = Field(alias='startedAt')
    ended_at: Optional[int] = Field(alias='endedAt')


class JobStageOutputDataInfoTrainingJobStageOutput(BaseModel):
    """@public"""
    typename__: Literal['TrainingJobStageOutput'] = Field(alias='__typename')
    training_monitoring_link: Optional[str] = Field(alias=
        'trainingMonitoringLink')
    total_num_samples: Optional[int] = Field(alias='totalNumSamples')
    processed_num_samples: Optional[int] = Field(alias='processedNumSamples')
    checkpoints: List[str]


class JobStageOutputDataInfoEvalJobStageOutput(BaseModel):
    """@public"""
    typename__: Literal['EvalJobStageOutput'] = Field(alias='__typename')
    total_num_samples: Optional[int] = Field(alias='totalNumSamples')
    processed_num_samples: Optional[int] = Field(alias='processedNumSamples')


class JobStageOutputDataInfoBatchInferenceJobStageOutput(BaseModel):
    """@public"""
    typename__: Literal['BatchInferenceJobStageOutput'] = Field(alias=
        '__typename')
    total_num_samples: Optional[int] = Field(alias='totalNumSamples')
    processed_num_samples: Optional[int] = Field(alias='processedNumSamples')


class MetricWithContextData(BaseModel):
    """@public"""
    id: Any
    key: str
    name: str
    kind: MetricKind
    description: str
    scoring_type: MetricScoringType = Field(alias='scoringType')
    created_at: Any = Field(alias='createdAt')


class UseCaseData(BaseModel):
    """@public"""
    id: Any
    key: str
    name: str
    description: str
    created_at: int = Field(alias='createdAt')
    metrics: List['UseCaseDataMetrics']
    model_services: List['UseCaseDataModelServices'] = Field(alias=
        'modelServices')


class UseCaseDataMetrics(MetricWithContextData):
    """@public"""
    pass


class UseCaseDataModelServices(ModelServiceData):
    """@public"""
    pass


class EvaluationJobData(BaseModel):
    """@public"""
    id: Any
    name: str
    status: EvaluationJobStatus
    created_at: int = Field(alias='createdAt')
    started_at: Optional[int] = Field(alias='startedAt')
    ended_at: Optional[int] = Field(alias='endedAt')
    duration_ms: Optional[int] = Field(alias='durationMs')
    model_services: List['EvaluationJobDataModelServices'] = Field(alias=
        'modelServices')
    judge: Optional['EvaluationJobDataJudge']
    stages: List['EvaluationJobDataStages']
    use_case: Optional['EvaluationJobDataUseCase'] = Field(alias='useCase')
    report: Optional['EvaluationJobDataReport']
    dataset: Optional['EvaluationJobDataDataset']
    created_by: Optional['EvaluationJobDataCreatedBy'] = Field(alias=
        'createdBy')


class EvaluationJobDataModelServices(ModelServiceData):
    """@public"""
    pass


class EvaluationJobDataJudge(ModelServiceData):
    """@public"""
    pass


class EvaluationJobDataStages(JobStageOutputData):
    """@public"""
    pass


class EvaluationJobDataUseCase(UseCaseData):
    """@public"""
    pass


class EvaluationJobDataReport(AbCampaignReportData):
    """@public"""
    pass


class EvaluationJobDataDataset(DatasetData):
    """@public"""
    pass


class EvaluationJobDataCreatedBy(BaseModel):
    """@public"""
    id: Any
    email: str
    name: str


class ListCompletionsFilterOutputData(BaseModel):
    """@public"""
    use_case: str = Field(alias='useCase')
    models: Optional[List[str]]
    timerange: Optional['ListCompletionsFilterOutputDataTimerange']
    feedbacks: Optional[List['ListCompletionsFilterOutputDataFeedbacks']]
    labels: Optional[List['ListCompletionsFilterOutputDataLabels']]
    tags: Optional[List[str]]
    source: Optional[List[CompletionSourceOutput]]


class ListCompletionsFilterOutputDataTimerange(BaseModel):
    """@public"""
    from_: Any = Field(alias='from')
    to: Any


class ListCompletionsFilterOutputDataFeedbacks(BaseModel):
    """@public"""
    metric: str


class ListCompletionsFilterOutputDataLabels(BaseModel):
    """@public"""
    key: str
    value: Optional[List[str]]


class MetricDataAdmin(BaseModel):
    """@public"""
    id: Any
    key: str
    name: str
    kind: MetricKind
    description: str
    scoring_type: MetricScoringType = Field(alias='scoringType')
    use_cases: List['MetricDataAdminUseCases'] = Field(alias='useCases')
    created_at: int = Field(alias='createdAt')
    has_direct_feedbacks: bool = Field(alias='hasDirectFeedbacks')
    has_comparison_feedbacks: bool = Field(alias='hasComparisonFeedbacks')


class MetricDataAdminUseCases(BaseModel):
    """@public"""
    id: Any
    name: str
    key: str
    description: str


class ModelDataAdmin(BaseModel):
    """@public"""
    id: Any
    key: str
    name: str
    online: ModelOnline
    use_cases: List['ModelDataAdminUseCases'] = Field(alias='useCases')
    is_external: bool = Field(alias='isExternal')
    provider_name: ProviderName = Field(alias='providerName')
    is_adapter: bool = Field(alias='isAdapter')
    is_training: bool = Field(alias='isTraining')
    created_at: int = Field(alias='createdAt')
    kind: ModelKindFilter


class ModelDataAdminUseCases(BaseModel):
    """@public"""
    id: Any
    key: str
    name: str


class TrainingConfigOutputData(BaseModel):
    """@public"""
    base_training_params: 'TrainingConfigOutputDataBaseTrainingParams' = Field(
        alias='baseTrainingParams')
    training_metadata: 'TrainingConfigOutputDataTrainingMetadata' = Field(alias
        ='trainingMetadata')
    training_objective: Union[
        'TrainingConfigOutputDataTrainingObjectiveMetricTrainingParamsOutput',
        'TrainingConfigOutputDataTrainingObjectiveGuidelinesTrainingParamsOutput'
        ] = Field(alias='trainingObjective', discriminator='typename__')


class TrainingConfigOutputDataBaseTrainingParams(BaseModel):
    """@public"""
    learning_rate: float = Field(alias='learningRate')
    num_epochs: int = Field(alias='numEpochs')
    batch_size: int = Field(alias='batchSize')
    num_validations: int = Field(alias='numValidations')


class TrainingConfigOutputDataTrainingMetadata(BaseModel):
    """@public"""
    training_type: TrainingMetadataOutputTrainingType = Field(alias=
        'trainingType')
    alignment_method: TrainingMetadataOutputAlignmentMethod = Field(alias=
        'alignmentMethod')
    parameters: Optional[Annotated[Union[
        'TrainingConfigOutputDataTrainingMetadataParametersDpotrainingParamsOutput'
        ,
        'TrainingConfigOutputDataTrainingMetadataParametersPpotrainingParamsOutput'
        ], Field(discriminator='typename__')]]


class TrainingConfigOutputDataTrainingMetadataParametersDpotrainingParamsOutput(
    BaseModel):
    """@public"""
    typename__: Literal['DpotrainingParamsOutput'] = Field(alias='__typename')
    kl_div_coeff: float = Field(alias='klDivCoeff')


class TrainingConfigOutputDataTrainingMetadataParametersPpotrainingParamsOutput(
    BaseModel):
    """@public"""
    typename__: Literal['PpotrainingParamsOutput'] = Field(alias='__typename')
    kl_div_coeff: float = Field(alias='klDivCoeff')


class TrainingConfigOutputDataTrainingObjectiveMetricTrainingParamsOutput(
    BaseModel):
    """@public"""
    typename__: Literal['MetricTrainingParamsOutput'] = Field(alias=
        '__typename')
    metric_key: str = Field(alias='metricKey')
    metric_metadata: Optional[Annotated[Union[
        'TrainingConfigOutputDataTrainingObjectiveMetricTrainingParamsOutputMetricMetadataScalarMetricConfigOutput'
        ,], Field(discriminator='typename__')]] = Field(alias='metricMetadata')


class TrainingConfigOutputDataTrainingObjectiveMetricTrainingParamsOutputMetricMetadataScalarMetricConfigOutput(
    BaseModel):
    """@public"""
    typename__: Literal['ScalarMetricConfigOutput'] = Field(alias='__typename')
    threshold: Optional[float]


class TrainingConfigOutputDataTrainingObjectiveGuidelinesTrainingParamsOutput(
    BaseModel):
    """@public"""
    typename__: Literal['GuidelinesTrainingParamsOutput'] = Field(alias=
        '__typename')
    judge_model: str = Field(alias='judgeModel')
    judge_model_prompt: str = Field(alias='judgeModelPrompt')


class TrainingJobData(BaseModel):
    """@public"""
    id: Any
    name: str
    status: TrainingJobStatus
    created_at: int = Field(alias='createdAt')
    started_at: Optional[int] = Field(alias='startedAt')
    ended_at: Optional[int] = Field(alias='endedAt')
    duration_ms: Optional[int] = Field(alias='durationMs')
    stages: List['TrainingJobDataStages']
    parent_model: Optional['TrainingJobDataParentModel'] = Field(alias=
        'parentModel')
    child_model: Optional['TrainingJobDataChildModel'] = Field(alias=
        'childModel')
    use_case: Optional['TrainingJobDataUseCase'] = Field(alias='useCase')
    config: 'TrainingJobDataConfig'
    created_by: Optional['TrainingJobDataCreatedBy'] = Field(alias='createdBy')


class TrainingJobDataStages(JobStageOutputData):
    """@public"""
    pass


class TrainingJobDataParentModel(ModelData):
    """@public"""
    backbone: Optional['TrainingJobDataParentModelBackbone']


class TrainingJobDataParentModelBackbone(ModelData):
    """@public"""
    pass


class TrainingJobDataChildModel(ModelData):
    """@public"""
    backbone: Optional['TrainingJobDataChildModelBackbone']


class TrainingJobDataChildModelBackbone(ModelData):
    """@public"""
    pass


class TrainingJobDataUseCase(UseCaseData):
    """@public"""
    pass


class TrainingJobDataConfig(BaseModel):
    """@public"""
    output_name: str = Field(alias='outputName')
    sample_config: 'TrainingJobDataConfigSampleConfig' = Field(alias=
        'sampleConfig')
    training_config: 'TrainingJobDataConfigTrainingConfig' = Field(alias=
        'trainingConfig')


class TrainingJobDataConfigSampleConfig(BaseModel):
    """@public"""
    feedback_type: Optional[FeedbackTypeOutput] = Field(alias='feedbackType')
    selection_type: SelectionTypeOutput = Field(alias='selectionType')
    max_samples: Optional[int] = Field(alias='maxSamples')
    filter: Optional['TrainingJobDataConfigSampleConfigFilter']


class TrainingJobDataConfigSampleConfigFilter(ListCompletionsFilterOutputData):
    """@public"""
    pass


class TrainingJobDataConfigTrainingConfig(TrainingConfigOutputData):
    """@public"""
    pass


class TrainingJobDataCreatedBy(BaseModel):
    """@public"""
    id: Any
    email: str
    name: str


AbCampaignCreateData.model_rebuild()
MetricData.model_rebuild()
AbCampaignDetailData.model_rebuild()
AbCampaignReportData.model_rebuild()
CompletionData.model_rebuild()
DatasetData.model_rebuild()
ModelData.model_rebuild()
ModelServiceData.model_rebuild()
JobStageOutputData.model_rebuild()
MetricWithContextData.model_rebuild()
UseCaseData.model_rebuild()
EvaluationJobData.model_rebuild()
ListCompletionsFilterOutputData.model_rebuild()
MetricDataAdmin.model_rebuild()
ModelDataAdmin.model_rebuild()
TrainingConfigOutputData.model_rebuild()
TrainingJobData.model_rebuild()
