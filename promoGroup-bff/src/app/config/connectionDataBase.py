import psycopg2
from dotenv import load_dotenv
import os
load_dotenv()

db_params = {
    'host': os.getenv('HOST'),
    'database': os.getenv('DATABASE'),
    'user': os.getenv('USER_DATABASE'),
    'password': os.getenv('PASSWORD_DATABASE')
}

try:
    conn = psycopg2.connect(**db_params)

except psycopg2.Error as e:
    with open('error.log', 'a') as log_file:
        log_file.write(f"Erro ao conectar ao banco de dados PostgreSQL: {e}\n")



