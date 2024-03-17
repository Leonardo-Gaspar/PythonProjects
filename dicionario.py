# l = {
#     "Julinha": 3,
#     "Enzo": 4,
#     "Leo": 6,
# }
#
# print("A nota do Enzo é: ",
#       + l["Enzo"])
#
# h = {
#     "a": None,
#     "b": 1,
#     1: "a",
#     2: (1,2,3),
#     (1,"a"): ["a, 1, True"],
#     (1, 1): True,
#     ("b","a"): False,
#     "dicionario" :{
#         "name":"bullbasaur",
#         "url": "adada",
#     }
# }
# print(["name" for "bullbasaur" in h ]

# from pprint import pprint
# s = " eu sou o leonardo, tenho 20 anos e gosto de volei"
#
# frequencia = {}
# for letra in s:
#     frequencia[letra] = 1 + frequencia.get(letra, 0)
# pprint(frequencia)

# from pprint import pprint
# s = " eu sou o leonardo, tenho 20 anos e gosto de volei, eu sou o leonardo, tenho 20 anos e gosto de volei, eu sou o leonardo, tenho 20 anos e gosto de volei,"
#
# frequencia_palavra = {}
# for palavra in s.split():
#     frequencia_palavra[palavra] = 1 + frequencia_palavra.get(palavra, 0)
#
# pprint(frequencia_palavra)


# listaUsuarios = {
#     "usuario1": {
#         "nome": "Leonardo",
#         "CPF": 51231322125,
#         "email": "leosaheb@jajaja.com",
#         "RG": 571717717,
#         "Telefone": 11991310730,
#     },
#     "usuario2":{
#         "nome": "Enzo",
#         "CPF": 71231322125,
#         "email": "enzofranco@jajaja.com",
#         "RG": 871717717,
#         "Telefone": 13991310730,
#     }
# }
# cadastro = {}
#
# nomeUsuario = input("Digite seu nome: ")
# cpfUsuario = input("Digite seu cpf: ")
# emailUsuario = input("Digite seu email: ")
# rgUsuario = input("Digite seu rg: ")
# telefoneUsuario = input("Digite seu telefone: ")
# def cadastro(nomeUsuario, cpfUsuario, emailUsuario, rgUsuario, telefoneUsuario):
#     usuario1 = {
#         "nome": nomeUsuario,
#         "cpf": cpfUsuario,
#         "email": emailUsuario,
#         "rg": rgUsuario,
#         "telefone": telefoneUsuario
#     }
#
#     return usuario1

# def f():
#     bd = []
#     while True:
#       # user = {
#         #     "nome":     input("Digite seu nome: "),
#         #     "cpf":      input("Digite seu cpf: "),
#         #     "email":    input("Digite seu email: "),
#         #     "rg":       input("Digite seu rg: "),
#         # },
#         # bd.append(user)
#
#         # print(" Usuario adicionado com sucesso")
#         # if input("Dejesa adicionar mais um usuario? ") == "n":
#         #     break
#
#
#     # print("\n USER2 \n")
#
#         nome=input("Digite seu nome: "),
#         cpf=input("Digite seu cpf: "),
#         email=input("Digite seu email: "),
#         rg=input("Digite seu rg: "),
#         user2 = {
#             "nome": nome,
#             "cpf": cpf,
#             "email": email,
#             "rg": rg,
#     }
#         bd.append(user2)
#
#         return bd
#
#
#
#
# BD = f()
# print(BD)


def create():

    bd = []

    while True:
        user = {
            "nome":     input("Digite seu nome: "),
            "cpf":      input("Digite seu cpf: "),
            "email":    input("Digite seu email: "),
            "rg":       input("Digite seu rg: "),
        },
        bd.append(user)

        print("User added successfuly")
        if input("DO you want to add another user? ") == "n":
            break
    return bd

def read(bd):
    key = input("Digite o campo deseja buscar: ")
    value = input("Digite o valor deseja buscar: ")

    results = []
    for user in bd:
        if user[key] == value:
            results.append(user)

    return results


def update(bd):
    # Busco os registros para alterar

    results = read(bd)
    key = input('Qual campo voce deseja alterar? ')
    value = input('Digite o novo valor:  ')

    for record in results:
        record[key] = value

# def delete(bd):
#     results = read(bd)
#     key = input('Qual campo voce deseja buscar para apagar: ')
#     value = input('Digite o novo valor para buscar:  ')
#
#     for user in bd:
#         if user[key] == value:
#             del user


BD = create()

# print(read(BD))
# update(BD)
# delete(BD)

print(BD)



