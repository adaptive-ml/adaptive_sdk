from typing import Any, Dict, List, Optional, Tuple, Union
from graphql import (
    DocumentNode,
    NamedTypeNode,
    NameNode,
    OperationDefinitionNode,
    OperationType,
    SelectionNode,
    SelectionSetNode,
    VariableDefinitionNode,
    VariableNode,
    print_ast,
)
from .add_external_model import AddExternalModel
from .add_hf_model import AddHFModel
from .add_model import AddModel
from .async_base_client_open_telemetry import AsyncBaseClientOpenTelemetry
from .attach_model_to_use_case import AttachModelToUseCase
from .base_model import UNSET, UnsetType, Upload
from .base_operation import GraphQLField
from .cancel_ab_campaign import CancelABCampaign
from .cancel_evaluation_job import CancelEvaluationJob
from .cancel_training_job import CancelTrainingJob
from .create_ab_campaign import CreateAbCampaign
from .create_evaluation_job import CreateEvaluationJob
from .create_metric import CreateMetric
from .create_role import CreateRole
from .create_team import CreateTeam
from .create_training_job import CreateTrainingJob
from .create_use_case import CreateUseCase
from .deploy_model import DeployModel
from .describe_ab_campaign import DescribeAbCampaign
from .describe_dataset import DescribeDataset
from .describe_evaluation_job import DescribeEvaluationJob
from .describe_interaction import DescribeInteraction
from .describe_metric import DescribeMetric
from .describe_metric_admin import DescribeMetricAdmin
from .describe_model import DescribeModel
from .describe_model_admin import DescribeModelAdmin
from .describe_training_job import DescribeTrainingJob
from .describe_use_case import DescribeUseCase
from .enums import CompletionGroupBy
from .input_types import (
    AbcampaignCreate,
    AbCampaignFilter,
    AddExternalModelInput,
    AddHFModelInput,
    AddModelInput,
    AttachModel,
    CursorPageInput,
    DatasetCreate,
    EvaluationCreate,
    ListCompletionsFilterInput,
    MetricCreate,
    MetricLink,
    MetricUnlink,
    ModelFilter,
    ModelPlacementInput,
    OrderPair,
    RoleCreate,
    TeamCreate,
    TeamMemberSet,
    TrainingJobInput,
    UpdateModelService,
    UseCaseCreate,
)
from .link_metric import LinkMetric
from .list_ab_campaigns import ListAbCampaigns
from .list_compute_pools import ListComputePools
from .list_datasets import ListDatasets
from .list_evaluation_jobs import ListEvaluationJobs
from .list_grouped_interactions import ListGroupedInteractions
from .list_interactions import ListInteractions
from .list_metrics import ListMetrics
from .list_models import ListModels
from .list_partitions import ListPartitions
from .list_permissions import ListPermissions
from .list_roles import ListRoles
from .list_teams import ListTeams
from .list_training_jobs import ListTrainingJobs
from .list_use_cases import ListUseCases
from .list_users import ListUsers
from .load_dataset import LoadDataset
from .me import Me
from .terminate_model import TerminateModel
from .unlink_metric import UnlinkMetric
from .update_model import UpdateModel
from .update_user import UpdateUser


def gql(q: str) -> str:
    return q


class AsyncGQLClient(AsyncBaseClientOpenTelemetry):
    """@private"""

    async def create_metric(self, input: MetricCreate, **kwargs: Any) -> CreateMetric:
        query = gql(
            """
            mutation CreateMetric($input: MetricCreate!) {
              createMetric(input: $input) {
                ...MetricData
              }
            }

            fragment MetricData on Metric {
              id
              key
              name
              kind
              description
              scoringType
              createdAt
              hasDirectFeedbacks
              hasComparisonFeedbacks
            }
            """
        )
        variables: Dict[str, object] = {"input": input}
        response = await self.execute(
            query=query, operation_name="CreateMetric", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return CreateMetric.model_validate(data)

    async def link_metric(self, input: MetricLink, **kwargs: Any) -> LinkMetric:
        query = gql(
            """
            mutation LinkMetric($input: MetricLink!) {
              linkMetric(input: $input) {
                ...MetricWithContextData
              }
            }

            fragment MetricWithContextData on MetricWithContext {
              id
              key
              name
              kind
              description
              scoringType
              createdAt
            }
            """
        )
        variables: Dict[str, object] = {"input": input}
        response = await self.execute(
            query=query, operation_name="LinkMetric", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return LinkMetric.model_validate(data)

    async def unlink_metric(self, input: MetricUnlink, **kwargs: Any) -> UnlinkMetric:
        query = gql(
            """
            mutation UnlinkMetric($input: MetricUnlink!) {
              unlinkMetric(input: $input)
            }
            """
        )
        variables: Dict[str, object] = {"input": input}
        response = await self.execute(
            query=query, operation_name="UnlinkMetric", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return UnlinkMetric.model_validate(data)

    async def attach_model_to_use_case(
        self, input: AttachModel, **kwargs: Any
    ) -> AttachModelToUseCase:
        query = gql(
            """
            mutation AttachModelToUseCase($input: AttachModel!) {
              attachModel(input: $input) {
                ...ModelServiceData
              }
            }

            fragment ModelData on Model {
              id
              key
              name
              online
              isExternal
              providerName
              isAdapter
              isTraining
              createdAt
              kind
              size
            }

            fragment ModelServiceData on ModelService {
              id
              key
              name
              model {
                ...ModelData
                backbone {
                  ...ModelData
                }
              }
              attached
              isDefault
              desiredOnline
              createdAt
            }
            """
        )
        variables: Dict[str, object] = {"input": input}
        response = await self.execute(
            query=query,
            operation_name="AttachModelToUseCase",
            variables=variables,
            **kwargs,
        )
        data = self.get_data(response)
        return AttachModelToUseCase.model_validate(data)

    async def add_external_model(
        self, input: AddExternalModelInput, **kwargs: Any
    ) -> AddExternalModel:
        query = gql(
            """
            mutation AddExternalModel($input: AddExternalModelInput!) {
              addExternalModel(input: $input) {
                ...ModelData
              }
            }

            fragment ModelData on Model {
              id
              key
              name
              online
              isExternal
              providerName
              isAdapter
              isTraining
              createdAt
              kind
              size
            }
            """
        )
        variables: Dict[str, object] = {"input": input}
        response = await self.execute(
            query=query,
            operation_name="AddExternalModel",
            variables=variables,
            **kwargs,
        )
        data = self.get_data(response)
        return AddExternalModel.model_validate(data)

    async def add_model(self, input: AddModelInput, **kwargs: Any) -> AddModel:
        query = gql(
            """
            mutation AddModel($input: AddModelInput!) {
              addModel(input: $input) {
                ...ModelData
                backbone {
                  ...ModelData
                }
              }
            }

            fragment ModelData on Model {
              id
              key
              name
              online
              isExternal
              providerName
              isAdapter
              isTraining
              createdAt
              kind
              size
            }
            """
        )
        variables: Dict[str, object] = {"input": input}
        response = await self.execute(
            query=query, operation_name="AddModel", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return AddModel.model_validate(data)

    async def update_model(
        self, input: UpdateModelService, **kwargs: Any
    ) -> UpdateModel:
        query = gql(
            """
            mutation UpdateModel($input: UpdateModelService!) {
              updateModelService(input: $input) {
                ...ModelServiceData
              }
            }

            fragment ModelData on Model {
              id
              key
              name
              online
              isExternal
              providerName
              isAdapter
              isTraining
              createdAt
              kind
              size
            }

            fragment ModelServiceData on ModelService {
              id
              key
              name
              model {
                ...ModelData
                backbone {
                  ...ModelData
                }
              }
              attached
              isDefault
              desiredOnline
              createdAt
            }
            """
        )
        variables: Dict[str, object] = {"input": input}
        response = await self.execute(
            query=query, operation_name="UpdateModel", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return UpdateModel.model_validate(data)

    async def deploy_model(
        self,
        id_or_key: Any,
        wait: bool,
        placement: Union[Optional[ModelPlacementInput], UnsetType] = UNSET,
        **kwargs: Any,
    ) -> DeployModel:
        query = gql(
            """
            mutation DeployModel($idOrKey: IdOrKey!, $wait: Boolean!, $placement: ModelPlacementInput) {
              deployModel(idOrKey: $idOrKey, wait: $wait, placement: $placement)
            }
            """
        )
        variables: Dict[str, object] = {
            "idOrKey": id_or_key,
            "wait": wait,
            "placement": placement,
        }
        response = await self.execute(
            query=query, operation_name="DeployModel", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return DeployModel.model_validate(data)

    async def terminate_model(
        self, id_or_key: Any, force: bool, **kwargs: Any
    ) -> TerminateModel:
        query = gql(
            """
            mutation TerminateModel($idOrKey: IdOrKey!, $force: Boolean!) {
              terminateModel(idOrKey: $idOrKey, force: $force)
            }
            """
        )
        variables: Dict[str, object] = {"idOrKey": id_or_key, "force": force}
        response = await self.execute(
            query=query, operation_name="TerminateModel", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return TerminateModel.model_validate(data)

    async def create_use_case(
        self, input: UseCaseCreate, **kwargs: Any
    ) -> CreateUseCase:
        query = gql(
            """
            mutation CreateUseCase($input: UseCaseCreate!) {
              createUseCase(input: $input) {
                ...UseCaseData
              }
            }

            fragment MetricWithContextData on MetricWithContext {
              id
              key
              name
              kind
              description
              scoringType
              createdAt
            }

            fragment ModelData on Model {
              id
              key
              name
              online
              isExternal
              providerName
              isAdapter
              isTraining
              createdAt
              kind
              size
            }

            fragment ModelServiceData on ModelService {
              id
              key
              name
              model {
                ...ModelData
                backbone {
                  ...ModelData
                }
              }
              attached
              isDefault
              desiredOnline
              createdAt
            }

            fragment UseCaseData on UseCase {
              id
              key
              name
              description
              createdAt
              metrics {
                ...MetricWithContextData
              }
              modelServices {
                ...ModelServiceData
              }
            }
            """
        )
        variables: Dict[str, object] = {"input": input}
        response = await self.execute(
            query=query, operation_name="CreateUseCase", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return CreateUseCase.model_validate(data)

    async def create_ab_campaign(
        self, input: AbcampaignCreate, **kwargs: Any
    ) -> CreateAbCampaign:
        query = gql(
            """
            mutation CreateAbCampaign($input: AbcampaignCreate!) {
              createAbCampaign(input: $input) {
                ...AbCampaignCreateData
              }
            }

            fragment AbCampaignCreateData on Abcampaign {
              id
              key
              status
              beginDate
            }
            """
        )
        variables: Dict[str, object] = {"input": input}
        response = await self.execute(
            query=query,
            operation_name="CreateAbCampaign",
            variables=variables,
            **kwargs,
        )
        data = self.get_data(response)
        return CreateAbCampaign.model_validate(data)

    async def cancel_ab_campaign(self, input: Any, **kwargs: Any) -> CancelABCampaign:
        query = gql(
            """
            mutation CancelABCampaign($input: IdOrKey!) {
              cancelAbCampaign(input: $input)
            }
            """
        )
        variables: Dict[str, object] = {"input": input}
        response = await self.execute(
            query=query,
            operation_name="CancelABCampaign",
            variables=variables,
            **kwargs,
        )
        data = self.get_data(response)
        return CancelABCampaign.model_validate(data)

    async def load_dataset(
        self, input: DatasetCreate, file: Upload, **kwargs: Any
    ) -> LoadDataset:
        query = gql(
            """
            mutation LoadDataset($input: DatasetCreate!, $file: Upload!) {
              createDataset(input: $input, file: $file) {
                ...DatasetData
              }
            }

            fragment DatasetData on Dataset {
              id
              key
              name
              createdAt
              kind
              records
              metricsUsage {
                feedbackCount
                comparisonCount
                metric {
                  ...MetricData
                }
              }
            }

            fragment MetricData on Metric {
              id
              key
              name
              kind
              description
              scoringType
              createdAt
              hasDirectFeedbacks
              hasComparisonFeedbacks
            }
            """
        )
        variables: Dict[str, object] = {"input": input, "file": file}
        response = await self.execute(
            query=query, operation_name="LoadDataset", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return LoadDataset.model_validate(data)

    async def create_training_job(
        self, input: TrainingJobInput, **kwargs: Any
    ) -> CreateTrainingJob:
        query = gql(
            """
            mutation CreateTrainingJob($input: TrainingJobInput!) {
              createTrainingJob(input: $input) {
                ...TrainingJobData
              }
            }

            fragment JobStageOutputData on JobStageOutput {
              name
              status
              parent
              stageId
              info {
                __typename
                ... on TrainingJobStageOutput {
                  monitoringLink
                  totalNumSamples
                  processedNumSamples
                  checkpoints
                }
                ... on EvalJobStageOutput {
                  totalNumSamples
                  processedNumSamples
                  monitoringLink
                }
                ... on BatchInferenceJobStageOutput {
                  totalNumSamples
                  processedNumSamples
                  monitoringLink
                }
              }
              startedAt
              endedAt
            }

            fragment ListCompletionsFilterOutputData on ListCompletionsFilterOutput {
              useCase
              models
              timerange {
                from
                to
              }
              feedbacks {
                metric
              }
              labels {
                key
                value
              }
              tags
              source
            }

            fragment MetricWithContextData on MetricWithContext {
              id
              key
              name
              kind
              description
              scoringType
              createdAt
            }

            fragment ModelData on Model {
              id
              key
              name
              online
              isExternal
              providerName
              isAdapter
              isTraining
              createdAt
              kind
              size
            }

            fragment ModelServiceData on ModelService {
              id
              key
              name
              model {
                ...ModelData
                backbone {
                  ...ModelData
                }
              }
              attached
              isDefault
              desiredOnline
              createdAt
            }

            fragment TrainingConfigOutputData on TrainingConfigOutput {
              baseTrainingParams {
                learningRate
                numEpochs
                batchSize
                numValidations
              }
              trainingMetadata {
                trainingType
                alignmentMethod
                parameters {
                  __typename
                  ... on DpotrainingParamsOutput {
                    klDivCoeff
                  }
                  ... on PpotrainingParamsOutput {
                    klDivCoeff
                  }
                }
              }
              trainingObjective {
                __typename
                ... on MetricTrainingParamsOutput {
                  metricKey
                  metricMetadata {
                    ... on ScalarMetricConfigOutput {
                      threshold
                    }
                  }
                }
                ... on GuidelinesTrainingParamsOutput {
                  judgeModel
                  judgeModelPrompt {
                    name
                    description
                  }
                }
              }
            }

            fragment TrainingJobData on TrainingJob {
              id
              name
              status
              createdAt
              startedAt
              endedAt
              durationMs
              stages {
                ...JobStageOutputData
              }
              parentModel {
                ...ModelData
                backbone {
                  ...ModelData
                }
              }
              childModel {
                ...ModelData
                backbone {
                  ...ModelData
                }
              }
              useCase {
                ...UseCaseData
              }
              config {
                outputName
                sampleConfig {
                  feedbackType
                  datasource {
                    __typename
                    ... on SampleDatasourceCompletionsOutput {
                      selectionType
                      maxSamples
                      filter {
                        ...ListCompletionsFilterOutputData
                      }
                    }
                    ... on SampleDatasourceDatasetOutput {
                      datasetKey
                    }
                  }
                }
                trainingConfig {
                  ...TrainingConfigOutputData
                }
              }
              createdBy {
                id
                email
                name
              }
            }

            fragment UseCaseData on UseCase {
              id
              key
              name
              description
              createdAt
              metrics {
                ...MetricWithContextData
              }
              modelServices {
                ...ModelServiceData
              }
            }
            """
        )
        variables: Dict[str, object] = {"input": input}
        response = await self.execute(
            query=query,
            operation_name="CreateTrainingJob",
            variables=variables,
            **kwargs,
        )
        data = self.get_data(response)
        return CreateTrainingJob.model_validate(data)

    async def cancel_training_job(self, id: Any, **kwargs: Any) -> CancelTrainingJob:
        query = gql(
            """
            mutation CancelTrainingJob($id: UUID!) {
              cancelTrainingJob(id: $id)
            }
            """
        )
        variables: Dict[str, object] = {"id": id}
        response = await self.execute(
            query=query,
            operation_name="CancelTrainingJob",
            variables=variables,
            **kwargs,
        )
        data = self.get_data(response)
        return CancelTrainingJob.model_validate(data)

    async def create_evaluation_job(
        self, input: EvaluationCreate, **kwargs: Any
    ) -> CreateEvaluationJob:
        query = gql(
            """
            mutation CreateEvaluationJob($input: EvaluationCreate!) {
              createEvaluationJob(input: $input) {
                ...EvaluationJobData
              }
            }

            fragment AbCampaignReportData on AbReport {
              pValue
              variants {
                variant {
                  id
                  key
                  name
                }
                interval {
                  start
                  middle
                  end
                }
                feedbacks
                comparisons {
                  feedbacks
                  wins
                  losses
                  tiesGood
                  tiesBad
                  variant {
                    id
                    key
                    name
                  }
                }
              }
            }

            fragment DatasetData on Dataset {
              id
              key
              name
              createdAt
              kind
              records
              metricsUsage {
                feedbackCount
                comparisonCount
                metric {
                  ...MetricData
                }
              }
            }

            fragment EvaluationJobData on EvaluationJob {
              id
              name
              status
              createdAt
              startedAt
              endedAt
              durationMs
              modelServices {
                ...ModelServiceData
              }
              judge {
                ...ModelData
              }
              stages {
                ...JobStageOutputData
              }
              useCase {
                ...UseCaseData
              }
              report {
                ...AbCampaignReportData
              }
              dataset {
                ...DatasetData
              }
              createdBy {
                id
                email
                name
              }
            }

            fragment JobStageOutputData on JobStageOutput {
              name
              status
              parent
              stageId
              info {
                __typename
                ... on TrainingJobStageOutput {
                  monitoringLink
                  totalNumSamples
                  processedNumSamples
                  checkpoints
                }
                ... on EvalJobStageOutput {
                  totalNumSamples
                  processedNumSamples
                  monitoringLink
                }
                ... on BatchInferenceJobStageOutput {
                  totalNumSamples
                  processedNumSamples
                  monitoringLink
                }
              }
              startedAt
              endedAt
            }

            fragment MetricData on Metric {
              id
              key
              name
              kind
              description
              scoringType
              createdAt
              hasDirectFeedbacks
              hasComparisonFeedbacks
            }

            fragment MetricWithContextData on MetricWithContext {
              id
              key
              name
              kind
              description
              scoringType
              createdAt
            }

            fragment ModelData on Model {
              id
              key
              name
              online
              isExternal
              providerName
              isAdapter
              isTraining
              createdAt
              kind
              size
            }

            fragment ModelServiceData on ModelService {
              id
              key
              name
              model {
                ...ModelData
                backbone {
                  ...ModelData
                }
              }
              attached
              isDefault
              desiredOnline
              createdAt
            }

            fragment UseCaseData on UseCase {
              id
              key
              name
              description
              createdAt
              metrics {
                ...MetricWithContextData
              }
              modelServices {
                ...ModelServiceData
              }
            }
            """
        )
        variables: Dict[str, object] = {"input": input}
        response = await self.execute(
            query=query,
            operation_name="CreateEvaluationJob",
            variables=variables,
            **kwargs,
        )
        data = self.get_data(response)
        return CreateEvaluationJob.model_validate(data)

    async def cancel_evaluation_job(
        self, id: Any, **kwargs: Any
    ) -> CancelEvaluationJob:
        query = gql(
            """
            mutation CancelEvaluationJob($id: UUID!) {
              cancelEvaluationJob(id: $id)
            }
            """
        )
        variables: Dict[str, object] = {"id": id}
        response = await self.execute(
            query=query,
            operation_name="CancelEvaluationJob",
            variables=variables,
            **kwargs,
        )
        data = self.get_data(response)
        return CancelEvaluationJob.model_validate(data)

    async def add_hf_model(self, input: AddHFModelInput, **kwargs: Any) -> AddHFModel:
        query = gql(
            """
            mutation AddHFModel($input: AddHFModelInput!) {
              importHfModel(input: $input)
            }
            """
        )
        variables: Dict[str, object] = {"input": input}
        response = await self.execute(
            query=query, operation_name="AddHFModel", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return AddHFModel.model_validate(data)

    async def update_user(self, input: TeamMemberSet, **kwargs: Any) -> UpdateUser:
        query = gql(
            """
            mutation UpdateUser($input: TeamMemberSet!) {
              setTeamMember(input: $input) {
                user {
                  ...UserData
                }
                team {
                  id
                  key
                  name
                  createdAt
                }
                role {
                  id
                  key
                  name
                  createdAt
                  permissions
                }
              }
            }

            fragment UserData on User {
              id
              email
              name
              createdAt
              teams {
                team {
                  id
                  key
                  name
                  createdAt
                }
                role {
                  id
                  key
                  name
                  createdAt
                  permissions
                }
              }
            }
            """
        )
        variables: Dict[str, object] = {"input": input}
        response = await self.execute(
            query=query, operation_name="UpdateUser", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return UpdateUser.model_validate(data)

    async def create_role(self, input: RoleCreate, **kwargs: Any) -> CreateRole:
        query = gql(
            """
            mutation CreateRole($input: RoleCreate!) {
              createRole(input: $input) {
                id
                key
                name
                createdAt
                permissions
              }
            }
            """
        )
        variables: Dict[str, object] = {"input": input}
        response = await self.execute(
            query=query, operation_name="CreateRole", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return CreateRole.model_validate(data)

    async def create_team(self, input: TeamCreate, **kwargs: Any) -> CreateTeam:
        query = gql(
            """
            mutation CreateTeam($input: TeamCreate!) {
              createTeam(input: $input) {
                id
                key
                name
                createdAt
              }
            }
            """
        )
        variables: Dict[str, object] = {"input": input}
        response = await self.execute(
            query=query, operation_name="CreateTeam", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return CreateTeam.model_validate(data)

    async def list_datasets(self, input: Any, **kwargs: Any) -> ListDatasets:
        query = gql(
            """
            query ListDatasets($input: IdOrKey!) {
              datasets(useCase: $input) {
                ...DatasetData
              }
            }

            fragment DatasetData on Dataset {
              id
              key
              name
              createdAt
              kind
              records
              metricsUsage {
                feedbackCount
                comparisonCount
                metric {
                  ...MetricData
                }
              }
            }

            fragment MetricData on Metric {
              id
              key
              name
              kind
              description
              scoringType
              createdAt
              hasDirectFeedbacks
              hasComparisonFeedbacks
            }
            """
        )
        variables: Dict[str, object] = {"input": input}
        response = await self.execute(
            query=query, operation_name="ListDatasets", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return ListDatasets.model_validate(data)

    async def describe_dataset(self, input: Any, **kwargs: Any) -> DescribeDataset:
        query = gql(
            """
            query DescribeDataset($input: IdOrKey!) {
              dataset(idOrKey: $input) {
                ...DatasetData
              }
            }

            fragment DatasetData on Dataset {
              id
              key
              name
              createdAt
              kind
              records
              metricsUsage {
                feedbackCount
                comparisonCount
                metric {
                  ...MetricData
                }
              }
            }

            fragment MetricData on Metric {
              id
              key
              name
              kind
              description
              scoringType
              createdAt
              hasDirectFeedbacks
              hasComparisonFeedbacks
            }
            """
        )
        variables: Dict[str, object] = {"input": input}
        response = await self.execute(
            query=query, operation_name="DescribeDataset", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return DescribeDataset.model_validate(data)

    async def describe_use_case(self, input: Any, **kwargs: Any) -> DescribeUseCase:
        query = gql(
            """
            query DescribeUseCase($input: IdOrKey!) {
              useCase(idOrKey: $input) {
                ...UseCaseData
              }
            }

            fragment MetricWithContextData on MetricWithContext {
              id
              key
              name
              kind
              description
              scoringType
              createdAt
            }

            fragment ModelData on Model {
              id
              key
              name
              online
              isExternal
              providerName
              isAdapter
              isTraining
              createdAt
              kind
              size
            }

            fragment ModelServiceData on ModelService {
              id
              key
              name
              model {
                ...ModelData
                backbone {
                  ...ModelData
                }
              }
              attached
              isDefault
              desiredOnline
              createdAt
            }

            fragment UseCaseData on UseCase {
              id
              key
              name
              description
              createdAt
              metrics {
                ...MetricWithContextData
              }
              modelServices {
                ...ModelServiceData
              }
            }
            """
        )
        variables: Dict[str, object] = {"input": input}
        response = await self.execute(
            query=query, operation_name="DescribeUseCase", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return DescribeUseCase.model_validate(data)

    async def list_use_cases(self, **kwargs: Any) -> ListUseCases:
        query = gql(
            """
            query ListUseCases {
              useCases {
                ...UseCaseData
              }
            }

            fragment MetricWithContextData on MetricWithContext {
              id
              key
              name
              kind
              description
              scoringType
              createdAt
            }

            fragment ModelData on Model {
              id
              key
              name
              online
              isExternal
              providerName
              isAdapter
              isTraining
              createdAt
              kind
              size
            }

            fragment ModelServiceData on ModelService {
              id
              key
              name
              model {
                ...ModelData
                backbone {
                  ...ModelData
                }
              }
              attached
              isDefault
              desiredOnline
              createdAt
            }

            fragment UseCaseData on UseCase {
              id
              key
              name
              description
              createdAt
              metrics {
                ...MetricWithContextData
              }
              modelServices {
                ...ModelServiceData
              }
            }
            """
        )
        variables: Dict[str, object] = {}
        response = await self.execute(
            query=query, operation_name="ListUseCases", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return ListUseCases.model_validate(data)

    async def list_models(self, filter: ModelFilter, **kwargs: Any) -> ListModels:
        query = gql(
            """
            query ListModels($filter: ModelFilter! = {inStorage: null, available: null, trainable: null, kind: [Generation, Embedding], viewAll: false, online: null}) {
              models(filter: $filter) {
                ...ModelDataAdmin
                backbone {
                  ...ModelDataAdmin
                }
              }
            }

            fragment ModelDataAdmin on Model {
              id
              key
              name
              online
              useCases {
                id
                key
                name
              }
              isExternal
              providerName
              isAdapter
              isTraining
              createdAt
              kind
              size
            }
            """
        )
        variables: Dict[str, object] = {"filter": filter}
        response = await self.execute(
            query=query, operation_name="ListModels", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return ListModels.model_validate(data)

    async def describe_model_admin(
        self, input: Any, **kwargs: Any
    ) -> DescribeModelAdmin:
        query = gql(
            """
            query DescribeModelAdmin($input: IdOrKey!) {
              model(idOrKey: $input) {
                ...ModelDataAdmin
                backbone {
                  ...ModelDataAdmin
                }
              }
            }

            fragment ModelDataAdmin on Model {
              id
              key
              name
              online
              useCases {
                id
                key
                name
              }
              isExternal
              providerName
              isAdapter
              isTraining
              createdAt
              kind
              size
            }
            """
        )
        variables: Dict[str, object] = {"input": input}
        response = await self.execute(
            query=query,
            operation_name="DescribeModelAdmin",
            variables=variables,
            **kwargs,
        )
        data = self.get_data(response)
        return DescribeModelAdmin.model_validate(data)

    async def describe_model(self, input: Any, **kwargs: Any) -> DescribeModel:
        query = gql(
            """
            query DescribeModel($input: IdOrKey!) {
              model(idOrKey: $input) {
                ...ModelData
                backbone {
                  ...ModelData
                }
              }
            }

            fragment ModelData on Model {
              id
              key
              name
              online
              isExternal
              providerName
              isAdapter
              isTraining
              createdAt
              kind
              size
            }
            """
        )
        variables: Dict[str, object] = {"input": input}
        response = await self.execute(
            query=query, operation_name="DescribeModel", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return DescribeModel.model_validate(data)

    async def list_metrics(self, **kwargs: Any) -> ListMetrics:
        query = gql(
            """
            query ListMetrics {
              metrics {
                ...MetricDataAdmin
              }
            }

            fragment MetricDataAdmin on Metric {
              id
              key
              name
              kind
              description
              scoringType
              useCases {
                id
                name
                key
                description
              }
              createdAt
              hasDirectFeedbacks
              hasComparisonFeedbacks
            }
            """
        )
        variables: Dict[str, object] = {}
        response = await self.execute(
            query=query, operation_name="ListMetrics", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return ListMetrics.model_validate(data)

    async def describe_metric_admin(
        self, input: Any, **kwargs: Any
    ) -> DescribeMetricAdmin:
        query = gql(
            """
            query DescribeMetricAdmin($input: IdOrKey!) {
              metric(idOrKey: $input) {
                ...MetricDataAdmin
              }
            }

            fragment MetricDataAdmin on Metric {
              id
              key
              name
              kind
              description
              scoringType
              useCases {
                id
                name
                key
                description
              }
              createdAt
              hasDirectFeedbacks
              hasComparisonFeedbacks
            }
            """
        )
        variables: Dict[str, object] = {"input": input}
        response = await self.execute(
            query=query,
            operation_name="DescribeMetricAdmin",
            variables=variables,
            **kwargs,
        )
        data = self.get_data(response)
        return DescribeMetricAdmin.model_validate(data)

    async def describe_metric(self, input: Any, **kwargs: Any) -> DescribeMetric:
        query = gql(
            """
            query DescribeMetric($input: IdOrKey!) {
              metric(idOrKey: $input) {
                ...MetricData
              }
            }

            fragment MetricData on Metric {
              id
              key
              name
              kind
              description
              scoringType
              createdAt
              hasDirectFeedbacks
              hasComparisonFeedbacks
            }
            """
        )
        variables: Dict[str, object] = {"input": input}
        response = await self.execute(
            query=query, operation_name="DescribeMetric", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return DescribeMetric.model_validate(data)

    async def list_ab_campaigns(
        self, input: AbCampaignFilter, **kwargs: Any
    ) -> ListAbCampaigns:
        query = gql(
            """
            query ListAbCampaigns($input: AbCampaignFilter!) {
              abCampaigns(filter: $input) {
                ...AbCampaignDetailData
              }
            }

            fragment AbCampaignCreateData on Abcampaign {
              id
              key
              status
              beginDate
            }

            fragment AbCampaignDetailData on Abcampaign {
              ...AbCampaignCreateData
              feedbackType
              trafficSplit
              endDate
              metric {
                ...MetricData
              }
              useCase {
                id
                key
                name
              }
              models {
                id
                key
                name
              }
              feedbacks
              hasEnoughFeedbacks
            }

            fragment MetricData on Metric {
              id
              key
              name
              kind
              description
              scoringType
              createdAt
              hasDirectFeedbacks
              hasComparisonFeedbacks
            }
            """
        )
        variables: Dict[str, object] = {"input": input}
        response = await self.execute(
            query=query, operation_name="ListAbCampaigns", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return ListAbCampaigns.model_validate(data)

    async def describe_ab_campaign(
        self, input: Any, **kwargs: Any
    ) -> DescribeAbCampaign:
        query = gql(
            """
            query DescribeAbCampaign($input: IdOrKey!) {
              abCampaign(idOrKey: $input) {
                ...AbCampaignDetailData
                report {
                  ...AbCampaignReportData
                }
              }
            }

            fragment AbCampaignCreateData on Abcampaign {
              id
              key
              status
              beginDate
            }

            fragment AbCampaignDetailData on Abcampaign {
              ...AbCampaignCreateData
              feedbackType
              trafficSplit
              endDate
              metric {
                ...MetricData
              }
              useCase {
                id
                key
                name
              }
              models {
                id
                key
                name
              }
              feedbacks
              hasEnoughFeedbacks
            }

            fragment AbCampaignReportData on AbReport {
              pValue
              variants {
                variant {
                  id
                  key
                  name
                }
                interval {
                  start
                  middle
                  end
                }
                feedbacks
                comparisons {
                  feedbacks
                  wins
                  losses
                  tiesGood
                  tiesBad
                  variant {
                    id
                    key
                    name
                  }
                }
              }
            }

            fragment MetricData on Metric {
              id
              key
              name
              kind
              description
              scoringType
              createdAt
              hasDirectFeedbacks
              hasComparisonFeedbacks
            }
            """
        )
        variables: Dict[str, object] = {"input": input}
        response = await self.execute(
            query=query,
            operation_name="DescribeAbCampaign",
            variables=variables,
            **kwargs,
        )
        data = self.get_data(response)
        return DescribeAbCampaign.model_validate(data)

    async def list_interactions(
        self,
        filter: ListCompletionsFilterInput,
        page: CursorPageInput,
        order: Union[Optional[List[OrderPair]], UnsetType] = UNSET,
        **kwargs: Any,
    ) -> ListInteractions:
        query = gql(
            """
            query ListInteractions($filter: ListCompletionsFilterInput!, $page: CursorPageInput!, $order: [OrderPair!] = [{field: "created_at", order: DESC}]) {
              completions(filter: $filter, page: $page, order: $order) {
                totalCount
                pageInfo {
                  hasNextPage
                  endCursor
                }
                nodes {
                  ...CompletionData
                }
              }
            }

            fragment CompletionComparisonFeedbackData on Completion {
              id
              completion
              source
              model {
                id
                key
                name
              }
            }

            fragment CompletionData on Completion {
              id
              prompt
              chatMessages {
                role
                content
              }
              completion
              source
              model {
                id
                key
                name
              }
              directFeedbacks {
                id
                value
                metric {
                  ...MetricData
                }
                reason
                details
                createdAt
              }
              comparisonFeedbacks {
                id
                createdAt
                usecase {
                  id
                  key
                  name
                }
                metric {
                  id
                  key
                  name
                }
                preferedCompletion {
                  ...CompletionComparisonFeedbackData
                }
                otherCompletion {
                  ...CompletionComparisonFeedbackData
                }
              }
              labels {
                key
                value
              }
              metadata {
                parameters
                timings
                usage
                system
              }
              createdAt
            }

            fragment MetricData on Metric {
              id
              key
              name
              kind
              description
              scoringType
              createdAt
              hasDirectFeedbacks
              hasComparisonFeedbacks
            }
            """
        )
        variables: Dict[str, object] = {"filter": filter, "page": page, "order": order}
        response = await self.execute(
            query=query,
            operation_name="ListInteractions",
            variables=variables,
            **kwargs,
        )
        data = self.get_data(response)
        return ListInteractions.model_validate(data)

    async def list_grouped_interactions(
        self,
        filter: ListCompletionsFilterInput,
        group_by: CompletionGroupBy,
        page: CursorPageInput,
        order: Union[Optional[List[OrderPair]], UnsetType] = UNSET,
        **kwargs: Any,
    ) -> ListGroupedInteractions:
        query = gql(
            """
            query ListGroupedInteractions($filter: ListCompletionsFilterInput!, $groupBy: CompletionGroupBy!, $page: CursorPageInput!, $order: [OrderPair!] = [{field: "group", order: ASC}]) {
              completionsGrouped(
                groupBy: $groupBy
                filter: $filter
                page: $page
                order: $order
              ) {
                totalCount
                groupBy
                pageInfo {
                  hasNextPage
                  endCursor
                }
                nodes {
                  key
                  count
                  directFeedbacksStats {
                    metric {
                      ...MetricData
                    }
                    feedbacks
                    average
                    max
                    min
                    stddev
                    sum
                  }
                  completions(page: $page, order: [{field: "created_at", order: DESC}]) {
                    nodes {
                      ...CompletionData
                    }
                  }
                }
              }
            }

            fragment CompletionComparisonFeedbackData on Completion {
              id
              completion
              source
              model {
                id
                key
                name
              }
            }

            fragment CompletionData on Completion {
              id
              prompt
              chatMessages {
                role
                content
              }
              completion
              source
              model {
                id
                key
                name
              }
              directFeedbacks {
                id
                value
                metric {
                  ...MetricData
                }
                reason
                details
                createdAt
              }
              comparisonFeedbacks {
                id
                createdAt
                usecase {
                  id
                  key
                  name
                }
                metric {
                  id
                  key
                  name
                }
                preferedCompletion {
                  ...CompletionComparisonFeedbackData
                }
                otherCompletion {
                  ...CompletionComparisonFeedbackData
                }
              }
              labels {
                key
                value
              }
              metadata {
                parameters
                timings
                usage
                system
              }
              createdAt
            }

            fragment MetricData on Metric {
              id
              key
              name
              kind
              description
              scoringType
              createdAt
              hasDirectFeedbacks
              hasComparisonFeedbacks
            }
            """
        )
        variables: Dict[str, object] = {
            "filter": filter,
            "groupBy": group_by,
            "page": page,
            "order": order,
        }
        response = await self.execute(
            query=query,
            operation_name="ListGroupedInteractions",
            variables=variables,
            **kwargs,
        )
        data = self.get_data(response)
        return ListGroupedInteractions.model_validate(data)

    async def describe_interaction(
        self, use_case: Any, id: Any, **kwargs: Any
    ) -> DescribeInteraction:
        query = gql(
            """
            query DescribeInteraction($useCase: IdOrKey!, $id: UUID!) {
              completion(useCase: $useCase, id: $id) {
                ...CompletionData
              }
            }

            fragment CompletionComparisonFeedbackData on Completion {
              id
              completion
              source
              model {
                id
                key
                name
              }
            }

            fragment CompletionData on Completion {
              id
              prompt
              chatMessages {
                role
                content
              }
              completion
              source
              model {
                id
                key
                name
              }
              directFeedbacks {
                id
                value
                metric {
                  ...MetricData
                }
                reason
                details
                createdAt
              }
              comparisonFeedbacks {
                id
                createdAt
                usecase {
                  id
                  key
                  name
                }
                metric {
                  id
                  key
                  name
                }
                preferedCompletion {
                  ...CompletionComparisonFeedbackData
                }
                otherCompletion {
                  ...CompletionComparisonFeedbackData
                }
              }
              labels {
                key
                value
              }
              metadata {
                parameters
                timings
                usage
                system
              }
              createdAt
            }

            fragment MetricData on Metric {
              id
              key
              name
              kind
              description
              scoringType
              createdAt
              hasDirectFeedbacks
              hasComparisonFeedbacks
            }
            """
        )
        variables: Dict[str, object] = {"useCase": use_case, "id": id}
        response = await self.execute(
            query=query,
            operation_name="DescribeInteraction",
            variables=variables,
            **kwargs,
        )
        data = self.get_data(response)
        return DescribeInteraction.model_validate(data)

    async def describe_training_job(
        self, id: Any, **kwargs: Any
    ) -> DescribeTrainingJob:
        query = gql(
            """
            query DescribeTrainingJob($id: UUID!) {
              trainingJob(id: $id) {
                ...TrainingJobData
              }
            }

            fragment JobStageOutputData on JobStageOutput {
              name
              status
              parent
              stageId
              info {
                __typename
                ... on TrainingJobStageOutput {
                  monitoringLink
                  totalNumSamples
                  processedNumSamples
                  checkpoints
                }
                ... on EvalJobStageOutput {
                  totalNumSamples
                  processedNumSamples
                  monitoringLink
                }
                ... on BatchInferenceJobStageOutput {
                  totalNumSamples
                  processedNumSamples
                  monitoringLink
                }
              }
              startedAt
              endedAt
            }

            fragment ListCompletionsFilterOutputData on ListCompletionsFilterOutput {
              useCase
              models
              timerange {
                from
                to
              }
              feedbacks {
                metric
              }
              labels {
                key
                value
              }
              tags
              source
            }

            fragment MetricWithContextData on MetricWithContext {
              id
              key
              name
              kind
              description
              scoringType
              createdAt
            }

            fragment ModelData on Model {
              id
              key
              name
              online
              isExternal
              providerName
              isAdapter
              isTraining
              createdAt
              kind
              size
            }

            fragment ModelServiceData on ModelService {
              id
              key
              name
              model {
                ...ModelData
                backbone {
                  ...ModelData
                }
              }
              attached
              isDefault
              desiredOnline
              createdAt
            }

            fragment TrainingConfigOutputData on TrainingConfigOutput {
              baseTrainingParams {
                learningRate
                numEpochs
                batchSize
                numValidations
              }
              trainingMetadata {
                trainingType
                alignmentMethod
                parameters {
                  __typename
                  ... on DpotrainingParamsOutput {
                    klDivCoeff
                  }
                  ... on PpotrainingParamsOutput {
                    klDivCoeff
                  }
                }
              }
              trainingObjective {
                __typename
                ... on MetricTrainingParamsOutput {
                  metricKey
                  metricMetadata {
                    ... on ScalarMetricConfigOutput {
                      threshold
                    }
                  }
                }
                ... on GuidelinesTrainingParamsOutput {
                  judgeModel
                  judgeModelPrompt {
                    name
                    description
                  }
                }
              }
            }

            fragment TrainingJobData on TrainingJob {
              id
              name
              status
              createdAt
              startedAt
              endedAt
              durationMs
              stages {
                ...JobStageOutputData
              }
              parentModel {
                ...ModelData
                backbone {
                  ...ModelData
                }
              }
              childModel {
                ...ModelData
                backbone {
                  ...ModelData
                }
              }
              useCase {
                ...UseCaseData
              }
              config {
                outputName
                sampleConfig {
                  feedbackType
                  datasource {
                    __typename
                    ... on SampleDatasourceCompletionsOutput {
                      selectionType
                      maxSamples
                      filter {
                        ...ListCompletionsFilterOutputData
                      }
                    }
                    ... on SampleDatasourceDatasetOutput {
                      datasetKey
                    }
                  }
                }
                trainingConfig {
                  ...TrainingConfigOutputData
                }
              }
              createdBy {
                id
                email
                name
              }
            }

            fragment UseCaseData on UseCase {
              id
              key
              name
              description
              createdAt
              metrics {
                ...MetricWithContextData
              }
              modelServices {
                ...ModelServiceData
              }
            }
            """
        )
        variables: Dict[str, object] = {"id": id}
        response = await self.execute(
            query=query,
            operation_name="DescribeTrainingJob",
            variables=variables,
            **kwargs,
        )
        data = self.get_data(response)
        return DescribeTrainingJob.model_validate(data)

    async def list_training_jobs(self, **kwargs: Any) -> ListTrainingJobs:
        query = gql(
            """
            query ListTrainingJobs {
              trainingJobs {
                ...TrainingJobData
              }
            }

            fragment JobStageOutputData on JobStageOutput {
              name
              status
              parent
              stageId
              info {
                __typename
                ... on TrainingJobStageOutput {
                  monitoringLink
                  totalNumSamples
                  processedNumSamples
                  checkpoints
                }
                ... on EvalJobStageOutput {
                  totalNumSamples
                  processedNumSamples
                  monitoringLink
                }
                ... on BatchInferenceJobStageOutput {
                  totalNumSamples
                  processedNumSamples
                  monitoringLink
                }
              }
              startedAt
              endedAt
            }

            fragment ListCompletionsFilterOutputData on ListCompletionsFilterOutput {
              useCase
              models
              timerange {
                from
                to
              }
              feedbacks {
                metric
              }
              labels {
                key
                value
              }
              tags
              source
            }

            fragment MetricWithContextData on MetricWithContext {
              id
              key
              name
              kind
              description
              scoringType
              createdAt
            }

            fragment ModelData on Model {
              id
              key
              name
              online
              isExternal
              providerName
              isAdapter
              isTraining
              createdAt
              kind
              size
            }

            fragment ModelServiceData on ModelService {
              id
              key
              name
              model {
                ...ModelData
                backbone {
                  ...ModelData
                }
              }
              attached
              isDefault
              desiredOnline
              createdAt
            }

            fragment TrainingConfigOutputData on TrainingConfigOutput {
              baseTrainingParams {
                learningRate
                numEpochs
                batchSize
                numValidations
              }
              trainingMetadata {
                trainingType
                alignmentMethod
                parameters {
                  __typename
                  ... on DpotrainingParamsOutput {
                    klDivCoeff
                  }
                  ... on PpotrainingParamsOutput {
                    klDivCoeff
                  }
                }
              }
              trainingObjective {
                __typename
                ... on MetricTrainingParamsOutput {
                  metricKey
                  metricMetadata {
                    ... on ScalarMetricConfigOutput {
                      threshold
                    }
                  }
                }
                ... on GuidelinesTrainingParamsOutput {
                  judgeModel
                  judgeModelPrompt {
                    name
                    description
                  }
                }
              }
            }

            fragment TrainingJobData on TrainingJob {
              id
              name
              status
              createdAt
              startedAt
              endedAt
              durationMs
              stages {
                ...JobStageOutputData
              }
              parentModel {
                ...ModelData
                backbone {
                  ...ModelData
                }
              }
              childModel {
                ...ModelData
                backbone {
                  ...ModelData
                }
              }
              useCase {
                ...UseCaseData
              }
              config {
                outputName
                sampleConfig {
                  feedbackType
                  datasource {
                    __typename
                    ... on SampleDatasourceCompletionsOutput {
                      selectionType
                      maxSamples
                      filter {
                        ...ListCompletionsFilterOutputData
                      }
                    }
                    ... on SampleDatasourceDatasetOutput {
                      datasetKey
                    }
                  }
                }
                trainingConfig {
                  ...TrainingConfigOutputData
                }
              }
              createdBy {
                id
                email
                name
              }
            }

            fragment UseCaseData on UseCase {
              id
              key
              name
              description
              createdAt
              metrics {
                ...MetricWithContextData
              }
              modelServices {
                ...ModelServiceData
              }
            }
            """
        )
        variables: Dict[str, object] = {}
        response = await self.execute(
            query=query,
            operation_name="ListTrainingJobs",
            variables=variables,
            **kwargs,
        )
        data = self.get_data(response)
        return ListTrainingJobs.model_validate(data)

    async def describe_evaluation_job(
        self, id: Any, **kwargs: Any
    ) -> DescribeEvaluationJob:
        query = gql(
            """
            query DescribeEvaluationJob($id: UUID!) {
              evaluationJob(id: $id) {
                ...EvaluationJobData
              }
            }

            fragment AbCampaignReportData on AbReport {
              pValue
              variants {
                variant {
                  id
                  key
                  name
                }
                interval {
                  start
                  middle
                  end
                }
                feedbacks
                comparisons {
                  feedbacks
                  wins
                  losses
                  tiesGood
                  tiesBad
                  variant {
                    id
                    key
                    name
                  }
                }
              }
            }

            fragment DatasetData on Dataset {
              id
              key
              name
              createdAt
              kind
              records
              metricsUsage {
                feedbackCount
                comparisonCount
                metric {
                  ...MetricData
                }
              }
            }

            fragment EvaluationJobData on EvaluationJob {
              id
              name
              status
              createdAt
              startedAt
              endedAt
              durationMs
              modelServices {
                ...ModelServiceData
              }
              judge {
                ...ModelData
              }
              stages {
                ...JobStageOutputData
              }
              useCase {
                ...UseCaseData
              }
              report {
                ...AbCampaignReportData
              }
              dataset {
                ...DatasetData
              }
              createdBy {
                id
                email
                name
              }
            }

            fragment JobStageOutputData on JobStageOutput {
              name
              status
              parent
              stageId
              info {
                __typename
                ... on TrainingJobStageOutput {
                  monitoringLink
                  totalNumSamples
                  processedNumSamples
                  checkpoints
                }
                ... on EvalJobStageOutput {
                  totalNumSamples
                  processedNumSamples
                  monitoringLink
                }
                ... on BatchInferenceJobStageOutput {
                  totalNumSamples
                  processedNumSamples
                  monitoringLink
                }
              }
              startedAt
              endedAt
            }

            fragment MetricData on Metric {
              id
              key
              name
              kind
              description
              scoringType
              createdAt
              hasDirectFeedbacks
              hasComparisonFeedbacks
            }

            fragment MetricWithContextData on MetricWithContext {
              id
              key
              name
              kind
              description
              scoringType
              createdAt
            }

            fragment ModelData on Model {
              id
              key
              name
              online
              isExternal
              providerName
              isAdapter
              isTraining
              createdAt
              kind
              size
            }

            fragment ModelServiceData on ModelService {
              id
              key
              name
              model {
                ...ModelData
                backbone {
                  ...ModelData
                }
              }
              attached
              isDefault
              desiredOnline
              createdAt
            }

            fragment UseCaseData on UseCase {
              id
              key
              name
              description
              createdAt
              metrics {
                ...MetricWithContextData
              }
              modelServices {
                ...ModelServiceData
              }
            }
            """
        )
        variables: Dict[str, object] = {"id": id}
        response = await self.execute(
            query=query,
            operation_name="DescribeEvaluationJob",
            variables=variables,
            **kwargs,
        )
        data = self.get_data(response)
        return DescribeEvaluationJob.model_validate(data)

    async def list_evaluation_jobs(self, **kwargs: Any) -> ListEvaluationJobs:
        query = gql(
            """
            query ListEvaluationJobs {
              evaluationJobs {
                ...EvaluationJobData
              }
            }

            fragment AbCampaignReportData on AbReport {
              pValue
              variants {
                variant {
                  id
                  key
                  name
                }
                interval {
                  start
                  middle
                  end
                }
                feedbacks
                comparisons {
                  feedbacks
                  wins
                  losses
                  tiesGood
                  tiesBad
                  variant {
                    id
                    key
                    name
                  }
                }
              }
            }

            fragment DatasetData on Dataset {
              id
              key
              name
              createdAt
              kind
              records
              metricsUsage {
                feedbackCount
                comparisonCount
                metric {
                  ...MetricData
                }
              }
            }

            fragment EvaluationJobData on EvaluationJob {
              id
              name
              status
              createdAt
              startedAt
              endedAt
              durationMs
              modelServices {
                ...ModelServiceData
              }
              judge {
                ...ModelData
              }
              stages {
                ...JobStageOutputData
              }
              useCase {
                ...UseCaseData
              }
              report {
                ...AbCampaignReportData
              }
              dataset {
                ...DatasetData
              }
              createdBy {
                id
                email
                name
              }
            }

            fragment JobStageOutputData on JobStageOutput {
              name
              status
              parent
              stageId
              info {
                __typename
                ... on TrainingJobStageOutput {
                  monitoringLink
                  totalNumSamples
                  processedNumSamples
                  checkpoints
                }
                ... on EvalJobStageOutput {
                  totalNumSamples
                  processedNumSamples
                  monitoringLink
                }
                ... on BatchInferenceJobStageOutput {
                  totalNumSamples
                  processedNumSamples
                  monitoringLink
                }
              }
              startedAt
              endedAt
            }

            fragment MetricData on Metric {
              id
              key
              name
              kind
              description
              scoringType
              createdAt
              hasDirectFeedbacks
              hasComparisonFeedbacks
            }

            fragment MetricWithContextData on MetricWithContext {
              id
              key
              name
              kind
              description
              scoringType
              createdAt
            }

            fragment ModelData on Model {
              id
              key
              name
              online
              isExternal
              providerName
              isAdapter
              isTraining
              createdAt
              kind
              size
            }

            fragment ModelServiceData on ModelService {
              id
              key
              name
              model {
                ...ModelData
                backbone {
                  ...ModelData
                }
              }
              attached
              isDefault
              desiredOnline
              createdAt
            }

            fragment UseCaseData on UseCase {
              id
              key
              name
              description
              createdAt
              metrics {
                ...MetricWithContextData
              }
              modelServices {
                ...ModelServiceData
              }
            }
            """
        )
        variables: Dict[str, object] = {}
        response = await self.execute(
            query=query,
            operation_name="ListEvaluationJobs",
            variables=variables,
            **kwargs,
        )
        data = self.get_data(response)
        return ListEvaluationJobs.model_validate(data)

    async def list_users(self, **kwargs: Any) -> ListUsers:
        query = gql(
            """
            query ListUsers {
              users {
                ...UserData
              }
            }

            fragment UserData on User {
              id
              email
              name
              createdAt
              teams {
                team {
                  id
                  key
                  name
                  createdAt
                }
                role {
                  id
                  key
                  name
                  createdAt
                  permissions
                }
              }
            }
            """
        )
        variables: Dict[str, object] = {}
        response = await self.execute(
            query=query, operation_name="ListUsers", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return ListUsers.model_validate(data)

    async def me(self, **kwargs: Any) -> Me:
        query = gql(
            """
            query Me {
              me {
                ...UserData
                apiKeys {
                  key
                  createdAt
                }
              }
            }

            fragment UserData on User {
              id
              email
              name
              createdAt
              teams {
                team {
                  id
                  key
                  name
                  createdAt
                }
                role {
                  id
                  key
                  name
                  createdAt
                  permissions
                }
              }
            }
            """
        )
        variables: Dict[str, object] = {}
        response = await self.execute(
            query=query, operation_name="Me", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return Me.model_validate(data)

    async def list_teams(self, **kwargs: Any) -> ListTeams:
        query = gql(
            """
            query ListTeams {
              teams {
                id
                key
                name
                createdAt
              }
            }
            """
        )
        variables: Dict[str, object] = {}
        response = await self.execute(
            query=query, operation_name="ListTeams", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return ListTeams.model_validate(data)

    async def list_roles(self, **kwargs: Any) -> ListRoles:
        query = gql(
            """
            query ListRoles {
              roles {
                id
                key
                name
                createdAt
                permissions
              }
            }
            """
        )
        variables: Dict[str, object] = {}
        response = await self.execute(
            query=query, operation_name="ListRoles", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return ListRoles.model_validate(data)

    async def list_permissions(self, **kwargs: Any) -> ListPermissions:
        query = gql(
            """
            query ListPermissions {
              permissions
            }
            """
        )
        variables: Dict[str, object] = {}
        response = await self.execute(
            query=query, operation_name="ListPermissions", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return ListPermissions.model_validate(data)

    async def list_partitions(self, **kwargs: Any) -> ListPartitions:
        query = gql(
            """
            query ListPartitions {
              partitions {
                ...PartitionData
              }
            }

            fragment ModelData on Model {
              id
              key
              name
              online
              isExternal
              providerName
              isAdapter
              isTraining
              createdAt
              kind
              size
            }

            fragment PartitionData on Partition {
              id
              key
              computePool {
                key
                name
              }
              status
              url
              worldSize
              gpuTypes
              createdAt
              onlineModels {
                ...ModelData
              }
            }
            """
        )
        variables: Dict[str, object] = {}
        response = await self.execute(
            query=query, operation_name="ListPartitions", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return ListPartitions.model_validate(data)

    async def list_compute_pools(self, **kwargs: Any) -> ListComputePools:
        query = gql(
            """
            query ListComputePools {
              computePools {
                key
                name
                capabilities
                partitions {
                  ...PartitionData
                }
              }
            }

            fragment ModelData on Model {
              id
              key
              name
              online
              isExternal
              providerName
              isAdapter
              isTraining
              createdAt
              kind
              size
            }

            fragment PartitionData on Partition {
              id
              key
              computePool {
                key
                name
              }
              status
              url
              worldSize
              gpuTypes
              createdAt
              onlineModels {
                ...ModelData
              }
            }
            """
        )
        variables: Dict[str, object] = {}
        response = await self.execute(
            query=query,
            operation_name="ListComputePools",
            variables=variables,
            **kwargs,
        )
        data = self.get_data(response)
        return ListComputePools.model_validate(data)

    async def execute_custom_operation(
        self, *fields: GraphQLField, operation_type: OperationType, operation_name: str
    ) -> Dict[str, Any]:
        selections = self._build_selection_set(fields)
        combined_variables = self._combine_variables(fields)
        variable_definitions = self._build_variable_definitions(
            combined_variables["types"]
        )
        operation_ast = self._build_operation_ast(
            selections, operation_type, operation_name, variable_definitions
        )
        response = await self.execute(
            print_ast(operation_ast),
            variables=combined_variables["values"],
            operation_name=operation_name,
        )
        return self.get_data(response)

    def _combine_variables(
        self, fields: Tuple[GraphQLField, ...]
    ) -> Dict[str, Dict[str, Any]]:
        variables_types_combined = {}
        processed_variables_combined = {}
        for field in fields:
            formatted_variables = field.get_formatted_variables()
            variables_types_combined.update(
                {k: v["type"] for k, v in formatted_variables.items()}
            )
            processed_variables_combined.update(
                {k: v["value"] for k, v in formatted_variables.items()}
            )
        return {
            "types": variables_types_combined,
            "values": processed_variables_combined,
        }

    def _build_variable_definitions(
        self, variables_types_combined: Dict[str, str]
    ) -> List[VariableDefinitionNode]:
        return [
            VariableDefinitionNode(
                variable=VariableNode(name=NameNode(value=var_name)),
                type=NamedTypeNode(name=NameNode(value=var_value)),
            )
            for var_name, var_value in variables_types_combined.items()
        ]

    def _build_operation_ast(
        self,
        selections: List[SelectionNode],
        operation_type: OperationType,
        operation_name: str,
        variable_definitions: List[VariableDefinitionNode],
    ) -> DocumentNode:
        return DocumentNode(
            definitions=[
                OperationDefinitionNode(
                    operation=operation_type,
                    name=NameNode(value=operation_name),
                    variable_definitions=variable_definitions,
                    selection_set=SelectionSetNode(selections=selections),
                )
            ]
        )

    def _build_selection_set(
        self, fields: Tuple[GraphQLField, ...]
    ) -> List[SelectionNode]:
        return [field.to_ast(idx) for idx, field in enumerate(fields)]

    async def query(self, *fields: GraphQLField, operation_name: str) -> Dict[str, Any]:
        return await self.execute_custom_operation(
            *fields, operation_type=OperationType.QUERY, operation_name=operation_name
        )

    async def mutation(
        self, *fields: GraphQLField, operation_name: str
    ) -> Dict[str, Any]:
        return await self.execute_custom_operation(
            *fields,
            operation_type=OperationType.MUTATION,
            operation_name=operation_name,
        )
