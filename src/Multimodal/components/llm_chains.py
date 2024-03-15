import chromadb
from langchain.chains import LLMChain
from langchain.chains.retrieval_qa.base import RetrievalQA
from langchain_community.embeddings import HuggingFaceInstructEmbeddings
from langchain.memory import ConversationBufferWindowMemory
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers
from langchain_community.vectorstores import Chroma
from langchain_community.llms import Ollama

from Multimodal.components.prompt_templates import memory_prompt_template
from Multimodal.config.configuration import ConfigurationManager
from Multimodal.entity import LLMChainsConfig


class LLMChains:
    def __init__(self, config: LLMChainsConfig ) -> None:
        self.config = config

    def main(self):
        self.create_llm()
        self.create_llm_chain()
        self.create_chat_memory()
        self.create_prompt_from_template()


    def create_llm(self):
        llm = CTransformers(model_path = str(self.config.model_path_large))
        return llm
       
    def create_llm_chain(self):
        pass
    def create_chat_memory(self):
        pass
    def create_prompt_from_template(self):
        pass
    def load_normal_chain(self):
        pass 

from pathlib import Path
llm = CTransformers(model="/Users/omidsardari/WORK/Becoming a Data Scientist/Python Projects/Multimodal_Local_Chat/artifacts/model_load/text_processing_model/mistral-7b-instruct-v0.1.Q3_K_M.gguf/mistral-7b-instruct-v0.1.Q5_K_M.gguf")
"mistral-7b-instruct-v0.1.Q3_K_M.gguf"
llm = CTransformers(model ="mistral-7b-instruct-v0.1.Q5_K_M.gguf")
llm =
llm
#********************************************************************************************************
# ******                                       Temporary parts                                   *******
import os 
print (os.getcwd())
os.chdir("../../..")
print (os.getcwd())

configuration = ConfigurationManager()
config = configuration.get_llm_chains_config()
llm_chains = LLMChains(config)
llm_chains.create_llm()



#********************************************************************************************************








