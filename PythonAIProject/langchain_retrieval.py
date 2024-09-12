# Importa o ChatOpenAI da biblioteca langchain_openai, que faz a integração com o modelo GPT da OpenAI.
from langchain_openai import ChatOpenAI
# Habilita o modo de debug para fornecer mais informações sobre a execução do código.
from langchain.globals import set_debug

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA

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

carregador = TextLoader("GTB_gold_Nov23.txt", encoding = "utf-8")
documentos = carregador.load()

quebrador = CharacterTextSplitter(chunk_size=1000, chunk_overlap = 200)
textos = quebrador.split_documents(documentos)

embeddings = OpenAIEmbeddings()
db = FAISS.from_documents(textos, embeddings)

qa_chain = RetrievalQA.from_chain_type(llm, retriever = db.as_retriever())

pergunta = "Como devo proceder caso tenha um item comprado roubado"
resultado = qa_chain.invoke({'query': pergunta})
