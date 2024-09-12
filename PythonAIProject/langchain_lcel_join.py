#LangChain Expression Language (LCEL) Project
'''
Características principais do LCEL

-Suporte a streaming: melhora o tempo até a primeira saída, sendo ideal para processamento em tempo real.

-Suporte assíncrono: permite execução tanto síncrona quanto assíncrona, adequada para prototipagem e produção.

-Execução paralela otimizada: executa etapas paralelas automaticamente para reduzir a latência.

-Retentativas e alternativas: melhora a confiabilidade em escala com configurações de retentativa e alternativa.

-Acesso a resultados intermediários: permite monitoramento e depuração em cadeias complexas.

-Esquemas de entrada e saída: facilita a validação com esquemas Pydantic e JSONSchema.

-Integração com Langsmith e Langserve: oferece observabilidade e facilita a implantação.
'''

# Importa o ChatOpenAI da biblioteca langchain_openai, que faz a integração com o modelo GPT da OpenAI.
from langchain_openai import ChatOpenAI
# Importa as classes para criar templates de prompts (perguntas) para o modelo.
from langchain.prompts import PromptTemplate
from langchain.prompts import ChatPromptTemplate
# Habilita o modo de debug para fornecer mais informações sobre a execução do código.
from langchain.globals import set_debug
# Biblioteca para manipulação de variáveis de ambiente.
import os
# Carrega a biblioteca dotenv para carregar variáveis de ambiente de um arquivo .env.
from dotenv import load_dotenv
# Importa a classe BaseModel e o Field para definir modelos de dados usando Pydantic.
from langchain_core.pydantic_v1 import Field, BaseModel
# Importa o JsonOutputParser para fazer o parsing (conversão) da saída do modelo para JSON usando Pydantic.
from langchain_core.output_parsers import JsonOutputParser, StrOutputParser
#importa  a biblioteca operator a qual puxa itemgetter, que pega uma variavel ja utilizada para extrair
from operator import itemgetter
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

# Cria um template de prompt para devolver um modelo final ao usuario
modelo_final = ChatPromptTemplate.from_messages([ 
    ("ai", "Sugestão de viagem para a cidade: {cidade}"),
    ("ai", "Restaurantes que voce não ode perder: {restaurantes}"),
    ("ai", "Atividades e locais culturais: {locais_culturais}"),
    ("system", "combine as informações anteriores em 2 parágrafos coerentes")
])


#Faz com que o modelo passe pelo llm e vá ao parseador automáticamente
parte1 = modelo_cidade | llm | parseador
parte2 = modelo_restaurantes | llm | StrOutputParser()
parte3 = modelo_cultural | llm | StrOutputParser()
resposta_final = modelo_final | llm | StrOutputParser()

#Junta a cadeia e torna em uma sequência
cadeia = (parte1 | 
          {
            "restaurantes" : parte2,
            "locais_culturais" : parte3,
            "cidade": itemgetter("cidade")
            } | resposta_final)


# Invoca a cadeia de prompts 
resultado = cadeia.invoke({"interesse":"praias"})
print(resultado)