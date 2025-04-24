from .utils import get_run_id, run_training_job
import os
from adaptive_sdk.input_types import AdaptRequestConfigInput

suffix = get_run_id()
dataset_key = f"scaryLetter.dataset.jsonl-{suffix}"
model = "llama_3.1_8b_instruct"

ppo_config = AdaptRequestConfigInput = {
    "output_name": f"RLEF training from GH run [{suffix}]",
    "training_config": {
        "base_training_params": {
            "learning_rate": 1e-5,
            "num_epochs": 1,
            "batch_size": 32,
            "num_validations": 10,
        },
        "training_metadata": {
            "training_type": "PARAMETER_EFFICIENT",  # "FULL_WEIGHTS"
            "alignment_method": "PPO",
            "parameters": {
                "ppo": {
                    "kl_div_coeff": 0.01,
                }
            },
        },
        "training_objective": {
            "reward_server": {
                "remote_env": "testing-reward-server"
            }
        },
    },
    "sample_config": {
        "datasource": {"dataset": {"dataset": dataset_key}},
    },
}

run_training_job(
    use_case="reward-server-tests",
    model=model,
    dataset_key=dataset_key,
    dataset_file="scaryLetter.dataset.jsonl",
    compute_pool="default",
    config=ppo_config,
    create_use_case=False
)
