import os
import socket
from types import SimpleNamespace


def get_size(x):
    try:
        if x.endswith("TB"):
            return float(x.replace("TB", "")) * (2**40)
        if x.endswith("GB"):
            return float(x.replace("GB", "")) * (2**30)
        if x.endswith("MB"):
            return float(x.replace("MB", "")) * (2**20)
        if x.endswith("KB"):
            return float(x.replace("KB", "")) * (2**10)
        if x.endswith("B"):
            return float(x.replace("B", ""))
        return 2**31
    except Exception:
        return 2**31


version = "0.0.1"

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    host = s.getsockname()[0]
    s.close()
except OSError:
    host = "localhost"

port = "10101"
url = f"http://{host}:{port}/"


default_cfg = {
    "url": url,
    "name": "H2O LLM Studio",
    "version": version,
    "github": "https://github.com/h2oai/h2o-llmstudio",
    "min_experiment_disk_space": get_size(
        os.getenv("MIN_DISK_SPACE_FOR_EXPERIMENTS", "2GB")
    ),
    "separate_user_space": False,
    "allowed_file_extensions": os.getenv(
        "ALLOWED_FILE_EXTENSIONS", ".zip,.csv,.pq"
    ).split(","),
    "dbs_path": "data/dbs/",
    "s3_bucket": f"{os.getenv('AWS_BUCKET', 'bucket_name')}",
    "s3_filename": os.path.join(
        f"{os.getenv('AWS_BUCKET', 'bucket_name')}",
        "default.zip",
    ),
    "cfg_file": "text_causal_language_modeling_config",
    "start_page": "home",
    "kaggle_command": ("kaggle competitions download -c " "dataset"),
    "problem_types": [
        "text_causal_language_modeling_config",
    ],
    "problem_categories": ["text"],
    "dataset_keys": [
        "train_dataframe",
        "validation_dataframe",
        "prompt_column",
        "answer_column",
        "parent_id_column",
    ],
    "dataset_trigger_keys": [
        "train_dataframe",
        "validation_dataframe",
    ],
    "dataset_extra_keys": [
        "validation_strategy",
        "data_sample",
        "data_sample_choice",
    ],
    "dataset_folder_keys": [
        "train_dataframe",
        "validation_dataframe",
    ],
    "user_settings": {
        "theme_dark": True,
        "default_aws_bucket_name": f"{os.getenv('AWS_BUCKET', 'bucket_name')}",
        "default_aws_access_key": os.environ["AWS_ACCESS_KEY_ID"]
        if "AWS_ACCESS_KEY_ID" in os.environ
        else "",
        "default_aws_secret_key": os.environ["AWS_SECRET_ACCESS_KEY"]
        if "AWS_SECRET_ACCESS_KEY" in os.environ
        else "",
        "default_kaggle_username": "",
        "default_kaggle_secret_key": "",
        "set_max_epochs": 50,
        "set_max_batch_size": 256,
        "set_max_gradient_clip": 10,
        "default_number_of_workers": 8,
        "default_logger": "None",
        "default_neptune_project": os.getenv("NEPTUNE_PROJECT", ""),
        "default_neptune_api_token": os.getenv("NEPTUNE_API_TOKEN", ""),
        "default_openai_api_token": os.getenv("OPENAI_API_KEY", ""),
        "default_huggingface_api_token": os.getenv("HUGGINGFACE_TOKEN", ""),
        "delete_dialogs": True,
        "chart_plot_max_points": 1000,
    },
}

default_cfg = SimpleNamespace(**default_cfg)
