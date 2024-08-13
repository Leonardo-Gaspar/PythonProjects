import json
import oracledb

class Sistema:
    def __init__(self):
        self.usuario = usuario
        self.senha = senha
        self.oracle = oracle
        self.produtos = []
        self.industrias = []
        self.aprendizado = {}

    def menu_crud(self):
        print("\n--- Menu CRUD ---")
        print("1. Adicionar")
        print("2. Remover")
        print("3. Atualizar")
        print("4. Pesquisar")
        print("5. Sair")

    def mostrar_menu(self):
        print("\n--- Menu ---")
        print("1. Produtos")
        print("2. Indústrias")
        print("3. Aprendizado")
        print("4. Sair")

    def executar_crud(self):
        print("Bem-vindo à Salesforce!")
        while True:
            self.menu_crud()
            escolha = input("Escolha uma opção (1-5): ")

            if escolha == "1":
                self.adicionar_dados_menu()
            elif escolha == "2":
                self.remover_dados_menu()
            elif escolha == "3":
                self.atualizar_dados_menu()
            elif escolha == "4":
                self.pesquisar_dados_menu()
            elif escolha == "5":
                print("Encerrando programa")
                break
            else:
                print("\nOpção inválida. Selecione uma opção válida")
                self.menu_crud()

    def adicionar_dados_menu(self):
        while True:
            try:
                self.mostrar_menu()
                escolha = input("Escolha onde deseja adicionar os dados (1-4): ")
                if escolha == "1":
                    self.adicionar_menu_produtos()
                elif escolha == "2":
                    self.adicionar_menu_industrias()
                elif escolha == "3":
                    self.adicionar_menu_aprendizado()
                elif escolha == "4":
                    print("Encerrando programa")
                    break
                else:
                    print("\nOpção inválida. Selecione uma opção válida")
                    self.menu_crud()
            except ConnectionError:
                print("Erro ao conectar!")

    def remover_dados_menu(self):
        while True:
            try:
                self.mostrar_menu()
                escolha = input("Escolha onde deseja remover os dados (1-4): ")
                if escolha == "1":
                    self.remover_menu_produtos()
                elif escolha == "2":
                    self.remover_menu_industrias()
                elif escolha == "3":
                    self.remover_menu_aprendizado()
                elif escolha == "4":
                    print("Encerrando programa")
                    break
                else:
                    print("\nOpção inválida. Selecione uma opção válida")
                    self.menu_crud()
            except ConnectionError:
                print("Erro ao conectar!")

    def atualizar_dados_menu(self):
        while True:
            try:
                self.mostrar_menu()
                escolha = input("Escolha onde deseja adicionar os dados (1-6): ")
                if escolha == "1":
                    self.atualizar_menu_produtos()
                elif escolha == "2":
                    self.atualizar_menu_industrias()
                elif escolha == "3":
                    self.atualizar_menu_aprendizado()
                elif escolha == "4":
                    print("Encerrando programa")
                    break
                else:
                    print("\nOpção inválida. Selecione uma opção válida")
                    self.menu_crud()
            except ConnectionError:
                print("Erro ao conectar!")

    def pesquisar_dados_menu(self):
        while True:
            try:
                self.mostrar_menu()
                escolha = input("Escolha onde deseja adicionar os dados (1-6): ")
                if escolha == "1":
                    self.pesquisar_menu_produtos()
                elif escolha == "2":
                    self.pesquisar_menu_industrias()
                elif escolha == "3":
                    self.pesquisar_menu_aprendizado()
                elif escolha == "4":
                    print("Encerrando programa")
                    break
                else:
                    print("\nOpção inválida. Selecione uma opção válida")
                    self.menu_crud()
            except ConnectionError:
                print("Erro ao conectar!")

    def adicionar_menu_produtos(self):
        print("\n---Produtos ---")
        while True:
            print("\n---Menu Produtos---")
            print("1. Customer 360")
            print("2. Vendas")
            print("3. Atendimento ao Cliente")
            print("4. Marketing")
            print("5. Commerce")
            print("6. Data Cloud")
            print("7. Tableau")
            print("8. Mulesoft")
            print("9. Slack")
            print("10. Plataforma")
            print("11. Sustentabilidade")
            print("12. Voltar para menu")
            print("13. Sair")

            escolha_produto = input("Qual área deseja adicionar? (1-13): ")

            if escolha_produto == "1":
                tabela = "t_produto_py"
                area_produto = "Customer 360"
                print("\n---Customer 360---")
                try:
                    id_produto = int(input("Insira o id do produto: "))
                    nm_produto = input("Insira o nome do produto: ")
                    ds_produto = input("Insira a descrição do produto: ")
                    valor_produto = float(input("Insira o valor do produto: "))
                    sql_insert = f"INSERT INTO {tabela} VALUES ( {id_produto},'{area_produto}', '{nm_produto}', '{ds_produto}', {valor_produto})"

                    print("Adicionado com sucesso!")
                except ValueError:
                    print("Valor não compatível. Retornando...")
                try:
                    insert(usuario, senha, oracle, sql_insert)
                except ConnectionError:
                    print("Erro ao conectar com o banco!")

            elif escolha_produto == "2":
                tabela = "t_produto_py"
                area_produto = "Vendas"
                print("\n---Vendas---")
                try:
                    id_produto = int(input("Insira o id do produto: "))
                    nm_produto = input("Insira o nome do produto: ")
                    ds_produto = input("Insira a descrição do produto: ")
                    valor_produto = float(input("Insira o valor do produto: "))
                    sql_insert = f"INSERT INTO {tabela} VALUES ( {id_produto},'{area_produto}', '{nm_produto}', '{ds_produto}', {valor_produto})"

                    print("Adicionado com sucesso!")
                except ValueError:
                    print("Valor não compatível. Retornando...")
                try:
                    insert(usuario, senha, oracle, sql_insert)
                except ConnectionError:
                    print("Erro ao conectar com o banco!")

            elif escolha_produto == "3":
                tabela = "t_produto_py"
                area_produto = "Atendimento ao Cliente"
                print("\n---Atendimento ao Cliente---")
                try:
                    id_produto = int(input("Insira o id do produto: "))
                    nm_produto = input("Insira o nome do produto: ")
                    ds_produto = input("Insira a descrição do produto: ")
                    valor_produto = float(input("Insira o valor do produto: "))
                    sql_insert = f"INSERT INTO {tabela} VALUES ( {id_produto},'{area_produto}', '{nm_produto}', '{ds_produto}', {valor_produto})"

                    print("Adicionado com sucesso!")
                except ValueError:
                    print("Valor não compatível. Retornando...")
                try:
                    insert(usuario, senha, oracle, sql_insert)
                except ConnectionError:
                    print("Erro ao conectar com o banco!")

            elif escolha_produto == "4":
                tabela = "t_produto_py"
                area_produto = "Marketing"
                print("\n---Marketing---")
                try:
                    id_produto = int(input("Insira o id do produto: "))
                    nm_produto = input("Insira o nome do produto: ")
                    ds_produto = input("Insira a descrição do produto: ")
                    valor_produto = float(input("Insira o valor do produto: "))
                    sql_insert = f"INSERT INTO {tabela} VALUES ( {id_produto},'{area_produto}', '{nm_produto}', '{ds_produto}', {valor_produto})"

                    print("Adicionado com sucesso!")
                except ValueError:
                    print("Valor não compatível. Retornando...")
                try:
                    insert(usuario, senha, oracle, sql_insert)
                except ConnectionError:
                    print("Erro ao conectar com o banco!")
            elif escolha_produto == "5":
                tabela = "t_produto_py"
                area_produto = "Commerce"
                print("\n---Commerce---")
                try:
                    id_produto = int(input("Insira o id do produto: "))
                    nm_produto = input("Insira o nome do produto: ")
                    ds_produto = input("Insira a descrição do produto: ")
                    valor_produto = float(input("Insira o valor do produto: "))
                    sql_insert = f"INSERT INTO {tabela} VALUES ( {id_produto},'{area_produto}', '{nm_produto}', '{ds_produto}', {valor_produto})"

                    print("Adicionado com sucesso!")
                except ValueError:
                    print("Valor não compatível. Retornando...")
                try:
                    insert(usuario, senha, oracle, sql_insert)
                except ConnectionError:
                    print("Erro ao conectar com o banco!")

            elif escolha_produto == "6":
                tabela = "t_produto_py"
                area_produto = "Data Cloud"
                print("\n---Data Cloud---")
                try:
                    id_produto = int(input("Insira o id do produto: "))
                    nm_produto = input("Insira o nome do produto: ")
                    ds_produto = input("Insira a descrição do produto: ")
                    valor_produto = float(input("Insira o valor do produto: "))
                    sql_insert = f"INSERT INTO {tabela} VALUES ( {id_produto},'{area_produto}', '{nm_produto}', '{ds_produto}', {valor_produto})"

                    print("Adicionado com sucesso!")
                except ValueError:
                    print("Valor não compatível. Retornando...")
                try:
                    insert(usuario, senha, oracle, sql_insert)
                except ConnectionError:
                    print("Erro ao conectar com o banco!")
            elif escolha_produto == "7":
                tabela = "t_produto_py"
                area_produto = "Tableau"
                print("\n---Tableau---")
                try:
                    id_produto = int(input("Insira o id do produto: "))
                    nm_produto = input("Insira o nome do produto: ")
                    ds_produto = input("Insira a descrição do produto: ")
                    valor_produto = float(input("Insira o valor do produto: "))
                    sql_insert = f"INSERT INTO {tabela} VALUES ( {id_produto},'{area_produto}', '{nm_produto}', '{ds_produto}', {valor_produto})"

                    print("Adicionado com sucesso!")
                except ValueError:
                    print("Valor não compatível. Retornando...")
                try:
                    insert(usuario, senha, oracle, sql_insert)
                except ConnectionError:
                    print("Erro ao conectar com o banco!")
            elif escolha_produto == "8":
                tabela = "t_produto_py"
                area_produto = "Mulesoft"
                print("\n---Mulesoft---")
                try:
                    id_produto = int(input("Insira o id do produto: "))
                    nm_produto = input("Insira o nome do produto: ")
                    ds_produto = input("Insira a descrição do produto: ")
                    valor_produto = float(input("Insira o valor do produto: "))
                    sql_insert = f"INSERT INTO {tabela} VALUES ( {id_produto},'{area_produto}', '{nm_produto}', '{ds_produto}', {valor_produto})"

                    print("Adicionado com sucesso!")
                except ValueError:
                    print("Valor não compatível. Retornando...")
                try:
                    insert(usuario, senha, oracle, sql_insert)
                except ConnectionError:
                    print("Erro ao conectar com o banco!")
            elif escolha_produto == "9":
                tabela = "t_produto_py"
                area_produto = "Slack"
                print("\n---Slack---")
                try:
                    id_produto = int(input("Insira o id do produto: "))
                    nm_produto = input("Insira o nome do produto: ")
                    ds_produto = input("Insira a descrição do produto: ")
                    valor_produto = float(input("Insira o valor do produto: "))
                    sql_insert = f"INSERT INTO {tabela} VALUES ( {id_produto},'{area_produto}', '{nm_produto}', '{ds_produto}', {valor_produto})"

                    print("Adicionado com sucesso!")
                except ValueError:
                    print("Valor não compatível. Retornando...")
                try:
                    insert(usuario, senha, oracle, sql_insert)
                except ConnectionError:
                    print("Erro ao conectar com o banco!")
            elif escolha_produto == "10":
                tabela = "t_produto_py"
                area_produto = "Plataforma"
                print("\n---Plataforma---")
                try:
                    id_produto = int(input("Insira o id do produto: "))
                    nm_produto = input("Insira o nome do produto: ")
                    ds_produto = input("Insira a descrição do produto: ")
                    valor_produto = float(input("Insira o valor do produto: "))
                    sql_insert = f"INSERT INTO {tabela} VALUES ( {id_produto},'{area_produto}', '{nm_produto}', '{ds_produto}', {valor_produto})"

                    print("Adicionado com sucesso!")
                except ValueError:
                    print("Valor não compatível. Retornando...")
                try:
                    insert(usuario, senha, oracle, sql_insert)
                except ConnectionError:
                    print("Erro ao conectar com o banco!")
            elif escolha_produto == "11":
                tabela = "t_produto_py"
                area_produto = "Sustentabilidade"
                print("\n---Sustentabilidade---")
                try:
                    id_produto = int(input("Insira o id do produto: "))
                    nm_produto = input("Insira o nome do produto: ")
                    ds_produto = input("Insira a descrição do produto: ")
                    valor_produto = float(input("Insira o valor do produto: "))
                    sql_insert = f"INSERT INTO {tabela} VALUES ( {id_produto},'{area_produto}', '{nm_produto}', '{ds_produto}', {valor_produto})"

                    print("Adicionado com sucesso!")
                except ValueError:
                    print("Valor não compatível. Retornando...")
                try:
                    insert(usuario, senha, oracle, sql_insert)
                except ConnectionError:
                    print("Erro ao conectar com o banco!")
            elif escolha_produto == "12":
                print("\n---Voltando para o Menu---")
                self.menu_crud()
            elif escolha_produto == "13":
                break
            else:
                print("\nOpção inválida. Selecione uma opção válida")
                self.menu_crud()

            self.mostrar_resumo_operacao("Produtos")


    def adicionar_menu_industrias(self):
        print("\n---Industrias---")
        while True:
            print("\n---Menu Indústrias---")
            print("1. Automotivo")
            print("2. Comunicações")
            print("3. Bens de Consumo")
            print("4. Serviços Financeiros")
            print("5. Saúde & Ciências da vida")
            print("6. Manufatura")
            print("7. Mídia")
            print("8. Setor Público")
            print("9. Varejo")
            print("10. Tecnologia")
            print("11. Voltar para o Menu")
            print("12. Sair")

            escolha_industria = input("Escolha o produto que deseja (1-12): ")

            if escolha_industria == "1":
                print("\n---Automotivo---")
                tabela = "t_industria_py"
                area_industria = "Automotiva"
                try:
                    id_industria = int(input("Insira o id da industria: "))
                    nm_industria = input("Insira o nome da industria: ")
                    ds_industria = input("Insira a descrição da industria: ")
                    valor_industria = float(input("Insira o valor da industria: "))
                    sql_insert = f"INSERT INTO {tabela} VALUES ( {id_industria},'{area_industria}', '{nm_industria}', '{ds_industria}', {valor_industria})"

                    print("\nAdicionado com sucesso!")
                except ValueError:
                    print("\nValor não compatível. Retornando...")
                try:
                    insert(usuario, senha, oracle, sql_insert)
                except ConnectionError:
                    print("\nErro ao conectar com o banco!")

            elif escolha_industria == "2":
                print("\n---Comunicações---")
                tabela = "t_industria_py"
                area_industria = "Comunicações"
                try:
                    id_industria = int(input("Insira o id da industria: "))
                    nm_industria = input("Insira o nome da industria: ")
                    ds_industria = input("Insira a descrição da industria: ")
                    valor_industria = float(input("Insira o valor da industria: "))
                    sql_insert = f"INSERT INTO {tabela} VALUES ( {id_industria},'{area_industria}', '{nm_industria}', '{ds_industria}', {valor_industria})"

                    print("\nAdicionado com sucesso!")
                except ValueError:
                    print("\nValor não compatível. Retornando...")
                try:
                    insert(usuario, senha, oracle, sql_insert)
                except ConnectionError:
                    print("\nErro ao conectar com o banco!")

            elif escolha_industria == "3":
                print("\n---Bens de Consumo---")
                tabela = "t_industria_py"
                area_industria = "Bens de Consumo"
                try:
                    id_industria = int(input("Insira o id da industria: "))
                    nm_industria = input("Insira o nome da industria: ")
                    ds_industria = input("Insira a descrição da industria: ")
                    valor_industria = float(input("Insira o valor da industria: "))
                    sql_insert = f"INSERT INTO {tabela} VALUES ( {id_industria},'{area_industria}', '{nm_industria}', '{ds_industria}', {valor_industria})"

                    print("\nAdicionado com sucesso!")
                except ValueError:
                    print("\nValor não compatível. Retornando...")
                try:
                    insert(usuario, senha, oracle, sql_insert)
                except ConnectionError:
                    print("\nErro ao conectar com o banco!")

            elif escolha_industria == "4":
                print("\n---Serviços Financeiros---")
                tabela = "t_industria_py"
                area_industria = "Serviços Financeiros"
                try:
                    id_industria = int(input("Insira o id da industria: "))
                    nm_industria = input("Insira o nome da industria: ")
                    ds_industria = input("Insira a descrição da industria: ")
                    valor_industria = float(input("Insira o valor da industria: "))
                    sql_insert = f"INSERT INTO {tabela} VALUES ( {id_industria},'{area_industria}', '{nm_industria}', '{ds_industria}', {valor_industria})"

                    print("\nAdicionado com sucesso!")
                except ValueError:
                    print("\nValor não compatível. Retornando...")
                try:
                    insert(usuario, senha, oracle, sql_insert)
                except ConnectionError:
                    print("\nErro ao conectar com o banco!")

            elif escolha_industria == "5":
                print("\n---Saúde & Ciências da vida---")
                tabela = "t_industria_py"
                area_industria = "Saúde & Ciências da vida"
                try:
                    id_industria = int(input("Insira o id da industria: "))
                    nm_industria = input("Insira o nome da industria: ")
                    ds_industria = input("Insira a descrição da industria: ")
                    valor_industria = float(input("Insira o valor da industria: "))
                    sql_insert = f"INSERT INTO {tabela} VALUES ( {id_industria},'{area_industria}', '{nm_industria}', '{ds_industria}', {valor_industria})"

                    print("\nAdicionado com sucesso!")
                except ValueError:
                    print("\nValor não compatível. Retornando...")
                try:
                    insert(usuario, senha, oracle, sql_insert)
                except ConnectionError:
                    print("\nErro ao conectar com o banco!")

            elif escolha_industria == "6":
                print("\n---Manufatura---")
                tabela = "t_industria_py"
                area_industria = "Manufatura"
                try:
                    id_industria = int(input("Insira o id da industria: "))
                    nm_industria = input("Insira o nome da industria: ")
                    ds_industria = input("Insira a descrição da industria: ")
                    valor_industria = float(input("Insira o valor da industria: "))
                    sql_insert = f"INSERT INTO {tabela} VALUES ( {id_industria},'{area_industria}', '{nm_industria}', '{ds_industria}', {valor_industria})"

                    print("\nAdicionado com sucesso!")
                except ValueError:
                    print("\nValor não compatível. Retornando...")
                try:
                    insert(usuario, senha, oracle, sql_insert)
                except ConnectionError:
                    print("\nErro ao conectar com o banco!")

            elif escolha_industria == "7":
                print("\n---Mídia---")
                tabela = "t_industria_py"
                area_industria = "Mídia"
                try:
                    id_industria = int(input("Insira o id da industria: "))
                    nm_industria = input("Insira o nome da industria: ")
                    ds_industria = input("Insira a descrição da industria: ")
                    valor_industria = float(input("Insira o valor da industria: "))
                    sql_insert = f"INSERT INTO {tabela} VALUES ( {id_industria},'{area_industria}', '{nm_industria}', '{ds_industria}', {valor_industria})"

                    print("\nAdicionado com sucesso!")
                except ValueError:
                    print("\nValor não compatível. Retornando...")
                try:
                    insert(usuario, senha, oracle, sql_insert)
                except ConnectionError:
                    print("\nErro ao conectar com o banco!")

            elif escolha_industria == "8":
                print("\n---Setor Público---")
                tabela = "t_industria_py"
                area_industria = "Setor Público"
                try:
                    id_industria = int(input("Insira o id da industria: "))
                    nm_industria = input("Insira o nome da industria: ")
                    ds_industria = input("Insira a descrição da industria: ")
                    valor_industria = float(input("Insira o valor da industria: "))
                    sql_insert = f"INSERT INTO {tabela} VALUES ( {id_industria},'{area_industria}', '{nm_industria}', '{ds_industria}', {valor_industria})"

                    print("\nAdicionado com sucesso!")
                except ValueError:
                    print("\nValor não compatível. Retornando...")
                try:
                    insert(usuario, senha, oracle, sql_insert)
                except ConnectionError:
                    print("\nErro ao conectar com o banco!")

            elif escolha_industria == "9":
                print("\n---Varejo---")
                tabela = "t_industria_py"
                area_industria = "Varejo"
                try:
                    id_industria = int(input("Insira o id da industria: "))
                    nm_industria = input("Insira o nome da industria: ")
                    ds_industria = input("Insira a descrição da industria: ")
                    valor_industria = float(input("Insira o valor da industria: "))
                    sql_insert = f"INSERT INTO {tabela} VALUES ( {id_industria},'{area_industria}', '{nm_industria}', '{ds_industria}', {valor_industria})"

                    print("\nAdicionado com sucesso!")
                except ValueError:
                    print("\nValor não compatível. Retornando...")
                try:
                    insert(usuario, senha, oracle, sql_insert)
                except ConnectionError:
                    print("\nErro ao conectar com o banco!")

            elif escolha_industria == "10":
                print("\n---Tecnologia---")
                tabela = "t_industria_py"
                area_industria = "Tecnologia"
                try:
                    id_industria = int(input("Insira o id da industria: "))
                    nm_industria = input("Insira o nome da industria: ")
                    ds_industria = input("Insira a descrição da industria: ")
                    valor_industria = float(input("Insira o valor da industria: "))
                    sql_insert = f"INSERT INTO {tabela} VALUES ( {id_industria},'{area_industria}', '{nm_industria}', '{ds_industria}', {valor_industria})"

                    print("\nAdicionado com sucesso!")
                except ValueError:
                    print("\nValor não compatível. Retornando...")
                try:
                    insert(usuario, senha, oracle, sql_insert)
                except ConnectionError:
                    print("\nErro ao conectar com o banco!")

            elif escolha_industria == "11":
                print("\n---Voltando para o Menu---")
                self.menu_crud()

            elif escolha_industria == "12":
                print("Saindo...")
                break
            else:
                print("\nOpção inválida. Selecione uma opção válida")
                self.menu_crud()
            self.mostrar_resumo_operacao("Indústrias")

    def adicionar_menu_aprendizado(self):
        while True:
            print("\n---Aprendizado ---")
            print("\n---Menu Aprendizado---\n")
            print("1. Trailhead")
            print("2. Eventos & Experiências")
            print("3. Histórias de Clientes")
            print("4. Blogs")
            print("5. Voltar para o Menu")
            print("6. Sair")

            escolha_aprendizado = input("Escolha o produto que deseja (1-6): ")

            if escolha_aprendizado == "1":
                print("\n---Trailhead---")
                tabela = "t_aprendizado_py"
                area_aprendizado = "Trailhead"
                try:
                    id_aprendizado = int(input("Insira o id aprendizado: "))
                    nm_aprendizado = input("Insira o nome da aprendizado: ")
                    ds_aprendizado = input("Insira a descrição da aprendizado: ")
                    valor_aprendizado = float(input("Insira o valor da aprendizado: "))
                    sql_insert = f"INSERT INTO {tabela} VALUES ( {id_aprendizado},'{area_aprendizado}', '{nm_aprendizado}', '{ds_aprendizado}', {valor_aprendizado})"

                    print("\nAdicionado com sucesso!")
                except ValueError:
                    print("\nValor não compatível. Retornando...")
                try:
                    insert(usuario, senha, oracle, sql_insert)
                except ConnectionError:
                    print("\nErro ao conectar com o banco!")

            elif escolha_aprendizado == "2":
                print("\n---Eventos & Experiências---")
                tabela = "t_aprendizado_py"
                area_aprendizado = "Eventos e Experiências"
                try:
                    id_aprendizado = int(input("Insira o id aprendizado: "))
                    nm_aprendizado = input("Insira o nome da aprendizado: ")
                    ds_aprendizado = input("Insira a descrição da aprendizado: ")
                    valor_aprendizado = float(input("Insira o valor da aprendizado: "))
                    sql_insert = f"INSERT INTO {tabela} VALUES ( {id_aprendizado},'{area_aprendizado}', '{nm_aprendizado}', '{ds_aprendizado}', {valor_aprendizado})"

                    print("\nAdicionado com sucesso!")
                except ValueError:
                    print("\nValor não compatível. Retornando...")
                try:
                    insert(usuario, senha, oracle, sql_insert)
                except ConnectionError:
                    print("\nErro ao conectar com o banco!")

            elif escolha_aprendizado == "3":
                print("\n---Histórias de Clientes---")
                tabela = "t_aprendizado_py"
                area_aprendizado = "Histórias de Clientes"
                try:
                    id_aprendizado = int(input("Insira o id aprendizado: "))
                    nm_aprendizado = input("Insira o nome da aprendizado: ")
                    ds_aprendizado = input("Insira a descrição da aprendizado: ")
                    valor_aprendizado = float(input("Insira o valor da aprendizado: "))
                    sql_insert = f"INSERT INTO {tabela} VALUES ( {id_aprendizado},'{area_aprendizado}', '{nm_aprendizado}', '{ds_aprendizado}', {valor_aprendizado})"

                    print("\nAdicionado com sucesso!")
                except ValueError:
                    print("\nValor não compatível. Retornando...")
                try:
                    insert(usuario, senha, oracle, sql_insert)
                except ConnectionError:
                    print("\nErro ao conectar com o banco!")

            elif escolha_aprendizado == "4":
                print("\n---Blogs---")
                tabela = "t_aprendizado_py"
                area_aprendizado = "Blogs"
                try:
                    id_aprendizado = int(input("Insira o id aprendizado: "))
                    nm_aprendizado = input("Insira o nome da aprendizado: ")
                    ds_aprendizado = input("Insira a descrição da aprendizado: ")
                    valor_aprendizado = float(input("Insira o valor da aprendizado: "))
                    sql_insert = f"INSERT INTO {tabela} VALUES ( {id_aprendizado},'{area_aprendizado}', '{nm_aprendizado}', '{ds_aprendizado}', {valor_aprendizado})"

                    print("\nAdicionado com sucesso!")
                except ValueError:
                    print("\nValor não compatível. Retornando...")
                try:
                    insert(usuario, senha, oracle, sql_insert)
                except ConnectionError:
                    print("\nErro ao conectar com o banco!")

            elif escolha_aprendizado == "5":
                print("\n---Voltando para o Menu---")
                self.menu_crud()

            elif escolha_aprendizado == "6":
                print("Saindo...")
                break
            else:
                print("\nOpção inválida. Selecione uma opção válida")
                self.menu_crud()
            self.mostrar_resumo_operacao("Aprendizado")

    def remover_menu_produtos(self):
        print("\n---Produtos ---")
        while True:
            print("\n---Menu Produtos---")
            print("1. Customer 360")
            print("2. Vendas")
            print("3. Atendimento ao Cliente")
            print("4. Marketing")
            print("5. Commerce")
            print("6. Data Cloud")
            print("7. Tableau")
            print("8. Mulesoft")
            print("9. Slack")
            print("10. Plataforma")
            print("11. Sustentabilidade")
            print("12. Voltar para menu")
            print("13. Sair")

            escolha_produto = input("Qual área deseja remover? (1-13): ")

            if escolha_produto == "1":
                tabela = "t_produto_py"
                print("\n---Customer 360---")
                try:
                    id_produto = int(input("Insira o id do produto que deseja remover: "))
                    sql_delete = f"DELETE FROM {tabela} WHERE id_produto = {id_produto}"
                    delete(usuario, senha, oracle, sql_delete)

                    print("\nDeletado com sucesso!")
                except ValueError:
                    print("\nValor não compatível. Retornando...")
                try:
                    delete(usuario, senha, oracle, sql_delete)
                except ConnectionError:
                    print("\nErro ao conectar com o banco!")

            elif escolha_produto == "2":
                tabela = "t_produto_py"
                print("\n---Vendas---")
                try:
                    id_produto = int(input("Insira o id do produto que deseja remover: "))
                    sql_delete = f"DELETE FROM {tabela} WHERE id_produto = {id_produto}"
                    delete(usuario, senha, oracle, sql_delete)

                    print("\nDeletado com sucesso!")
                except ValueError:
                    print("\nValor não compatível. Retornando...")
                try:
                    delete(usuario, senha, oracle, sql_delete)
                except ConnectionError:
                    print("\nErro ao conectar com o banco!")

            elif escolha_produto == "3":
                tabela = "t_produto_py"
                print("\n---Atendimento ao Cliente---")
                try:
                    id_produto = int(input("Insira o id do produto que deseja remover: "))
                    sql_delete = f"DELETE FROM {tabela} WHERE id_produto = {id_produto}"
                    delete(usuario, senha, oracle, sql_delete)

                    print("\nDeletado com sucesso!")
                except ValueError:
                    print("\nValor não compatível. Retornando...")
                try:
                    delete(usuario, senha, oracle, sql_delete)
                except ConnectionError:
                    print("\nErro ao conectar com o banco!")

            elif escolha_produto == "4":
                tabela = "t_produto_py"
                print("\n---Marketing---")
                try:
                    id_produto = int(input("Insira o id do produto que deseja remover: "))
                    sql_delete = f"DELETE FROM {tabela} WHERE id_produto = {id_produto}"
                    delete(usuario, senha, oracle, sql_delete)

                    print("\nDeletado com sucesso!")
                except ValueError:
                    print("\nValor não compatível. Retornando...")
                try:
                    delete(usuario, senha, oracle, sql_delete)
                except ConnectionError:
                    print("\nErro ao conectar com o banco!")

            elif escolha_produto == "5":
                tabela = "t_produto_py"
                print("\n---Commerce---")
                try:
                    id_produto = int(input("Insira o id do produto que deseja remover: "))
                    sql_delete = f"DELETE FROM {tabela} WHERE id_produto = {id_produto}"
                    delete(usuario, senha, oracle, sql_delete)

                    print("\nDeletado com sucesso!")
                except ValueError:
                    print("\nValor não compatível. Retornando...")
                try:
                    delete(usuario, senha, oracle, sql_delete)
                except ConnectionError:
                    print("\nErro ao conectar com o banco!")

            elif escolha_produto == "6":
                tabela = "t_produto_py"
                print("\n---Data Cloud---")
                try:
                    id_produto = int(input("Insira o id do produto que deseja remover: "))
                    sql_delete = f"DELETE FROM {tabela} WHERE id_produto = {id_produto}"
                    delete(usuario, senha, oracle, sql_delete)

                    print("\nDeletado com sucesso!")
                except ValueError:
                    print("\nValor não compatível. Retornando...")
                try:
                    delete(usuario, senha, oracle, sql_delete)
                except ConnectionError:
                    print("\nErro ao conectar com o banco!")

            elif escolha_produto == "7":
                tabela = "t_produto_py"
                print("\n---Tableau---")
                try:
                    id_produto = int(input("Insira o id do produto que deseja remover: "))
                    sql_delete = f"DELETE FROM {tabela} WHERE id_produto = {id_produto}"
                    delete(usuario, senha, oracle, sql_delete)

                    print("\nDeletado com sucesso!")
                except ValueError:
                    print("\nValor não compatível. Retornando...")
                try:
                    delete(usuario, senha, oracle, sql_delete)
                except ConnectionError:
                    print("\nErro ao conectar com o banco!")

            elif escolha_produto == "8":
                tabela = "t_produto_py"
                print("\n---Mulesoft---")
                try:
                    id_produto = int(input("Insira o id do produto que deseja remover: "))
                    sql_delete = f"DELETE FROM {tabela} WHERE id_produto = {id_produto}"
                    delete(usuario, senha, oracle, sql_delete)

                    print("\nDeletado com sucesso!")
                except ValueError:
                    print("\nValor não compatível. Retornando...")
                try:
                    delete(usuario, senha, oracle, sql_delete)
                except ConnectionError:
                    print("\nErro ao conectar com o banco!")

            elif escolha_produto == "9":
                tabela = "t_produto_py"
                print("\n---Slack---")
                try:
                    id_produto = int(input("Insira o id do produto que deseja remover: "))
                    sql_delete = f"DELETE FROM {tabela} WHERE id_produto = {id_produto}"
                    delete(usuario, senha, oracle, sql_delete)

                    print("\nDeletado com sucesso!")
                except ValueError:
                    print("\nValor não compatível. Retornando...")
                try:
                    delete(usuario, senha, oracle, sql_delete)
                except ConnectionError:
                    print("\nErro ao conectar com o banco!")

            elif escolha_produto == "10":
                tabela = "t_produto_py"
                print("\n---Plataforma---")
                try:
                    id_produto = int(input("Insira o id do produto que deseja remover: "))
                    sql_delete = f"DELETE FROM {tabela} WHERE id_produto = {id_produto}"
                    delete(usuario, senha, oracle, sql_delete)

                    print("\nDeletado com sucesso!")
                except ValueError:
                    print("\nValor não compatível. Retornando...")
                try:
                    delete(usuario, senha, oracle, sql_delete)
                except ConnectionError:
                    print("\nErro ao conectar com o banco!")

            elif escolha_produto == "11":
                tabela = "t_produto_py"
                print("\n---Sustentabilidade---")
                try:
                    id_produto = int(input("Insira o id do produto que deseja remover: "))
                    sql_delete = f"DELETE FROM {tabela} WHERE id_produto = {id_produto}"
                    delete(usuario, senha, oracle, sql_delete)

                    print("\nDeletado com sucesso!")
                except ValueError:
                    print("\nValor não compatível. Retornando...")
                try:
                    delete(usuario, senha, oracle, sql_delete)
                except ConnectionError:
                    print("\nErro ao conectar com o banco!")

            elif escolha_produto == "12":
                print("\n---Voltando para o Menu---")
                self.menu_crud()

            elif escolha_produto == "13":
                break
            else:
                print("\nOpção inválida. Selecione uma opção válida")
                self.menu_crud()

            self.mostrar_resumo_operacao("Produtos")

    def remover_menu_industrias(self):
        print("\n---Industrias---")
        while True:
            print("\n---Menu Indústrias---")
            print("1. Automotivo")
            print("2. Comunicações")
            print("3. Bens de Consumo")
            print("4. Serviços Financeiros")
            print("5. Saúde & Ciências da vida")
            print("6. Manufatura")
            print("7. Mídia")
            print("8. Setor Público")
            print("9. Varejo")
            print("10. Tecnologia")
            print("11. Voltar para o Menu")
            print("12. Sair")

            escolha_industria = input("Escolha a área que deseja remover (1-12): ")

            if escolha_industria == "1":
                print("\n---Automotivo---")
                tabela = "t_industria_py"
                try:
                    id_industria = int(input("Insira o id da indústria que deseja remover: "))
                    sql_delete = f"DELETE FROM {tabela} WHERE id_industria = {id_industria}"
                    delete(usuario, senha, oracle, sql_delete)

                    print("\nDeletado com sucesso!")
                except ValueError:
                    print("\nValor não compatível. Retornando...")
                try:
                    delete(usuario, senha, oracle, sql_delete)
                except ConnectionError:
                    print("\nErro ao conectar com o banco!")

            elif escolha_industria == "2":
                print("\n---Comunicações---")
                tabela = "t_industria_py"
                try:
                    id_industria = int(input("Insira o id da indústria que deseja remover: "))
                    sql_delete = f"DELETE FROM {tabela} WHERE id_industria = {id_industria}"
                    delete(usuario, senha, oracle, sql_delete)

                    print("\nDeletado com sucesso!")
                except ValueError:
                    print("\nValor não compatível. Retornando...")
                try:
                    delete(usuario, senha, oracle, sql_delete)
                except ConnectionError:
                    print("\nErro ao conectar com o banco!")

            elif escolha_industria == "3":
                print("\n---Bens de Consumo---")
                tabela = "t_industria_py"
                try:
                    id_industria = int(input("Insira o id da indústria que deseja remover: "))
                    sql_delete = f"DELETE FROM {tabela} WHERE id_industria = {id_industria}"
                    delete(usuario, senha, oracle, sql_delete)

                    print("\nDeletado com sucesso!")
                except ValueError:
                    print("\nValor não compatível. Retornando...")
                try:
                    delete(usuario, senha, oracle, sql_delete)
                except ConnectionError:
                    print("\nErro ao conectar com o banco!")

            elif escolha_industria == "4":
                print("\n---Serviços Financeiros---")
                tabela = "t_industria_py"
                try:
                    id_industria = int(input("Insira o id da indústria que deseja remover: "))
                    sql_delete = f"DELETE FROM {tabela} WHERE id_industria = {id_industria}"
                    delete(usuario, senha, oracle, sql_delete)

                    print("\nDeletado com sucesso!")
                except ValueError:
                    print("\nValor não compatível. Retornando...")
                try:
                    delete(usuario, senha, oracle, sql_delete)
                except ConnectionError:
                    print("\nErro ao conectar com o banco!")

            elif escolha_industria == "5":
                print("\n---Saúde & Ciências da vida---")
                tabela = "t_industria_py"
                try:
                    id_industria = int(input("Insira o id da indústria que deseja remover: "))
                    sql_delete = f"DELETE FROM {tabela} WHERE id_industria = {id_industria}"
                    delete(usuario, senha, oracle, sql_delete)

                    print("\nDeletado com sucesso!")
                except ValueError:
                    print("\nValor não compatível. Retornando...")
                try:
                    delete(usuario, senha, oracle, sql_delete)
                except ConnectionError:
                    print("\nErro ao conectar com o banco!")

            elif escolha_industria == "6":
                print("\n---Manufatura---")
                tabela = "t_industria_py"
                try:
                    id_industria = int(input("Insira o id da indústria que deseja remover: "))
                    sql_delete = f"DELETE FROM {tabela} WHERE id_industria = {id_industria}"
                    delete(usuario, senha, oracle, sql_delete)

                    print("\nDeletado com sucesso!")
                except ValueError:
                    print("\nValor não compatível. Retornando...")
                try:
                    delete(usuario, senha, oracle, sql_delete)
                except ConnectionError:
                    print("\nErro ao conectar com o banco!")

            elif escolha_industria == "7":
                print("\n---Mídia---")
                tabela = "t_industria_py"
                try:
                    id_industria = int(input("Insira o id da indústria que deseja remover: "))
                    sql_delete = f"DELETE FROM {tabela} WHERE id_industria = {id_industria}"
                    delete(usuario, senha, oracle, sql_delete)

                    print("\nDeletado com sucesso!")
                except ValueError:
                    print("\nValor não compatível. Retornando...")
                try:
                    delete(usuario, senha, oracle, sql_delete)
                except ConnectionError:
                    print("\nErro ao conectar com o banco!")

            elif escolha_industria == "8":
                print("\n---Setor Público---")
                tabela = "t_industria_py"
                try:
                    id_industria = int(input("Insira o id da indústria que deseja remover: "))
                    sql_delete = f"DELETE FROM {tabela} WHERE id_industria = {id_industria}"
                    delete(usuario, senha, oracle, sql_delete)

                    print("\nDeletado com sucesso!")
                except ValueError:
                    print("\nValor não compatível. Retornando...")
                try:
                    delete(usuario, senha, oracle, sql_delete)
                except ConnectionError:
                    print("\nErro ao conectar com o banco!")

            elif escolha_industria == "9":
                print("\n---Varejo---")
                tabela = "t_industria_py"
                try:
                    id_industria = int(input("Insira o id da indústria que deseja remover: "))
                    sql_delete = f"DELETE FROM {tabela} WHERE id_industria = {id_industria}"
                    delete(usuario, senha, oracle, sql_delete)

                    print("\nDeletado com sucesso!")
                except ValueError:
                    print("\nValor não compatível. Retornando...")
                try:
                    delete(usuario, senha, oracle, sql_delete)
                except ConnectionError:
                    print("\nErro ao conectar com o banco!")

            elif escolha_industria == "10":
                print("\n---Tecnologia---")
                tabela = "t_industria_py"
                try:
                    id_industria = int(input("Insira o id da indústria que deseja remover: "))
                    sql_delete = f"DELETE FROM {tabela} WHERE id_industria = {id_industria}"
                    delete(usuario, senha, oracle, sql_delete)

                    print("\nDeletado com sucesso!")
                except ValueError:
                    print("\nValor não compatível. Retornando...")
                try:
                    delete(usuario, senha, oracle, sql_delete)
                except ConnectionError:
                    print("\nErro ao conectar com o banco!")

            elif escolha_industria == "11":
                print("\n---Voltando para o Menu---")
                self.menu_crud()

            elif escolha_industria == "12":
                print("Saindo...")
                break
            else:
                print("\nOpção inválida. Selecione uma opção válida")
                self.menu_crud()
            self.mostrar_resumo_operacao("Indústrias")

    def remover_menu_aprendizado(self):
        while True:
            print("\n---Aprendizado ---")
            print("\n---Menu Aprendizado---\n")
            print("1. Trailhead")
            print("2. Eventos & Experiências")
            print("3. Histórias de Clientes")
            print("4. Blogs")
            print("5. Voltar para o Menu")
            print("6. Sair")

            escolha_aprendizado = input("Escolha a área que deseja remover (1-6): ")

            if escolha_aprendizado == "1":
                print("\n---Trailhead---")
                tabela = "t_aprendizado_py"
                try:
                    id_aprendizado = int(input("Insira o id do aprendizado que deseja remover: "))
                    sql_delete = f"DELETE FROM {tabela} WHERE id_aprendizado = {id_aprendizado}"
                    delete(usuario, senha, oracle, sql_delete)

                    print("\nDeletado com sucesso!")
                except ValueError:
                    print("\nValor não compatível. Retornando...")
                try:
                    delete(usuario, senha, oracle, sql_delete)
                except ConnectionError:
                    print("\nErro ao conectar com o banco!")

            elif escolha_aprendizado == "2":
                print("\n---Eventos & Experiências---")
                tabela = "t_aprendizado_py"
                try:
                    id_aprendizado = int(input("Insira o id do aprendizado que deseja remover: "))
                    sql_delete = f"DELETE FROM {tabela} WHERE id_aprendizado = {id_aprendizado}"
                    delete(usuario, senha, oracle, sql_delete)

                    print("\nDeletado com sucesso!")
                except ValueError:
                    print("\nValor não compatível. Retornando...")
                try:
                    delete(usuario, senha, oracle, sql_delete)
                except ConnectionError:
                    print("\nErro ao conectar com o banco!")

            elif escolha_aprendizado == "3":
                print("\n---Histórias de Clientes---")
                tabela = "t_aprendizado_py"
                try:
                    id_aprendizado = int(input("Insira o id do aprendizado que deseja remover: "))
                    sql_delete = f"DELETE FROM {tabela} WHERE id_aprendizado = {id_aprendizado}"
                    delete(usuario, senha, oracle, sql_delete)

                    print("\nDeletado com sucesso!")
                except ValueError:
                    print("\nValor não compatível. Retornando...")
                try:
                    delete(usuario, senha, oracle, sql_delete)
                except ConnectionError:
                    print("\nErro ao conectar com o banco!")

            elif escolha_aprendizado == "4":
                print("\n---Blogs---")
                tabela = "t_aprendizado_py"
                try:
                    id_aprendizado = int(input("Insira o id do aprendizado que deseja remover: "))
                    sql_delete = f"DELETE FROM {tabela} WHERE id_aprendizado = {id_aprendizado}"
                    delete(usuario, senha, oracle, sql_delete)

                    print("\nDeletado com sucesso!")
                except ValueError:
                    print("\nValor não compatível. Retornando...")
                try:
                    delete(usuario, senha, oracle, sql_delete)
                except ConnectionError:
                    print("\nErro ao conectar com o banco!")

            elif escolha_aprendizado == "5":
                print("\n---Voltando para o Menu---")
                self.menu_crud()

            elif escolha_aprendizado == "6":
                print("Saindo...")
                break
            else:
                print("\nOpção inválida. Selecione uma opção válida")
                self.menu_crud()
            self.mostrar_resumo_operacao("Aprendizado")

    def atualizar_menu_produtos(self):
        print("\n---Produtos ---")
        while True:
            print("\n---Menu Produtos---")
            print("1. Customer 360")
            print("2. Vendas")
            print("3. Atendimento ao Cliente")
            print("4. Marketing")
            print("5. Commerce")
            print("6. Data Cloud")
            print("7. Tableau")
            print("8. Mulesoft")
            print("9. Slack")
            print("10. Plataforma")
            print("11. Sustentabilidade")
            print("12. Voltar para menu")
            print("13. Sair")

            escolha_produto = input("Qual área deseja atualizar? (1-13): ")

            if escolha_produto == "1":
                tabela = "t_produto_py"
                print("\n---Customer 360---")
                try:
                    id_produto = int(input("Insira o id do produto que deseja alterar: "))
                    alterar_produto = str(input("Insira o que deseja alterar: "))
                    produto_alterado = str(input("Insira para o que deseja alterar: "))
                    sql_update = f"UPDATE {tabela} SET {alterar_produto} = {produto_alterado} where id_produto = {id_produto}"
                    update(usuario, senha, oracle, sql_update)

                    print("\nAtualizado com sucesso!")
                except ValueError:
                    print("\nValor não compatível. Retornando...")
                try:
                    update(usuario, senha, oracle, sql_update)
                except ConnectionError:
                    print("\nErro ao conectar com o banco!")

            elif escolha_produto == "2":
                tabela = "t_produto_py"
                print("\n---Vendas---")
                try:
                    id_produto = int(input("Insira o id do produto que deseja alterar: "))
                    alterar_produto = str(input("Insira o que deseja alterar: "))
                    produto_alterado = str(input("Insira para o que deseja alterar: "))
                    sql_update = f"UPDATE {tabela} SET {alterar_produto} = {produto_alterado} where id_produto = {id_produto}"
                    update(usuario, senha, oracle, sql_update)

                    print("\nAtualizado com sucesso!")
                except ValueError:
                    print("\nValor não compatível. Retornando...")
                try:
                    update(usuario, senha, oracle, sql_update)
                except ConnectionError:
                    print("\nErro ao conectar com o banco!")

            elif escolha_produto == "3":
                tabela = "t_produto_py"
                print("\n---Atendimento ao Cliente---")
                try:
                    id_produto = int(input("Insira o id do produto que deseja alterar: "))
                    alterar_produto = str(input("Insira o que deseja alterar: "))
                    produto_alterado = str(input("Insira para o que deseja alterar: "))
                    sql_update = f"UPDATE {tabela} SET {alterar_produto} = {produto_alterado} where id_produto = {id_produto}"
                    update(usuario, senha, oracle, sql_update)

                    print("\nAtualizado com sucesso!")
                except ValueError:
                    print("\nValor não compatível. Retornando...")
                try:
                    update(usuario, senha, oracle, sql_update)
                except ConnectionError:
                    print("\nErro ao conectar com o banco!")

            elif escolha_produto == "4":
                tabela = "t_produto_py"
                print("\n---Marketing---")
                try:
                    id_produto = int(input("Insira o id do produto que deseja alterar: "))
                    alterar_produto = str(input("Insira o que deseja alterar: "))
                    produto_alterado = str(input("Insira para o que deseja alterar: "))
                    sql_update = f"UPDATE {tabela} SET {alterar_produto} = {produto_alterado} where id_produto = {id_produto}"
                    update(usuario, senha, oracle, sql_update)

                    print("\nAtualizado com sucesso!")
                except ValueError:
                    print("\nValor não compatível. Retornando...")
                try:
                    update(usuario, senha, oracle, sql_update)
                except ConnectionError:
                    print("\nErro ao conectar com o banco!")

            elif escolha_produto == "5":
                tabela = "t_produto_py"
                print("\n---Commerce---")
                try:
                    id_produto = int(input("Insira o id do produto que deseja alterar: "))
                    alterar_produto = str(input("Insira o que deseja alterar: "))
                    produto_alterado = str(input("Insira para o que deseja alterar: "))
                    sql_update = f"UPDATE {tabela} SET {alterar_produto} = {produto_alterado} where id_produto = {id_produto}"
                    update(usuario, senha, oracle, sql_update)

                    print("\nAtualizado com sucesso!")
                except ValueError:
                    print("\nValor não compatível. Retornando...")
                try:
                    update(usuario, senha, oracle, sql_update)
                except ConnectionError:
                    print("\nErro ao conectar com o banco!")

            elif escolha_produto == "6":
                tabela = "t_produto_py"
                print("\n---Data Cloud---")
                try:
                    id_produto = int(input("Insira o id do produto que deseja alterar: "))
                    alterar_produto = str(input("Insira o que deseja alterar: "))
                    produto_alterado = str(input("Insira para o que deseja alterar: "))
                    sql_update = f"UPDATE {tabela} SET {alterar_produto} = {produto_alterado} where id_produto = {id_produto}"
                    update(usuario, senha, oracle, sql_update)

                    print("\nAtualizado com sucesso!")
                except ValueError:
                    print("\nValor não compatível. Retornando...")
                try:
                    update(usuario, senha, oracle, sql_update)
                except ConnectionError:
                    print("\nErro ao conectar com o banco!")

            elif escolha_produto == "7":
                tabela = "t_produto_py"
                print("\n---Tableau---")
                try:
                    id_produto = int(input("Insira o id do produto que deseja alterar: "))
                    alterar_produto = str(input("Insira o que deseja alterar: "))
                    produto_alterado = str(input("Insira para o que deseja alterar: "))
                    sql_update = f"UPDATE {tabela} SET {alterar_produto} = {produto_alterado} where id_produto = {id_produto}"
                    update(usuario, senha, oracle, sql_update)

                    print("\nAtualizado com sucesso!")
                except ValueError:
                    print("\nValor não compatível. Retornando...")
                try:
                    update(usuario, senha, oracle, sql_update)
                except ConnectionError:
                    print("\nErro ao conectar com o banco!")

            elif escolha_produto == "8":
                tabela = "t_produto_py"
                print("\n---Mulesoft---")
                try:
                    id_produto = int(input("Insira o id do produto que deseja alterar: "))
                    alterar_produto = str(input("Insira o que deseja alterar: "))
                    produto_alterado = str(input("Insira para o que deseja alterar: "))
                    sql_update = f"UPDATE {tabela} SET {alterar_produto} = {produto_alterado} where id_produto = {id_produto}"
                    update(usuario, senha, oracle, sql_update)

                    print("\nAtualizado com sucesso!")
                except ValueError:
                    print("\nValor não compatível. Retornando...")
                try:
                    update(usuario, senha, oracle, sql_update)
                except ConnectionError:
                    print("\nErro ao conectar com o banco!")

            elif escolha_produto == "9":
                tabela = "t_produto_py"
                print("\n---Slack---")
                try:
                    id_produto = int(input("Insira o id do produto que deseja alterar: "))
                    alterar_produto = str(input("Insira o que deseja alterar: "))
                    produto_alterado = str(input("Insira para o que deseja alterar: "))
                    sql_update = f"UPDATE {tabela} SET {alterar_produto} = {produto_alterado} where id_produto = {id_produto}"
                    update(usuario, senha, oracle, sql_update)

                    print("\nAtualizado com sucesso!")
                except ValueError:
                    print("\nValor não compatível. Retornando...")
                try:
                    update(usuario, senha, oracle, sql_update)
                except ConnectionError:
                    print("\nErro ao conectar com o banco!")

            elif escolha_produto == "10":
                tabela = "t_produto_py"
                print("\n---Plataforma---")
                try:
                    id_produto = int(input("Insira o id do produto que deseja alterar: "))
                    alterar_produto = str(input("Insira o que deseja alterar: "))
                    produto_alterado = str(input("Insira para o que deseja alterar: "))
                    sql_update = f"UPDATE {tabela} SET {alterar_produto} = {produto_alterado} where id_produto = {id_produto}"
                    update(usuario, senha, oracle, sql_update)

                    print("\nAtualizado com sucesso!")
                except ValueError:
                    print("\nValor não compatível. Retornando...")
                try:
                    update(usuario, senha, oracle, sql_update)
                except ConnectionError:
                    print("\nErro ao conectar com o banco!")

            elif escolha_produto == "11":
                tabela = "t_produto_py"
                print("\n---Sustentabilidade---")
                try:
                    id_produto = int(input("Insira o id do produto que deseja alterar: "))
                    alterar_produto = str(input("Insira o que deseja alterar: "))
                    produto_alterado = str(input("Insira para o que deseja alterar: "))
                    sql_update = f"UPDATE {tabela} SET {alterar_produto} = {produto_alterado} where id_produto = {id_produto}"
                    update(usuario, senha, oracle, sql_update)

                    print("\nAtualizado com sucesso!")
                except ValueError:
                    print("\nValor não compatível. Retornando...")
                try:
                    update(usuario, senha, oracle, sql_update)
                except ConnectionError:
                    print("\nErro ao conectar com o banco!")

            elif escolha_produto == "12":
                print("\n---Voltando para o Menu---")
                self.menu_crud()

            elif escolha_produto == "13":
                break
            else:
                print("\nOpção inválida. Selecione uma opção válida")
                self.menu_crud()

            self.mostrar_resumo_operacao("Produtos")

    def atualizar_menu_industrias(self):
        print("\n---Industrias---")
        while True:
            print("\n---Menu Indústrias---")
            print("1. Automotivo")
            print("2. Comunicações")
            print("3. Bens de Consumo")
            print("4. Serviços Financeiros")
            print("5. Saúde & Ciências da vida")
            print("6. Manufatura")
            print("7. Mídia")
            print("8. Setor Público")
            print("9. Varejo")
            print("10. Tecnologia")
            print("11. Voltar para o Menu")
            print("12. Sair")

            escolha_industria = input("Escolha a área que deseja atualizar (1-12): ")

            if escolha_industria == "1":
                print("\n---Automotivo---")
                tabela = "t_industria_py"
                try:
                    id_industria = int(input("Insira o id do produto que deseja alterar: "))
                    alterar_industria = str(input("Insira o que deseja alterar: "))
                    industria_alterada = str(input("Insira para o que deseja alterar: "))
                    sql_update = f"UPDATE {tabela} SET {alterar_industria} = {industria_alterada} where id_produto = {id_industria}"
                    update(usuario, senha, oracle, sql_update)

                    print("\nAtualizado com sucesso!")
                except ValueError:
                    print("\nValor não compatível. Retornando...")
                try:
                    update(usuario, senha, oracle, sql_update)
                except ConnectionError:
                    print("\nErro ao conectar com o banco!")

            elif escolha_industria == "2":
                print("\n---Comunicações---")
                tabela = "t_industria_py"
                try:
                    id_industria = int(input("Insira o id do produto que deseja alterar: "))
                    alterar_industria = str(input("Insira o que deseja alterar: "))
                    industria_alterada = str(input("Insira para o que deseja alterar: "))
                    sql_update = f"UPDATE {tabela} SET {alterar_industria} = {industria_alterada} where id_produto = {id_industria}"
                    update(usuario, senha, oracle, sql_update)

                    print("\nAtualizado com sucesso!")
                except ValueError:
                    print("\nValor não compatível. Retornando...")
                try:
                    update(usuario, senha, oracle, sql_update)
                except ConnectionError:
                    print("\nErro ao conectar com o banco!")

            elif escolha_industria == "3":
                print("\n---Bens de Consumo---")
                tabela = "t_industria_py"
                try:
                    id_industria = int(input("Insira o id do produto que deseja alterar: "))
                    alterar_industria = str(input("Insira o que deseja alterar: "))
                    industria_alterada = str(input("Insira para o que deseja alterar: "))
                    sql_update = f"UPDATE {tabela} SET {alterar_industria} = {industria_alterada} where id_produto = {id_industria}"
                    update(usuario, senha, oracle, sql_update)

                    print("\nAtualizado com sucesso!")
                except ValueError:
                    print("\nValor não compatível. Retornando...")
                try:
                    update(usuario, senha, oracle, sql_update)
                except ConnectionError:
                    print("\nErro ao conectar com o banco!")

            elif escolha_industria == "4":
                print("\n---Serviços Financeiros---")
                tabela = "t_industria_py"
                try:
                    id_industria = int(input("Insira o id do produto que deseja alterar: "))
                    alterar_industria = str(input("Insira o que deseja alterar: "))
                    industria_alterada = str(input("Insira para o que deseja alterar: "))
                    sql_update = f"UPDATE {tabela} SET {alterar_industria} = {industria_alterada} where id_produto = {id_industria}"
                    update(usuario, senha, oracle, sql_update)

                    print("\nAtualizado com sucesso!")
                except ValueError:
                    print("\nValor não compatível. Retornando...")
                try:
                    update(usuario, senha, oracle, sql_update)
                except ConnectionError:
                    print("\nErro ao conectar com o banco!")

            elif escolha_industria == "5":
                print("\n---Saúde & Ciências da vida---")
                tabela = "t_industria_py"
                try:
                    id_industria = int(input("Insira o id do produto que deseja alterar: "))
                    alterar_industria = str(input("Insira o que deseja alterar: "))
                    industria_alterada = str(input("Insira para o que deseja alterar: "))
                    sql_update = f"UPDATE {tabela} SET {alterar_industria} = {industria_alterada} where id_produto = {id_industria}"
                    update(usuario, senha, oracle, sql_update)

                    print("\nAtualizado com sucesso!")
                except ValueError:
                    print("\nValor não compatível. Retornando...")
                try:
                    update(usuario, senha, oracle, sql_update)
                except ConnectionError:
                    print("\nErro ao conectar com o banco!")

            elif escolha_industria == "6":
                print("\n---Manufatura---")
                tabela = "t_industria_py"
                try:
                    id_industria = int(input("Insira o id do produto que deseja alterar: "))
                    alterar_industria = str(input("Insira o que deseja alterar: "))
                    industria_alterada = str(input("Insira para o que deseja alterar: "))
                    sql_update = f"UPDATE {tabela} SET {alterar_industria} = {industria_alterada} where id_produto = {id_industria}"
                    update(usuario, senha, oracle, sql_update)

                    print("\nAtualizado com sucesso!")
                except ValueError:
                    print("\nValor não compatível. Retornando...")
                try:
                    update(usuario, senha, oracle, sql_update)
                except ConnectionError:
                    print("\nErro ao conectar com o banco!")

            elif escolha_industria == "7":
                print("\n---Mídia---")
                tabela = "t_industria_py"
                try:
                    id_industria = int(input("Insira o id do produto que deseja alterar: "))
                    alterar_industria = str(input("Insira o que deseja alterar: "))
                    industria_alterada = str(input("Insira para o que deseja alterar: "))
                    sql_update = f"UPDATE {tabela} SET {alterar_industria} = {industria_alterada} where id_produto = {id_industria}"
                    update(usuario, senha, oracle, sql_update)

                    print("\nAtualizado com sucesso!")
                except ValueError:
                    print("\nValor não compatível. Retornando...")
                try:
                    update(usuario, senha, oracle, sql_update)
                except ConnectionError:
                    print("\nErro ao conectar com o banco!")

            elif escolha_industria == "8":
                print("\n---Setor Público---")
                tabela = "t_industria_py"
                try:
                    id_industria = int(input("Insira o id do produto que deseja alterar: "))
                    alterar_industria = str(input("Insira o que deseja alterar: "))
                    industria_alterada = str(input("Insira para o que deseja alterar: "))
                    sql_update = f"UPDATE {tabela} SET {alterar_industria} = {industria_alterada} where id_produto = {id_industria}"
                    update(usuario, senha, oracle, sql_update)

                    print("\nAtualizado com sucesso!")
                except ValueError:
                    print("\nValor não compatível. Retornando...")
                try:
                    update(usuario, senha, oracle, sql_update)
                except ConnectionError:
                    print("\nErro ao conectar com o banco!")

            elif escolha_industria == "9":
                print("\n---Varejo---")
                tabela = "t_industria_py"
                try:
                    id_industria = int(input("Insira o id do produto que deseja alterar: "))
                    alterar_industria = str(input("Insira o que deseja alterar: "))
                    industria_alterada = str(input("Insira para o que deseja alterar: "))
                    sql_update = f"UPDATE {tabela} SET {alterar_industria} = {industria_alterada} where id_produto = {id_industria}"
                    update(usuario, senha, oracle, sql_update)

                    print("\nAtualizado com sucesso!")
                except ValueError:
                    print("\nValor não compatível. Retornando...")
                try:
                    update(usuario, senha, oracle, sql_update)
                except ConnectionError:
                    print("\nErro ao conectar com o banco!")

            elif escolha_industria == "10":
                print("\n---Tecnologia---")
                tabela = "t_industria_py"
                try:
                    id_industria = int(input("Insira o id do produto que deseja alterar: "))
                    alterar_industria = str(input("Insira o que deseja alterar: "))
                    industria_alterada = str(input("Insira para o que deseja alterar: "))
                    sql_update = f"UPDATE {tabela} SET {alterar_industria} = {industria_alterada} where id_produto = {id_industria}"
                    update(usuario, senha, oracle, sql_update)

                    print("\nAtualizado com sucesso!")
                except ValueError:
                    print("\nValor não compatível. Retornando...")
                try:
                    update(usuario, senha, oracle, sql_update)
                except ConnectionError:
                    print("\nErro ao conectar com o banco!")

            elif escolha_industria == "11":
                print("\n---Voltando para o Menu---")
                self.menu_crud()

            elif escolha_industria == "12":
                print("Saindo...")
                break
            else:
                print("\nOpção inválida. Selecione uma opção válida")
                self.menu_crud()
            self.mostrar_resumo_operacao("Indústrias")

    def atualizar_menu_aprendizado(self):
        while True:
            print("\n---Aprendizado ---")
            print("\n---Menu Aprendizado---\n")
            print("1. Trailhead")
            print("2. Eventos & Experiências")
            print("3. Histórias de Clientes")
            print("4. Blogs")
            print("5. Voltar para o Menu")
            print("6. Sair")

            escolha_aprendizado = input("Escolha a área que deseja remover (1-6): ")

            if escolha_aprendizado == "1":
                print("\n---Trailhead---")
                tabela = "t_aprendizado_py"
                try:
                    id_aprendizado = int(input("Insira o id do produto que deseja alterar: "))
                    alterar_aprendizado = str(input("Insira o que deseja alterar: "))
                    aprendizado_alterado = str(input("Insira para o que deseja alterar: "))
                    sql_update = f"UPDATE {tabela} SET {alterar_aprendizado} = {aprendizado_alterado} where id_produto = {id_aprendizado}"
                    update(usuario, senha, oracle, sql_update)

                    print("\nAtualizado com sucesso!")
                except ValueError:
                    print("\nValor não compatível. Retornando...")
                try:
                    update(usuario, senha, oracle, sql_update)
                except ConnectionError:
                    print("\nErro ao conectar com o banco!")

            elif escolha_aprendizado == "2":
                print("\n---Eventos & Experiências---")
                tabela = "t_aprendizado_py"
                try:
                    id_aprendizado = int(input("Insira o id do produto que deseja alterar: "))
                    alterar_aprendizado = str(input("Insira o que deseja alterar: "))
                    aprendizado_alterado = str(input("Insira para o que deseja alterar: "))
                    sql_update = f"UPDATE {tabela} SET {alterar_aprendizado} = {aprendizado_alterado} where id_produto = {id_aprendizado}"
                    update(usuario, senha, oracle, sql_update)

                    print("\nAtualizado com sucesso!")
                except ValueError:
                    print("\nValor não compatível. Retornando...")
                try:
                    update(usuario, senha, oracle, sql_update)
                except ConnectionError:
                    print("\nErro ao conectar com o banco!")

            elif escolha_aprendizado == "3":
                print("\n---Histórias de Clientes---")
                tabela = "t_aprendizado_py"
                try:
                    id_aprendizado = int(input("Insira o id do produto que deseja alterar: "))
                    alterar_aprendizado = str(input("Insira o que deseja alterar: "))
                    aprendizado_alterado = str(input("Insira para o que deseja alterar: "))
                    sql_update = f"UPDATE {tabela} SET {alterar_aprendizado} = {aprendizado_alterado} where id_produto = {id_aprendizado}"
                    update(usuario, senha, oracle, sql_update)

                    print("\nAtualizado com sucesso!")
                except ValueError:
                    print("\nValor não compatível. Retornando...")
                try:
                    update(usuario, senha, oracle, sql_update)
                except ConnectionError:
                    print("\nErro ao conectar com o banco!")

            elif escolha_aprendizado == "4":
                print("\n---Blogs---")
                tabela = "t_aprendizado_py"
                try:
                    id_aprendizado = int(input("Insira o id do produto que deseja alterar: "))
                    alterar_aprendizado = str(input("Insira o que deseja alterar: "))
                    aprendizado_alterado = str(input("Insira para o que deseja alterar: "))
                    sql_update = f"UPDATE {tabela} SET {alterar_aprendizado} = {aprendizado_alterado} where id_produto = {id_aprendizado}"
                    update(usuario, senha, oracle, sql_update)

                    print("\nAtualizado com sucesso!")
                except ValueError:
                    print("\nValor não compatível. Retornando...")
                try:
                    update(usuario, senha, oracle, sql_update)
                except ConnectionError:
                    print("\nErro ao conectar com o banco!")

            elif escolha_aprendizado == "5":
                print("\n---Voltando para o Menu---")
                self.menu_crud()

            elif escolha_aprendizado == "6":
                print("Saindo...")
                break
            else:
                print("\nOpção inválida. Selecione uma opção válida")
                self.menu_crud()
            self.mostrar_resumo_operacao("Aprendizado")

    def pesquisar_menu_produtos(self):
        print("\n---Produtos ---")

        while True:
            print("\n---Menu Produtos---")
            print("1. Customer 360")
            print("2. Vendas")
            print("3. Atendimento ao Cliente")
            print("4. Marketing")
            print("5. Commerce")
            print("6. Data Cloud")
            print("7. Tableau")
            print("8. Mulesoft")
            print("9. Slack")
            print("10. Plataforma")
            print("11. Sustentabilidade")
            print("12. Visualizar Tudo")
            print("13. Voltar para menu")
            print("14. Sair")

            escolha_produto = input("Qual área deseja visualizar? (1-14): ")

            if escolha_produto == "1":
                tabela = "t_produto_py"
                print("\n---Customer 360---")
                area_produto = "Customer 360"
                try:
                    sql_select = f"select * from {tabela} Where area_produto = '{area_produto}'"
                    print("\nBusca feita com sucesso!")
                except ValueError:
                    print("\nValor não compatível. Retornando...")
                try:
                    select(usuario, senha, oracle, sql_select)
                except ConnectionError:
                    print("\nErro ao conectar com o banco!")

            elif escolha_produto == "2":
                tabela = "t_produto_py"
                print("\n---Vendas---")
                area_produto = "Vendas"
                try:
                    sql_select = f"select * from {tabela} Where area_produto = '{area_produto}'"
                    select(usuario, senha, oracle, sql_select)

                    print("\nBusca feita com sucesso!")
                except ValueError:
                    print("\nValor não compatível. Retornando...")
                try:
                    select(usuario, senha, oracle, sql_select)
                except ConnectionError:
                    print("\nErro ao conectar com o banco!")

            elif escolha_produto == "3":
                tabela = "t_produto_py"
                print("\n---Atendimento ao Cliente---")
                area_produto = "Atendimento ao Cliente"
                try:
                    sql_select = f"select * from {tabela} Where area_produto = '{area_produto}'"
                    select(usuario, senha, oracle, sql_select)

                    print("\nBusca feita com sucesso!")
                except ValueError:
                    print("\nValor não compatível. Retornando...")
                try:
                    select(usuario, senha, oracle, sql_select)
                except ConnectionError:
                    print("\nErro ao conectar com o banco!")

            elif escolha_produto == "4":
                tabela = "t_produto_py"
                print("\n---Marketing---")
                area_produto = "Marketing"
                try:
                    sql_select = f"select * from {tabela} Where area_produto = '{area_produto}'"
                    select(usuario, senha, oracle, sql_select)

                    print("\nBusca feita com sucesso!")
                except ValueError:
                    print("\nValor não compatível. Retornando...")
                try:
                    select(usuario, senha, oracle, sql_select)
                except ConnectionError:
                    print("\nErro ao conectar com o banco!")

            elif escolha_produto == "5":
                tabela = "t_produto_py"
                print("\n---Commerce---")
                area_produto = "Commerce"
                try:
                    sql_select = f"select * from {tabela} Where area_produto = '{area_produto}'"
                    select(usuario, senha, oracle, sql_select)

                    print("\nBusca feita com sucesso!")
                except ValueError:
                    print("\nValor não compatível. Retornando...")
                try:
                    select(usuario, senha, oracle, sql_select)
                except ConnectionError:
                    print("\nErro ao conectar com o banco!")

            elif escolha_produto == "6":
                tabela = "t_produto_py"
                print("\n---Data Cloud---")
                area_produto = "Data Cloud"
                try:
                    sql_select = f"select * from {tabela} Where area_produto = '{area_produto}'"
                    select(usuario, senha, oracle, sql_select)

                    print("\nBusca feita com sucesso!")
                except ValueError:
                    print("\nValor não compatível. Retornando...")
                try:
                    select(usuario, senha, oracle, sql_select)
                except ConnectionError:
                    print("\nErro ao conectar com o banco!")

            elif escolha_produto == "7":
                tabela = "t_produto_py"
                print("\n---Tableau---")
                area_produto = "Tableau"
                try:
                    sql_select = f"select * from {tabela} Where area_produto = '{area_produto}'"
                    select(usuario, senha, oracle, sql_select)

                    print("\nBusca feita com sucesso!")
                except ValueError:
                    print("\nValor não compatível. Retornando...")
                try:
                    select(usuario, senha, oracle, sql_select)
                except ConnectionError:
                    print("\nErro ao conectar com o banco!")

            elif escolha_produto == "8":
                tabela = "t_produto_py"
                print("\n---Mulesoft---")
                area_produto = "Mulesoft"
                try:
                    sql_select = f"select * from {tabela} Where area_produto = '{area_produto}'"
                    select(usuario, senha, oracle, sql_select)

                    print("\nBusca feita com sucesso!")
                except ValueError:
                    print("\nValor não compatível. Retornando...")
                try:
                    select(usuario, senha, oracle, sql_select)
                except ConnectionError:
                    print("\nErro ao conectar com o banco!")

            elif escolha_produto == "9":
                tabela = "t_produto_py"
                print("\n---Slack---")
                area_produto = "Slack"
                try:
                    sql_select = f"select * from {tabela} Where area_produto = '{area_produto}'"
                    select(usuario, senha, oracle, sql_select)

                    print("\nBusca feita com sucesso!")
                except ValueError:
                    print("\nValor não compatível. Retornando...")
                try:
                    select(usuario, senha, oracle, sql_select)
                except ConnectionError:
                    print("\nErro ao conectar com o banco!")

            elif escolha_produto == "10":
                tabela = "t_produto_py"
                print("\n---Plataforma---")
                area_produto = "Plataforma"
                try:
                    sql_select = f"select * from {tabela} Where area_produto = '{area_produto}'"
                    select(usuario, senha, oracle, sql_select)

                    print("\nBusca feita com sucesso!")
                except ValueError:
                    print("\nValor não compatível. Retornando...")
                try:
                    select(usuario, senha, oracle, sql_select)
                except ConnectionError:
                    print("\nErro ao conectar com o banco!")

            elif escolha_produto == "11":
                tabela = "t_produto_py"
                print("\n---Sustentabilidade---")
                area_produto = "Sustentabilidade"
                try:
                    sql_select = f"select * from {tabela} Where area_produto = '{area_produto}'"
                    select(usuario, senha, oracle, sql_select)

                    print("\nBusca feita com sucesso!")
                except ValueError:
                    print("\nValor não compatível. Retornando...")
                try:
                    select(usuario, senha, oracle, sql_select)
                except ConnectionError:
                    print("\nErro ao conectar com o banco!")

            elif escolha_produto == "12":
                tabela = "t_produto_py"
                print("Visualizando Tudo")
                try:
                    sql_select = f"select * from {tabela}"
                    select(usuario, senha, oracle, sql_select)

                    print("\nBusca feita com sucesso!")
                except ValueError:
                    print("\nValor não compatível. Retornando...")
                try:
                    select(usuario, senha, oracle, sql_select)
                except ConnectionError:
                    print("\nErro ao conectar com o banco!")


            elif escolha_produto == "13":
                print("\n---Voltando para o Menu---")
                self.menu_crud()

            elif escolha_produto == "14":
                break
            else:
                print("\nOpção inválida. Selecione uma opção válida")
                self.menu_crud()

            self.mostrar_resumo_operacao("Produtos")


    def pesquisar_menu_industrias(self):
        print("\n---Industrias---")
        while True:
            print("\n---Menu Indústrias---")
            print("1. Automotivo")
            print("2. Comunicações")
            print("3. Bens de Consumo")
            print("4. Serviços Financeiros")
            print("5. Saúde & Ciências da vida")
            print("6. Manufatura")
            print("7. Mídia")
            print("8. Setor Público")
            print("9. Varejo")
            print("10. Tecnologia")
            print("11. Selecionar Tudo")
            print("12. Voltar para o Menu")
            print("13. Sair")

            escolha_industria = input("Escolha a área que deseja atualizar (1-12): ")

            if escolha_industria == "1":
                print("\n---Automotivo---")
                tabela = "t_industria_py"
                area_produto = "Automotivo"
                try:
                    sql_select = f"select * from {tabela} Where area_produto = '{area_produto}'"
                    select(usuario, senha, oracle, sql_select)

                    print("\nBusca feita com sucesso!")
                except ValueError:
                    print("\nValor não compatível. Retornando...")
                try:
                    select(usuario, senha, oracle, sql_select)
                except ConnectionError:
                    print("\nErro ao conectar com o banco!")

            elif escolha_industria == "2":
                print("\n---Comunicações---")
                tabela = "t_industria_py"
                area_produto = "Comunicações"
                try:
                    sql_select = f"select * from {tabela} Where area_produto = '{area_produto}'"
                    select(usuario, senha, oracle, sql_select)

                    print("\nBusca feita com sucesso!")
                except ValueError:
                    print("\nValor não compatível. Retornando...")
                try:
                    select(usuario, senha, oracle, sql_select)
                except ConnectionError:
                    print("\nErro ao conectar com o banco!")

            elif escolha_industria == "3":
                print("\n---Bens de Consumo---")
                tabela = "t_industria_py"
                area_produto = "Bens de Consumo"
                try:
                    sql_select = f"select * from {tabela} Where area_produto = '{area_produto}'"
                    select(usuario, senha, oracle, sql_select)

                    print("\nBusca feita com sucesso!")
                except ValueError:
                    print("\nValor não compatível. Retornando...")
                try:
                    select(usuario, senha, oracle, sql_select)
                except ConnectionError:
                    print("\nErro ao conectar com o banco!")

            elif escolha_industria == "4":
                print("\n---Serviços Financeiros---")
                tabela = "t_industria_py"
                area_produto = "Serviços Financeiros"
                try:
                    sql_select = f"select * from {tabela} Where area_produto = '{area_produto}'"
                    select(usuario, senha, oracle, sql_select)

                    print("\nBusca feita com sucesso!")
                except ValueError:
                    print("\nValor não compatível. Retornando...")
                try:
                    select(usuario, senha, oracle, sql_select)
                except ConnectionError:
                    print("\nErro ao conectar com o banco!")

            elif escolha_industria == "5":
                print("\n---Saúde & Ciências da vida---")
                tabela = "t_industria_py"
                area_produto = "Saúde & Ciências da vida"
                try:
                    sql_select = f"select * from {tabela} Where area_produto = '{area_produto}'"
                    select(usuario, senha, oracle, sql_select)

                    print("\nBusca feita com sucesso!")
                except ValueError:
                    print("\nValor não compatível. Retornando...")
                try:
                    select(usuario, senha, oracle, sql_select)
                except ConnectionError:
                    print("\nErro ao conectar com o banco!")

            elif escolha_industria == "6":
                print("\n---Manufatura---")
                tabela = "t_industria_py"
                area_produto = "Manufatura"
                try:
                    sql_select = f"select * from {tabela} Where area_produto = '{area_produto}'"
                    select(usuario, senha, oracle, sql_select)

                    print("\nBusca feita com sucesso!")
                except ValueError:
                    print("\nValor não compatível. Retornando...")
                try:
                    select(usuario, senha, oracle, sql_select)
                except ConnectionError:
                    print("\nErro ao conectar com o banco!")

            elif escolha_industria == "7":
                print("\n---Mídia---")
                tabela = "t_industria_py"
                area_produto = "Mídia"
                try:
                    sql_select = f"select * from {tabela} Where area_produto = '{area_produto}'"
                    select(usuario, senha, oracle, sql_select)

                    print("\nBusca feita com sucesso!")
                except ValueError:
                    print("\nValor não compatível. Retornando...")
                try:
                    select(usuario, senha, oracle, sql_select)
                except ConnectionError:
                    print("\nErro ao conectar com o banco!")

            elif escolha_industria == "8":
                print("\n---Setor Público---")
                tabela = "t_industria_py"
                area_produto = "Setor Público"
                try:
                    sql_select = f"select * from {tabela} Where area_produto = '{area_produto}'"
                    select(usuario, senha, oracle, sql_select)

                    print("\nBusca feita com sucesso!")
                except ValueError:
                    print("\nValor não compatível. Retornando...")
                try:
                    select(usuario, senha, oracle, sql_select)
                except ConnectionError:
                    print("\nErro ao conectar com o banco!")

            elif escolha_industria == "9":
                print("\n---Varejo---")
                tabela = "t_industria_py"
                area_produto = "Varejo"
                try:
                    sql_select = f"select * from {tabela} Where area_produto = '{area_produto}'"
                    select(usuario, senha, oracle, sql_select)

                    print("\nBusca feita com sucesso!")
                except ValueError:
                    print("\nValor não compatível. Retornando...")
                try:
                    select(usuario, senha, oracle, sql_select)
                except ConnectionError:
                    print("\nErro ao conectar com o banco!")

            elif escolha_industria == "10":
                print("\n---Tecnologia---")
                tabela = "t_industria_py"
                area_produto = "Tecnologia"
                try:
                    sql_select = f"select * from {tabela} Where area_produto = '{area_produto}'"
                    select(usuario, senha, oracle, sql_select)

                    print("\nBusca feita com sucesso!")
                except ValueError:
                    print("\nValor não compatível. Retornando...")
                try:
                    select(usuario, senha, oracle, sql_select)
                except ConnectionError:
                    print("\nErro ao conectar com o banco!")

            elif escolha_industria == "11":
                print("\n---Selecionando Tudo---")
                tabela = "t_industria_py"
                try:
                    sql_select = f"select * from {tabela}"
                    select(usuario, senha, oracle, sql_select)

                    print("\nBusca feita com sucesso!")
                except ValueError:
                    print("\nValor não compatível. Retornando...")
                try:
                    select(usuario, senha, oracle, sql_select)
                except ConnectionError:
                    print("\nErro ao conectar com o banco!")

            elif escolha_industria == "12":
                print("\n---Voltando para o Menu---")
                self.menu_crud()

            elif escolha_industria == "13":
                print("Saindo...")
                break
            else:
                print("\nOpção inválida. Selecione uma opção válida")
                self.menu_crud()
            self.mostrar_resumo_operacao("Indústrias")

    def pesquisar_menu_aprendizado(self):
        while True:
            print("\n---Aprendizado ---")
            print("\n---Menu Aprendizado---\n")
            print("1. Trailhead")
            print("2. Eventos & Experiências")
            print("3. Histórias de Clientes")
            print("4. Blogs")
            print("5. Selecionar Tudo")
            print("6. Voltar para o Menu")
            print("7. Sair")

            escolha_aprendizado = input("Escolha a área que deseja remover (1-6): ")

            if escolha_aprendizado == "1":
                print("\n---Trailhead---")
                tabela = "t_aprendizado_py"
                area_produto = "Trailhead"
                try:
                    sql_select = f"select * from {tabela} Where area_produto = '{area_produto}'"
                    select(usuario, senha, oracle, sql_select)

                    print("\nBusca feita com sucesso!")
                except ValueError:
                    print("\nValor não compatível. Retornando...")
                try:
                    select(usuario, senha, oracle, sql_select)
                except ConnectionError:
                    print("\nErro ao conectar com o banco!")

            elif escolha_aprendizado == "2":
                print("\n---Eventos & Experiências---")
                tabela = "t_aprendizado_py"
                area_produto = "Eventos & Experiências"
                try:
                    sql_select = f"select * from {tabela} Where area_produto = '{area_produto}'"
                    select(usuario, senha, oracle, sql_select)

                    print("\nBusca feita com sucesso!")
                except ValueError:
                    print("\nValor não compatível. Retornando...")
                try:
                    select(usuario, senha, oracle, sql_select)
                except ConnectionError:
                    print("\nErro ao conectar com o banco!")

            elif escolha_aprendizado == "3":
                print("\n---Histórias de Clientes---")
                tabela = "t_aprendizado_py"
                area_produto = "Histórias de Clientes"
                try:
                    sql_select = f"select * from {tabela} Where area_produto = '{area_produto}'"
                    select(usuario, senha, oracle, sql_select)

                    print("\nBusca feita com sucesso!")
                except ValueError:
                    print("\nValor não compatível. Retornando...")
                try:
                    select(usuario, senha, oracle, sql_select)
                except ConnectionError:
                    print("\nErro ao conectar com o banco!")

            elif escolha_aprendizado == "4":
                print("\n---Blogs---")
                tabela = "t_aprendizado_py"
                area_produto = "Blogs"
                try:
                    sql_select = f"select * from {tabela} Where area_produto = '{area_produto}'"
                    select(usuario, senha, oracle, sql_select)

                    print("\nBusca feita com sucesso!")
                except ValueError:
                    print("\nValor não compatível. Retornando...")
                try:
                    select(usuario, senha, oracle, sql_select)
                except ConnectionError:
                    print("\nErro ao conectar com o banco!")

            elif escolha_aprendizado == "5":
                print("\n---Selecionando Tudo---")
                tabela = "t_aprendizado_py"
                try:
                    sql_select = f"select * from {tabela}"
                    select(usuario, senha, oracle, sql_select)

                    print("\nBusca feita com sucesso!")
                except ValueError:
                    print("\nValor não compatível. Retornando...")
                try:
                    select(usuario, senha, oracle, sql_select)
                except ConnectionError:
                    print("\nErro ao conectar com o banco!")

            elif escolha_aprendizado == "6":
                print("\n---Voltando para o Menu---")
                self.menu_crud()

            elif escolha_aprendizado == "7":
                print("Saindo...")
                break
            else:
                print("\nOpção inválida. Selecione uma opção válida")
                self.menu_crud()
            self.mostrar_resumo_operacao("Aprendizado")


    def mostrar_resumo_operacao(self, funcionalidade):
        print(f"Operação na funcionalidade {funcionalidade} realizada.")
        opcao = input("Deseja realizar outra operação? : ")
        if opcao.lower() == "s" or opcao.lower() == "sim":
            self.executar_crud()
        if opcao.lower() == "n" or opcao.lower() == "nao":
            print("Encerrando o programa.")
            exit()
def carregar_dados(dados):
    try:
        with open(dados, 'r') as arquivo:
            dados = json.load(arquivo)
            return dados
    except FileNotFoundError:
        print(f'O arquivo {dados} não foi encontrado.')
        return


secret = carregar_dados('secret.json')

usuario = secret['user']  # Usuário
senha = secret['password']  # Senha
oracle = secret['dsn']  # Servidor


def insert(usuario, senha, oracle, sql):
    with oracledb.connect(user=usuario, password=senha, dsn=oracle) as connection:
        with connection.cursor() as cursor:
            cursor.execute(sql)
            # Confirmação da transação
            connection.commit()

def select(usuario, senha, oracle, sql):
    with oracledb.connect(user=usuario, password=senha, dsn=oracle) as connection:
        with connection.cursor() as cursor:
            cursor.execute(sql)
            dados = cursor.fetchall()
            print(dados)


def update(usuario, senha, oracle, sql):
    with oracledb.connect(user=usuario, password=senha, dsn=oracle) as connection:
        with connection.cursor() as cursor:
            cursor.execute(sql)
            # Confirmação da transação
            connection.commit()


def delete(usuario, senha, oracle, sql):
    with oracledb.connect(user=usuario, password=senha, dsn=oracle) as connection:
        with connection.cursor() as cursor:
            cursor.execute(sql)
            connection.commit()

if __name__ == "__main__":
    sistema = Sistema()
    sistema.executar_crud()