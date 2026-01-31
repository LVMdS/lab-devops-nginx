FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

# Adicionamos --default-timeout=100 para evitar erro em internet lenta
# E --retries para ele tentar de novo se falhar
RUN pip install --no-cache-dir --default-timeout=100 --retries 5 -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
