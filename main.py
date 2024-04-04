from pathlib import Path
from Multimodal.logging import logger

from Multimodal.config.configuration import ConfigurationManager
from Multimodal.components.model_load import ModelLoad


config = ConfigurationManager()


STAGE_NAME = "Models and Embeddings Load Stage"
try:
    logger.info(f"\n\nx{'=' * 80}x \n\n>>>>>> stage {STAGE_NAME} started <<<<<<") 
    model_load_config = config.get_model_load_config()
    downloader = ModelLoad(config=model_load_config)
    downloader.download_models()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx{'=' * 80}x")
except Exception as e:
        logger.exception(e)
        raise e



