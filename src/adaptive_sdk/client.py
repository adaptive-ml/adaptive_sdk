from .base_client import BaseSyncClient, BaseAsyncClient
from . import resources


class Adaptive(BaseSyncClient):
    def __init__(self, use_case: str, base_url: str, api_key: str | None = None) -> None:
        """
        Instantiates a new synchronous Adaptive client bounded to a use case.

        Args:
            use_case (str): A unique use case key; the client is bounded to this use case.
            base_url (str): The base URL for the Adaptive API.
            api_key (str, optional): API key for authentication.
                Defaults to None, in which use environment variable `ADAPTIVE_KEY` needs to be set.

        """
        super().__init__(base_url, api_key)
        self._use_case_key = use_case

        self.ab_tests: resources.ABTests = resources.ABTests(self, self._use_case_key)
        self.chat: resources.Chat = resources.Chat(self, self._use_case_key)
        self.completions: resources.Completions = resources.Completions(self, self._use_case_key)
        self.datasets: resources.Datasets = resources.Datasets(self, self._use_case_key)
        self.embeddings: resources.Embeddings = resources.Embeddings(self, self._use_case_key)
        self.evaluation: resources.Evaluation = resources.Evaluation(self, self._use_case_key)
        self.feedback: resources.Feedback = resources.Feedback(self, self._use_case_key)
        self.interactions: resources.Interactions = resources.Interactions(self, self._use_case_key)
        self.models: resources.Models = resources.Models(self, self._use_case_key)
        self.training: resources.Training = resources.Training(self, self._use_case_key)
        self.use_case: resources.UseCase = resources.UseCase(self, self._use_case_key)


class AdaptiveAdmin(BaseSyncClient):
    def __init__(self, base_url: str, api_key: str | None = None) -> None:
        """
        Instantiates a new synchronous AdaptiveAdmin client.

        Args:
            base_url (str): The base URL for the Adaptive API.
            api_key (str, optional): API key for authentication.
                Defaults to None, in which use environment variable `ADAPTIVE_KEY` needs to be set.

        """
        super().__init__(base_url, api_key)

        self.evaluation: resources.EvaluationAdmin = resources.EvaluationAdmin(self)
        self.feedback: resources.FeedbackAdmin = resources.FeedbackAdmin(self)
        self.models: resources.ModelsAdmin = resources.ModelsAdmin(self)
        self.training: resources.TrainingAdmin = resources.TrainingAdmin(self)
        self.use_cases: resources.UseCasesAdmin = resources.UseCasesAdmin(self)

    def with_use_case(self, use_case: str) -> Adaptive:
        """
        Convert admin client to use case-bounded client.

        Args:
            use_case (str): Use case key.
        """
        return Adaptive(use_case, self.base_url, self.api_key)


class AsyncAdaptive(BaseAsyncClient):
    def __init__(self, use_case: str, base_url: str, api_key: str | None = None) -> None:
        """
        Instantiates a new asynchronous Adaptive client bounded to a use case.

        Args:
            use_case (str): A unique use case key; the client is bounded to this use case.
            base_url (str): The base URL for the Adaptive API.
            api_key (str, optional): API key for authentication.
                Defaults to None, in which use environment variable `ADAPTIVE_KEY` needs to be set.

        """
        super().__init__(base_url, api_key)
        self._use_case_key = use_case

        self.ab_tests: resources.AsyncABTests = resources.AsyncABTests(self, self._use_case_key)  # hey
        self.chat: resources.AsyncChat = resources.AsyncChat(self, self._use_case_key)
        self.completions: resources.AsyncCompletions = resources.AsyncCompletions(self, self._use_case_key)
        self.datasets: resources.AsyncDatasets = resources.AsyncDatasets(self, self._use_case_key)
        self.embeddings: resources.AsyncEmbeddings = resources.AsyncEmbeddings(self, self._use_case_key)
        self.evaluation: resources.AsyncEvaluation = resources.AsyncEvaluation(self, self._use_case_key)
        self.feedback: resources.AsyncFeedback = resources.AsyncFeedback(self, self._use_case_key)
        self.interactions: resources.AsyncInteractions = resources.AsyncInteractions(self, self._use_case_key)
        self.models: resources.AsyncModels = resources.AsyncModels(self, self._use_case_key)
        self.training: resources.AsyncTraining = resources.AsyncTraining(self, self._use_case_key)
        self.use_case: resources.AsyncUseCase = resources.AsyncUseCase(self, self._use_case_key)


class AsyncAdaptiveAdmin(BaseAsyncClient):
    def __init__(self, base_url: str, api_key: str | None = None) -> None:
        """
        Instantiates a new asynchronous AdaptiveAdmin client.

        Args:
            base_url (str): The base URL for the Adaptive API.
            api_key (str, optional): API key for authentication.
                Defaults to None, in which use environment variable `ADAPTIVE_KEY` needs to be set.

        """
        super().__init__(base_url, api_key)

        self.evaluation: resources.AsyncEvaluationAdmin = resources.AsyncEvaluationAdmin(self)
        self.feedback: resources.AsyncFeedbackAdmin = resources.AsyncFeedbackAdmin(self)
        self.models: resources.AsyncModelsAdmin = resources.AsyncModelsAdmin(self)
        self.training: resources.AsyncTrainingAdmin = resources.AsyncTrainingAdmin(self)
        self.use_cases: resources.AsyncUseCasesAdmin = resources.AsyncUseCasesAdmin(self)

    def with_use_case(self, use_case: str) -> AsyncAdaptive:
        """
        Convert admin client to use case-bounded client.

        Args:
            use_case (str): Use case key.
        """
        return AsyncAdaptive(use_case, self.base_url, self.api_key)
