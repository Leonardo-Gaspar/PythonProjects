#I've used Google Colaboratory in this Course

# !pip install matplotlib


import numpy as np

import matplotlib
matplotlib.__version__

import matplotlib.pyplot as plt


estudantes = ["João","Maria","José"]
notas = [8.5, 9, 6.5]

plt.bar(x = estudantes, height = notas)

estudantes_2 = ["João","Maria","José", "Ana"]

#importando uma função especifica de uma biblioteca
from random import choice

estudantes = choice(estudantes_2)
print(estudantes)

lista = [8, 12, 54, 23, 43, 1, 90, 87, 105, 77]
lista_aleatoria = choice(lista)
print(lista_aleatoria)

notas = {
    '1° Trimestre': 8.5,
    '2° Trimestre': 9.5,
    '3° Trimestre': 7,
        }

# Calculano a soma
soma = 0

for nota in notas.values():
  soma += nota

print(soma)



#Usando função embutida "sum()"
somatorio = sum(notas.values())

print(somatorio)

#Usando função embutida "len()"
qtd_notas = len(notas)

print(qtd_notas)

#Calculando média
media = somatorio/qtd_notas

print(media)

help(round)

media = round(media,1)

print(media)

def media():
  calculo = (10 + 9 + 8)/3

  print(calculo)

media()

def media(nota_1, nota_2, nota_3):
  calculo = (nota_1 + nota_2 + nota_3)/3
  print(calculo)
media(3,6,9)

notas = [8.5, 9.0, 6.0, 10.0]

def media(lista):
  calculo = sum(lista) / len(lista)
  print(calculo)
media(notas)

resultado = media(notas)

print(resultado)

notas = [8.5, 9.0, 6.0, 10.0]

def media(lista):
  calculo = sum(lista) / len(lista)
  return(calculo)
media(notas)

resultado = media(notas)

print(resultado)

notas = [8.5, 9.0, 6.0, 10.0]

def boletim(lista):
  media = sum(lista) / len(lista)

  if media >=6:
    situacao = "aprovado(a)"
  else:
    situacao = "reprovado(a)"


  return (media, situacao)

print(boletim(notas))

media, situacao = boletim(notas)

media

situacao

print(f'O(a) estudante atingiu a media {media} e foi {situacao}')

#Comparando uma funcao de qualitativo no formato de funcao para funcao anonima

nota = float(input("Digite a nota do(a) estudante: "))

def qualitativo(x):
  return x + 0.5

qualitativo(nota)

#Testando a mesma funcao para uma funcao lambda

nota = float(input("Digite a nota do(a) estudante: "))

qualitativo = lambda x: x + 0.5

qualitativo(nota)

#Recebendo as notas e calculando a média ponderável
n1 = float(input("Digite a Primeira nota do(a) estudante: "))
n2 = float(input("Digite a Segunda nota do(a) estudante: "))
n3 = float(input("Digite a Terceira nota do(a) estudante: "))

media_ponderada = lambda x, y, z: (x*3 + y*2 + z*5)/10

media_estudante = media_ponderada(n1, n2, n3)

media_estudante

notas = [6.0, 7.0, 9.0, 5.5, 8.0]
qualitativo = 0.5

notas_atualizadas = map(lambda x: x + qualitativo, notas)

notas_atualizadas = list(notas_atualizadas)
notas_atualizadas

# EXERCICIO 6

notas_turma = ['João', 8.0, 9.0, 10.0, 'Maria', 9.0, 7.0, 6.0, 'José', 3.4, 7.0, 7.0, 'Cláudia', 5.5, 6.6, 8.0, 'Ana', 6.0, 10.0, 9.5]

nomes = []
notas_juntas = []

for i in range (len(notas_turma)):
  if i %  4 == 0:
    nomes.append(notas_turma[i])
  else:
    notas_juntas.append(notas_turma[i])

nomes

notas_juntas

notas = []

for i in range(0, len(notas_juntas), 3):
  notas.append([notas_juntas[i], notas_juntas[i + 1], notas_juntas[i + 2]])

notas

#Pesquisando por dentro da lista

notas [0]
notas[0][2]

# ***Exercicio 7***

estudantes = ['João', 'Maria', 'José', 'Cláudia', 'Ana']
estudantes

from random import randint

def gera_codigo():
  return str(randint(0,999))

codigo_estudantes = []

for i in range(len(estudantes)):
  codigo_estudantes.append((estudantes[i], estudantes[i][0] + gera_codigo()))
codigo_estudantes

## ***Exercicio 8 ***

# utilizar formato:

(expressao for item in lista)

notas = [[8.0, 9.0, 10.0], [9.0, 7.0, 6.0], [3.4, 7.0, 7.0], [5.5, 6.6, 8.0], [6.0, 10.0, 9.5]]

def media(lista: list=[0]) -> float:
  '''Função para calcular a média de notas passadas por uma lista '''

  calculo = sum(lista) / len(lista)

  return calculo

medias = [round(media(nota), 1) for nota in notas]
medias


# ***Exercicio 9***

# Usar a expressão

[expressao for item in lista if condi]


nomes = [('João', 'J814'), ('Maria', 'M353'), ('José', 'J344'), ('Cláudia', 'C92'), ('Ana', 'A365')]
medias = [9.0, 7.3, 5.8, 6.7, 8.5]

#Gerando a lista de nomes (extraindo da tupla)

nomes = [nome[0] for nome in nomes]
nomes

estudantes = list(zip(nomes, medias))
estudantes

#Gerando lista de pessoas candidatas à bolsa

candidatos = [estudante[0] for estudante in estudantes if estudante[1] >= 8.0]
candidatos

# ***Exercício 10 ***

# Usar a expressão

[resultado_if if cond else resultado_else for item in lista]

nomes = [('João', 'J814'), ('Maria', 'M353'), ('José', 'J344'), ('Cláudia', 'C92'), ('Ana', 'A365')]
notas = [[8.0, 9.0, 10.0], [9.0, 7.0, 6.0], [3.4, 7.0, 7.0], [5.5, 6.6, 8.0], [6.0, 10.0, 9.5]]
medias = [9.0, 7.3, 5.8, 6.7, 8.5]

situacao = ["Aprovado" if media >= 6 else "Reprovado" for media in medias]
situacao

cadastro = [x for x in [nomes, notas, medias, situacao]]
cadastro

lista_completa = [nomes, notas, medias, situacao]
lista_completa

# ***Exercício 11***

#Expressão usado

# [chave: valor for item in lista]

lista_completa = [
 [('João', 'J814'),('Maria', 'M353'),('José', 'J344'), ('Cláudia', 'C92'), ('Ana', 'A365')],
 [[8.0, 9.0, 10.0], [9.0, 7.0, 6.0], [3.4, 7.0, 7.0], [5.5, 6.6, 8.0], [6.0, 10.0, 9.5]],
 [9.0, 7.3, 5.8, 6.7, 8.5],
 ['Aprovado', 'Aprovado', 'Reprovado', 'Aprovado', 'Aprovado']]

#Coluna com os tipos de dados (exceto nome)

coluna = ["Notas", "Média Final", "Situação"]

cadastro = {coluna[i]: lista_completa[i + 1] for i in range(len(coluna))}
cadastro



#Adicionar o nome dos estudantes, extraindo apenas seus nomes

cadastro["Estudante"] = [lista_completa[0][i][0] for i in range(len(lista_completa[0]))]
cadastro

# ***Exercicio 12***

notas = {
  'João': [8.0, 9.0, 10.0],
  'Maria' : [9.0, 7.0, 6.0],
  'José' : [3.4, 7.0, 7.0],
  'Cláudia' : [5.5, 6.6, 8.0],
  'Ana' : [6.0, 10.0, 9.5],
  'Joaquim' : [5.5, 7.5, 9.0],
  'Júlia' : [6.0, 8.0, 7.0],
  'Pedro' : [3.0, 4.0, 6.0]
}

# ***Exercício 13***

try:
  nome = input("Digite o nome do estudante: ")
  resultado = notas[nome]
except KeyError as e:
  print(type(e), f'Erro: {e}')
  print("Estudante não matriculado na turma")
else:
  print(resultado)

# ***Exercício 14***

try:
  nome = input("Digite o nome do estudante: ")
  resultado = notas[nome]
except KeyError as e:
  print(type(e), f'Erro: {e}')
  print("Estudante não matriculado na turma")
else:
  print(resultado)
finally:
  print("A consulta foi encerrada!")

# ***Exercício 15***

def media(lista: list=[0]) -> float:
  ''' Função para calcular a média de notas passadas por uma lista

  lista: list, default[0]
    Lista com as notas para calcular a média
    return calculo: float
    Média calculada
  '''

  calculo =  sum(lista) / len(lista)
  if len(lista) > 4:
    raise ValueError("A lista não pode possuir mais que 4 notas")
  return calculo

try:
  notas = [6, 7, 8, 9]
  resultado = media(notas)
except TypeError:
  print("Não foi possível calcular a média do estudante. Só aceito valores numéricos")
except ValueError as e:
  print(e)
else:
  print(resultado)
finally:
  print("A consulta foi encerrada")


try:
  notas = [6, 7, 8, 9, 8]
  resultado = media(notas)
except TypeError:
  print("Não foi possível calcular a média do estudante. Só aceito valores numéricos")
except ValueError as e:
  print(e)
else:
  print(resultado)
finally:
  print("A consulta foi encerrada")

try:
  notas = [6, 7, 8, 9, "8"]
  resultado = media(notas)
except TypeError:
  print("Não foi possível calcular a média do estudante. Só aceito valores numéricos")
except ValueError as e:
  print(e)
else:
  print(resultado)
finally:
  print("A consulta foi encerrada")

# ***Iniciando Curso Numpy***

# ***Carregando dados***

import numpy as np

dado = np.loadtxt('apples_ts.csv', delimiter = ',', usecols= np.arange(1, 88, 1) )

dado

#ndim: serve para verificar as dimensões dos dados
dado.ndim #2 dimensões (linhas e colunas)

#size: verifica a quantidade de elementos de um array
dado.size

#shape: verifica o número de elementos em cada dimensão
dado.shape #(6,87) 6 linhas e 87 colunas

# T: Realiza a transposição do array
dado_transposto = dado.T

datas = dado_transposto[:,0]

precos = dado_transposto[:,1:6]

import matplotlib.pyplot as plt


datas = np.arange(1,88,1)

plt.plot(datas, precos[:,0])

#Atribuindo os valores às cidades

Moscow = precos[:,0]
Kaliningrad = precos[:,1]
Petersburg = precos[:,2]
Krasnodar = precos[:,3]
Ekaterinburg = precos[:,4]

Moscow

Moscow.shape

#Separando os preços por ano

Moscow_ano1 = Moscow[0:12]
Moscow_ano2 = Moscow[12:24]
Moscow_ano3 = Moscow[24:36]
Moscow_ano4 = Moscow[36:48]


#Visualizando os dados selecionados
plt.plot(np.arange(1,13,1),Moscow_ano1)
plt.plot(np.arange(1,13,1),Moscow_ano2)
plt.plot(np.arange(1,13,1),Moscow_ano3)
plt.plot(np.arange(1,13,1),Moscow_ano4)
#Função legend: Adiciona a um gráfico
plt.legend(['Ano1','Ano2','Ano3','Ano4'])

#Comparando arrays iguais ou próximos
#array_equal: Verifica se dois arrays são iguais
np.array_equal(Moscow_ano3, Moscow_ano4)

#allclose: Verifica se arrays são próximos( dentro de um intervalo)
np.allclose(Moscow_ano3,Moscow_ano4, 10)

plt.plot(datas, Kaliningrad)

#isnan: Verifica valores não numéricos
np.isnan(Kaliningrad)
sum(np.isnan(Kaliningrad))

(Kaliningrad[3] + Kaliningrad[5])/2

#Para preencher o espaço em branco que havia no gráfico (Nan)
Kaliningrad[4] = np.mean([Kaliningrad[3] , Kaliningrad[5]])

#Comparando as médias de preço de duas cidades
np.mean(Moscow)

np.mean(Kaliningrad)

plt.plot(datas, Moscow)

#Ajustando a reta para entender a taxa de crescimento do preço das maçãs
x = datas
y = 2*x+80

plt.plot(datas,Moscow)
plt.plot(x,y)

#power: Eleva valores a uma potencia
np.sum(np.power(Moscow-y,2))

np.sqrt(np.sum(np.power(Moscow-y,2)))

y = 0.52*x+80

plt.plot(datas,Moscow)
plt.plot(x,y)

np.sqrt(np.sum(np.power(Moscow-y,2)))

np.linalg.norm(Moscow-y)

y= Moscow
x = datas
n = np.size(Moscow)

(x**2).shape

a = (n*np.sum(x*y) - np.sum(x)*np.sum(y))/ (n*np.sum(x**2) - np.sum(x)**2)

# ***Coenficiente linear***

b = np.mean(y) - a*np.mean(x)

y = a*x+b

np.linalg.norm(Moscow - y)

plt.plot(datas,Moscow)
plt.plot(x,y)

# ***Estimativa de valor***

plt.plot(datas,Moscow)
plt.plot(x,y)
plt.plot(41.5,41.5*a+b,'*r')

# ***Estimando valores futuros***

plt.plot(datas,Moscow)
plt.plot(x,y)
plt.plot(100,100*a+b,'*r')

#random.randint: Gera números inteiros aleatórios
np.random.randint(low =40, high = 100, size = 100)

#random.uniform
coef_angulares = np.random.uniform(low = 0.10, high =0.90, size = 100)

norma = np.array([])
for i in range(100):
  norma = np.append(norma,np.linalg.norm(Moscow-(coef_angulares[i]*x+b)))
  print(norma)

coef_angulares[1]

np.random.uniform(low = 0.10, high =0.90, size = 100)

#random.seed: seleciona um número semente fixo para inicializar o gerador aleatório
np.random.seed(16)
np.random.uniform(low = 0.10, high =0.90, size = 100)

np.random.seed(84)
np.random.uniform(low = 0.10, high =0.90, size = 100)

norma = np.array([])
for i in range(100):
  norma = np.append(norma,np.linalg.norm(Moscow-(coef_angulares[i]*x+b)))

# ***Salvando Resultados***

norma

coef_angulares

#np.column_stack: Une dois ou mais arrays, lado a lado como colunas, em uma matriz

dados = np.column_stack([norma, coef_angulares])

dados.shape

#savetxt: Salva um array em um arquivo de texto

np.savetxt('dados.csv', dados, delimiter=',')

# ***Iniciando Curso Pandas Alura***

#Projeto Imobiliária

# !pip install pandas

import pandas as pd

url = 'https://github.com/alura-cursos/pandas-conhecendo-a-biblioteca/blob/main/base-de-dados/aluguel.csv'

dados = pd.read_csv('aluguel.csv', sep = ';')

dados.head(10) #10 primeiros dados da tabela

dados.tail(10) #10 Últimos dados da tabela

type(dados)

# ***Características gerais da base de dadoss***

dados.shape

dados.columns

dados.info()

dados['Tipo']

dados[['Quartos', 'Valor']]

# ***Análise exploratória de dados***

# **Qual valor médio de aluguel por tipo de imóvel**

dados['Valor'].mean()

#groupby: Agrupando os dados
dados.groupby('Tipo')[['Valor']].mean().sort_values('Valor')

df_preco_tipo = dados.groupby('Tipo')[['Valor']].mean().sort_values('Valor')

df_preco_tipo.plot(kind = 'barh', figsize = (14,10), color = 'purple')

# ***Removendo os imóveis comerciais***

dados.Tipo.unique()

imoveis_comerciais = ['Conjunto Comercial/Sala',
                      'Prédio Inteiro', 'Loja/Salão',
                      'Galpão/Depósito/Armazém',
                      'Casa Comercial', 'Terreno Padrão',
                      'Loja Shopping/ Ct Comercial',
                      'Box/Garagem', 'Chácara',
                      'Loteamento/Condomínio', 'Sítio',
                      'Pousada/Chalé', 'Hotel', 'Indústria']


dados.query('@imoveis_comerciais in Tipo')

dados.query('@imoveis_comerciais not in Tipo')

df_tipo_imoveis = dados.query('@imoveis_comerciais not in Tipo')

df_tipo_imoveis.head()

df_tipo_imoveis.Tipo.unique()

df_preco_tipo = df_tipo_imoveis.groupby('Tipo')[['Valor']].mean().sort_values('Valor')

df_preco_tipo.plot(kind = 'barh', figsize = (14,10), color = 'purple')

# ***Qual o percentual de cada tipo de imóvel na nossa base de dados***

df_tipo_imoveis.Tipo.unique()

df_tipo_imoveis.Tipo.value_counts()

df_tipo_imoveis.Tipo.value_counts(normalize=True).to_frame().sort_values('Tipo')

df_percentual_tipo = df_tipo_imoveis.Tipo.value_counts(normalize=True).to_frame().sort_values('Tipo')

df_percentual_tipo.plot(kind ='bar', figsize = (14,10), color = 'green', xlabel = 'Tipos', ylabel = 'Percentual')

df_percentual_tipo.query('Tipo == "Apartamento"')

df_tipo_imoveis.query('Tipo == "Apartamento"')

df = df_tipo_imoveis.query('Tipo == "Apartamento"')
df.head()

# ***Tratando e filtrando os dados ***

# **Lidando com dados nulos**

df.isnull()

df.isnull().sum()

#fillna: completa dados NA
df = df.fillna(0)

df.isnull().sum()

# ***Removendo Registros***

df.query('Valor == 0 | Condominio == 0')

registros_a_remover = df.query('Valor == 0 | Condominio == 0').index

registros_a_remover

df.drop(registros_a_remover, axis = 0, inplace = True)

df.head()

df.Tipo.unique()

df.drop('Tipo', axis=1, inplace = True)

df.head()

# ***Filtros***

# Apartamentos que possuem 1 quarto e alugal menor que 1200

df['Quartos'] == 1

selecao1 = df['Quartos'] == 1
df[selecao1]

selecao2 = df['Valor'] < 1200
df[selecao2]

selecao_final = (selecao1) & (selecao2)
df[selecao_final]

df_1 = df[selecao_final]

# Filtro 2

selecao_1 = df['Quartos'] == 2

selecao_2 = df['Valor'] < 3000

selecao_3 = df['Area'] > 70

selecao_final = (selecao_1) & (selecao_2) & (selecao_3)
df[selecao_final]

# ou podemos fazer

selecao = (df['Quartos'] >= 2) & (df['Valor'] < 3000) & (df['Area'] > 70)
df[selecao]

# ***Salvando os dados tratados***

df.to_csv('dados_apartamentos.csv')

pd.read_csv('dados_apartamentos.csv') #surgiu um "unnamed: 0"

df.to_csv('dados_apartamentos.csv', index = False) #Retiramos o índice criado

pd.read_csv('dados_apartamentos.csv')

df.to_csv('dados_apartamentos.csv', index = False, sep = ';') #trocando a separação de dados, de vírgula para ponto e vírgula

pd.read_csv('dados_apartamentos.csv')

pd.read_csv('dados_apartamentos.csv', sep = ';')

# ***Criando colunas numéricas***

url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'
dados = pd.read_csv(url, sep=';')
dados.head()

dados['Valor_por_mes'] = dados['Valor'] + dados['Condominio'] #Criando coluna "Valor_por_mes"
dados.head()

dados['Valor_por_ano'] = dados['Valor_por_mes'] *12 + dados['IPTU']   #Criando coluna "Valor_por_ano"
dados.head()

# ***Criando coluna categorica***

dados['Descricao'] = dados['Tipo'] + ' em ' + dados['Bairro']
dados.head()

dados['Descricao'] = dados['Tipo'] + ' em ' + dados['Bairro'] + ' com ' + \
                                        dados['Quartos'].astype(str) + ' quarto(s) ' + \
                                        ' e ' + dados['Vagas'].astype(str) + ' vaga(s) de garagem.'
dados.head()

# ***Criação da coluna binária***

dados['Possui_suite'] = dados['Suites'].apply(lambda x: "Sim" if x > 0 else "Não")
dados.head()

dados.to_csv('dados_completos_dev.csv', index = False, sep = ';')

# ***Pandas I/O***

import pandas as pd

# https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html

url = 'https://raw.githubusercontent.com/alura-cursos/pandas/main/superstore_data.csv'
dados_mercado = pd.read_csv(url)
dados_mercado.head()

url_2 = 'https://raw.githubusercontent.com/alura-cursos/Pandas/main/superstore_data_ponto_virgula.csv'
dados_ponto_virgula = pd.read_csv(url_2, sep = ';')
dados_ponto_virgula.head()

# Função nrows = leitura de numero especifico de linhas

dados_primeiras_linhas = pd.read_csv(url, nrows = 5)
dados_primeiras_linhas

# Função usecols = leitura de colunas especificas  

dados_selecao = pd.read_csv(url, usecols = ['Id', 'Year_Birth', 'Income'])
dados_selecao

#usando o índice
dados_selecao = pd.read_csv(url, usecols = [0, 1, 4])
dados_selecao

# 'index = False': Para retirar a introdução automática do index

dados_selecao.to_csv('clientes_mercado.csv', index = False)

clientes_mercado = pd.read_csv('/content/clientes_mercado.csv')
clientes_mercado

# Lendo arquivo Excel


url = 'https://github.com/alura-cursos/Pandas/blob/main/emissoes_CO2.xlsx?raw=True'
dados_co2 = pd.read_excel(url)
dados_co2.head()

# Visualizar se há diversas planilhas dentro desses dados do excel

pd.ExcelFile(url).sheet_names

# https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html

percapita = pd.read_excel(url, sheet_name = 'emissoes_percapita')
percapita.head()

fontes = pd.read_excel(url, sheet_name = 'fontes')
fontes.head()

intervalo = pd.read_excel(url, sheet_name = 'emissoes_C02', usecols = 'A:D' )
intervalo

intervalo_2 = pd.read_excel(url, sheet_name = 'emissoes_C02', usecols = 'A:D', nrows = 10 )
intervalo_2

percapita.to_excel('co2_percapita.xlsx', index = False)

# lendo dados do google planilha

'https://docs.google.com/spreadsheets/d/1lzq0k-41-MbbS63C3Q9i1wPvLkSJt9zhr4Jolt1vEog/edit?usp=sharing'

sheet_id = '1lzq0k-41-MbbS63C3Q9i1wPvLkSJt9zhr4Jolt1vEog'

url = f'https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet'

dados_co2_sheets = pd.read_csv(url)

dados_co2_sheets

sheet_id = '1lzq0k-41-MbbS63C3Q9i1wPvLkSJt9zhr4Jolt1vEog'
sheet_name = 'emissoess_percapita'
url_percapita = f'https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}'

percapita_sheets = pd.read_csv(url_percapita)
percapita_sheets.head()

sheet_id = '1lzq0k-41-MbbS63C3Q9i1wPvLkSJt9zhr4Jolt1vEog'
sheet_name = 'fontes'
url_fontes = f'https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}'

fontes_sheets = pd.read_csv(url_fontes)
fontes_sheets.head()

# Lendo arquivo Json

dados_pacientes = pd.read_json('/content/pacientes.json')
dados_pacientes

dados_pacientes_2 = pd.read_json('/content/pacientes_2.json')
dados_pacientes_2

df_normalizado = pd.json_normalize(dados_pacientes_2['Pacientes'])
df_normalizado

#Salvando em formato json
df_normalizado.to_json('historico_pacientes_normalizado.json')

# Sabendo mais sobre normalização

dados = {'Pesquisa': 'Principais Indicadores de Doenca Cardiaca', 'Ano': 2020, 'Numero_Pacientes':3}
df = pd.json_normalize(dados)
df

json_lista = [
    { 'ID': '01', 'Faixa_etaria': '55-59', 'Sexo_biologico': 'feminino'},
    { 'ID': '02', 'Faixa_etaria': '80 ou +', 'Sexo_biologico': 'feminino'}
]
pd.json_normalize(json_lista)


json_obj = {
    'ID': '01',
    'Faixa_etaria': '55-59',
    'Sexo_biologico': 'Feminino',
    'Saude': {'Dificuldade_caminhar': 'Nao',
              'Atividade_fisica': 'Sim',
              'IMC': 16.6,
              'Doenca_cardiaca': 'Nao',
          }
      }
pd.json_normalize(json_obj)


json_list = [
    {
    'ID': '01',
    'Faixa_etaria': '55-59',
    'Sexo_biologico': 'Feminino',
    'Saude': {'Dificuldade_caminhar': 'Nao',
              'Atividade_fisica': 'Sim',
              'IMC': 16.6,
              'Doenca_cardiaca': 'Nao',
          }
      },
      {
          'ID': '02',
          'Faixa_etaria': '80 ou +',
          'Sexo_biologico': 'Feminino',
          'Saude': {'Dificuldade_caminhar': 'Nao',
                    'Atividade_fisica': 'Sim',
                    'IMC': 20.34,
                    'Doenca_cardiaca': 'Sim'}
       }
       ]
pd.json_normalize(json_list)


dados_dict = {
  "Pesquisa": "Principais Indicadores de Doenca Cardiaca",
  "Ano": 2020,
  "Pacientes": [
    {
      "ID": "01",
      "Faixa_etaria": "55-59",
      "Sexo_biologico": "Feminino",
      "Raça": "Branca",
      "IMC": 16.6,
      "Fumante": "Sim",
      "Consumo_alcool": "Nao",
      "Saude_fisica": 3,
      "Saude_mental": 30,
      "Dificuldade_caminhar": "Nao",
      "Atividade_fisica": "Sim",
      "Saude_geral": "Muito boa",
      "Horas_sono": 5,
      "Problemas_saude": [
        "Diabetes",
        "Asma",
        "Cancer_pele"
      ]
    },
    {
      "ID": "02",
      "Faixa_etaria": "80 ou +",
      "Sexo_biologico": "Feminino",
      "Raça": "Branca",
      "IMC": 20.34,
      "Fumante": "Nao",
      "Consumo_alcool": "Nao",
      "Saude_fisica": 0,
      "Saude_mental": 0,
      "Dificuldade_caminhar": "Nao",
      "Atividade_fisica": "Sim",
      "Saude_geral": "Muito boa",
      "Horas_sono": 7,
      "Problemas_saude": [
        "AVC"
      ]
    },
    {
      "ID": "03",
      "Faixa_etaria": "65-69",
      "Sexo_biologico": "Masculino",
      "Raça": "Branca",
      "IMC": 26.58,
      "Fumante": "Sim",
      "Consumo_alcool": "Nao",
      "Saude_fisica": 20,
      "Saude_mental": 30,
      "Dificuldade_caminhar": "Nao",
      "Atividade_fisica": "Sim",
      "Saude_geral": "Muito boa",
      "Horas_sono": 8,
      "Problemas_saude": [
        "diabetes",
        "Asma"
      ]
    }
  ]
}
pd.json_normalize(dados_dict)


pd.json_normalize(dados_dict['Pacientes'])



pd.json_normalize(dados_dict, record_path=['Pacientes'])


pd.json_normalize(
    dados_dict,
    record_path =['Pacientes'],
    meta=['Pesquisa', 'Ano']
)


import json

with open('pacientes_2.json','r') as f:
    dados = json.loads(f.read())

pd.json_normalize(dados, record_path='Pacientes', meta=['Pesquisa', 'Ano'])


#Fazendo leituras de página web (HTML)

dados_html = pd.read_html('/content/filmes_wikipedia.html')
dados_html

type(dados_html)

len(dados_html)

top_filmes = dados_html[1]
top_filmes

#Fazendo download do arquivo em html
top_filmes.to_html('top_filmes.html')

top_filmes.to_csv('top_filmes_1998.csv', index = False)

pd.read_csv('top_filmes_1998.csv')

# Fazendo leitura em XML

dados_imdb = pd.read_xml('/content/imdb_top_1000.xml')
dados_imdb.head(3)

dados_imdb.to_xml('filmes_imdb.xml')

# Tratando com banco de dados

import pandas as pd
import sqlalchemy

sqlalchemy.__version__

# pip install --upgrade 'sqlalchemy<2.0'

from sqlalchemy import create_engine, MetaData, Table, inspect

engine = create_engine('sqlite:///:memory:')

url = 'https://raw.githubusercontent.com/alura-cursos/Pandas/main/clientes_banco.csv'
dados = pd.read_csv(url)
dados.head()

dados.to_sql('clientes', engine, index = False)

inspector = inspect(engine)
inspector.get_table_names()

query = 'SELECT * from clientes WHERE Categoria_de_renda = "Empregado"'
empregados = pd.read_sql(query, engine)
empregados

empregados.to_sql('empregados', con = engine, index = False)

pd.read_sql_table('empregados', engine)

pd.read_sql_table('empregados', engine, columns = ['ID_Cliente', 'Grau_escolaridade', 'Rendimento_anual'])

query = 'SELECT * from clientes'

pd.read_sql(query, engine)

query = 'DELETE FROM clientes WHERE ID_Cliente = 5008804'
with engine.connect() as conn:
  conn.execute(query)

pd.read_sql_table('clientes', engine)

query = 'UPDATE clientes SET Grau_escolaridade = "Ensino Superior" WHERE ID_Cliente = 5008808	'
with engine.connect() as conn:
  conn.execute(query)

pd.read_sql_table('clientes', engine)

# ***Pandas: Selecionando e agrupando dados***

import pandas as pd

emissoes_gases = pd.read_excel("/content/1-SEEG10_GERAL-BR_UF_2022.10.27-FINAL-SITE.xlsx", sheet_name = 'GEE Estados')

emissoes_gases

emissoes_gases.info()

# Ajustando os Dados

emissoes_gases['Emissão / Remoção / Bunker'].unique()

# filtrando dados de 'Remoção'

(emissoes_gases['Emissão / Remoção / Bunker'] == 'Remoção NCI') | (emissoes_gases['Emissão / Remoção / Bunker'] == 'Remoção')

# Método ***isin***, seleciona valores dentro de outros valores

emissoes_gases[emissoes_gases['Emissão / Remoção / Bunker'].isin(['Remoção NCI', 'Remoção'])]

# Deram valores negativos, como o esperado, agora iremos verificar se todos deram realmente negativo, para confirmar a filtragem dos dados

# função 'loc', utilizada para ver nao so colunas, como as linhas também

emissoes_gases.loc[emissoes_gases['Emissão / Remoção / Bunker'].isin(['Remoção NCI', 'Remoção']), 1970:2021]

# função 'max', para extrair o máximo de todas as colunas

emissoes_gases.loc[emissoes_gases['Emissão / Remoção / Bunker'].isin(['Remoção NCI', 'Remoção']), 1970:2021].max()

emissoes_gases.loc[emissoes_gases['Emissão / Remoção / Bunker'] == 'Bunker', 'Estado'].unique()

emissoes_gases = emissoes_gases[emissoes_gases['Emissão / Remoção / Bunker'] == 'Emissão']
emissoes_gases

emissoes_gases = emissoes_gases.drop(columns = 'Emissão / Remoção / Bunker')
emissoes_gases

# ***Modificando o formato do DataFrame***

emissoes_gases.loc[:,'Nível 1 - Setor': 'Produto'].columns

colunas_info = list(emissoes_gases.loc[:,'Nível 1 - Setor': 'Produto'].columns)
colunas_info

emissoes_gases.loc[:, 1970:2021].columns

colunas_emissao = list(emissoes_gases.loc[:, 1970:2021].columns)
colunas_emissao

# Função melt, transforma formato amplo(wide) em longo(long)

emissoes_gases.melt(id_vars = colunas_info, value_vars = colunas_emissao, var_name = 'Ano', value_name = 'Emissão')

emissoes_por_ano = emissoes_gases.melt(id_vars = colunas_info, value_vars = colunas_emissao, var_name = 'Ano', value_name = 'Emissão')
emissoes_por_ano

emissoes_por_ano.groupby('Gás')

emissoes_por_ano.groupby('Gás').groups

emissoes_por_ano.groupby('Gás').get_group('CO2 (t)')