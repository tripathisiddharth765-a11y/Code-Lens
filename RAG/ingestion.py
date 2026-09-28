from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma 
from dotenv import load_dotenv
load_dotenv() 

embeddingModel = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")

data=TextLoader("data/doc.txt").load()

spliter=RecursiveCharacterTextSplitter(
    chunk_size=500,
    
)

chunks=spliter.split_documents(data)

vector_store=Chroma.from_documents(
    chunks,
    embeddingModel,
    persist_directory="./db"
    )




























