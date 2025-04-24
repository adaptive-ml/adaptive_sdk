from .utils import get_run_id, run_training_job
import os
from adaptive_sdk.input_types import AdaptRequestConfigInput

suffix = get_run_id()
dataset_key = f"hh-preference-training-200-{suffix}"
model = "llama_3.1_8b_instruct"

ppo_config = AdaptRequestConfigInput = {
    "output_name": "my-output-model-v0",
    "training_config": {
        "base_training_params": {
            "learning_rate": 1e-5,
            "num_epochs": 1,
            "batch_size": 32,
            "num_validations": 10,
        },
        "training_metadata": {
            "training_type": "PARAMETER_EFFICIENT",  # "FULL_WEIGHTS"
            "alignment_method": "PPO",  # "DPO" "SFT" "PPO"
            "parameters": {
                "dpo": {  # this depends on the alignment method
                    "kl_div_coeff": 0.01,
                }
            },
        },
        "training_objective": {
            "metric": {  # preference criteria from the dataset
                "metric_key": "helpfulness",
            }
        },
    },
    "sample_config": {
        "feedback_type": "PREFERENCE",
        "datasource": {"dataset": {"dataset": dataset_key}},
    },
}

run_training_job(
    use_case=f"e2e-training-usecase{suffix}",
    model=model,
    dataset_key=dataset_key,
    dataset_file="hh-preference-training-200.jsonl",
    compute_pool="default",
    config=ppo_config,
)
