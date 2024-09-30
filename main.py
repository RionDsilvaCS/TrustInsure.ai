from llama_deploy import LlamaDeployClient, ControlPlaneConfig

client = LlamaDeployClient(ControlPlaneConfig())

session = client.get_or_create_session("123456")

query = """Claim a bike insurance for me and the follwing are the details: the policy number is BI67890, 
            the insured name is Jane Smith, claim type is theft, the policy report number is PR12345 and incident details is that "bike stolen from driveway". 
            The bike details are from Honda company, the model is CBR1000RR and purchased in the year 2024"""

result = session.run("form_agent", query=query)

print(result)