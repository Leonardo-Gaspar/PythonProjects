#Implementando imports
import os

#Iniciando meu programa com um Título
def exibir_nome_programa():
    print("""
        𝕊𝕒𝕓𝕠𝕣 𝔼𝕩𝕡𝕣𝕖𝕤𝕤
        \n""")
#Função para exibir o Menu
def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurantes')
    print('4. Sair')
    
#Função para finalizar meu programa
def finalizar_app():
    os.system('cls')
    print('Finalizando o app\n')

#Função para opção escolhida
def escolher_opcao():
    opcao_escolhida = int(input('\nEscolha uma opção: '))
    print(f'\nVocê escolheu a opção {opcao_escolhida}')
 
    if (opcao_escolhida == 1):
        print('\nVocê escolheu a opção de Cadastrar restaurante\n')
            
    elif(opcao_escolhida == 2):
        print('\nVocê escolheu a opção de Listar restaurantes')
    elif(opcao_escolhida == 3):
        print('\nVocê escolheu a opção de Ativar restaurantes')
    elif(opcao_escolhida == 4):
        finalizar_app()
    else:
        print('\nVocê escolheu uma opção inválida')

#Função main
def main():
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()
     
if __name__ == '__main__':
    main()
    
      