import streamlit as st
import time
import os 
from llama_deploy import LlamaDeployClient, ControlPlaneConfig
from dotenv import load_dotenv
load_dotenv()

client = LlamaDeployClient(ControlPlaneConfig())

session_id = os.getenv("MULTI_SESSION_ID")
session = client.get_or_create_session(session_id)

st.set_page_config(page_title="Multi Agent", page_icon="🪄")

st.title("Multi Agent 🪄")
st.markdown(
    """
    Search, Claim and Clear your doubts at one click 🖱️
    """
)

# llama deploy response
def response_generator(query):
    response = session.run("orch_agent", query=query)
    for word in response.split(" "):
        yield word + " "
        time.sleep(0.05)


# Function for first None request
def fake_data():
    _LOREM_IPSUM = "Hello, I am your dedicated assistant for researching, acquiring, and enhancing your understanding of insurance 🤝"
    for word in _LOREM_IPSUM.split(" "):
        yield word + " "
        time.sleep(0.05)

if "messages_3" not in st.session_state:
    st.session_state.messages_3 = []

# Saving messages_3 state
for message in st.session_state.messages_3:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User input
if prompt := st.chat_input("Type your questions here !!!"):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages_3.append({"role": "user", "content": prompt})

# Input passed to API
with st.chat_message("assistant"):
    if prompt is not None:
        response = st.write_stream(response_generator(str(prompt)))
    else:
        response = st.write_stream(fake_data())

st.session_state.messages_3.append({"role": "assistant", "content": response})