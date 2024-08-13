# frase = 'O Python eh uma linguagem de programaçao multiparadigma.'\
#     'Python foi criado por Guido van Rossum'.lower()
# #print(frase.count('python'))

# i = 0
# apareceu_mais_vzs = 0
# letra_que_apareceu_mais_vzs = ''
# while i < len(frase):
#     letra_atual = frase[i]

#     if letra_atual == ' ':
#         i += 1
#         continue

#     qntd_vzs_letra_apareceu = frase.count(letra_atual)

#     if apareceu_mais_vzs < qntd_vzs_letra_apareceu:
#         apareceu_mais_vzs = qntd_vzs_letra_apareceu
#         letra_que_apareceu_mais_vzs = letra_atual
#     i += 1
# print(
#     'A letra que apareceu mais vezes foi ' 
#     f'"{letra_que_apareceu_mais_vzs}" que apareceu '
#     f'{apareceu_mais_vzs}x'
# )


'''Teste 7'''
# start = 0
# end = 10
# while start < end:
#     start += 1
#     print(start)
linhas = 3
colunas = 3
 
linha = 1
while linha <= linhas:
    coluna = 1
    while coluna <= colunas:
        print(linha, coluna)
        coluna += 1
    linha += 1