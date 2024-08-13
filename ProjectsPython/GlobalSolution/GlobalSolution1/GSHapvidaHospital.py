class Sistema:
    def __init__(self):
        self.cadastro = None
        self.cliente = []
        self.empresa = []
        self.prestador = {}
        self.corretor = {}
        self.suporte = {}
    def cadastrar_paciente(self):
        print("\n--- Cadastro ---")
        nome = input("Nome do paciente: ")
        email = input("Email do paciente: ")
        rg = input("RG do paciente: ")
        cpf = input("CPF do paciente: ")
        telefone = input("Telefone do paciente: ")
        data_nascimento = input("Data de nascimento (dd/mm/aa):  ")
        tipo_sanguineo = input("Tipo sanguíneo: ")

        self.cliente = {"Nome": nome, "\nEmail": email, "\nTelefone": telefone}
        print(f"Nome: {nome}\nEmail: {email}\nTelefone: {telefone}\nRG: {rg} \nCPF: {cpf}\nData de nascimento: {data_nascimento}\nTipo sanguíneo: {tipo_sanguineo}")
        print("Cadastro realizado com sucesso!")
    def mostrar_menu(self):
        print("\n--- Menu ---")
        print("1. Menu Cliente")
        print("2. Menu Empresa")
        print("3. Menu Prestador")
        print("4. Menu Corretor")
        print("5. Menu Suporte")
        print("6. Sair")

    def executar(self):
        print("Bem-vindo à Hapvida NotreDame Intermédica!")
        self.cadastrar_paciente()
        while True:
            self.mostrar_menu()
            print("---------------------------------------------------------------------")
            escolha = input("Escolha uma opção (1-6): ")
            print("---------------------------------------------------------------------")

            if escolha == "1":
                self.menu_cliente()
            elif escolha == "2":
                self.menu_empresa()
            elif escolha == "3":
                self.menu_prestador()
            elif escolha == "4":
                self.menu_corretor()
            elif escolha == "5":
                self.menu_suporte()
            elif escolha == "6":
                print("Encerrando o programa.")
                break
            else:
                print("Opção inválida. Escolha uma opção válida.")

    def menu_cliente(self):
        print("\n--- Cliente ---")
        print("\n--- Menu Cliente---")
        print("1. Consulta")
        print("2. Carteira Online")
        print("3. Rede Credenciada Odontológica")
        print("4. Guia Médico")
        print("5. Solicitar Autorização")
        print("6. Atualizar Dados")
        print("7. Setor Financeiro")
        print("8. PIN-SS(Portal de Informações do Beneficiário")
        print("9. Substituição de Prestadores")
        print("10. Centrais de Atendimento Presencial")
        print("11. Histórico de Solicitações")
        print("12. Kit Boas-Vindas")
        print("13. Senha Liberada")
        print("14. Clube Vantagens")
        print("15. Central de Serviços")
        print("16. Extrato de Coparticipação")
        print("17. Consignados")
        print("18. Ajuda")

        print("---------------------------------------------------------------------------")
        escolha_cliente = input("Escolha a área que deseja (1-18): ")
        print("---------------------------------------------------------------------------")

        if escolha_cliente == "1":
            print("\n--- Consulta ---\n")
            print("--- Menu Consulta ---")
            print("1. Marcar Consulta")
            print("2. Desmarcar Consulta")
            print("3. Consulta Odonto")
            print("4. Exames")
            print("5. Consulta Reajuste de Contrato")

            print("---------------------------------------------------------------------------")
            escolha_consulta = input("Escolha sua opção (1-5): ")
            print("---------------------------------------------------------------------------")

            if escolha_consulta == "1":
                print("Link direcionado à página Marcar Consulta: https://www.hapvida.com.br/site/lp-escolha-experiencia/?url=https%3A//www.hapvida.com.br/site/marquesuaconsulta")
            elif escolha_consulta == "2":
                print("Link direcionado à página Desmarcar Consulta: https://www.hapvida.com.br/site/lp-escolha-experiencia/?url=https%3A//webhap.hapvida.com.br/pls/webhap/pk_saude.formulario%3Fpds_app%3DwebNewDesmarcaConsulta.inicio%26pfl_mobile%3DN%26pfl_tipo%3DS%26pfl_situacao%3DA")
            elif escolha_consulta== "3":
                print("Link direcionado à página Consulta Odonto: https://www.hapvida.com.br/site/lp-escolha-experiencia/?url=/pls/podontow/webnewdentalcliente.pr_login_n%3FpOrgAmb%3D2")
            elif escolha_consulta == "4":
                print("Link direcionado à página Exames: https://www.hapvida.com.br/site/exames")
            elif escolha_consulta == "5":
                print("Link direcionado à página Consulta Reajuste de Contrato: https://webhap.hapvida.com.br/pls/webhap/pk_ajuste_contrato.principal")
            else:
                print("Digite uma opção válida.")
        elif escolha_cliente == "2":
            print("\n---Carteira Online---")
            print("Link direcionado à página Carteira Online: https://www.hapvida.com.br/site/lp-escolha-experiencia/?url=https%3A//webhap.hapvida.com.br/pls/webhap/pk_carteira_provisoria.login_usuario_form")
        elif escolha_cliente == "3":
            print("\n---Rede Credenciada Odontológica---")
            print("Link direcionado à página Rede Credenciada Odontológica: https://www.hapvida.com.br/site/lp-escolha-experiencia/?url=https%3A//webhap.hapvida.com.br/pls/podontow/webdentalredecredenciada.selecionaRede")
        elif escolha_cliente == "4":
            print("\n---Guia Médico---")
            print("Link direcionado à página Guia Médico: https://www.hapvida.com.br/site/lp-escolha-experiencia/?url=https%3A//webhap.hapvida.com.br/pls/webhap/webnewredecredenciada.selecionarede ")
        elif escolha_cliente == "5":
            print("\n---Solicitar Autorização---")
            print("Link direcionado à página Solicitar Autorização: https://app.hapvida.com.br/solicitacaoautorizacao/login ")
        elif escolha_cliente == "6":
            print("\n---Atualizar Dados---")
            print("Link direcionado à página Atualizar Dados: https://webhap.hapvida.com.br/pls/webhap/pk_atualiza_dados.principal")
        elif escolha_cliente == "7":
            print("\n---Setor Financeiro---")
            print("\n--- Menu Setor Financeiro Cliente ---")
            print("1. Boleto de Pagamento")
            print("2. Boleto Digital e Notificações")
            print("3. Imposto de Renda")
            print("4. Ficha Financeira")
            print("5. Declaração de Quitação Anual")
            print("6. Negociação de Dívida")
            print("7. Nota Fiscal")

            print("---------------------------------------------------------------------------")
            escolha_financeiro_cliente = input("Escolha sua opção (1-7): ")
            print("---------------------------------------------------------------------------")

            if escolha_financeiro_cliente == "1":
                print("Link direcionado à página Boleto de Pagamento: https://www.hapvida.com.br/site/lp-escolha-experiencia/?url=https%3A//webhap.hapvida.com.br/pls/webhap/webNewBoleto.login ")
            elif escolha_financeiro_cliente == "2":
                print("Link direcionado à página Boleto Digital e Notificações: https://www.hapvida.com.br/site/lp-escolha-experiencia/?url=https%3A//notificacaoeletronica.hapvida.com.br/notificacao-eletronica/autenticacao.xhtml%3FcdEmpresa%3D1")
            elif escolha_financeiro_cliente == "3":
                print("Link direcionado à página Imposto de Renda: https://www.hapvida.com.br/site/lp-escolha-experiencia/?url=https%3A//webhap.hapvida.com.br/pls/webhap/webnewirusuario.login")
            elif escolha_financeiro_cliente == "4":
                print("Link direcionado à página Ficha Financeira: https://www.hapvida.com.br/site/lp-escolha-experiencia/?url=https%3A//webhap.hapvida.com.br/pls/webhap/webfichafinanceira.login")
            elif escolha_financeiro_cliente == "5":
                print("Link direcionado à página Declaração de Quitação Anual: https://webhap.hapvida.com.br/pls/webhap/webNewQuitacaoAnual.login")
            elif escolha_financeiro_cliente == "6":
                print("Link direcionado à página Negociação de Dívida: https://www.hapvida.com.br/pls/webhap/pk_saude.formulario?pds_app=pk_selfcheckout.pr_inicio&pfl_mobile=N&pfl_tipo=S&pfl_situacao=A&p_ambiente=S")
            elif escolha_financeiro_cliente == "7":
                print("Link direcionado à página Nota Fiscal: https://www.hapvida.com.br/pls/webhap/pk_nota_fiscal_ind.login_usuario_form")
            else:
                print("Digite uma opção válida.")
        elif escolha_cliente == "8":
            print("\n---PIN-SS (Portal de Informaçoes do Benefício)---")
            print("Link direcionado à página PIN-SS (Portal de Informaçoes do Benefício): https://webhap.hapvida.com.br/pls/webhap/pk_portal_transparente.login")
        elif escolha_cliente == "9":
            print("\n---Substituição de Prestadores---")
            print("Link direcionado à página Substituição de Prestadores: https://webhap.hapvida.com.br/pls/webhap/webNewSubstituicaoRede.login")
        elif escolha_cliente == "10":
            print("\n---Centrais de Atendimento Presencial---")
            print("Link direcionado à página Centrais de Atendimento Presencial: https://www.hapvida.com.br/site/atendimento-ao-cliente")
        elif escolha_cliente == "11":
            print("\n---Histórico de Solicitações---")
            print("Link direcionado à página Histórico de Solicitações: https://webhap.hapvida.com.br/pls/webhap/pk_saude.formulario?pds_app=webNewHapMovelLinhaDireta.listarSacMsg&pfl_mobile=N&pfl_tipo=S&pfl_situacao=A")
        elif escolha_cliente == "12":
            print("\n---Kit Boas-Vindas---")
            print("Link direcionado à página Kit Boas-Vindas: https://www.hapvida.com.br/site/noticias/confira-onde-voc%C3%AA-pode-pegar-seu-kit-boas-vindas-carteirinha-e-guia-m%C3%A9dico")
        elif escolha_cliente == "13":
            print("\n---Senha Liberada---")
            print("Link direcionado à página Senha Liberada: https://webhap.hapvida.com.br/pls/webhap/pk_saude.formulario?pds_app=webNewHapMovelSenhaLiberada.execLogon&pfl_mobile=N&pfl_tipo=S&pfl_situacao=A")
        elif escolha_cliente == "14":
            print("\n---Clube Vantagens---")
            print("Link direcionado à página Clube Vantagens: https://clube.hapvidandi.com.br/")
        elif escolha_cliente == "15":
            print("\n---Central de Serviços---")
            print("Link direcionado à página Central de Serviços: https://cafex.hapvida.com.br/sigo/linha-frente/#/login/1")
        elif escolha_cliente == "16":
            print("\n---Extrato de Coparticipações---")
            print("Link direcionado à página Extrato de Coparticipações: https://www.hapvida.com.br/site/lp-escolha-experiencia/?url=https%3A//webhap.hapvida.com.br/pls/webhap/webnewextratoutilizacao.login")
        elif escolha_cliente == "17":
            print("\n---Consignados---")
            print("Link direcionado à página Consignados: https://www.hapvida.com.br/site/noticias/confira-os-extratos-de-consigna%C3%A7%C3%B5es")
        elif escolha_cliente == "18":
            print("\n---Ajuda---")
            print("Link direcionado à página Ajuda: https://www.hapvida.com.br/site/central_de_ajuda")
        else:
            print("Opção inválida. Escolha uma opção válida.")

        self.mostrar_resumo_operacao("Cliente")

    def menu_empresa(self):
        print("\n--- Empresa ---")
        print("\n--- Menu Empresa---")
        print("1. Sistema de Movimentação")
        print("2. Carteira Online")
        print("3. Autenticar Atestados")
        print("4. Reajuste de Contratos")
        print("5. Setor Financeiro")

        print("---------------------------------------------------------------------")
        escolha_empresa = input("Escolha a área que deseja (1-5): ")
        print("---------------------------------------------------------------------")

        if escolha_empresa == "1":
            print("\n---Sistema de Movimentação---")
            print("Link direcionado à página Sistema de Movimentação: https://webhap.hapvida.com.br/pls/webhap/webnewcadastrousuario.login")
        elif escolha_empresa == "2":
            print("\n---Carteira Online---")
            print("Link direcionado à página Carteira Online: https://webhap.hapvida.com.br/pls/webhap/pk_carteira_provisoria.login_empresa_form")
        elif escolha_empresa == "3":
            print("\n---Autenticar Atestados---")
            print("Link direcionado à página Autenticar Atestados: https://webhap.hapvida.com.br/pls/webhap/pk_autentica_atestado_internet.login")
        elif escolha_empresa == "4":
            print("\n---Reajuste de Contratos---")
            print("Link direcionado à página Reajuste de Contratos: https://www.hapvida.com.br/site/noticias/reajuste-de-contratos-0")
        elif escolha_empresa == "5":
            print("\n---Setor Financeiro---")
            print("\n---Menu Setor Financeiro Empresa---")
            print("1. Boleto de Pagamento")
            print("2. Nota Fiscal")
            print("3. Custo Operacional")
            print("4. Troca de Arquivos (Relatório de Faturas)")
            print("5. Extrato de Utilização")
            print("6. Negociação de Dívida")
            print("7. Declaração de Quitação Anual")

            print("---------------------------------------------------------------------")
            escolha_financeiro_empresa = input("Digite a opção (1-7): ")
            print("---------------------------------------------------------------------")

            if escolha_financeiro_empresa == "1":
                print("Link direcionado à página Boleto de Pagamento:  https://webhap.hapvida.com.br/pls/webhap/webNewBoletoEmpresa.Login")
            elif escolha_financeiro_empresa == "2":
                print("Link direcionado à página Nota Fiscal: https://webhap.hapvida.com.br/pls/webhap/pk_nota_fiscal.login")
            elif escolha_financeiro_empresa == "3":
                print("Link direcionado à página Custo Operacional:  https://webhap.hapvida.com.br/pls/webhap/WEBNEWOPERACIONALEMPRESA.login")
            elif escolha_financeiro_empresa == "4":
                print("Link direcionado à página Troca de Arquivos (Relatório de Faturas): https://webhap.hapvida.com.br/pls/webhap/webNewTrocaArquivo.login")
            elif escolha_financeiro_empresa == "5":
                print("Link direcionado à página Extrato de Utilização:  https://webhap.hapvida.com.br/pls/webhap/webnewextratoutilizacao.login")
            elif escolha_financeiro_empresa == "6":
                print("Link direcionado à página Negociação de Dívida:  https://www.hapvida.com.br/pls/webhap/webnewnegocie.divida")
            elif escolha_financeiro_empresa == "7":
                print("Link direcionado à página Declaração de Quitação Anual:  https://www.hapvida.com.br/pls/webhap/webnewquitacaoanualpj.login")
            else:
                print("Digite uma opção válida.")
        else:
            print("Opção inválida. Selecione uma opção válida")
        self.mostrar_resumo_operacao("Empresa")

    def menu_prestador(self):
        print("\n--- Prestador ---")
        print("\n--- Menu Prestador---")
        print("1. Autorização de Procedimentos")
        print("2. Demonstrativo de Pagamento")
        print("3. Folha Médica")
        print("4. Produção médica")
        print("5. TISS")
        print("6. Documentos")
        print("7. Imposto de Renda")
        print("8. Índices e Metas")
        print("9. Carta Resposta de Revisão de Glosa")
        print("10. Auditoria Odontologia")
        print("11. Prestadores Odontologia")
        print("12. Situação Odontológica")
        print("13. Integração Médica")
        print("14. Intercâmbio")
        print("15. Folha Médica - Diagnósticos")
        print("16. Reset de Senha AD")

        print("---------------------------------------------------------------------")
        escolha_prestador = input("Escolha o produto que deseja (1-16): ")
        print("---------------------------------------------------------------------")

        if escolha_prestador == "1":
            print("\n---Autorização de Procedimentos---")
            print("Link direcionado à página Autorização de Procedimentos: https://savi3.hapvida.com.br/savi3//login.faces")
        elif escolha_prestador == "2":
            print("\n---Demonstrativo de Pagamento---")
            print("Link direcionado à página Demonstrativo de Pagamento: https://webhap.hapvida.com.br/pls/webhap/pk_demonstrativo_pagamento.login")
        elif escolha_prestador == "3":
            print("\n---Folha Médica---")
            print("Link direcionado à página Folha Médica: https://webhap.hapvida.com.br/pls/webhap/webNewPessoal.login")
        elif escolha_prestador == "4":
            print("\n---Produção médica---")
            print("Link direcionado à página Produção médica: https://portalprestador.hapvida.com.br/tiss-hapvida-web/auth")
        elif escolha_prestador == "5":
            print("\n---TISS---")
            print("Link direcionado à página TISS: https://webhap.hapvida.com.br/pls/webhap/tutorialtiss.emissaoGuia")
        elif escolha_prestador == "6":
            print("\n---Documentos---")
            print("Link direcionado à página Documentos: https://webhap.hapvida.com.br/pls/webhap/webdocumentos.principal")
        elif escolha_prestador == "7":
            print("\n---Imposto de Renda---")
            print("Link direcionado à página Imposto de Renda: https://webhap.hapvida.com.br/pls/webhap/webnewirprestador.login")
        elif escolha_prestador == "8":
            print("\n---Índices e Metas---")
            print("Link direcionado à página Índices e Metas: https://webhap.hapvida.com.br/pls/webhap/webnewindicemetascredenciado.login")
        elif escolha_prestador == "9":
            print("\n---Carta Resposta de Revisão de Glosa---")
            print("Link direcionado à página Carta Resposta de Revisão de Glosa: https://webhap.hapvida.com.br/pls/webhap/webnewrevisaoglosa.Login")
        elif escolha_prestador == "10":
            print("\n---Auditoria Odontologia---")
            print("Link direcionado à página Auditoria Odontologia: https://www.hapvida.com.br:7779/forms/frmservlet?form=tod04014.fmx&usesdi=YES&config=jhapvida")
        elif escolha_prestador == "11":
            print("\n---Prestadores Odontologia---")
            print("Link direcionado à página Prestadores Odontologia: https://webhap.hapvida.com.br/pls/podontow/webnewdentalprestador.pr_login")
        elif escolha_prestador == "12":
            print("\n---Situação Odontológica---")
            print("Link direcionado à página Situação Odontológica: https://webhap.hapvida.com.br/pls/webhap/pk_odon_beneficiario.login")
        elif escolha_prestador == "13":
            print("\n---Integração Médica---")
            print("Link direcionado à página Integração Médica: https://www.hapvida.com.br/site/integracao-medicos/login")
        elif escolha_prestador == "14":
            print("\n---Intercâmbio---")
            print("Link direcionado à página Intercâmbio: https://webhap.hapvida.com.br/pls/webhap/webnewcongenere.Login")
        elif escolha_prestador == "15":
            print("\n---Folha Médica - Diagnósticos---")
            print("Link direcionado à página Folha Médica - Diagnósticos: http://fmvi.hapvida.com.br/folhamedvidaimagem/")
        elif escolha_prestador == "16":
            print("\n---Reset de Senha AD---")
            print("Link direcionado à página Reset de Senha AD: https://hapvida.service-now.com/sd?id=sd_password_reset_ad")
        else:
            print("Opção inválida. Selecione uma opção válida")
        self.mostrar_resumo_operacao("Prestador ")

    def menu_corretor(self):
        print("\n--- Corretor ---")
        print("\n--- Menu Corretor---")
        print("1. Ficha de Proposta Individual")
        print("2. Sistema de Movimentação")
        print("3. Movimentação Odontológica")
        print("4. Troca de Arquivos")
        print("5. Controle de Proposta por Senha")
        print("6. Consulta CNPJ")
        print("7. Proposta Vendedor")
        print("8. Comisssão")
        print("9. Contratos Administradora")
        print("10. Controle de Relatórios")
        print("11. Portal de Venda - Super Simples e PME")
        print("12. Cadastro Empresa")
        print("13. Cadastro Empresa Odontologia")
        print("14. Cadastro Empresa Modelo")

        print("---------------------------------------------------------------------")
        escolha_corretor = input("Escolha o produto que deseja (1-14): ")
        print("---------------------------------------------------------------------")

        if escolha_corretor == "1":
            print("\n---Ficha de Proposta Individual---")
            print("Link direcionado à página Ficha de Proposta Individual: https://www.hapvida.com.br:7779/forms/frmservlet?form=t221d_i.fmx&usesdi=YES&config=jhapvida")
        elif escolha_corretor == "2":
            print("\n---Sistema de Movimentação---")
            print("Link direcionado à página Sistema de Movimentação: https://webhap.hapvida.com.br/pls/webhap/webnewcadastrousuario.login")
        elif escolha_corretor == "3":
            print("\n---Movimentação Odontológica---")
            print("Link direcionado à página Movimentação Odontológica: https://webhap.hapvida.com.br/pls/webhap/webNewDentalParceiroComercial.portal?pOpCorpo=LOGIN_PIM&pOrgAmb=1")
        elif escolha_corretor == "4":
            print("\n---Troca de Arquivos---")
            print("Link direcionado à página Troca de Arquivos: https://webhap.hapvida.com.br/pls/webhap/webnewtrocaarquivo.login")
        elif escolha_corretor == "5":
            print("\n---Controle de Proposta por Senha---")
            print("Link direcionado à página Controle de Proposta por Senha: https://webhap.hapvida.com.br/pls/webhap/pr_proposta")
        elif escolha_corretor == "6":
            print("\n---Consulta CNPJ---")
            print("Link direcionado à página Consulta CNPJ: http://websrv.hapvida.com.br:8763/servicos/autenticacao.jsf")
        elif escolha_corretor == "7":
            print("\n---Proposta Vendedor---")
            print("Link direcionado à página Proposta Vendedor: https://webhap.hapvida.com.br/pls/webhap/webNewCadastroEmpresa.Login")
        elif escolha_corretor == "8":
            print("\n---Comisssão---")
            print("Link direcionado à página Comisssão: https://www.hapvida.com.br:7779/forms/frmservlet?form=t221dpv.fmx&usesdi=YES&config=jhapvida")
        elif escolha_corretor == "9":
            print("\n---Contratos Administradora---")
            print("Link direcionado à página Contratos Administradora: https://webhap.hapvida.com.br/pls/webhap/webNewCadastroEmpresa.Login")
        elif escolha_corretor == "10":
            print("\n---Controle de Relatórios---")
            print("Link direcionado à página Controle de Relatórios: https://www.hapvida.com.br:7779/forms/frmservlet?form=t221d_e.fmx&usesdi=YES&config=jhapvida")
        elif escolha_corretor == "11":
            print("\n---Portal de Venda - Super Simples e PME---")
            print("Link direcionado à página Portal de Venda - Super Simples e PME: https://webhap.hapvida.com.br/pls/webhap/pk_controle_comissao.login")
        elif escolha_corretor == "12":
            print("\n---Cadastro Empresa---")
            print("Link direcionado à página Cadastro Empresa: https://www.hapvida.com.br:7779/forms/frmservlet?form=taffix.fmx&usesdi=YES&config=jhapvida")
        elif escolha_corretor == "13":
            print("\n---Cadastro Empresa Odontologia---")
            print("Link direcionado à página Cadastro Empresa Odontologia: https://webhap.hapvida.com.br/pls/webhap/webnewcontrolerelatorio.Login")
        elif escolha_corretor == "14":
            print("\n---Cadastro Empresa Modelo---")
            print("Link direcionado à página Cadastro Empresa Modelo: https://hapvida.planium.io/web/login/entrar")
        else:
            print("Opção inválida. Selecione uma opção válida")
        self.mostrar_resumo_operacao("Corretor")

    def menu_suporte(self):
        print("\n--- Central de Ajuda ---")
        print("1. Guia Médico ")
        print("2. Acesibilidade")
        print("3. Perguntas Frequentes")

        print("---------------------------------------------------------------------")
        escolha_suporte = input("Escolha o produto que deseja (1-3): ")
        print("---------------------------------------------------------------------")

        if escolha_suporte == "1":
            print("\n---Guia Médico---")
            print("Link direcionado à página Guia Médico: https://www.hapvida.com.br/pls/webhap/webnewredecredenciada.selecionarede")
        elif escolha_suporte == "2":
            print("\n---Acessibilidade---")
            print("Link direcionado à página Acessibilidade: https://www.hapvida.com.br/site/acessibilidade")
        elif escolha_suporte == "3":
            print("\n---Perguntas Frequentes---")
            print("Link direcionado à página de Perguntas Frequentes: https://www.hapvida.com.br/site/central_de_ajuda")
        else:
            print("Opção inválida. Selecione uma opção válida")
        self.mostrar_resumo_operacao("Suporte")

    def mostrar_resumo_operacao(self, funcionalidade):
        print(f"Operação na funcionalidade {funcionalidade} realizada.")
        opcao = input("Deseja realizar outra operação? (S/N): ")
        if opcao.lower() != "s":
            print("Encerrando o programa.")
            exit()


if __name__ == "__main__":
    sistema = Sistema()
    sistema.executar()