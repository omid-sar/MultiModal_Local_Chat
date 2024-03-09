from pathlib import Path
from Multimodal.logging import logger
from Multimodal.utils.common import create_directories

logger.info("Welcome to my custome log")
from Multimodal.config.configuration import ConfigurationManager 

config = ConfigurationManager()
pdf_processing_config = config.get_pdf_processing_config()
pdf_processing_config.processed_directory
processed_directory = Path(pdf_processing_config.processed_directory)
create_directories([processed_directory])


import os
os.makedirs(processed_directory)