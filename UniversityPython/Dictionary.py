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
        if input("DO you want to add another user? ") != "yes":
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