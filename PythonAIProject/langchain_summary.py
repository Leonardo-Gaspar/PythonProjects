# Importa o ChatOpenAI da biblioteca langchain_openai, que faz a integração com o modelo GPT da OpenAI.
from langchain_openai import ChatOpenAI
# Habilita o modo de debug para fornecer mais informações sobre a execução do código.
from langchain.globals import set_debug
from langchain.chains import ConversationChain
from langchain.memory import ConversationSummaryMemory
# Biblioteca para manipulação de variáveis de ambiente.
import os
# Carrega a biblioteca dotenv para carregar variáveis de ambiente de um arquivo .env.
from dotenv import load_dotenv
# Carrega as variáveis de ambiente do arquivo .env.
load_dotenv()
# Ativa o modo de debug para rastrear os processos da execução.
set_debug(True)

# Inicializa o modelo GPT-3.5-turbo com temperatura de 0.5 e a chave da API OpenAI.
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.5,
    api_key=os.getenv("OPENAI_API_KEY")  # Obtém a chave da API do arquivo .env
)

mensagens = [
        "Quero visitar um lugar no Brasil famoso por suas praias e cultura. Pode me recomendar?",
        "Qual é o melhor período do ano para visitar em termos de clima?",
        "Quais tipos de atividades ao ar livre estão disponíveis?",
        "Alguma sugestão de acomodação eco-friendly por lá?",
        "Cite outras 20 cidades com características semelhantes às que descrevemos até agora. Rankeie por mais interessante, incluindo no meio ai a que você já sugeriu.",
        "Na primeira cidade que você sugeriu lá atrás, quero saber 5 restaurantes para visitar. Responda somente o nome da cidade e o nome dos restaurantes.",
]
memory = ConversationSummaryMemory(llm = llm)

conversation = ConversationChain(llm = llm,
                                 verbose = True,
                                 memory = memory)


for mensagem in mensagens:
    resposta = conversation.predict(input = mensagem)
    print(resposta)

print(memory.load_memory_variables({}))