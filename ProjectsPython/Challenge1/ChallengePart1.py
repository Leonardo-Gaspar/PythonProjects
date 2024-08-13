class Sistema:
    def __init__(self):
        self.cadastro = None
        self.produtos = []
        self.industrias = []
        self.aprendizado = {}
        self.suporte = {}
        self.empresa_info = {
            "Nome": "Salesforce",
            "Endereço": "Av. Jornalista Roberto Marinho, 85 - 14º andar - Cidade Monções, São Paulo - SP, 04575-000 Brasil.",
            "Telefone": "0800 891 1887",
        }
    def cadastrar_cliente(self):
        print("\n--- Cadastro ---")
        nome = input("Nome do cliente: ")
        email = input("Email do cliente: ")
        telefone = input("Telefone do cliente: ")

        self.cliente = {"Nome": nome, "\nEmail": email, "\nTelefone": telefone}
        print(f"Nome: {nome}\nEmail: {email}\nTelefone: {telefone}")
        print("Cadastro realizado com sucesso!")
    def mostrar_menu(self):
        print("\n--- Menu ---")
        print("1. Produtos")
        print("2. Indústrias")
        print("3. Aprendizado")
        print("4. Suporte")
        print("5. Empresa")
        print("6. Sair")

    def executar(self):
        print("Bem-vindo à Salesforce!")
        self.cadastrar_cliente()
        while True:
            self.mostrar_menu()
            escolha = input("Escolha uma opção (1-6): ")

            if escolha == "1":
                self.menu_produtos()
            elif escolha == "2":
                self.menu_industrias()
            elif escolha == "3":
                self.menu_aprendizado()
            elif escolha == "4":
                self.menu_suporte()
            elif escolha == "5":
                self.menu_empresa()
            elif escolha == "6":
                print("Encerrando o programa.")
                break
            else:
                print("Opção inválida. Escolha uma opção válida.")

    def menu_produtos(self):
        print("\n--- Produtos ---")
        print("\n--- Menu Produtos---")
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


        escolha_produto = input("Escolha o produto que deseja (1-11): ")

        if escolha_produto == "1":
            print("\n---Customer 360---")
            #implementar link para a nova página
            print("Link direcionado à página Customer 360: 'Link para a página'")
        elif escolha_produto == "2":
            print("\n---Vendas---")
            #implementar link para a nova página
            print("Link direcionado à página Vendas: 'Link para a página'")
        elif escolha_produto == "3":
            print("\n---Atendimento ao Cliente---")
            #implementar link para a nova página
            print("Link direcionado à página Atendimento ao Cliente: 'Link para a página'")
        elif escolha_produto == "4":
            print("\n---Marketing---")
            #implementar link para a nova página
            print("Link direcionado à página Marketing: 'Link para a página'")
        elif escolha_produto == "5":
            print("\n---Commerce---")
            #implementar link para a nova página
            print("Link direcionado à página Commerce: 'Link para a página'")
        elif escolha_produto == "6":
            print("\n---Data Cloud---")
            #implementar link para a nova página
            print("Link direcionado à página Data Cloud: 'Link para a página'")
        elif escolha_produto == "7":
            print("\n---Tableau---")
            #implementar link para a nova página
            print("Link direcionado à página Tableau: 'Link para a página'")
        elif escolha_produto == "8":
            print("\n---Mulesoft---")
            #implementar link para a nova página
            print("Link direcionado à página Mulesoft: 'Link para a página'")
        elif escolha_produto == "9":
            print("\n---Slack---")
            #implementar link para a nova página
            print("Link direcionado à página Slack: 'Link para a página'")
        elif escolha_produto == "10":
            print("\n---Plataforma---")
            #implementar link para a nova página
            print("Link direcionado à página Plataforma: 'Link para a página'")
        elif escolha_produto == "11":
            print("\n---Sustentabilidade---")
            #implementar link para a nova página
            print("Link direcionado à página Sustentabilidade: 'Link para a página'")
        else:
            print("Opção inválida. Escolha uma opção válida.")

        self.mostrar_resumo_operacao("Produtos")

    def menu_industrias(self):
        print("\n--- Indústrias ---")
        print("\n--- Menu Indústrias---")
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

        escolha_industria = input("Escolha o produto que deseja (1-10): ")

        if escolha_industria == "1":
            print("\n---Automotivo---")
            # implementar link para a nova página
            print("Link direcionado à página Automotivo: 'Link para a página'")
        elif escolha_industria == "2":
            print("\n---Comunicações---")
            # implementar link para a nova página
            print("Link direcionado à página Comunicações: 'Link para a página'")
        elif escolha_industria == "3":
            print("\n---Bens de Consumo---")
            # implementar link para a nova página
            print("Link direcionado à página Bens de Consumo: 'Link para a página'")
        elif escolha_industria == "4":
            print("\n---Serviços Financeiros---")
            # implementar link para a nova página
            print("Link direcionado à página Serviços Financeiros: 'Link para a página'")
        elif escolha_industria == "5":
            print("\n---Saúde & Ciências da vida---")
            # implementar link para a nova página
            print("Link direcionado à página Saúde & Ciências da Vida: 'Link para a página'")
        elif escolha_industria == "6":
            print("\n---Manufatura---")
            # implementar link para a nova página
            print("Link direcionado à página Manufatura: 'Link para a página'")
        elif escolha_industria == "7":
            print("\n---Mídia---")
            # implementar link para a nova página
            print("Link direcionado à página Mídia: 'Link para a página'")
        elif escolha_industria == "8":
            print("\n---Setor Público---")
            # implementar link para a nova página
            print("Link direcionado à página Setor Público: 'Link para a página'")
        elif escolha_industria == "9":
            print("\n---Varejo---")
            # implementar link para a nova página
            print("Link direcionado à página Varejo: 'Link para a página'")
        elif escolha_industria == "10":
            print("\n---Tecnologia---")
            # implementar link para a nova página
            print("Link direcionado à página Tecnologia: 'Link para a página'")
        else:
            print("Opção inválida. Selecione uma opção válida")
        self.mostrar_resumo_operacao("Indústrias")

    def menu_aprendizado(self):
        print("\n--- Aprendizado ---")
        print("\n--- Menu Aprendizado---")
        print("1. Trailhead")
        print("2. Eventos & Experiências")
        print("3. Histórias de Clientes")
        print("4. Blogs")
        print("5. Por Tópico")
        print("6. Por Tipo de Conteúdo")
        print("7. Por Função")
        print("8. Por Indútria")
        print("9. Por Tipo de Conteúdo")

        escolha_aprendizado = input("Escolha o produto que deseja (1-9): ")

        if escolha_aprendizado == "1":
            print("\n---Trailhead---")
            # implementar link para a nova página
            print("Link direcionado à página Trailhead: 'Link para a página'")
        elif escolha_aprendizado == "2":
            print("\n---Eventos & Experiências---")
            # implementar link para a nova página
            print("Link direcionado à página Eventos e Experiências: 'Link para a página'")
        elif escolha_aprendizado == "3":
            print("\n---Histórias de Clientes---")
            # implementar link para a nova página
            print("Link direcionado à página Histórias de Clientes: 'Link para a página'")
        elif escolha_aprendizado == "4":
            print("\n---Blogs---")
            # implementar link para a nova página
            print("Link direcionado à página Blogs: 'Link para a página'")
        elif escolha_aprendizado == "5":
            print("\n---Por Tópico---")
            # implementar link para a nova página
            print("Link direcionado à página Por Tópico: 'Link para a página'")
        elif escolha_aprendizado == "6":
            print("\n---Por Tipo de Conteúdo---")
            # implementar link para a nova página
            print("Link direcionado à página Por Tipo de Conteúdo: 'Link para a página'")
        elif escolha_aprendizado == "7":
            print("\n---Por Função---")
            # implementar link para a nova página
            print("Link direcionado à página Por Função: 'Link para a página'")
        elif escolha_aprendizado == "8":
            print("\n---Por Indústria---")
            # implementar link para a nova página
            print("Link direcionado à página Por Indústrias: 'Link para a página'")
        elif escolha_aprendizado == "9":
            print("\n---Por Tipo de Conteúdo---")
            # implementar link para a nova página
            print("Link direcionado à página Por Tipo de Conteúdo: 'Link para a página'")
        else:
            print("Opção inválida. Selecione uma opção válida")
        self.mostrar_resumo_operacao("Aprendizado")

    def menu_suporte(self):
        print("\n--- Suporte ---")
        print("\n--- Menu Suporte---")
        print("1. Ajuda e Documentação")
        print("2. Comunidades")
        print("3. Serviços e Planos")
        print("4. Link para Chatbot")

        escolha_suporte = input("Escolha o produto que deseja (1-4): ")

        if escolha_suporte == "1":
            print("\n---Ajuda e Documentação---")
            # implementar link para a nova página
            print("Link direcionado à página Ajuda e Documentação: 'Link para a página'")
        elif escolha_suporte == "2":
            print("\n---Comunidades---")
            # implementar link para a nova página
            print("Link direcionado à página Comunidades: 'Link para a página'")
        elif escolha_suporte == "3":
            print("\n---Serviços e Planos---")
            # implementar link para a nova página
            print("Link direcionado à página Serviços e Planos: 'Link para a página'")
        elif escolha_suporte == "4":
            print("\n---Chatbot---")
            # implementar link para a nova página
            print("Link direcionado à página Chatbot: 'Link para a página'")
        else:
            print("Opção inválida. Selecione uma opção válida")
        self.mostrar_resumo_operacao("Suporte")

    def menu_empresa(self):
        print("\n--- Empresa ---")
        print("\n--- Menu Empresa---")
        print("1. Sobre a Salesforce")
        print("2. Nossos Valores")
        print("3. Nosso Impacto")
        print("4. Carreiras")
        print("5. Notícias")
        print("6. Mais Marcas da Salesforce")
        print("7. Informações da Empresa")

        escolha_empresa = input("Escolha o produto que deseja (1-7---): ")

        if escolha_empresa == "1":
            print("\n---Sobre a Salesforce---")
            # implementar link para a nova página
            print("Link direcionado à página Sobre a Salesforce: 'Link para a página'")
        elif escolha_empresa == "2":
            print("\n---Nossos Valores---")
            # implementar link para a nova página
            print("Link direcionado à página Nossos Valores: 'Link para a página'")
        elif escolha_empresa == "3":
            print("\n---Nosso Impacto---")
            # implementar link para a nova página
            print("Link direcionado à página Nosso Impacto: 'Link para a página'")
        elif escolha_empresa == "4":
            print("\n---Carreiras---")
            # implementar link para a nova página
            print("Link direcionado à página Carreiras: 'Link para a página'")
        elif escolha_empresa == "5":
            print("\n---Notícias---")
            # implementar link para a nova página
            print("Link direcionado à página Notícias: 'Link para a página'")
        elif escolha_empresa == "6":
            print("\n---Mais Marcas da Salesforce---")
            # implementar link para a nova página
            print("Link direcionado à página Mais Marcas da Salesforce: 'Link para a página'")
        elif escolha_empresa == "7":
            print("\n---Informações da Empresa---")
            for key, value in self.empresa_info.items():
                print(f"{key}: {value}")
            print("Link direcionado à página Por Função: 'Link para a página'")
        else:
            print("Opção inválida. Selecione uma opção válida")
        self.mostrar_resumo_operacao("Empresa")

    def mostrar_resumo_operacao(self, funcionalidade):
        print(f"Operação na funcionalidade {funcionalidade} realizada.")
        opcao = input("Deseja realizar outra operação? (S/N): ")
        if opcao.lower() != "s":
            print("Encerrando o programa.")
            exit()


if __name__ == "__main__":
    sistema = Sistema()
    sistema.executar()