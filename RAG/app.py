from retreiver import Retreiver
import streamlit as st
from dotenv import load_dotenv
load_dotenv() 

st.title("A simple QA rag")

if query:=st.chat_input("Ask ANything! : "):
    result=Retreiver(query)
    st.write(result)
    











