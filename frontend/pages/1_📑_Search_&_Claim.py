import streamlit as st
import time
import os 
from llama_deploy import LlamaDeployClient, ControlPlaneConfig
from dotenv import load_dotenv
load_dotenv()

client = LlamaDeployClient(ControlPlaneConfig())

session_id = os.getenv("FORM_SESSION_ID")
session = client.get_or_create_session(session_id)

st.set_page_config(page_title="Search & Claim Agent", page_icon="📑")

st.title("Search & Claim Agent 📑")
st.markdown(
    """
    Automate form-filling with Al for error-free applications and higher claim acceptance rates ✅
    """
)

# llama deploy response
def response_generator(query):
    response = session.run("form_agent", query=query)
    for word in response.split(" "):
        yield word + " "
        time.sleep(0.05)


# Function for first None request
def fake_data():
    _LOREM_IPSUM = "Hello, I am your dedicated assistant for insurance inquiries and claims 🤝"
    for word in _LOREM_IPSUM.split(" "):
        yield word + " "
        time.sleep(0.05)

if "messages" not in st.session_state:
    st.session_state.messages = []

# Saving messages state
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User input
if prompt := st.chat_input("Type your questions here !!!"):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

# Input passed to API
with st.chat_message("assistant"):
    if prompt is not None:
        response = st.write_stream(response_generator(str(prompt)))
    else:
        response = st.write_stream(fake_data())

st.session_state.messages.append({"role": "assistant", "content": response})