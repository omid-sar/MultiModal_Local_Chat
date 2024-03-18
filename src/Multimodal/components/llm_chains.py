import chromadb
from langchain.chains import LLMChain
from langchain.chains.retrieval_qa.base import RetrievalQA
#from langchain_community.embeddings import HuggingFaceInstructEmbeddings
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

    def run(self, chat_history, user_input):
        memory = self.create_chat_memory(chat_history)
        llm= self.create_llm()
        chat_prompt = self.create_prompt_from_template(memory_prompt_template)
        llm_chain = self.create_llm_chain(llm, chat_prompt, memory)
        return llm_chain.run(human_input=user_input, history=memory.chat_memory.messages, stop=["Human"])
     

    def create_llm(self):
        llm = CTransformers(model=self.config.model_path_small, model_type=self.config.model_type, config=self.config.model_config)
        return llm
    # I just replaced HuggingFaceInstructEmbeddings by HuggingFaceEmbeddings
    # Just write now i want the code is working
    # I should fix the problem then
    @staticmethod
    def create_embeddings(self):
        return HuggingFaceEmbeddings(model_name=self.config.embedding_path)
    
    def create_prompt_from_template(self,template):
        return PromptTemplate.from_template(template)
   
    def create_llm_chain(self, llm, chat_prompt, memory):
        return LLMChain(llm=llm, prompt=chat_prompt, memory=memory)
    


    def create_chat_memory(self, chat_history):
        return ConversationBufferWindowMemory(memory_key="history", chat_memory=chat_history, k= 5)
      
    

#********************************************************************************************************
# ******                                       Temporary parts                                   *******

"""import os 
from langchain.memory import StreamlitChatMessageHistory
from langchain.schema import BaseChatMessageHistory
print (os.getcwd())
os.chdir("../../..")
print (os.getcwd())
configuration = ConfigurationManager()
config = configuration.get_llm_chains_config()

llm_chains = LLMChains(config)


from langchain.memory import ChatMessageHistory


empty_chat_history = ChatMessageHistory()
llm_chains.run(chat_history=empty_chat_history, user_input="Go")
"""
#**********************************************************************************************************
# Import necessary libraries and modules
