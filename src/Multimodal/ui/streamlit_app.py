import streamlit as st
import sqlite3
from streamlit_mic_recorder import mic_recorder

from Multimodal.config.configuration import ConfigurationManager
from Multimodal.components.llm_chains import load_normal_chain, load_pdf_chat_chain
from Multimodal.utils.common import get_timestamp, load_config, get_avatar


from image_handler import handle_image
from audio_handler import transcribe_audio
from pdf_handler import add_documents_to_db
from html_templates import css
from database_operations import load_last_k_text_messages, save_text_message, save_image_message, save_audio_message, load_messages, get_all_chat_history_ids, delete_chat_history
