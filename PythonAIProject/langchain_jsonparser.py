# Importa o ChatOpenAI da biblioteca langchain_openai, que faz a integração com o modelo GPT da OpenAI.
from langchain_openai import ChatOpenAI
# Importa as classes para criar templates de prompts (perguntas) para o modelo.
from langchain.prompts import PromptTemplate
from langchain.prompts import ChatPromptTemplate
# Importa SimpleSequentialChain, que permite criar cadeias de chamadas de modelo de forma sequencial.
from langchain.chains import SimpleSequentialChain
# Importa LLMChain, que permite a integração entre o modelo de linguagem e o template.
from langchain.chains import LLMChain
# Habilita o modo de debug para fornecer mais informações sobre a execução do código.
from langchain.globals import set_debug
# Biblioteca para manipulação de variáveis de ambiente.
import os
# Carrega a biblioteca dotenv para carregar variáveis de ambiente de um arquivo .env.
from dotenv import load_dotenv
# Importa a classe BaseModel e o Field para definir modelos de dados usando Pydantic.
from langchain_core.pydantic_v1 import Field, BaseModel
# Importa o JsonOutputParser para fazer o parsing (conversão) da saída do modelo para JSON usando Pydantic.
from langchain_core.output_parsers import JsonOutputParser
# Carrega as variáveis de ambiente do arquivo .env.
load_dotenv()
# Ativa o modo de debug para rastrear os processos da execução.
set_debug(True)

# Define uma classe Destino usando Pydantic para especificar o formato dos dados de saída.
class Destino(BaseModel):
    cidade = Field("cidade a visitar")  # Define o campo cidade.
    motivo = Field("motivo pelo qual é interessante visitar")  # Define o campo motivo.

# Inicializa o modelo GPT-3.5-turbo com temperatura de 0.5 e a chave da API OpenAI.
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.5,
    api_key=os.getenv("OPENAI_API_KEY")  # Obtém a chave da API do arquivo .env
)

# Cria um parseador que converte a resposta do modelo em um formato JSON baseado na classe Destino.
parseador = JsonOutputParser(pydantic_object=Destino)

# Cria um template de prompt para sugerir uma cidade com base no interesse do usuário e o formato de saída.
modelo_cidade = PromptTemplate(
    template="""Sugira uma cidade dado meu interesse por {interesse}.
    {formatacao_de_saida}
    """,
    input_variables=["interesse"],  # Variável que será substituída pelo interesse fornecido pelo usuário.
    partial_variables={"formatacao_de_saida": parseador.get_format_instructions()},  # Instruções de formatação JSON.
)

# Cria um template de prompt para sugerir restaurantes populares em uma determinada cidade.
modelo_restaurantes = ChatPromptTemplate.from_template(
    "Sugira restaurantes populares entre locais em {cidade}"
)

# Cria um template de prompt para sugerir atividades culturais em uma determinada cidade.
modelo_cultural = ChatPromptTemplate.from_template(
    "Sugira atividades e locais culturais em {cidade}"
)

# Cria uma cadeia LLM para gerar o nome de uma cidade baseado no interesse do usuário.
cadeia_cidade = LLMChain(
    prompt=modelo_cidade,
    llm=llm
)

# Cria uma cadeia LLM para sugerir restaurantes baseados na cidade gerada anteriormente.
cadeia_restaurantes = LLMChain(
    prompt=modelo_restaurantes,
    llm=llm
)

# Cria uma cadeia LLM para sugerir atividades culturais na cidade.
cadeia_cultural = LLMChain(
    prompt=modelo_cultural,
    llm=llm
)

# Cria uma cadeia sequencial que executa as chamadas de modelo em sequência: cidade -> restaurantes -> cultura.
cadeia = SimpleSequentialChain(
    chains=[cadeia_cidade, cadeia_restaurantes, cadeia_cultural],
    verbose=True  # Exibe mais informações durante a execução.
)

# Invoca a cadeia de prompts com o interesse 'praias' e imprime o resultado final.
resultado = cadeia.invoke("praias")
print(resultado)
