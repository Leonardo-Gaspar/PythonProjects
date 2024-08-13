"""
Faça um programa que peça ao usuário para digitar um número inteiro
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero_usuario = input('Digite um número: ')

if numero_usuario.isdigit():
    numero_usuario_int= int(numero_usuario)
    par_ou_impar = numero_usuario_int % 2 == 0
    par_impar_texto = 'ímpar'

    if par_ou_impar:
        par_impar_texto = 'par'
   
    print(f'O número {numero_usuario_int} é {par_impar_texto}')
else:
    print('Você não digitou numero inteiro')


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
horario_usuario = input('Digite seu horário em numeros inteiros: ')
try:
    hora = int(horario_usuario)
    bom_dia = hora >= 0 and hora <= 11
    boa_tarde = hora >= 12 and hora <= 17
    boa_noite = hora >= 18 and hora <= 23
    if bom_dia:
        print('Tenha um bom dia!')
    elif boa_tarde:
        print('Tenha uma boa tarde!')
    elif boa_noite:
        print('Tenha uma boa noite!')
    else:
        print('Não conheço essa hora')
except:
    print('Por favor, digite apenas números inteiros')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome_usuario = input('Digite seu nome: ')
numero_de_digitos_nome = len(nome_usuario)

if numero_de_digitos_nome > 2:
    if numero_de_digitos_nome <= 4:
        print('Seu nome é curto')
    elif numero_de_digitos_nome > 4 and numero_de_digitos_nome <= 6:
        print('Seu nome tem tamanho normal')
    else:
        print('Seu nome é grande')
    
else:
    print('Digite pelo menos 3 letras')