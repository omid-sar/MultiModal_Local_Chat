import os
from pathlib import Path
import subprocess
from huggingface_hub import hf_hub_download, snapshot_download


from Multimodal.logging import logger
from Multimodal.utils.common import get_size
from Multimodal.entity import ModelLoadConfig
#import huggingface-cli

class ModelLoad:
    def __init__(self, config: ModelLoadConfig):
        self.config = config


    def download_models(self):
        self.download_text_processing_models()
        self.download_sentences_embedding_model()
        self.download_audio_transcription_model()
        self.download_multimodal_models()


    def download_text_processing_models(self):
        model_names= self.config.text_processing_model_names
        base_model_path = self.config.text_processing_model_directory
       
        for model_name in model_names:
            repo_id , filename = model_name.split()
            model_path = base_model_path / filename
            if not model_path.exists():
                model_path.mkdir(parents=True, exist_ok=True)
                cmd = f"huggingface-cli download {model_name} --local-dir {model_path} --local-dir-use-symlinks False"
                subprocess.run(cmd, shell=True, check=True)
                #hf_hub_download(repo_id=repo_id, filename=filename, cache_dir=model_path)
                logger.info(f"{model_name} downloaded and saved to {model_path}")
            else:
                logger.info(f"Model {model_name} already exists at {model_path}. Skipping download. Size: {get_size(model_path)}")


   
    def download_sentences_embedding_model(self):
        model_name = self.config.sentences_embedding_model_name
        model_path = self.config.sentences_embedding_model_directory

        if not model_path.exists():
            snapshot_download(repo_id=model_name, cache_dir=model_path)
            logger.info(f"{model_name} downloaded and saved to {model_path}")
        else:
            logger.info(f"Model {model_name} already exists at {model_path}. Skipping download. Size: {get_size(model_path)}")


    def download_audio_transcription_model(self):
        model_name = self.config.audio_transcription_model_name
        model_path = self.config.audio_transcription_model_directory 

        if not model_path.exists():
            snapshot_download(repo_id=model_name, cache_dir=model_path)
            logger.info(f"{model_name} downloaded and saved to {model_path}")
        else:
            logger.info(f"Model {model_name} already exists at {model_path}. Skipping download. Size: {get_size(model_path)}")

    def download_multimodal_models(self):
        model_names= self.config.multimodal_model_names
        base_model_path = self.config.multimodal_model_directory
        
        for model_name in model_names:
            repo_id, filename = model_name.split()
            model_path = base_model_path / filename
            if not model_path.exists():
                model_path.mkdir(parents=True, exist_ok=True)
                cmd = f"huggingface-cli download {model_name} --local-dir {model_path} --local-dir-use-symlinks False"
                subprocess.run(cmd, shell=True, check=True)
                #hf_hub_download(repo_id=repo_id, filename=filename, cache_dir= model_path)
                logger.info(f"{filename} downloaded and saved to {model_path}")
            else:
                logger.info(f"Model {filename} already exists at {model_path}. Skipping download. Size: {get_size(model_path)}")

      
       
