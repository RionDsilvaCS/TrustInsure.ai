from llama_index.core.agent import ReActAgent
from llama_index.llms.ollama import Ollama
from .agent_tool import agent_as_tools
# from .agent_template import orch_agent_prompt

class OrchAgent:
    def __init__(self) -> None:

        _llm = Ollama(model="gemma2:2b", request_timeout=120.0)

        self.agent = ReActAgent.from_tools(agent_as_tools, llm=_llm, verbose=True)
        # self.agent.update_prompts({"agent_worker:system_prompt": orch_agent_prompt})

    def get_agent(self):
        return self.agent
    