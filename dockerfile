# Usa Python 3.11 slim come base
FROM python:3.11-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Installa dipendenze di sistema
RUN apt-get update && apt-get install -y \
    postgresql-client \
    gcc \
    python3-dev \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Crea directory di lavoro
WORKDIR /app

# Copia requirements e installa dipendenze Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia il codice dell'applicazione
COPY . .

# Crea directory per static files
RUN mkdir -p staticfiles

# Script di entrypoint
COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

# Esponi la porta 8000
EXPOSE 8000

# Usa lo script di entrypoint
ENTRYPOINT ["/docker-entrypoint.sh"]

# Comando di default
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]