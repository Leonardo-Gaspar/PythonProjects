import json

def cadastrar():
    print("\n--- Cadastro ---")
    nome = input("Digite seu nome: ")
    email = input("Digite seu email: ")
    telefone = input("Digite seu telefone: ")

    cliente = {"Nome": nome, "Email": email, "Telefone": telefone}

    # Salvando os dados do cliente em um arquivo JSON
    with open('clientsPart3.json', 'a') as arquivo_json:
        json.dump(cliente, arquivo_json)
        arquivo_json.write(',')
        arquivo_json.write('\n')

    print(f"\nNome: {nome}\nEmail: {email}\nTelefone: {telefone}")
    print("Cadastro realizado com sucesso!")

#Adicionando dados
def create_data(lista_dados):
    try:
        name = input("Insira seu nome : ")
        age = int(input("Insira a idade: "))
        data = {"nome": name, "idade": age}
        lista_dados.append(data)
        print("Dado adicionado com sucesso!")
    except ValueError:
        print("Dados inválido. Por favor, digite uma idade válida.")

#Removendo dados
def remove_data(lista_dados):
    try:
        id = int(input("Insira o id que deseja remover: "))
        if 0 <= id < len(lista_dados):
            del lista_dados[id]
            print("Dado removido com sucesso!")
        else:
            print("Id inválido.")
    except ValueError:
        print("Dado inválido. Por favor, digite um id válido.")

#Atualizando dados
def update_data(lista_dados):
    try:
        id = int(input("Insira o id que deseja atualizar: "))
        if 0 <= id < len(lista_dados):
            name = input("Insira o novo nome: ")
            age = int(input("Insira a idade: "))
            lista_dados[id] = {"nome": name, "idade": age}
            print("Dado atualizado com sucesso!")
        else:
            print("Id inválido.")
    except ValueError:
        print("Dado inválido. Por favor digite um id válido e/ou idade válida.")

#Consultando dados
def display_data(lista_dados):
    print("\nLista de dados:")
    for id, data in enumerate(lista_dados):
        id = id + 1
        print(f"{id}: nome: {data['nome']} - {data['idade']} anos")

def iniciar_sistema():
    lista_dados = []

    while True:
        print("\nMenu:")
        print("1. Adicionar dado")
        print("2. Remover dado")
        print("3. Atualizar dado")
        print("4. Pesquisar dado")

        choice = input("Digite uma opção de 1-4: ")

        if choice == "1":
            create_data(lista_dados)
        elif choice == "2":
            remove_data(lista_dados)
        elif choice == "3":
            update_data(lista_dados)
        elif choice == "4":
            display_data(lista_dados)
        elif choice == "5":
            print("Desligando programa.")
            break
        else:
            print("Escolha inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    sistema = cadastrar()
    iniciar_sistema()