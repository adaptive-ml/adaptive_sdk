# adaptive-sdk

The Python Client SDK for Adaptive Engine

## Installation
```
git clone https://github.com/adaptive-ml/adaptive_sdk.git
cd adaptive_sdk
pip install .

```

## Usage

Please refer to the public SDK [documentation](https://docs.adaptive-ml.com/introduction) and [reference](https://docs.adaptive-ml.com/sdk-reference/reference) for detailed usage instructions and examples.


Basic clients instantiation:
```python
from adaptive_sdk import Adaptive
# Similar async client is available AsyncAdaptive

# Adaptive client
client = AdaptiveAdmin(base_url="YOUR_ADAPTIVE_URL", api_key="ADAPTIVE_API_KEY")
client.set_default_use_case("my_use_case_key")  # Set default use case for client
```

