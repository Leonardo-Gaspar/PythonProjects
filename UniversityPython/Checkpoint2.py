def reta(x):
    f = 2 * x + 3
    return f


print(reta(1))

c = 2


def media_de_dois_numeros(a, b=0):
    return (a + b) / c


print(media_de_dois_numeros(2, 3))
print(media_de_dois_numeros(2, b=3))
print(media_de_dois_numeros(a=2, b=3))
print(media_de_dois_numeros(a=2, b=3))


print(media_de_dois_numeros(2))

def media_de_tres_numeros(a, b, c):
    return (a + b + c) / 3


print(media_de_tres_numeros(3, 3, 3))
print(media_de_tres_numeros(3, b=3, c=3))
print(media_de_tres_numeros(a=3, b=3, c=3))

def valida_senha(senha):
    senha_cadastrada = "senha123"
    if senha == senha_cadastrada:
        return True
    else:
        return False


senha = input("Digite sua senha: ")
senha_esta_correta = valida_senha(senha)
if senha_esta_correta:
    print("Login com sucesso")  # idealmente redirecionar pra recursos do sistema
else:
    print("Senha errada")

def calc_media(*args):
    soma = 0
    contador = 0
    for numero in args:
        soma += numero
        contador += 1
    media = soma / contador
    return media


print(calc_media(1))
print(calc_media(1, 2, 3))
print(calc_media(1, 2, 3, 4))
print(calc_media(1, 2, 3, 4, 5))
print(calc_media(1, 2, 3, 4, 5, 6, 7))
print(calc_media(6, 745, 0, 897, 45673))

def calculadora(operacao: str, num_1: float, num_2: float):
    match operacao:
        case "adicao":
            return num_1 + num_2
        case "subtracao":
            return num_1 - num_2
        case "multiplicacao":
            return num_1 * num_2
        case "divisao":
            if num_2 != 0:
                return num_1 / num_2
            print("Valor invÃ¡lido para operaÃ§Ã£o de divisÃ£o com zero")
        case _:
            print("Nenhuma operaÃ§Ã£o vÃ¡lida.")


operacao = input("Digite a operaÃ§Ã£o desejada: ")
num_1 = float(input("Digite o primeiro nÃºmero: "))
num_2 = float(input("Digite o segundo nÃºmero: "))

resultado = calculadora(operacao, num_1, num_2)
print(resultado)

def calculadora(operacao: str, num_1: float, num_2: float, *args):
    match operacao:
        case "adicao":
            soma = num_1 + num_2
            for num in args:
                soma += num
            return soma
        case "subtracao":
            subtracao = num_1 - num_2
            for num in args:
                subtracao -= num
            return subtracao
        case "multiplicacao":
            multiplicacao = num_1 * num_2
            for num in args:
                multiplicacao *= num
            return multiplicacao
        case "divisao":
            if num_2 == 0:
                print("Valor invÃ¡lido para operaÃ§Ã£o de divisÃ£o com zero")
                return
            div = num_1 / num_2
            for num in args:
                if num == 0:
                    print("Valor invÃ¡lido para operaÃ§Ã£o de divisÃ£o com zero")
                    return
                div /= num
            return div
        case _:
            print("Nenhuma operaÃ§Ã£o vÃ¡lida.")


while True:
    operacao = input("Digite a operaÃ§Ã£o desejada: ")
    num_1 = float(input("Digite o primeiro nÃºmero: "))
    num_2 = float(input("Digite o segundo nÃºmero: "))
    nums = []  # lista --> checkpoint 3 apenas
    while True:
        adicional = input("VocÃª gostaria de adicionar mais algum nÃºmero? [s/N]\t")
        if adicional == 's':
            nums.append(float(input("Digite o prÃ³ximo nÃºmero: ")))
        else:
            break

    resultado = calculadora(operacao, num_1, num_2, *nums)
    print(resultado)

    continuar = input("VocÃª gostaria de executar uma nova operaÃ§Ã£o? [s/N]\t")
    if continuar == "N":
        break