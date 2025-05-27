from .utils import get_run_id, run_training_job

suffix = get_run_id()
dataset_key = f"scaryLetter.dataset.jsonl-{suffix}"
model = "llama_3.1_8b_instruct"
output_model_name = f"RLEF training from GH run [{suffix}]"

run_training_job(
    use_case="reward-server-tests",
    model=model,
    dataset_key=dataset_key,
    dataset_file="scaryLetter.dataset.jsonl",
    compute_pool="default",
    create_use_case=False,
    data_source="DATASET",
    data_config={"dataset": dataset_key},
    parameter_efficient=True,
    alignment_method="PPO",
    alignment_objective={"reward_server": {"remote_env": "testing-reward-server"}},
    alignment_params={"ppo": {"kl_div_coeff": 0.01, "steps": 10}},
    base_training_params={
        "learning_rate": 1e-5,
        "num_epochs": 1,
        "batch_size": 32,
        "num_validations": 10,
    },
)
