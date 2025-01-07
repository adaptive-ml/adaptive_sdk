from copy import deepcopy
from adaptive_sdk import input_types

default_sample_config = {"selection_type": "ALL"}

default_base_training_params = {
    "learning_rate": 0.00001,
    "batch_size": 32,
    "num_epochs": 1,
    "num_validations": 10,
}

default_training_metadata = {
    "training_type": "PARAMETER_EFFICIENT",
    "alignment_method": "PPO",
    "parameters": {"ppo": {"kl_div_coeff": 0.01}},
}


def update_training_config_with_defaults(config: input_types.AdaptRequestConfigInput):
    new_config = deepcopy(config)

    if "training_config" not in new_config:
        raise ValueError("config is missing a `training_config`")

    if "sample_config" not in new_config:
        new_config["sample_config"] = {}  # type:ignore

    if "base_training_params" not in new_config["training_config"]:
        new_config["training_config"]["base_training_params"] = {}  # type:ignore

    if "training_metadata" not in new_config["training_config"]:
        new_config["training_config"]["training_metadata"] = {}  # type:ignore

    new_config["sample_config"] = {  # type:ignore
        **default_sample_config,
        **new_config["sample_config"],
    }

    new_config["training_config"]["base_training_params"] = {  # type:ignore
        **default_base_training_params,
        **new_config["training_config"]["base_training_params"],
    }

    new_config["training_config"]["training_metadata"] = {  # type:ignore
        **default_training_metadata,
        **new_config["training_config"]["training_metadata"],
    }

    if new_config["training_config"]["training_metadata"]["alignment_method"] == "DPO":
        new_config["training_config"]["training_metadata"]["parameters"]["dpo"] = new_config["training_config"][  # type: ignore
            "training_metadata"
        ][
            "parameters"
        ][
            "ppo"
        ]
        del new_config["training_config"]["training_metadata"]["parameters"]["ppo"]  # type: ignore

    return new_config
