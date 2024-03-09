import os
from Multimodal.constants import *
from Multimodal.utils.common import read_yaml, create_directories
from pathlib import Path
from dotenv import load_dotenv
from Multimodal.entity import PDFProcessingConfig
from Multimodal.entity import URLProcessingConfig
from Multimodal.entity import DataCleaningConfig
from Multimodal.entity import VectorizationConfig
from Multimodal.entity import DatabaseManagementConfig
from Multimodal.entity import OpenAIIntegrationConfig
from Multimodal.entity import ChatHistoryConfig
from Multimodal.entity import ApplicationConfig
from Multimodal.entity import ExperimentalConfig



class ConfigurationManager:
    def __init__(self, config_filepath=CONFIG_FILE_PATH):
        self.config = read_yaml(config_filepath)
 

        create_directories([Path(self.config['artifacts_root'])])

    def get_pdf_processing_config(self) -> PDFProcessingConfig:
        config = self.config['pdf_processing']
        return PDFProcessingConfig(
            root_dir=Path(config['root_dir']),
            processed_directory=Path(config['processed_directory']),
            temp_directory=Path(config['temp_directory'])
        )

    def get_url_processing_config(self) -> URLProcessingConfig:
        config = self.config['url_processing']
        return URLProcessingConfig(
            root_dir=Path(config['root_dir']),
            processed_directory=Path(config['processed_directory']),
            temp_directory=Path(config['temp_directory'])
        )

    def get_data_cleaning_config(self) -> DataCleaningConfig:
        config = self.config['data_cleaning']
        return DataCleaningConfig(
            root_dir=Path(config['root_dir']),
            cleaned_data_directory=Path(config['cleaned_data_directory']),
            rules=config['rules']
        )

    def get_vectorization_config(self) -> VectorizationConfig:
        config = self.config['vectorization']
        return VectorizationConfig(
            root_dir=Path(config['root_dir']),
            embedding_model=config['embedding_model'],
            vector_db_directory=Path(config['vector_db_directory'])
        )

    def get_database_management_config(self) -> DatabaseManagementConfig:
        config = self.config['database_management']
        return DatabaseManagementConfig(
            root_dir=Path(config['root_dir']),
            db_path=Path(config['db_path'])
        )

    def get_openai_integration_config(self) -> OpenAIIntegrationConfig:
        config = self.config['openai_integration']
        return OpenAIIntegrationConfig(
            root_dir=Path(config['root_dir']),
            api_key=os.getenv("OPENAI_API_KEY"),
            default_model=config['default_model'],
            temperature=config['temperature']
        )


    def get_chat_history_config(self) -> ChatHistoryConfig:
        config = self.config['chat_history']
        return ChatHistoryConfig(
            root_dir=Path(config['root_dir']),
            max_entries=config['max_entries'],
            storage_file=Path(config['storage_file'])
        )

    def get_application_config(self) -> ApplicationConfig:
        config = self.config['application']
        load_dotenv()
        return ApplicationConfig(
            streamlit_app_root=Path(config['streamlit_app']['root_dir']),
            streamlit_app_port=config['streamlit_app']['port'],
            api_service_root=Path(config['api_service']['root_dir']),
            api_service_port=config['api_service']['port'],
        )

    def get_experimental_config(self) -> ExperimentalConfig:
        config = self.config['experimental']
        return ExperimentalConfig(
            root_dir=Path(config['root_dir']),
            trials_notebook=Path(config['trials_notebook'])
        )
