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

def inserir_dados_csv(conexao, caminho_csv_1, caminho_csv_2):
    try:
        dados_1 = pd.read_csv(caminho_csv_1)
        dados_2 = pd.read_csv(caminho_csv_2)

        colunas_dados_1 = {'Entidade', 'Ano', 'Produção Anual de Plástico'}
        colunas_dados_2 = {'Entidade', 'Código', 'Ano', 'Participação na emissão global de plásticos para o oceano'}

        if not colunas_dados_1.issubset(dados_1.columns):
            print(f"O arquivo CSV {caminho_csv_1} não contém as colunas necessárias: {colunas_dados_1}. Colunas encontradas: {dados_1.columns.tolist()}")
            return

        if not colunas_dados_2.issubset(dados_2.columns):
            print(f"O arquivo CSV {caminho_csv_2} não contém as colunas necessárias: {colunas_dados_2}. Colunas encontradas: {dados_2.columns.tolist()}")
            return


        cursor = conexao.cursor()

        sql_1 = """
        INSERT INTO producao_plastico_global (entidade, ano, producao_plastico_anual)
        VALUES (:1, :2, :3)
        """

        sql_2 = """
                INSERT INTO participacao_despejo_residuo_plastico (entidade, codigo, ano, participacao_emissao_plastico)
                VALUES (:1, :2, :3, :4)
                """

        for index, row in dados_1.iterrows():
            cursor.execute(sql_1, (row['Entidade'], row['Ano'], row['Produção Anual de Plástico']))

        for index, row in dados_2.iterrows():
            cursor.execute(sql_2, (row['Entidade'], row['Código'], row['Ano'],
                                   row['Participação na emissão global de plásticos para o oceano']))

        conexao.commit()
    except Exception as e:
        print(f"Erro ao inserir dados: {e}")


if __name__ == "__main__":
    usuario = "RM553383"
    senha = "281003"
    dsn = "oracle.fiap.com.br:1521/orcl"
    caminho_csv_1 = "producao_de_platico_global.csv"
    caminho_csv_2 = "participacao_despejo_residuo_plastico.csv"


    conexao = conectar_oracle(usuario, senha, dsn)

    if conexao:
        try:
            inserir_dados_csv(conexao, caminho_csv_1, caminho_csv_2)
            print("Dados inseridos com sucesso!")
        except ConnectionError as e:
            print(f"erro ao inserir dados da Produção de Plástico Global: {e}")
        finally:
            conexao.close()
            print("Conexão com o banco de dados Oracle encerrada.")