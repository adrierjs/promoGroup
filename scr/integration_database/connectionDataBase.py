import psycopg2
from dotenv import load_dotenv
import os
load_dotenv()

# Parâmetros de conexão com o banco de dados PostgreSQL
db_params = {
    'host': os.getenv('HOST'),     # Endereço do servidor PostgreSQL
    'database': os.getenv('DATABASE'),  # Nome do banco de dados
    'user': os.getenv('USER_DATABASE'),         # Nome de usuário do PostgreSQL
    'password': os.getenv('PASSWORD_DATABASE')      # Senha do PostgreSQL
}

oi = {}
try:
    # Conectando ao banco de dados
    conn = psycopg2.connect(**db_params)

    # Criando um cursor para executar consultas
    cursor = conn.cursor()


except psycopg2.Error as e:
    print("Erro ao conectar ao banco de dados PostgreSQL:", e)



