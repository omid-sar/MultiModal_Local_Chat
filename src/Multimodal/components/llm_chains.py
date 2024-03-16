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
#from langchain.embeddings import HuggingFaceEmbeddings
from langchain_community.embeddings import HuggingFaceEmbeddings

class LLMChains:
    def __init__(self, config: LLMChainsConfig ) -> None:
        self.config = config

    def main(self):
        self.create_llm()
        self.create_embeddings()
        self.create_llm_chain()
        self.create_chat_memory()
        self.create_prompt_from_template(memory_prompt_template)

  
    def create_llm(self):
        llm = CTransformers(model=self.config.model_path_large, model_type=self.config.model_type, config=self.config.model_config)
        return llm
    # I just replaced HuggingFaceInstructEmbeddings by HuggingFaceEmbeddings
    # Just write now i want the code is working
    # I should fix the problem then
    def create_embeddings(self):
        return HuggingFaceEmbeddings(model_name=self.config.embedding_path)
    
    def create_prompt_from_template(self,template):
        return PromptTemplate.from_template(template)
   
    def create_llm_chain(self):
        pass

    def create_chat_memory(self, chat_history):
        ConversationBufferWindowMemory(memory_key="history", chat_memory=chat_history, k= 5)
        pass
    
    def load_normal_chain(self):
        pass 



#********************************************************************************************************
# ******                                       Temporary parts                                   *******

import os 
print (os.getcwd())
os.chdir("../../..")
print (os.getcwd())
configuration = ConfigurationManager()
config = configuration.get_llm_chains_config()

llm_chains = LLMChains(config)
llm_chains.main()

#**********************************************************************************************************
