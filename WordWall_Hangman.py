# for i in range(10):
#     if i == 2:
#         print('i é 2, pulando...')
#         continue

#     if i == 8:
#         print('i é 8, seu else não executará')
#         break

#     for j in range(1, 3):
#         print(i, j)
# else:
#     print('For completo com sucesso!')


palavra_secreta = 'medalha'
letras_acertadas = ''
numero_tentativas = 0

while True:

    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1
    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    print('Palavra formada: ', palavra_formada)

    if palavra_formada == palavra_secreta:
        print('\nVoce ganhou, parabéns!!')
        print(f'A palavra secreta era: {palavra_secreta}/n')
        print('Tentativas:', numero_tentativas)
        letras_acertadas = ''
        numero_tentativas = 0
    
