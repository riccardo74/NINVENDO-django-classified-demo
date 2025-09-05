#!/usr/bin/env python
"""
Script per testare la connessione al database
Eseguilo con: python manage.py shell < test_db_connection.py
"""

from django.db import connection
from django.conf import settings
import os

print("🔍 VERIFICA CONNESSIONE DATABASE")
print("=" * 50)

# 1. Verifica configurazione
print("📋 Configurazione Database:")
db_config = settings.DATABASES['default']
print(f"   Engine: {db_config['ENGINE']}")
print(f"   Name: {db_config.get('NAME', 'N/A')}")
print(f"   Host: {db_config.get('HOST', 'N/A')}")
print(f"   Port: {db_config.get('PORT', 'N/A')}")
print(f"   User: {db_config.get('USER', 'N/A')}")
print()

# 2. Verifica variabili d'ambiente
print("🌍 Variabili d'Ambiente:")
database_url = os.environ.get('DATABASE_URL')
if database_url:
    # Nascondi la password per sicurezza
    safe_url = database_url.split('@')[1] if '@' in database_url else database_url
    print(f"   DATABASE_URL: postgresql://***@{safe_url}")
else:
    print("   DATABASE_URL: NON IMPOSTATA")
print()

# 3. Test connessione diretta
print("🔌 Test Connessione:")
try:
    with connection.cursor() as cursor:
        # Query per ottenere info sul server
        cursor.execute("SELECT version();")
        version = cursor.fetchone()[0]
        print(f"   ✅ PostgreSQL Version: {version}")
        
        # Query per ottenere il nome del database
        cursor.execute("SELECT current_database();")
        current_db = cursor.fetchone()[0]
        print(f"   ✅ Database corrente: {current_db}")
        
        # Query per ottenere l'host (se possibile)
        cursor.execute("SELECT inet_server_addr();")
        server_addr = cursor.fetchone()[0]
        if server_addr:
            print(f"   ✅ Server Address: {server_addr}")
        else:
            print("   ✅ Server Address: localhost o connessione locale")
        
        # Query per ottenere la porta
        cursor.execute("SHOW port;")
        port = cursor.fetchone()[0]
        print(f"   ✅ Porta: {port}")
        
        # Test scrittura - crea una tabella temporanea
        cursor.execute("""
            CREATE TEMP TABLE test_render_connection (
                id SERIAL PRIMARY KEY,
                test_message TEXT,
                created_at TIMESTAMP DEFAULT NOW()
            );
        """)
        
        cursor.execute("""
            INSERT INTO test_render_connection (test_message) 
            VALUES ('Test connessione a Render PostgreSQL');
        """)
        
        cursor.execute("SELECT * FROM test_render_connection;")
        test_data = cursor.fetchone()
        print(f"   ✅ Test scrittura: {test_data[1]}")
        print(f"   ✅ Timestamp server: {test_data[2]}")
        
except Exception as e:
    print(f"   ❌ Errore connessione: {e}")

print()

# 4. Verifica se è SQLite (fallback)
if 'sqlite' in db_config['ENGINE'].lower():
    print("⚠️  ATTENZIONE: Stai usando SQLite, non PostgreSQL!")
    print("   Verifica le variabili d'ambiente DATABASE_URL")
else:
    print("✅ Confermato: Stai usando PostgreSQL")

# 5. Test specifico per Render
print()
print("🌐 Test Specifico Render:")
if database_url and 'render.com' in database_url:
    print("   ✅ URL contiene 'render.com' - probabilmente collegato a Render")
elif database_url and any(host in database_url for host in ['localhost', '127.0.0.1', '::1']):
    print("   ⚠️  URL contiene localhost - probabilmente database locale")
else:
    print("   ❓ Non è possibile determinare se è Render dal solo URL")

print()
print("🎯 CONCLUSIONE:")
if 'postgresql' in db_config['ENGINE'] and database_url and 'render.com' in database_url:
    print("   ✅ MOLTO PROBABILMENTE COLLEGATO A RENDER POSTGRESQL")
else:
    print("   ❌ PROBABILMENTE NON COLLEGATO A RENDER")

print("\n" + "=" * 50)