from src.tools.rag_agent import RAGAgent
from src.tools.form_agent import FormAgent
from llama_deploy import (
    deploy_workflow,
    WorkflowServiceConfig,
    ControlPlaneConfig,
    SimpleMessageQueueConfig,
)
import asyncio
from llama_index.core.workflow import Workflow, StartEvent, StopEvent, step

form_agent_obj = FormAgent()
form_agent = form_agent_obj.get_agent()

rag_agent_obj = RAGAgent()
rag_agent = rag_agent_obj.get_agent()

class Formflow(Workflow):
    @step()
    async def run_step(self, ev: StartEvent) -> StopEvent:
        
        query= str(ev.get("query", ""))
        if len(query) != 0:
            result = form_agent.chat(query)
        else:
            result = "Enter the input for variable query"
        
        return StopEvent(result=result)

class RAGflow(Workflow):
    @step()
    async def run_step(self, ev: StartEvent) -> StopEvent:
        
        query= str(ev.get("query", ""))
        if len(query) != 0:
            result = rag_agent.chat(query)
        else:
            result = "Enter the input for variable query"
        
        return StopEvent(result=result)

async def main():
    form_task = asyncio.create_task(
        deploy_workflow(
            Formflow(),
            WorkflowServiceConfig(
                host="127.0.0.1", port=8002, service_name="form_agent"
            ),
            ControlPlaneConfig(),
        )
    )

    rag_task = asyncio.create_task(
        deploy_workflow(
            RAGflow(),
            WorkflowServiceConfig(
                host="127.0.0.1", port=8003, service_name="rag_agent"
            ),
            ControlPlaneConfig(),
        )
    )

    await asyncio.gather(form_task, rag_task)


if __name__ == "__main__":
    asyncio.run(main())