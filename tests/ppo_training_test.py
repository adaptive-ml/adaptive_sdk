from .utils import get_run_id, run_training_job

suffix = get_run_id()
dataset_key = f"hh-preference-training-200-{suffix}"
model = "llama_3.1_8b_instruct"
output_model_name = "my-output-model-v0"


run_training_job(
    use_case=f"e2e-training-usecase{suffix}",
    model=model,
    output_model_name=output_model_name,
    dataset_key=dataset_key,
    dataset_file="hh-preference-training-200.jsonl",
    compute_pool="default",
    data_source="DATASET",
    data_config={"dataset": dataset_key},
    feedback_type="PREFERENCE",
    parameter_efficient=True,
    alignment_method="PPO",
    alignment_objective={"metric": {"metric_key": "helpfulness"}},
    alignment_params={"ppo": {"kl_div_coeff": 0.01, "steps": 10}},
    base_training_params={"learning_rate": 1e-5, "num_epochs": 1, "batch_size": 32, "num_validations": 10},
)
