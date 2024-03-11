import os
from box.exceptions import BoxValueError
import yaml
import json
from typing import List
# Assuming HumanMessage and AIMessage are defined elsewhere and imported correctly
from Multimodal.logging import logger
from Multimodal.constants import *
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import re
from langchain.schema.messages import HumanMessage, AIMessage


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")


@ensure_annotations
def save_chat_history_json(chat_history: List, file_path: str) -> None:
    """
    Saves the chat history to a JSON file.

    Args:
        chat_history: A list of message objects (either HumanMessage or AIMessage).
        file_path: The path to the file where the chat history will be saved.
    """
    with open(file_path, "w") as f:
        json_data = []
        for message in chat_history:
            message_dict = message.dict()
            json_data.append(message_dict)
        json.dump(json_data, f, ensure_ascii=False, indent=4)  
    logger.info(f"Chat history successfully save to {file_path}. ")



@ensure_annotations
def load_chat_history_json(file_path: str) -> List:
    """
    Loads the chat history from a JSON file and returns a list of message objects.

    Args:
        file_path: The path to the file from which the chat history will be loaded.

    Returns:
        A list of message objects (either HumanMessage or AIMessage based on the type specified in the JSON).
    """
    with open(file_path, "r") as f:
        json_data = json.load(f)
        messages = []
        for message in json_data:
            if message["type"] == "human":
                messages.append(HumanMessage(**message))
            else:
                messages.append(AIMessage(**message))
            logger.info(f"Chat history successfully loaded from {file_path}.")
            return messages



@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"


@ensure_annotations
def get_avatar(sender_type: str) -> str:
    """
    Returns the avatar file path for a given sender type ('human' or 'bot').
    """
    if sender_type == "human":
        return USER_AVATAR_FILE_PATH
    else:
        return BOT_AVATAR_FILE_PATH


def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


class DirectoryTree:
    def __init__(self, root_path: Path):
        self.root_path = root_path
        self.tree = []

    def _generate_tree(self, directory: Path, level: int = 0):
        """Helper recursive function to generate tree, excluding certain files/directories."""
        # Skip directories like '__pycache__', '.git', and other unwanted patterns
        if re.match(r'(__pycache__|\.git|\.github|.DS_Store)', directory.name):
            return

        indent = "  " * level
        self.tree.append(f"{indent}{directory.name}/\n")

        for item in directory.iterdir():
            if item.is_dir():
                self._generate_tree(item, level + 1)
            else:
                # Skip files with unwanted patterns
                if not re.match(r'(\.pyc|\.DS_Store|cache-|.*\.log|.*\.sample|FETCH_HEAD|ORIG_HEAD|COMMIT_EDITMSG)', item.name):
                    self.tree.append(f"{indent}  {item.name}\n")

    def write_to_file(self, file_output_name: str = "output.txt"):
        """Writes the tree structure to a file."""
        self._generate_tree(self.root_path)

        with open(file_output_name, 'w') as output_file:
            output_file.writelines(self.tree)





    