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

# Expor porta 5000 (apenas para documentação, o Render usará a porta $PORT)
EXPOSE 5000

# Definir variáveis de ambiente
ENV FLASK_APP=app.py
ENV FLASK_ENV=production
ENV PYTHONUNBUFFERED=1
# Adiciona o diretório atual (app) e o subdiretório src ao PYTHONPATH
ENV PYTHONPATH=/app:/app/src

# Comando para iniciar a aplicação
# 1. Usa 'python -m gunicorn' para garantir que o executável seja encontrado.
# 2. Usa a variável de ambiente $PORT fornecida pelo Render.
# 3. Usa 'app:aplicativo' para carregar o módulo 'app.py' e a instância 'aplicativo'.
CMD ["python", "-m", "gunicorn", "--bind", "0.0.0.0:${PORT}", "--workers", "4", "--timeout", "60", "app:aplicativo"]
