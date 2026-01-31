# 1. Escolhe uma imagem base leve do Python
FROM python:3.9-slim

# 2. Define a pasta de trabalho dentro do container
WORKDIR /app

# 3. Copia o arquivo de dependências e instala
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copia o resto do código (o main.py)
COPY . .

# 5. Comando para rodar a API quando o container ligar
# Host 0.0.0.0 libera acesso externo ao container
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
