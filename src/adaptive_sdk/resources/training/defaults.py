from copy import deepcopy
from loguru import logger
from pprint import pformat

from adaptive_sdk import input_types

default_sample_config = {"datasource": {"completions": {"selection_type": "ALL"}}}

default_base_training_params = {
    "learning_rate": 0.00001,
    "batch_size": 32,
    "num_epochs": 1,
    "num_validations": 10,
}

default_training_metadata = {"training_type": "PARAMETER_EFFICIENT", "alignment_method": "PPO"}


def update_training_config_with_defaults(config: input_types.AdaptRequestConfigInput):
    new_config = deepcopy(config)

    if "training_config" not in new_config:
        raise ValueError("config is missing a `training_config`")
    else:
        if "training_objective" not in new_config["training_config"]:
            raise ValueError("`training_config` is missing a `training_objective`")

    if "sample_config" not in new_config:
        new_config["sample_config"] = {}  # type: ignore
        logger.info(f"Did not specify `sample_config`, using default: \n{pformat(default_sample_config)}")

    if "base_training_params" not in new_config["training_config"]:
        new_config["training_config"]["base_training_params"] = {}  # type: ignore
        logger.info(
            f"Did not specify `training_config.base_training_params`, using default: \n{pformat(default_base_training_params)}"
        )

    if "training_metadata" not in new_config["training_config"]:
        new_config["training_config"]["training_metadata"] = {}  # type: ignore
        logger.info(
            f"Did not specify `training_config.training_metadata`, using default: \n{pformat(default_training_metadata)}"
        )

    new_config["sample_config"] = {  # type: ignore[typeddict-item]
        **deepcopy(default_sample_config),  # type: ignore[typeddict-item]
        **new_config["sample_config"],  # type: ignore[typeddict-item]
    }

    new_config["training_config"]["base_training_params"] = {  # type: ignore[typeddict-item]
        **deepcopy(default_base_training_params),  # type: ignore[typeddict-item]#
        **new_config["training_config"]["base_training_params"],  # type: ignore[typeddict-item]
    }

    new_config["training_config"]["training_metadata"] = {  # type: ignore[typeddict-item]
        **deepcopy(default_training_metadata),  # type: ignore[typeddict-item]
        **new_config["training_config"]["training_metadata"],  # type: ignore[typeddict-item]
    }

    return new_config
