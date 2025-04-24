import functools
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)


def log_function_name(func):
    """Decorator to log the function name when called."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logging.warning(f"Calling function: {func.__name__}")
        return func(*args, **kwargs)

    return wrapper


from adaptive_sdk import Adaptive
from adaptive_sdk.input_types import AdaptRequestConfigInput
from adaptive_sdk.graphql_client.enums import TrainingJobStatus
import os
import time


def get_run_id():
    return os.getenv("GITHUB_RUN_ID", "")


def run_training_job(
    use_case: str,
    model: str,
    dataset_key: str,
    dataset_file: str,
    compute_pool: str,
    config: AdaptRequestConfigInput,
    create_use_case: bool = True
):
    base_url = os.getenv("TESTING_ADAPTIVE_BASE_URL")
    api_key = os.getenv("TESTING_ADAPTIVE_API_KEY")
    cf_access_client_id = os.getenv("CF_ACCESS_CLIENT_ID")
    cf_access_client_secret = os.getenv("CF_ACCESS_CLIENT_SECRET")

    print(f"Running training test -- use case url: {base_url}/usecases/{use_case}")
    print(f"Training with config:{config}")

    assert base_url
    assert api_key

    client = Adaptive(
        base_url=base_url,
        api_key=api_key,
        default_headers=(
            {
                "CF-Access-Client-Id": cf_access_client_id,
                "CF-Access-Client-Secret": cf_access_client_secret,
            }
            if cf_access_client_id and cf_access_client_secret
            else None
        ),
    )

    if create_use_case:
        print(f"Creating usecase {use_case}")
        client.use_cases.create(
            key=use_case, name=use_case, description="A use case for training e2e tests"
        )

    client.set_default_use_case(use_case)

    if client.datasets.get(dataset_key) is None:
        print(f"Uploading dataset {dataset_file} into key {dataset_key}")
        new_ds = client.datasets.upload(
            file_path=f"./tests/integration_data/{dataset_file}",
            dataset_key=dataset_key,
        )

    print(f"Attaching model {model}")
    client.models.attach(
        model=model, wait=True, placement={"compute_pools": [compute_pool]}
    )

    training_job = client.training.jobs.create(
        model=model, config=config, wait=True, compute_pool=compute_pool
    )
    assert training_job

    job_id = training_job.id
    url_link = f"{base_url}/usecases/{use_case}/trainings/{job_id}"

    while True:
        job = client.training.jobs.get(job_id)
        if job.status == TrainingJobStatus.CANCELED:
            raise ValueError(
                f"Training job [{job_id}] has been cancelled. See {url_link}"
            )
        if job.status == TrainingJobStatus.FAILED:
            raise ValueError(
                f"Failed training job [{job_id}]. To check job status go to: {url_link}"
            )

        if job.status == TrainingJobStatus.COMPLETED:
            print(f"Training job [{job_id}] done with success")
            break

        print(f"Awaiting for job [{job_id}] completion")
        time.sleep(60 * 3)
