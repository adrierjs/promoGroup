# Use uma imagem base com suporte a Python
FROM python:3.10

# Defina o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copie o arquivo requirements.txt para o contêiner
COPY requirements.txt .

# Instale as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante do código para o contêiner
COPY . .

# Comando padrão para ser executado quando o contêiner for iniciado
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
