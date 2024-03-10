from dataclasses import dataclass
from pathlib import Path
from typing import List, Tuple

@dataclass(frozen=True)
class ModelLoadConfig:
    root_dir: Path
    model_names: List[str]
    model_directory: Path

@dataclass(frozen=True)
class URLProcessingConfig:
    root_dir: Path
    processed_directory: Path
    temp_directory: Path

@dataclass(frozen=True)
class DataCleaningConfig:
    root_dir: Path
    cleaned_data_directory: Path
    rules: List[str]

@dataclass(frozen=True)
class VectorizationConfig:
    root_dir: Path
    embedding_model: str
    vector_db_directory: Path

@dataclass(frozen=True)
class DatabaseManagementConfig:
    root_dir: Path
    db_path: Path

@dataclass(frozen=True)
class OpenAIIntegrationConfig:
    root_dir: Path
    api_key: str
    default_model: str
    temperature: float

@dataclass(frozen=True)
class ChatHistoryConfig:
    root_dir: Path
    max_entries: int
    storage_file: Path

@dataclass(frozen=True)
class ApplicationConfig:
    streamlit_app_root: Path
    streamlit_app_port: int
    api_service_root: Path
    api_service_port: int

@dataclass(frozen=True)
class ExperimentalConfig:
    root_dir: Path
    trials_notebook: Path
