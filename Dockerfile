# Imagem base
FROM python:3.10

# Diretório de trabalho
WORKDIR /app

# Copia os arquivos do projeto
COPY . /app

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Define a porta
ENV PORT=8080

# Comando para rodar a app
CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]
