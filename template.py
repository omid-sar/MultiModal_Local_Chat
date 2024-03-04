import os
import logging
from pathlib import Path

logging.basicConfig(
    level=logging.INFO, format="[%(asctime)s]: %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
)

project_name = "RagNavigator"
list_of_files = [
    "github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_preprocessing.py",
    f"src/{project_name}/components/model_training.py",
    f"src/{project_name}/components/model_evaluation.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/data_utils.py",  #
    f"src/{project_name}/utils/model_utils.py",  # For model-related utility functions
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/pipeline/data_ingestion.py",  # For data ingestion processes
    f"src/{project_name}/pipeline/data_preprocessing.py",  # For data preprocessing steps
    f"src/{project_name}/pipeline/model_training.py",  # For model training processes
    f"src/{project_name}/pipeline/model_evaluation.py",  # For model evaluation processes
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/models/__init__.py",  # For model definitions
    f"src/{project_name}/constants/__init__.py",
    "config/config.yml",
    "params.yml",
    "app.py",  # For model serving/application interface
    "main.py",  # Main script to run the pipeline
    "Dockerfile",  # For containerization
    "artifacts/.gitkeep",  # Placeholder for artifacts directory
]
project_name = "RagNavigator"
list_of_files = [
    "github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/pdf_processor.py",  # For handling PDF file reading and processing
    f"src/{project_name}/components/url_processor.py",  # For extracting and processing content from URLs
    f"src/{project_name}/components/data_cleaner.py",  # For cleaning and preparing data for vectorization
    f"src/{project_name}/components/vectorizer.py",  # For converting processed text to vectors using ChromaDB or similar
    f"src/{project_name}/components/database_manager.py",  # For interacting with the vector database
    f"src/{project_name}/components/api_connector.py",  # For handling OpenAI API requests and responses
    f"src/{project_name}/components/chat_history.py",  # For saving and retrieving chat history
    f"src/{project_name}/components/configuration_manager.py",  # For managing model and API configurations
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common_utils.py",  # General utility functions
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",  # Project configuration settings
    f"src/{project_name}/ui/__init__.py",
    f"src/{project_name}/ui/streamlit_app.py",  # Main Streamlit app interface
    f"src/{project_name}/constants/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    "config/config.yaml",
    "app.py",  # Entry point for running the Streamlit app
    "main.py",  # Main script for initializing components and starting the app
    "Dockerfile",  # For containerization
    "artifacts/.gitkeep",
    "research/trials.ipynb",  # For experimental code and research
]


# Create the files and directories
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory {filedir} for the file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Created empty file {filepath}")

    else:
        logging.info(f"File {filepath} already exists")


