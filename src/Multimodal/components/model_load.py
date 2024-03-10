import os
from pathlib import Path
from huggingface_hub import hf_hub_download

from Multimodal.logging import logger
from Multimodal.utils.common import get_size
from Multimodal.entity import ModelLoadConfig


class ModelLoad:
    def __init__(self, config: ModelLoadConfig):
        self.config = config
                   
    def download_models(self):
        """
        Downloads each model in the model_names list to the target directory if not already present.
        """
        for model_name in self.config.model_names:
            repo_id, filename = model_name.split()
            model_path = self.config.model_directory / filename
            if not model_path.exists():
                hf_hub_download(repo_id=repo_id, filename=filename, cache_dir=self.config.model_directory)
                logger.info(f"{filename} downloaded and saved to {model_path}")
            else:
                logger.info(f"Model {filename} already exists at {model_path}. Skipping download. Size: {get_size(dataset_path)}")




from Multimodal.config.configuration import ConfigurationManager



class ModelLoadPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_load_config = config.get_model_load_config()
        downloader = ModelLoad(config=model_load_config)
        downloader.download_models()

model = ModelLoadPipeline()
model.main()