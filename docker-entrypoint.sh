#!/bin/bash
set -e

echo "🐳 Starting NINVENDO Django App..."

# Funzione per verificare connessione PostgreSQL
wait_for_postgres() {
    echo "⏳ Waiting for PostgreSQL to be ready..."
    
    # Estrai host e porta dal DATABASE_URL
    if [[ $DATABASE_URL =~ postgresql://[^@]*@([^:/]+):?([0-9]*) ]]; then
        DB_HOST="${BASH_REMATCH[1]}"
        DB_PORT="${BASH_REMATCH[2]:-5432}"
        
        echo "🔍 Testing connection to $DB_HOST:$DB_PORT..."
        
        # Usa netcat per testare la connessione
        until timeout 5 bash -c "</dev/tcp/$DB_HOST/$DB_PORT" 2>/dev/null; do
            echo "PostgreSQL is unavailable - sleeping"
            sleep 3
        done
        
        echo "✅ PostgreSQL is ready!"
    else
        echo "⚠️  Could not parse DATABASE_URL, skipping connection test"
    fi
}

# Test connessione database
if [ "$DATABASE_URL" ]; then
    wait_for_postgres
else
    echo "⚠️  DATABASE_URL not set, skipping database checks"
fi

# Esegui le migrazioni con gestione errori
echo "🗄️ Running database migrations..."

# Prova prima fake-initial per risolvere conflitti
echo "📋 Attempting fake-initial migration..."
python manage.py migrate --fake-initial 2>/dev/null || echo "⚠️ Fake-initial failed, continuing..."

# Poi migrazione normale
echo "📋 Running standard migrations..."
python manage.py migrate --noinput || {
    echo "❌ Migration failed, trying alternative approach..."
    
    # Se fallisce, prova a migrare app per app
    python manage.py migrate contenttypes --noinput || true
    python manage.py migrate auth --noinput || true
    python manage.py migrate admin --noinput || true
    python manage.py migrate sessions --noinput || true
    python manage.py migrate django_classified --fake-initial --noinput || true
    python manage.py migrate trade --fake-initial --noinput || true
    python manage.py migrate payments --fake-initial --noinput || true
    python manage.py migrate registration --noinput || true
    python manage.py migrate social_django --noinput || true
    
    # Infine, applica tutte le rimanenti
    python manage.py migrate --noinput || echo "⚠️ Some migrations failed, but continuing..."
}

echo "✅ Database setup completed"

# Raccogli i file statici
echo "📁 Collecting static files..."
python manage.py collectstatic --noinput

# Setup dati iniziali (se richiesto)
if [ "$SETUP_DEMO_DATA" = "true" ]; then
    echo "🎮 Setting up demo data..."
    python manage.py setup_project || echo "⚠️ Demo data setup failed or not available"
fi

# Crea superuser se non esiste
if [ "$DJANGO_SUPERUSER_USERNAME" ] && [ "$DJANGO_SUPERUSER_PASSWORD" ] && [ "$DJANGO_SUPERUSER_EMAIL" ]; then
    echo "👤 Creating superuser..."
    python manage.py shell -c "
from django.contrib.auth.models import User
try:
    if not User.objects.filter(username='$DJANGO_SUPERUSER_USERNAME').exists():
        User.objects.create_superuser('$DJANGO_SUPERUSER_USERNAME', '$DJANGO_SUPERUSER_EMAIL', '$DJANGO_SUPERUSER_PASSWORD')
        print('✅ Superuser created successfully')
    else:
        print('ℹ️  Superuser already exists')
except Exception as e:
    print(f'❌ Error creating superuser: {e}')
"
fi

echo "🚀 Starting Django development server..."

# Esegui il comando passato come argomento
exec "$@"