import streamlit as st
import time
import os 
from llama_deploy import LlamaDeployClient, ControlPlaneConfig
from dotenv import load_dotenv
load_dotenv()

client = LlamaDeployClient(ControlPlaneConfig())

session_id = os.getenv("RAG_SESSION_ID")
session = client.get_or_create_session(session_id)

st.set_page_config(page_title="Knowledge Agent", page_icon="📖")

st.title("Knowledge Agent 📖")
st.markdown(
    """
    Ensure clear understanding of policy terms and conditions 📋 
    """
)

# llama deploy response
def response_generator(query):
    response = session.run("rag_agent", query=query)
    for word in response.split(" "):
        yield word + " "
        time.sleep(0.05)


# Function for first None request
def fake_data():
    _LOREM_IPSUM = "Hello, I am your dedicated personal knowledge assistant specializing in insurance 🤝"
    for word in _LOREM_IPSUM.split(" "):
        yield word + " "
        time.sleep(0.05)

if "messages_2" not in st.session_state:
    st.session_state.messages_2 = []

# Saving messages_2 state
for message in st.session_state.messages_2:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User input
if prompt := st.chat_input("Type your questions here !!!"):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages_2.append({"role": "user", "content": prompt})

# Input passed to API
with st.chat_message("assistant"):
    if prompt is not None:
        response = st.write_stream(response_generator(str(prompt)))
    else:
        response = st.write_stream(fake_data())

st.session_state.messages_2.append({"role": "assistant", "content": response})