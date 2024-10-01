import oracledb
import pandas as pd

def conectar_oracle(self, user, password, dsn):
    try:
        connection = oracledb.connect(user=user, password=password, dsn=dsn)
        print("Conexão com o banco de dados Oracle estabelecida com sucesso!")
        return connection
    except oracledb.DatabaseError as e:
        erro, = e.args
        print(f"Erro ao conectar ao banco de dados Oracle: {erro.message}")
        return None
def insert_data(user, password, dsn):
    conectar_oracle()
    if conectar_oracle == True:

if __name__ == "__main__":
    try:
        self.conectar_oracle()
    except:
        break
    