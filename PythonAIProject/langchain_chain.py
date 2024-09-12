# Importa o ChatOpenAI da biblioteca langchain_openai, que faz a integração com o modelo GPT da OpenAI.
from langchain_openai import ChatOpenAI
# Importa as classes para criar templates de prompts (perguntas) para o modelo.
from langchain.prompts import PromptTemplate
from langchain.prompts import ChatPromptTemplate
# Importa LLMChain, que permite a integração entre o modelo de linguagem e o template.
from langchain.chains import LLMChain
# Importa SimpleSequentialChain, que permite criar cadeias de chamadas de modelo de forma sequencial.
from langchain.chains import SimpleSequentialChain
# Habilita o modo de debug para fornecer mais informações sobre o que está acontecendo no código.
from langchain.globals import set_debug
# Carrega a biblioteca os para manipulação de variáveis de ambiente.
import os
# Carrega a biblioteca dotenv para carregar variáveis de ambiente a partir de um arquivo .env.
from dotenv import load_dotenv
# Carrega as variáveis de ambiente do arquivo .env.
load_dotenv()
# Ativa o modo de debug para rastrear os processos da execução.
set_debug(True)

# Cria um template de prompt para sugerir uma cidade de acordo com o interesse do usuário.
modelo_cidade = ChatPromptTemplate.from_template(
    "Sugira uma cidade dado meu interesse por {interessse}. A sua saída deve ser somente o nome da cidade. Cidade:"
)

# Cria um template de prompt para sugerir restaurantes populares em uma determinada cidade.
modelo_restaurantes = ChatPromptTemplate.from_template(
    "Sugira restaurantes populares entre locais em {cidade}"
)

# Cria um template de prompt para sugerir atividades culturais em uma determinada cidade.
modelo_cultural = ChatPromptTemplate.from_template(
    "Sugira atividades e locais culturais em {cidade}"
)

# Inicializa o modelo GPT-3.5-turbo com temperatura de 0.5 e a chave da API OpenAI.
llm = ChatOpenAI(
    model ='gpt-3.5-turbo',
    temperature = 0.5, 
    api_key = os.getenv('OPENAI_API_KEY')  # Obtém a chave da API a partir das variáveis de ambiente
)

# Cria uma cadeia LLM para gerar o nome de uma cidade baseado no interesse do usuário.
cadeia_cidade = LLMChain(
    prompt = modelo_cidade, 
    llm=llm
)

# Cria uma cadeia LLM para sugerir restaurantes baseados na cidade gerada anteriormente.
cadeia_restaurantes = LLMChain(
    prompt = modelo_restaurantes, 
    llm=llm
)

# Cria uma cadeia LLM para sugerir atividades culturais na cidade.
cadeia_cultural = LLMChain(
    prompt = modelo_cultural, 
    llm=llm
)

# Cria uma cadeia sequencial que executa os prompts na ordem definida (cidade -> restaurantes -> cultura).
sequencia_cadeia_simples = SimpleSequentialChain(
    chains = [cadeia_cidade, cadeia_restaurantes, cadeia_cultural],
    verbose = True  # Exibe mais informações durante a execução
)

# Invoca a cadeia de prompts com o interesse 'praias' e imprime o resultado final.
resultado = sequencia_cadeia_simples.invoke("praias")
print(resultado)
