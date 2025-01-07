from enum import Enum


class AbcampaignStatus(str, Enum):
    """@public"""
    WARMUP = 'WARMUP'
    IN_PROGRESS = 'IN_PROGRESS'
    DONE = 'DONE'
    CANCELLED = 'CANCELLED'


class AuthProviderKind(str, Enum):
    """@public"""
    OIDC = 'OIDC'


class CompletionGroupBy(str, Enum):
    """@public"""
    MODEL = 'MODEL'
    PROMPT = 'PROMPT'


class CompletionSource(str, Enum):
    """@public"""
    LIVE = 'LIVE'
    OFFLINE = 'OFFLINE'
    AUTOMATION = 'AUTOMATION'
    DATASET = 'DATASET'


class CompletionSourceOutput(str, Enum):
    """@public"""
    LIVE = 'LIVE'
    OFFLINE = 'OFFLINE'
    AUTOMATION = 'AUTOMATION'


class EvaluationJobStatus(str, Enum):
    """@public"""
    PENDING = 'PENDING'
    RUNNING = 'RUNNING'
    COMPLETED = 'COMPLETED'
    FAILED = 'FAILED'
    CANCELED = 'CANCELED'


class ExternalModelProviderName(str, Enum):
    """@public"""
    OPEN_AI = 'OPEN_AI'
    GOOGLE = 'GOOGLE'


class FeedbackType(str, Enum):
    """@public"""
    DIRECT = 'DIRECT'
    COMPARISON = 'COMPARISON'


class FeedbackTypeInput(str, Enum):
    """@public"""
    DIRECT = 'DIRECT'
    PREFERENCE = 'PREFERENCE'


class FeedbackTypeOutput(str, Enum):
    """@public"""
    DIRECT = 'DIRECT'
    PREFERENCE = 'PREFERENCE'


class JobStatusOutput(str, Enum):
    """@public"""
    PENDING = 'PENDING'
    RUNNING = 'RUNNING'
    DONE = 'DONE'
    CANCELLED = 'CANCELLED'
    ERROR = 'ERROR'


class MetricAggregation(str, Enum):
    """@public"""
    AVERAGE = 'AVERAGE'
    SUM = 'SUM'
    COUNT = 'COUNT'


class MetricKind(str, Enum):
    """@public"""
    SCALAR = 'SCALAR'
    BOOL = 'BOOL'


class MetricScoringType(str, Enum):
    """@public"""
    HIGHER_IS_BETTER = 'HIGHER_IS_BETTER'
    LOWER_IS_BETTER = 'LOWER_IS_BETTER'


class ModelKindFilter(str, Enum):
    """@public"""
    Embedding = 'Embedding'
    Generation = 'Generation'


class ModelOnline(str, Enum):
    """@public"""
    ONLINE = 'ONLINE'
    PENDING = 'PENDING'
    OFFLINE = 'OFFLINE'
    ERROR = 'ERROR'


class OpenAIModel(str, Enum):
    """@public"""
    GPT4O = 'GPT4O'
    GPT4O_MINI = 'GPT4O_MINI'
    GPT4 = 'GPT4'
    GPT4_TURBO = 'GPT4_TURBO'
    GPT3_5_TURBO = 'GPT3_5_TURBO'


class ProviderName(str, Enum):
    """@public"""
    OPEN_AI = 'OPEN_AI'
    MANGROVE = 'MANGROVE'
    GOOGLE = 'GOOGLE'


class SelectionTypeInput(str, Enum):
    """@public"""
    ALL = 'ALL'
    RANDOM = 'RANDOM'
    LAST = 'LAST'


class SelectionTypeOutput(str, Enum):
    """@public"""
    ALL = 'ALL'
    RANDOM = 'RANDOM'
    LAST = 'LAST'


class SortDirection(str, Enum):
    """@public"""
    ASC = 'ASC'
    DESC = 'DESC'


class TimeseriesInterval(str, Enum):
    """@public"""
    HOUR = 'HOUR'
    DAY = 'DAY'
    WEEK = 'WEEK'
    MONTH = 'MONTH'
    QUARTER = 'QUARTER'
    YEAR = 'YEAR'


class TrainingJobStatus(str, Enum):
    """@public"""
    PENDING = 'PENDING'
    RUNNING = 'RUNNING'
    COMPLETED = 'COMPLETED'
    FAILED = 'FAILED'
    CANCELED = 'CANCELED'


class TrainingMetadataInputAlignmentMethod(str, Enum):
    """@public"""
    DPO = 'DPO'
    PPO = 'PPO'


class TrainingMetadataInputTrainingType(str, Enum):
    """@public"""
    FULL_WEIGHTS = 'FULL_WEIGHTS'
    PARAMETER_EFFICIENT = 'PARAMETER_EFFICIENT'


class TrainingMetadataOutputAlignmentMethod(str, Enum):
    """@public"""
    DPO = 'DPO'
    PPO = 'PPO'
    SFT = 'SFT'


class TrainingMetadataOutputTrainingType(str, Enum):
    """@public"""
    FULL_WEIGHTS = 'FULL_WEIGHTS'
    PARAMETER_EFFICIENT = 'PARAMETER_EFFICIENT'


class UnitPosition(str, Enum):
    """@public"""
    LEFT = 'LEFT'
    RIGHT = 'RIGHT'
