import oracledb
import os
from dotenv import load_dotenv

load_dotenv()

def conectar_oracle():
    try:
        user = os.getenv('ORACLE_USER')
        password = os.getenv('ORACLE_PASSWORD')
        dsn = os.getenv('ORACLE_DSN')

        connection = oracledb.connect(user=user, password=password, dsn=dsn)
        print("Conexão com o banco de dados Oracle estabelecida com sucesso!")
        return connection
    except oracledb.DatabaseError as e:
        erro, = e.args
        print(f"Erro ao conectar ao banco de dados Oracle: {erro.message}")
        return None

def insert_data():
    connection = conectar_oracle()
    if connection:
        try:
            cursor = connection.cursor()

            for i in range(1, 11):
                usuario_id = f'U{i:03d}'
                cursor.execute("""
                    INSERT INTO t_usuario_odontoprev (usuario_id, cpf, nome, sobrenome, data_nascimento, genero)
                    VALUES (:1, :2, :3, :4, TO_DATE(:5, 'YYYY-MM-DD'), :6)
                """, [usuario_id, f'000.000.000-0{i}', f'Nome{i}', f'Sobrenome{i}', '1990-01-01', 'M' if i % 2 == 0 else 'F'])

            for i in range(1, 11):
                atendimento_id = f'A{i:03d}'
                usuario_id = f'U{i:03d}'
                cursor.execute("""
                    INSERT INTO t_atendimento_usuario_odontoprev (atendimento_id, usuario_id, dentista_nome, clinica_nome, data_atendimento, descricao_procedimento, custo)
                    VALUES (:1, :2, :3, :4, TO_DATE(:5, 'YYYY-MM-DD'), :6, :7)
                """, [atendimento_id, usuario_id, f'Dentista{i}', f'Clinica{i}', '2023-01-01', f'Procedimento{i}', 100.0 + i])

            for i in range(1, 11):
                contato_usuario_id = f'C{i:03d}'
                usuario_id = f'U{i:03d}'
                cursor.execute("""
                    INSERT INTO t_contato_usuario_odontoprev (contato_usuario_id, usuario_id, email_usuario, telefone_usuario)
                    VALUES (:1, :2, :3, :4)
                """, [contato_usuario_id, usuario_id, f'email{i}@example.com', f'(11) 90000-000{i}'])

            for i in range(1, 11):
                endereco_usuario_id = f'E{i:03d}'
                usuario_id = f'U{i:03d}'
                cursor.execute("""
                    INSERT INTO t_endereco_usuario_odontoprev (endereco_usuario_id, usuario_id, cep_usuario, cidade_usuario, estado_usuario, logradouro_usuario, bairro_usuario)
                    VALUES (:1, :2, :3, :4, :5, :6, :7)
                """, [endereco_usuario_id, usuario_id, f'00000-00{i}', f'Cidade{i}', 'SP', f'Rua{i}', f'Bairro{i}'])

            for i in range(1, 11):
                imagem_usuario_id = f'I{i:03d}'
                usuario_id = f'U{i:03d}'
                cursor.execute("""
                    INSERT INTO t_imagem_usuario_odontoprev (imagem_usuario_id, usuario_id, imagem_url)
                    VALUES (:1, :2, :3)
                """, [imagem_usuario_id, usuario_id, f'https://example.com/imagem{i}.jpg'])

            for i in range(1, 11):
                previsao_usuario_id = f'P{i:03d}'
                imagem_usuario_id = f'I{i:03d}'
                usuario_id = f'U{i:03d}'
                cursor.execute("""
                    INSERT INTO t_previsao_usuario_odontoprev (previsao_usuario_id, imagem_usuario_id, usuario_id, previsao_texto, probabilidade, recomendacao)
                    VALUES (:1, :2, :3, :4, :5, :6)
                """, [previsao_usuario_id, imagem_usuario_id, usuario_id, f'Previsao texto {i}', 0.75 + (i * 0.01), f'Recomendacao {i}'])

            connection.commit()
            print("Dados inseridos com sucesso!")
        except oracledb.DatabaseError as e:
            erro, = e.args
            print(f"Erro ao inserir dados: {erro.message}")
            connection.rollback()
        finally:
            connection.close()
    else:
        print("Falha ao conectar, não foi possível inserir os dados.")

if __name__ == "__main__":
    try:
        insert_data()
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

    