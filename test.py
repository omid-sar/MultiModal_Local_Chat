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


llm = CTransformers(model ="mistral-7b-instruct-v0.1.Q5_K_M.gguf")
llm = CTransformers(model ="c4b062ec7f0f160e848a0e34c4e291b9e39b3fc60df5b201c038e7064dbbdcdc")