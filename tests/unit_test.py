import os
import pytest
from adaptive_sdk import Adaptive

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
        assert client.api_key == api_key_override, f"Expected {client.api_key}, but got {api_key_override}"
