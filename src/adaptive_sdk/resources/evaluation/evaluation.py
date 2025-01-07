from adaptive_sdk.base_client import BaseAsyncClient, BaseSyncClient
from .jobs import EvalJobs, EvalJobsAdmin, AsyncEvalJobs, AsyncEvalJobsAdmin
from ..base_resource import SyncAPIResource, AsyncAPIResource


class Evaluation(SyncAPIResource):
    def __init__(self, client: BaseSyncClient, use_case_key: str) -> None:
        super().__init__(client)
        self._use_case_key = use_case_key
        self.jobs = EvalJobs(self._client, self._use_case_key)


class EvaluationAdmin(SyncAPIResource):
    def __init__(self, client: BaseSyncClient) -> None:
        super().__init__(client)
        self.jobs = EvalJobsAdmin(self._client)


class AsyncEvaluation(AsyncAPIResource):
    def __init__(self, client: BaseAsyncClient, use_case_key: str) -> None:
        super().__init__(client)
        self._use_case_key = use_case_key
        self.jobs = AsyncEvalJobs(self._client, self._use_case_key)


class AsyncEvaluationAdmin(AsyncAPIResource):
    def __init__(self, client: BaseAsyncClient) -> None:
        super().__init__(client)
        self.jobs = AsyncEvalJobsAdmin(self._client)
