import oracledb
import pandas as pd


def conectar_oracle(usuario, senha, dsn):
    try:
        connection = oracledb.connect(user=usuario, password=senha, dsn=dsn)
        print("Conexão com o banco de dados Oracle estabelecida com sucesso!")
        return connection
    except oracledb.DatabaseError as e:
        erro, = e.args
        print(f"Erro ao conectar ao banco de dados Oracle: {erro.message}")
        return None


def exibir_dados(conexao, tabela):
    try:
        cursor = conexao.cursor()
        cursor.execute(f"SELECT * FROM {tabela}")
        rows = cursor.fetchall()
        colunas = [col[0] for col in cursor.description]

        df = pd.DataFrame(rows, columns=colunas)
        print(df)
    except Exception as e:
        print(f"Erro ao recuperar dados: {e}")


def menu(conexao):
    while True:
        print("\nMenu:")
        print("1. Exibir dados de Produção Plástico Global")
        print("2. Exibir dados de Participação Despejo Resíduo Plástico")
        print("3. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            exibir_dados(conexao, "producao_plastico_global")
        elif opcao == "2":
            exibir_dados(conexao, "participacao_despejo_residuo_plastico")
        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    usuario = "RM553383"
    senha = "281003"
    dsn = "oracle.fiap.com.br:1521/orcl"
    caminho_csv_1 = "producao_de_platico_global.csv"
    caminho_csv_2 = "participacao_despejo_residuo_plastico.csv"

    conexao = conectar_oracle(usuario, senha, dsn)

    if conexao:
        try:
            menu(conexao)
        except ConnectionError as e:
            print(f"Erro ao inserir dados: {e}")
        finally:
            conexao.close()
            print("Conexão com o banco de dados Oracle encerrada.")