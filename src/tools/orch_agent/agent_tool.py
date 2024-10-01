from llama_index.core.tools import QueryEngineTool, ToolMetadata
from src.tools.form_agent import FormAgent
from src.tools.rag_agent import RAGAgent

form_agent_obj = FormAgent()
form_agent = form_agent_obj.get_agent()

rag_agent_obj = RAGAgent()
rag_agent = rag_agent_obj.get_agent()

agent_as_tools = [
    QueryEngineTool(
        query_engine=form_agent,
        metadata=ToolMetadata(
            name="form_agent", description="Tool that will search latest insurance policies and claim existing insurance."
        ),
    ),

    QueryEngineTool(
        query_engine=rag_agent,
        metadata=ToolMetadata(
            name="insurance_knowledge_agent",
            description="Tool that can help to provide knowledge like what, why, when and types in insurance sector",
        ),
    ),
]
