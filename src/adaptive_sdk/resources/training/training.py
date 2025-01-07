from adaptive_sdk.base_client import BaseAsyncClient, BaseSyncClient
from .jobs import TrainingJobs, AsyncTrainingJobs, TrainingJobsAdmin, AsyncTrainingJobsAdmin
from ..base_resource import SyncAPIResource, AsyncAPIResource


class Training(SyncAPIResource):
    def __init__(self, client: BaseSyncClient, use_case_key: str) -> None:
        super().__init__(client)
        self._use_case_key = use_case_key
        self.jobs = TrainingJobs(self._client, self._use_case_key)


class TrainingAdmin(SyncAPIResource):
    def __init__(self, client: BaseSyncClient) -> None:
        super().__init__(client)
        self.jobs = TrainingJobsAdmin(self._client)


class AsyncTraining(AsyncAPIResource):
    def __init__(self, client: BaseAsyncClient, use_case_key: str) -> None:
        super().__init__(client)
        self._use_case_key = use_case_key
        self.jobs = AsyncTrainingJobs(self._client, self._use_case_key)


class AsyncTrainingAdmin(AsyncAPIResource):
    def __init__(self, client: BaseAsyncClient) -> None:
        super().__init__(client)
        self.jobs = AsyncTrainingJobsAdmin(self._client)
