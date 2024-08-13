x = int(input("Digite um numero de 1 a 3: "))
match x:
    case 1:
        print("Voce selecionou a primeira opcao")
    case 2:
        print("Voce selecionou a segunda opcao")
    case 3:
        print("Voce selecionou a terceira opcao")
    case _:
        print("Opção inválida")


selecao =input("Deseja entrar no programa? ").lower()
match selecao:
    case "s" | "sim":
        print("Voce entrou no programa")
    case "n" | "nao"| "não":
        print("Voce nao entrou no programa")
    case _:
        print("Opção inválida")

codigo_retorno_1 = int(input("Qual foi o código de retorno API? "))
match codigo_retorno_1:
    case 100|101|102:
        print("Código do tipo 1XX - Informativo")
    case 200 | 201 | 202:
        print("Código do tipo 2XX - Sucesso")
    case 300 | 301 | 302:
        print("Código do tipo 3XX - Redirecionamento")
    case 400 | 401 | 402:
        print("Código do tipo 4XX - Erro do cliente")
    case 500 | 501 | 502:
        print("Código do tipo 5XX - Erro do servidor")
    case _:
        print("Código desconhecido")

codigo_retorno_2 = int(input("Qual foi o código de retorno API? "))
familia_do_codigo = codigo_retorno_2 // 100
match familia_do_codigo:
    case 1:
        print("Código do tipo 1XX - Informativo")
    case 2:
        print("Código do tipo 2XX - Sucesso")
    case 3:
        print("Código do tipo 3XX - Redirecionamento")
    case 4:
        print("Código do tipo 4XX - Erro do cliente")
    case 5:
        print("Código do tipo 5XX - Erro do servidor")
    case _:
        print("Código desconhecido")

y = "jsahdadj"
y = 32323
y = 23.4
y = True

tipo_y = type(y)

match tipo_y:
    case int():
        print(f'Inteiro: {y}')
    case float():
        print(f'Float: {y}')
    case str():
        print(f'String: {y}')
    case bool():
        print(f'Boolean: {y}')

dia_numerico = input("Digite o número correspondente ao dia da semana \n" +
                     "\tExemplo: 1 para segunda...\n" +
                     "\tInsira: ")
if dia_numerico == "1":
    print("Hoje é Segunda-feira")
elif dia_numerico == "2":
    print("Hoje é Terça-feira")
elif dia_numerico == "3":
    print("Hoje é Quarta-feira")
elif dia_numerico == "4":
    print("Hoje é Quinta-feira")
elif dia_numerico == "5":
    print("Hoje é Sexta-feira")
elif dia_numerico == "6":
    print("Hoje é Sábado")
elif dia_numerico == "7":
    print("Hoje é Domingo")
else:
    print("Entrada inválido")

match dia_numerico:
    case "1":
        print("Hoje é Segunda-feira")
    case "2":
        print("Hoje é Terça-feira")
    case "3":
        print("Hoje é Quarta-feira")
    case "4":
        print("Hoje é Quinta-feira")
    case "5":
        print("Hoje é Sexta-feira")
    case "6":
        print("Hoje é Sábado")
    case "7":
        print("Hoje é Domingo")
    case _:
        print("Entrada inválido")

letra = input("Digite uma letra: ").upper()
letra = letra[0] if len(letra) > 1 else letra

match letra:
    case "A"|"E"|"I"|"O"|"U":
        print(f'{letra} é uma vogal')
    case _:
        print(f'{letra} é uma consoante')