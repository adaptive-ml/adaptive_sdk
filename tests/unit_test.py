from adaptive_sdk.patch import *
import os
import time

from adaptive_sdk.external.reward_client import RewardClient
from adaptive_sdk.external.reward_server import MyNoMetadataRewardServer, MyRewardServer
from adaptive_sdk.external.reward_types import Request, Turn
import httpx
import pytest
from adaptive_sdk import Adaptive
import multiprocessing as mp


valid_mock_url = "https://www.mock.com"
mock_api_key = "mock_api_key"


class TestClientParamValidation:
    # base function to check no error is raised
    def assert_not_raises(self, func, *args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            self.fail(f"{func.__name__} raised an exception: {e}")

    def test_validate_default_use_case(self):
        client = Adaptive(valid_mock_url, mock_api_key)
        with pytest.raises(ValueError):
            client.set_default_use_case(1)  # type: ignore
        with pytest.raises(ValueError):
            client.set_default_use_case(None)  # type: ignore
        with pytest.raises(ValueError):
            client.set_default_use_case("")
        with pytest.raises(ValueError):
            client.set_default_use_case(" ")

    def test_validate_url(self):
        bad_urls = ["http:/mock.com", "https//mock"]
        for url in bad_urls:
            with pytest.raises(ValueError):
                client = Adaptive(url, mock_api_key)

    def test_validate_api_key(self):
        if "ADAPTIVE_API_KEY" in os.environ:
            del os.environ["ADAPTIVE_API_KEY"]
        with pytest.raises(ValueError):
            client = Adaptive(valid_mock_url)

        os.environ["ADAPTIVE_API_KEY"] = mock_api_key
        Adaptive(base_url=valid_mock_url)

        api_key_override = "new_api_key"
        client = Adaptive(valid_mock_url, api_key_override)
        assert (
            client.api_key == api_key_override
        ), f"Expected {client.api_key}, but got {api_key_override}"


@pytest.fixture()
def scary_client():
    return RewardClient(
        base_url="http://localhost:50128",
        max_connections=32,
        timeout=5.0,
    )


@pytest.fixture()
def no_metadata_client():
    return RewardClient(
        base_url="http://localhost:50129",
        max_connections=32,
        timeout=5.0,
    )


@pytest.fixture()
def wrong_data():
    return Request(
        turns=[
            Turn(role="user", content="What is the scariest letter?"),
            Turn(role="assistant", content="The scariest letter is 'b'."),
        ],
        metadata={"a_wrong_key": "b"},
    )


@pytest.fixture()
def correct_data_list():
    return [
        Request(
            turns=[
                Turn(role="user", content="What is the scariest letter?"),
                Turn(role="assistant", content="The scariest letter is 'b'."),
            ],
            metadata={"scary_letter": "b"},
        ),
        Request(
            turns=[
                Turn(role="user", content="What is the scariest letter?"),
                Turn(role="assistant", content="The scariest letter is 'b'."),
            ],
            metadata={"scary_letter": "w"},
        ),
    ]


def run_server():
    MyRewardServer(port=50128)


def run_no_metadata_server():
    MyNoMetadataRewardServer(port=50129)


@pytest.fixture(scope="session", autouse=True)
def server():
    first_process = mp.Process(target=run_server)
    first_process.start()
    snd_process = mp.Process(target=run_no_metadata_server)
    snd_process.start()

    time.sleep(2)

    yield  # Test execution happens here

    # Teardown after all tests are done
    first_process.terminate()
    first_process.join()
    snd_process.terminate()
    snd_process.join()


@pytest.mark.asyncio
async def test_validate_metadata(
    scary_client: RewardClient, correct_data_list, wrong_data
):
    response = await scary_client.validate_metadata(correct_data_list[0].metadata)
    assert response.is_valid is True
    assert response.error_message is None

    response = await scary_client.validate_metadata(wrong_data.metadata)
    assert response.is_valid is False
    assert response.error_message is not None


@pytest.mark.asyncio
async def test_batch_validate_metadata(
    scary_client: RewardClient, correct_data_list, wrong_data
):
    response = await scary_client.batch_validate_metadata(
        [correct_data_list[0].metadata, wrong_data.metadata]
    )
    assert response.responses[0].is_valid is True
    assert response.responses[0].error_message is None

    assert response.responses[1].is_valid is False
    assert response.responses[1].error_message is not None


@pytest.mark.asyncio
async def test_score(scary_client: RewardClient, correct_data_list, wrong_data):
    response = await scary_client.score(correct_data_list[0])
    assert response.reward == 0.0

    response = await scary_client.score(correct_data_list[1])
    assert response.reward == 1.0

    with pytest.raises(httpx.HTTPStatusError):
        response = await scary_client.score(wrong_data)


@pytest.mark.asyncio
async def test_batch_score(scary_client: RewardClient, correct_data_list):
    response = await scary_client.batch_score(correct_data_list)
    assert response[0].reward == 0.0
    assert response[1].reward == 1.0


def test_blocking_batch_score(scary_client: RewardClient, correct_data_list):
    response = scary_client.blocking_batch_score(correct_data_list)
    assert response[0].reward == 0.0
    assert response[1].reward == 1.0


@pytest.mark.asyncio
async def test_score_no_metadata(no_metadata_client: RewardClient):
    request = Request(
        turns=[
            Turn(role="user", content="Hello my bot"),
            Turn(role="assistant", content="Hello"),
        ]
    )
    response = await no_metadata_client.score(request)
    assert response.reward == 5.0


@pytest.mark.asyncio
async def test_validation_of_empty_metadata(no_metadata_client: RewardClient):
    response = await no_metadata_client.validate_metadata({"key": "value"})
    assert not response.is_valid
