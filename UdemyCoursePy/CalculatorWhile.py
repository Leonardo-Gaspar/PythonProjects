""" Calculadora com while """

while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')

    numeros_validos = None

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números não são válidos')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue
    
    if len(operador)> 1:
        print('Digite apenas um operador.')
        continue

    print('Realizando sua conta, confira o resultado abaixo: ')    
    if operador is '+':
        resuldado_soma = num_1_float + num_2_float
        print(resuldado_soma)
    elif operador is '-':
        resultado_sub = num_1_float - num_2_float
        print(resultado_sub)
    elif operador is '/':
        resultado_divi = num_1_float / num_2_float
        print(resultado_divi)
    elif operador is '*':
        resultado_multi = num_1_float * num_2_float
        print(resultado_multi)
    else:
        print('Acho que não deveria chegar aqui :/' )

    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break
