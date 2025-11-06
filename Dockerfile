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
# Simplifica o PYTHONPATH para apenas o diretório de trabalho
ENV PYTHONPATH=/app

# Comando para iniciar a aplicação (forma shell para expansão de $PORT)
# O Gunicorn deve ser capaz de encontrar o 'src' se o diretório de trabalho estiver no PYTHONPATH.
CMD python -m gunicorn --bind 0.0.0.0:${PORT} --workers 4 --timeout 60 app:aplicativo
