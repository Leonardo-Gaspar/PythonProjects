"""
Faça uma lista de compras com listas
o usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista 
Não permita que o programa quebre com
error de índices inexistentes na lista
"""

import os 
lista = []
while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir -- [a]pagar -- [l]listar: ')

    if opcao == 'i':
        valor = input('Valor: ')
        lista.append(valor)
    elif opcao == 'a':
        indice_str = input('Escolha o índice para apagar: ')

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor, digite números inteiros')        
        except IndexError:
            print('Índice nao existe na lista')
    elif opcao == 'l':
        if len(lista) == 0:
            print('Não há nada para listar')
        for i, valor in enumerate(lista):
            print(i, valor)
    else:  
        print('Por favor, escolha "i", "a" ou "l"') 