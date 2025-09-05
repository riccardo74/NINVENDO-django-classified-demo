#!/bin/bash

echo "🐳 NINVENDO Docker Setup"
echo "========================"

# Verifica che Docker sia installato
if ! command -v docker &> /dev/null; then
    echo "❌ Docker non è installato. Installa Docker prima di continuare."
    exit 1
fi

if ! command -v docker-compose &> /dev/null; then
    echo "❌ Docker Compose non è installato. Installa Docker Compose prima di continuare."
    exit 1
fi

# Crea il file .env se non esiste
if [ ! -f .env ]; then
    echo "📝 Creando file .env..."
    cp .env.docker .env
    echo "⚠️  IMPORTANTE: Modifica il file .env con le tue credenziali del database Render!"
    echo "   Le credenziali le trovi nel dashboard di Render > PostgreSQL > Connect"
fi

# Verifica che le variabili essenziali siano impostate
echo "🔍 Verificando configurazione..."
source .env

if [ -z "$DATABASE_URL" ] || [ "$DATABASE_URL" = "postgresql://user:password@host:5432/database" ]; then
    echo "❌ DATABASE_URL non configurato correttamente nel file .env"
    echo "   Vai su Render > Database > Connect e copia l'External Database URL"
    exit 1
fi

echo "✅ Configurazione verificata!"

# Build e avvio dei container
echo "🏗️  Building Docker image..."
docker-compose build

echo "🚀 Starting containers..."
docker-compose up -d

# Attendi che i servizi siano pronti
echo "⏳ Waiting for services to be ready..."
sleep 10

# Mostra i logs
echo "📋 Container status:"
docker-compose ps

echo ""
echo "🎉 Setup completato!"
echo ""
echo "📊 Per vedere i logs:"
echo "   docker-compose logs -f web"
echo ""
echo "🌐 L'applicazione è disponibile su:"
echo "   http://localhost:8000"
echo ""
echo "👤 Credenziali admin di default:"
echo "   Username: admin"
echo "   Password: admin123"
echo ""
echo "🛑 Per fermare i container:"
echo "   docker-compose down"
echo ""
echo "🔧 Per accedere al container:"
echo "   docker-compose exec web bash"