# Usar imagem base Python 3.11
FROM python:3.11-slim

# Definir diretório de trabalho
WORKDIR /app

# Copiar requirements.txt
COPY requirements.txt .

# Instalar dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código da aplicação
COPY . .

# Expor porta 5000
EXPOSE 5000

# Definir variáveis de ambiente
ENV FLASK_APP=app.py
ENV FLASK_ENV=production
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app
# Comando para iniciar a aplicação
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "4", "--timeout", "60", "app:app"]
