# Usa uma imagem oficial do Python
FROM python:alpine

# Cria o diretório de trabalho dentro do container
WORKDIR /app

# Copia os requisitos e instala dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia os arquivos do projeto
COPY . .

# Comando para rodar o servidor
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]