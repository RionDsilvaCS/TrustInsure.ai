from src.db.read_db import SemanticBM25Retriever
from llama_index.core import get_response_synthesizer
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.core.tools import QueryEngineTool
from llama_index.core import Settings
from llama_index.llms.ollama import Ollama

Settings.llm = Ollama(model="gemma2:2b", request_timeout=120.0)

custom_retriever = SemanticBM25Retriever()
response_synthesizer = get_response_synthesizer()

query_engine = RetrieverQueryEngine(
    retriever=custom_retriever,
    response_synthesizer=response_synthesizer,
)

insurance_information_tool = QueryEngineTool.from_defaults(
    query_engine,
    name="insurance_knowledge_base",
    description="A RAG engine with knowledge of all knowledge, terms and conditions in insurance.",
)
