import os
import pymysql # MySQL
import pymssql # SQLServer
import mysql.connector
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

class Banco():
    def __init__(self):
        # Carregar dados do .env
        host = os.getenv("DB_HOST")
        user = os.getenv("DB_USER")
        password = os.getenv("DB_PASSWORD")
        database = os.getenv("DB_NAME")
        port = int(os.getenv("DB_PORT"))

        # Conexão com MySQL
        self.conexao = pymysql.connect(host=host, port=port, user=user, password=password, database=database)
        # Se quiser usar SQLServer, descomente a linha abaixo e comente a linha acima
        # self.conexao = pymssql.connect(host=host, user=user, password=password, database=database)

    def get_connection(self):
        return self.conexao

    def close_connection(self):
        if self.conexao:
            self.conexao.close()