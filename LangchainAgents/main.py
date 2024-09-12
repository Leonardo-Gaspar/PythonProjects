'''
LangSmith: Repositório com vários tipos de prompts e conversações
LangSmith -> openai-functions-agent

Agent: 
       -> llm         -> llm
       -> Ferramentas -> tools
       -> prompt      -> prompt
'''
from langchain.agents import AgentExecutor
from agent import AgenteOpenAIFunctions
from dotenv import load_dotenv

load_dotenv()

pergunta = "Quais os dados de Ana?"
pergunta = "Quais os dados de Bianca?"
pergunta = "Quais os dados de Ana e da Bianca?"
pergunta = "Crie um perfil academico para a Ana"
pergunta = "Compare o perfil academico da Ana com o da Bianca"

agente = AgenteOpenAIFunctions()
executor = AgentExecutor(agent=agente.agente,
                        tools=agente.tools,
                        verbose=True)
resposta = executor.invoke({"input" : pergunta})
print(resposta)




