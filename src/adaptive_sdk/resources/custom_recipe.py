from __future__ import annotations
from typing import TYPE_CHECKING, Sequence, Any
from pathlib import Path

from .base_resource import SyncAPIResource, AsyncAPIResource, UseCaseResource
from adaptive_sdk.graphql_client import (
    CustomScriptData,
    CustomScriptFilter,
    CustomScriptCreate,
    Upload,
    CustomRecipeConfigInput,
    CustomRecipeTrainingJobInput,
)

if TYPE_CHECKING:
    from adaptive_sdk.client import Adaptive, AsyncAdaptive
import mimetypes


class CustomRecipes(SyncAPIResource, UseCaseResource):  # type: ignore[misc]
    """
    Resource to interact with custom scripts.
    """

    def __init__(self, client: Adaptive) -> None:
        SyncAPIResource.__init__(self, client)
        UseCaseResource.__init__(self, client)

    def list(self) -> Sequence[CustomScriptData]:
        filter = CustomScriptFilter()
        return self._gql_client.list_custom_scripts(filter=filter).custom_scripts

    def upload(self, file_path: str, custom_script_key: str, name: str | None = None) -> CustomScriptData:
        input = CustomScriptCreate(
            key=custom_script_key,
            name=name,
        )
        filename = Path(file_path).stem
        content_type = mimetypes.guess_type(file_path)[0] or "application/octet-stream"
        with open(file_path, "rb") as f:
            file_upload = Upload(filename=filename, content=f, content_type=content_type)
            return self._gql_client.create_custom_script(input=input, file=file_upload).create_custom_script

    def run_training_recipe(
        self,
        model: str,
        recipe_key: str,
        output_name: str,
        dataset: str | None = None,
        recipe_args: Any | None = None,
        name: str | None = None,
        wait: bool = False,
        use_case: str | None = None,
        compute_pool: str | None = None,
    ):
        config = CustomRecipeConfigInput(
            recipe=recipe_key,
            args=recipe_args,
            outputName=output_name,
            dataset=dataset,
        )
        input = CustomRecipeTrainingJobInput(
            model=model,
            useCase=self.use_case_key(use_case),
            name=name,
            config=config,
            wait=wait,
            computePool=compute_pool,
        )
        return self._gql_client.create_custom_recipe_training_job(input).create_custom_recipe_training_job


class AsyncCustomRecipes(AsyncAPIResource, UseCaseResource):  # type: ignore[misc]
    """
    Resource to interact with custom scripts.
    """

    def __init__(self, client: AsyncAdaptive) -> None:
        AsyncAPIResource.__init__(self, client)
        UseCaseResource.__init__(self, client)

    async def list(self) -> Sequence[CustomScriptData]:
        filter = CustomScriptFilter()
        return (await self._gql_client.list_custom_scripts(filter=filter)).custom_scripts

    async def upload(self, file_path: str, custom_script_key: str, name: str | None = None) -> CustomScriptData:
        input = CustomScriptCreate(
            key=custom_script_key,
            name=name,
        )
        filename = Path(file_path).stem
        content_type = mimetypes.guess_type(file_path)[0] or "application/octet-stream"
        with open(file_path, "rb") as f:
            file_upload = Upload(filename=filename, content=f, content_type=content_type)
            return (await self._gql_client.create_custom_script(input=input, file=file_upload)).create_custom_script

    async def run_training_recipe(
        self,
        model: str,
        recipe_key: str,
        output_name: str,
        dataset: str | None = None,
        recipe_args: Any | None = None,
        name: str | None = None,
        wait: bool = False,
        use_case: str | None = None,
        compute_pool: str | None = None,
    ):
        config = CustomRecipeConfigInput(
            recipe=recipe_key,
            args=recipe_args,
            outputName=output_name,
            dataset=dataset,
        )
        input = CustomRecipeTrainingJobInput(
            model=model,
            useCase=self.use_case_key(use_case),
            name=name,
            config=config,
            wait=wait,
            computePool=compute_pool,
        )
        return (await self._gql_client.create_custom_recipe_training_job(input)).create_custom_recipe_training_job
