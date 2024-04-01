import streamlit as st
from pathlib import Path
import os
from langchain.memory import StreamlitChatMessageHistory
from Multimodal.config.configuration import ConfigurationManager
from Multimodal.components.llm_chains import LLMChains
from Multimodal.utils.common import save_chat_history_json, load_chat_history_json, get_timestamp, get_avatar
#import sqlite3
#from streamlit_mic_recorder import mic_recorder
configuration = ConfigurationManager()
config = configuration.get_llm_chains_config()
llm_chain = LLMChains(config)

def load_chain():
    pass


def set_send_input():
    st.session_state.send_input = True
    clear_input_field()


def clear_input_field():
    st.session_state.user_question = st.session_state.user_input
    st.session_state.user_input = ""    

def save_chat_history():
    if st.session_state.history != []:
        if st.session_state.session_key == "NEW_SESSION":
            st.session_state.new_session_key = get_timestamp() 

            file_path = Path(config.chat_sessions_directory + st.session_state.new_session_key + ".json")
        else:
            file_path = Path(config.chat_sessions_directory + st.session_state.session_key + ".json")
        
        save_chat_history_json(chat_history=st.session_state.history, file_path = file_path)


def main():
    # Title 
    st.title('The :blue[coolest] MultiModal ChatBot :sunglasses:')
    # Sidebar
    st.sidebar.title("Chat Session")
    chat_sessions = ["NEW_SESSION"] + os.listdir(config.chat_sessions_directory)
    # Instantiate container 
    chat_container = st.container()

    if "send_input" not in st.session_state:
        st.session_state.send_input = False
        st.session_state.user_question = ""
        st.session_state.session_key = "NEW_SESSION"
        st.session_state.new_session_key = None
        st.session_state.session_index_tracker = "NEW_SESSION"
    if st.session_state.session_key == "NEW_SESSION" and st.session_state.new_session_key != None:
        st.session_state.session_index_tracker = st.session_state.new_session_key
        st.session_state.new_session_key = None




