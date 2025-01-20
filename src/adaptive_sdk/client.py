from .base_client import BaseSyncClient, BaseAsyncClient, UseCaseClient
from . import resources


class Adaptive(BaseSyncClient, UseCaseClient):
    def __init__(self, base_url: str, api_key: str | None = None) -> None:
        """
        Instantiates a new synchronous Adaptive client bounded to a use case.

        Args:
            use_case (str): A unique use case key; the client is bounded to this use case.
            base_url (str): The base URL for the Adaptive API.
            api_key (str, optional): API key for authentication.
                Defaults to None, in which use environment variable `ADAPTIVE_KEY` needs to be set.

        """
        super().__init__(base_url, api_key)
        self.__use_case_key = None

        self.ab_tests: resources.ABTests = resources.ABTests(self)
        self.chat: resources.Chat = resources.Chat(self)
        self.completions: resources.Completions = resources.Completions(self)
        self.datasets: resources.Datasets = resources.Datasets(self)
        self.embeddings: resources.Embeddings = resources.Embeddings(self)
        self.evaluation: resources.Evaluation = resources.Evaluation(self)
        self.feedback: resources.Feedback = resources.Feedback(self)
        self.interactions: resources.Interactions = resources.Interactions(self)
        self.models: resources.Models = resources.Models(self)
        self.training: resources.Training = resources.Training(self)
        self.use_cases: resources.UseCase = resources.UseCase(self)
        self.users: resources.Users = resources.Users(self)

    @property
    def default_use_case(self) -> str | None:
        """
        Get the current default use case key.
        """
        return self.__use_case_key

    def set_default_use_case(self, use_case: str) -> None:
        """
        Set a default use case key to be used for use case-specific operations.
        """
        if not (isinstance(use_case, str) and bool(use_case.strip())):
            raise ValueError("use_case must be a non-empty string")
        self.__use_case_key = use_case


class AsyncAdaptive(BaseAsyncClient, UseCaseClient):
    def __init__(self, base_url: str, api_key: str | None = None) -> None:
        """
        Instantiates a new asynchronous Adaptive client bounded to a use case.

        Args:
            use_case (str): A unique use case key; the client is bounded to this use case.
            base_url (str): The base URL for the Adaptive API.
            api_key (str, optional): API key for authentication.
                Defaults to None, in which use environment variable `ADAPTIVE_KEY` needs to be set.

        """
        super().__init__(base_url, api_key)
        self.__use_case_key = None

        self.ab_tests: resources.AsyncABTests = resources.AsyncABTests(self)
        self.chat: resources.AsyncChat = resources.AsyncChat(self)
        self.completions: resources.AsyncCompletions = resources.AsyncCompletions(self)
        self.datasets: resources.AsyncDatasets = resources.AsyncDatasets(self)
        self.embeddings: resources.AsyncEmbeddings = resources.AsyncEmbeddings(self)
        self.evaluation: resources.AsyncEvaluation = resources.AsyncEvaluation(self)
        self.feedback: resources.AsyncFeedback = resources.AsyncFeedback(self)
        self.interactions: resources.AsyncInteractions = resources.AsyncInteractions(self)
        self.models: resources.AsyncModels = resources.AsyncModels(self)
        self.training: resources.AsyncTraining = resources.AsyncTraining(self)
        self.use_cases: resources.AsyncUseCase = resources.AsyncUseCase(self)
        self.users: resources.AsyncUsers = resources.AsyncUsers(self)

    @property
    def default_use_case(self) -> str | None:
        """
        Get the current default use case key.
        """
        return self.__use_case_key

    def set_default_use_case(self, use_case: str) -> None:
        """
        Set a default use case key to be used for use case-specific operations.
        """
        if not isinstance(use_case, str):
            raise TypeError("use_case must be a string")
        if not use_case.strip():
            raise ValueError("use_case cannot be empty or whitespace")
        self.__use_case_key = use_case
