import os
from dotenv import load_dotenv
import streamlit as st
from langchain.agents import initialize_agent,AgentType
from langchain_groq import ChatGroq
from langchain_community.tools import WikipediaQueryRun,ArxivQueryRun,DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper,ArxivAPIWrapper

st.title("Langchain Search Engine")
load_dotenv()

wikipedia_api_wrapper=WikipediaAPIWrapper(doc_content_chars_max=200,top_k_results=1)
arxiv_api_wrapper=ArxivAPIWrapper(doc_content_chars_max=200,top_k_results=1)



wikipedia=WikipediaQueryRun(api_wrapper=wikipedia_api_wrapper)
arxiv=ArxivQueryRun(api_wrapper=arxiv_api_wrapper)
web_search=search=DuckDuckGoSearchRun()


def store_message(role,content):
    message={
        "role":role,
        "content":content
    }
    st.session_state.message.append(message)

if "message" not in st.session_state:
    st.session_state["message"]=[
        {
        "role":"ai",
        "content":"How can i help you?"
    }
    ]
    

for msg in st.session_state.message:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt:=st.chat_input(placeholder="message Search engine"):
    store_message("user",prompt)
    st.chat_message("user").write(prompt)
    llm=ChatGroq(model="llama-3.1-8b-instant")
    tools=[wikipedia,arxiv,web_search]

    agent=initialize_agent(llm=llm,tools=tools,agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,handling_parsing_errors=True)
    response=agent.run(prompt)
    store_message("ai",response)
    st.chat_message("ai").write(response)