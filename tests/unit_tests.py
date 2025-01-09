import unittest
import os

from adaptive_sdk import Adaptive, AsyncAdaptive

valid_mock_url = "https://www.mock.com"
mock_api_key = "mock_api_key"


class ClientParamValidation(unittest.TestCase):
    # base function to check no error is raised
    def assert_not_raises(self, func, *args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            self.fail(f"{func.__name__} raised an exception: {e}")

    def test_validate_default_use_case(self):
        client = Adaptive(valid_mock_url, mock_api_key)
        with self.assertRaises(ValueError):
            client.set_default_use_case(1)  # type: ignore
        with self.assertRaises(ValueError):
            client.set_default_use_case(None)  # type: ignore
        with self.assertRaises(ValueError):
            client.set_default_use_case("")
        with self.assertRaises(ValueError):
            client.set_default_use_case(" ")

    def test_validate_url(self):
        bad_urls = ["http:/mock.com", "https//mock"]
        for url in bad_urls:
            with self.assertRaises(ValueError):
                client = Adaptive(url, mock_api_key)

    def test_validate_api_key(self):
        if "ADAPTIVE_API_KEY" in os.environ:
            del os.environ["ADAPTIVE_API_KEY"]
        with self.assertRaises(ValueError):
            client = Adaptive(valid_mock_url)

        os.environ["ADAPTIVE_API_KEY"] = mock_api_key
        self.assert_not_raises(Adaptive, base_url=valid_mock_url)

        api_key_override = "new_api_key"
        client = Adaptive(valid_mock_url, api_key_override)
        self.assertEqual(client.api_key, api_key_override)


if __name__ == "__main__":
    unittest.main()
