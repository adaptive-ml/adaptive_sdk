import asyncio
from adaptive_sdk import Adaptive, AsyncAdaptive, AdaptiveAdmin

from typing import Any, Dict, Type, Union, get_type_hints, List, TypedDict
from pydantic import BaseModel


def test_sync_client(
    addr: str, api_key: str, use_case_input: tuple[str, str], metric_input: tuple[str, str], model_key: str
):

    use_case_name = use_case_input[0]
    use_case_key = use_case_input[1]
    metric_name = metric[0]
    metric_key = metric[1]

    client = Adaptive(use_case_key, addr, api_key)
    admin_client = AdaptiveAdmin(addr, api_key)

    try:
        use_case = admin_client.use_cases.create(name=use_case_name, key=use_case_key)
        print(f"Use case created id={use_case.id} key={use_case.key}")
    except:
        use_case = client.use_case.get()

    if use_case is None:
        raise Exception("Could not get or create a use case")
    else:
        print(f"Use case retrieved id={use_case.id} key={use_case.key}")

    metrics = admin_client.feedback.list_keys()
    if not any(metric.key == metric_key for metric in metrics):
        response = admin_client.feedback.register_key(key=metric_key, kind="bool")
        print(f"created metric with id {response.id}")
    response = client.feedback.link(feedback_key=metric_key)
    print(f"Linked metric")

    model_attached = any(srv.model.key == model_key for srv in use_case.model_services)
    if not model_attached:
        response = client.models.attach(model=model_key, wait=False)
        print(f"Attached model {model_key}")

    response = client.interactions.create(
        model=model_key,
        messages=[{"role": "user", "content": "Hello"}],
        completion="Goodbye",
        feedbacks=[{"feedback_key": metric_key, "value": 0, "details": "This was bad"}],
        labels={"country": "Argentina"},
    )
    print(f"Interaction stored completion_id={response.completion_id}")

    # Add feedback after completion is stored
    client.feedback.log_metric(
        value=True, completion_id=response.completion_id, feedback_key=metric_key, details="I messed up it is good"
    )

    # Chat test
    response = client.chat.create(
        model=use_case.key,
        messages=[{"role": "user", "content": "Hello from SDK"}],
        labels={"country": "Spain"},
    )
    print(f"Chat response is:\n{response.choices[0].message.content}\n*****\n")

    # Completions test
    response = client.completions.create(prompt="Hello completion", model=use_case.key)
    print(f"Completion response:\n{response.choices[0].text}")

    # Streaming chat test
    stream_response = client.chat.create(
        model=use_case.key, messages=[{"role": "user", "content": "Hello from SDK"}], stream=True
    )

    print("Streaming response: ", end="", flush=True)
    for chunk in stream_response:
        if chunk.choices:
            content = chunk.choices[0].delta.content
            print(content, end="", flush=True)
    print()


async def test_async_client(
    addr: str, api_key: str, use_case_input: tuple[str, str], metric_input: tuple[str, str], model_key: str
):
    aclient = AsyncAdaptive(addr, api_key)

    use_case_name = use_case_input[0]
    use_case_key = use_case_input[1]
    metric_name = metric[0]
    metric_key = metric[1]

    # Async chat test
    response = await aclient.chat.create(model=use_case_key, messages=[{"role": "user", "content": "Hello from SDK"}])
    print(f"Async chat response: {response.choices[0].message.content}\n*****\n")  # type: ignore

    # Async streaming chat test
    stream_response = aclient.chat.create(
        model=use_case_key, messages=[{"role": "user", "content": "Hello from SDK"}], stream=True
    )

    print("Async chat streaming response: ", end="", flush=True)
    async for chunk in await stream_response:  # type: ignore
        if chunk.choices:
            content = chunk.choices[0].delta.content
            print(content, end="", flush=True)
    print("\n*****\n")

    # Async completions test
    response = await aclient.completions.create(model=use_case_key, prompt="Hello from SDK")
    print(f"Async completions response: {response.choices[0].text}\n*****\n")


if __name__ == "__main__":

    addr = "your_adaptive_url"
    api_key = "your_api_key"

    use_case = ("Test Use Case", "test-use-case")
    metric = ("Test metric", "test-metric")
    model_key = "minimal"

    # test_sync_client(addr, api_key, use_case, metric, model_key)
    asyncio.run(test_async_client(addr, api_key, use_case, metric, model_key))
