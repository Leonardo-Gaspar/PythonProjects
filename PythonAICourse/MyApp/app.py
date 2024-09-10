#Implementando imports
import os

#criando uma lista com dicionários para os restaurantes
restaurantes = [
    {'nome': 'Praça', 'categoria': 'Japonesa', 'ativo': False},
    {'nome': 'Pizza Suprema', 'categoria': 'Pizza', 'ativo': True},
    {'nome': 'Cantina', 'categoria': 'Italiano', 'ativo': False}
]

#Iniciando meu programa com um Título
def exibir_nome_programa():
    print("""
        𝕊𝕒𝕓𝕠𝕣 𝔼𝕩𝕡𝕣𝕖𝕤𝕤
        \n""")
#Função para exibir o Menu
def exibir_opcoes():
    ''' Exibe as opções disponíveis no menu principal '''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar/Desativar restaurantes')
    print('4. Sair')
    
#Função para finalizar meu programa
def finalizar_app():
    ''' Exibe mensagem de finalização do aplicativo '''
    exibir_subtitulo('Finalizando app')

#Função para retornar ao menu principal
def voltar_menu_principal():
    ''' Solicita uma tecla para voltar ao menu principal 
    
    Outputs:
    - Retorna ao menu principal
    '''
    input('Digite uma tecla pra voltar ao menu principal: ')
    main()
    
#Função para opção inválida
def opcao_invalida():
    ''' Exibe mensagem de opção inválida e retorna ao menu principal 
    
    Outputs:
    - Retorna ao menu principal
    '''
    print('Opção inválida!\n')
    voltar_menu_principal() 

#Função para limpar o terminal e exibir os subtitulos
def exibir_subtitulo(texto):
    ''' Exibe um subtítulo estilizado na tela 
    
    Inputs:
    - texto: str - O texto do subtítulo
    '''
    os.system('cls')
    linha_personalizacao = '*' * (len(texto))
    print(linha_personalizacao)
    print(texto)
    print(linha_personalizacao)
    print()
    
#Função para cadastrar um novo restaurante
def cadastrar_novo_restaurante():
    
    '''Essa função é responsável por cadastrar um novo restaurante
    - Nome do restaurante
    - Categoria

    Output:
    - Adiciona um novo restaurante à lista de restaurantes

    '''
    
    exibir_subtitulo('Cadastro de um novo restaurante')

    nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria_restaurante = input(f'Digite o nome da categoria do {nome_restaurante}(Ex: Pizzaria, Japonesa, Hamburgueria e etc): ')
    dados_restaurante = {'nome': nome_restaurante, 'categoria': categoria_restaurante, 'ativo': False}
    
    restaurantes.append(dados_restaurante)
    print(f'\nO restaurante {nome_restaurante} foi cadastrado com sucesso!') #Exibindo ao user
    voltar_menu_principal()

#Função para listar os restaurantes
def listar_restaurantes():
    ''' Lista os restaurantes presentes na lista 
    
    Outputs:
    - Exibe a lista de restaurantes na tela
    '''
    exibir_subtitulo('Listando todos os restaurantes')
    #Colocando um título para as colunas dos dados exibidos
    exibindo_titulo = f'{"Nome do Restaurante".ljust(22)} | {"Categoria".ljust(20)} | {"Status"}'
    linha_separacao = '_' * (len(exibindo_titulo) + 4)
    print(linha_separacao)
    print(exibindo_titulo)
    print(linha_separacao)
    
    for restaurante in restaurantes:    #Fazendo um loop para que os restaurantes sejam exibidos
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        atividade_restaurante = restaurante['ativo']   
        atividade_restaurante = 'ativado' if restaurante['ativo'] else 'desativado' # Utilizando ternário

        print(f'- {nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {atividade_restaurante}') 
    print()    
    voltar_menu_principal()

#Fazendo a função para alternar o estado do restaurante
def alternar_estado_restaurante():
    ''' Altera o estado ativo/desativado de um restaurante 
    
    Outputs:
    - Exibe mensagem indicando o sucesso da operação
    '''
    exibir_subtitulo('Alterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False
    
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo'] #Alternando o estado do restaurante
            mensagem = f'\nO restaurante {nome_restaurante} foi ativado com sucesso!\n' if restaurante['ativo'] else f'\nO restaurante {nome_restaurante} foi desativado com sucesso!\n' #Utilizando Ternário
            print(mensagem)
            
    if not restaurante_encontrado:
        print(f'O restaurante {nome_restaurante} não foi encontrado')
    
    voltar_menu_principal()
#Função para opção escolhida
def escolher_opcao():
    ''' Solicita e executa a opção escolhida pelo usuário 
    
    inputs: 
    - opcao_escolhida: Opção escolhida pelo usuário
    
    Outputs:
    - Executa a opção escolhida pelo usuário
    '''
    try: #Tentando converter user para int
        opcao_escolhida = int(input('\nEscolha uma opção: '))
    
        if (opcao_escolhida == 1):
            cadastrar_novo_restaurante()        
        elif(opcao_escolhida == 2):
            listar_restaurantes()
        elif(opcao_escolhida == 3):
            alternar_estado_restaurante()
        elif(opcao_escolhida == 4):
            finalizar_app()
        else:
            opcao_invalida()
    except: #Caso não converta para int, chama a função 
        opcao_invalida()

#Função main
def main():
    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()
     
if __name__ == '__main__':
    main()
    