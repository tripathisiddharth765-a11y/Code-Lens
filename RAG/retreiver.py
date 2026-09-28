from langchain_ollama import ChatOllama
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_chroma import Chroma 
from dotenv import load_dotenv
load_dotenv() 

embeddingModel = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
model=ChatOllama(
        model="qwen3:8b",
        temperature=0.7
    )

def Retreiver(query):
    
    vector_store=Chroma(
      persist_directory="./db",
        embedding_function=embeddingModel)

    retrieve=vector_store.as_retriever(
        kwargs={"k":3}
    )

   

    results=retrieve.invoke(query)

    context="\n\n".join(result.page_content for result in results)


    prompt = PromptTemplate(
    template="""
    You are a helpful assistant.

    Answer the query using ONLY the provided context.

    Context:
    {context}

    Question:
    {query}

    If the answer cannot be found in the context,
    say that you don't know.

    Answer:
    """,
        input_variables=["context", "query"]
    )


    chain=prompt|model|StrOutputParser()

    Answer=chain.invoke({
        "context":context,
        "query":query
    })
    return Answer








