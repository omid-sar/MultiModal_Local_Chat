import streamlit as st
from Multimodal.config.configuration import ConfigurationManager
from Multimodal.components.llm_chains import LLMChains
from Multimodal.utils.common import get_timestamp, get_avatar
#import sqlite3
#from streamlit_mic_recorder import mic_recorder

def load_chain():
    return 


def set_send_input():
    st.session_state.send_input = True
    clear_input_field()


def clear_input_field():
    st.session_state.user_question = st.session_state.user_input
    st.session_state.user_input = ""    




def main():
    # Title 
    st.title('The :blue[coolest] MultiModal ChatBot :sunglasses:')
    # Instantiate container 
    chat_container = st.container()

    if "send_input" not in st.session_state:
        st.session_state.send_input = False
        st.session_state.user_question = ""
    # We dont use chat_input beacuse of multimodality of model, user may want to upload a file or etc.
    user_input = st.text_input("Type your prompt here", key="user_input", on_change=set_send_input)

    send_buttom = st.button(":blue[SEND]", key="send_buttom")
    if send_buttom or st.session_state.send_input:
        if st.session_state.user_question != "":
            llm_response = f"This is Place holder for the future model response and the prompt was: {st.session_state.user_question}"


            with chat_container:
                st.chat_message("user").write(st.session_state.user_question)
                st.chat_message("ai").write(llm_response)

   

if __name__ =="__main__":
    main()
