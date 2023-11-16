# Use a imagem base do Python
FROM python:3.10

# Configuração do diretório de trabalho
WORKDIR /app

# Copie os arquivos do projeto para o contêiner
COPY . /app

# Instale as dependências
RUN pip install -r requirements.txt

# Execute as migrações do banco de dados
RUN python manage.py migrate

# Exponha a porta 8000 (ou a porta que você está usando)
EXPOSE 8000

# Comando para iniciar a aplicação
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]