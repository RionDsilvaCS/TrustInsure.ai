from llama_index.core.agent import ReActAgent
from llama_index.llms.ollama import Ollama
from llama_index.core.tools import FunctionTool
from .agent_tool import search_and_list_insurance_tool, bike_insurance_claim_tool
from .agent_template import form_agent_prompt

class FormAgent:
    def __init__(self) -> None:
        _search_tool = FunctionTool.from_defaults(fn=search_and_list_insurance_tool)
        _bike_claim_tool = FunctionTool.from_defaults(fn=bike_insurance_claim_tool)
        _llm = Ollama(model="gemma2:2b", request_timeout=120.0)

        self.agent = ReActAgent.from_tools([_search_tool, _bike_claim_tool], llm=_llm, verbose=True)
        self.agent.update_prompts({"agent_worker:system_prompt": form_agent_prompt})

    def get_agent(self):
        return self.agent
