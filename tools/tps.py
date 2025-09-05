#!/usr/bin/env python3
"""
Script per testare e diagnosticare il proxy PostgreSQL
Esegui: python test_postgres_proxy.py
"""

import socket
import time
import subprocess
import sys
import os
from urllib.parse import urlparse

def test_basic_connectivity():
    """Test 1: Connettività di base"""
    print("🔍 TEST 1: Connettività Base")
    print("=" * 50)
    
    host = '100.108.112.117'
    ports = [5432, 6543, 6432]
    
    results = {}
    
    for port in ports:
        try:
            start = time.time()
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(5)
            s.connect((host, port))
            connect_time = (time.time() - start) * 1000
            s.close()
            print(f'✅ Port {port}: OPEN ({connect_time:.1f}ms)')
            results[port] = True
        except Exception as e:
            print(f'❌ Port {port}: CLOSED - {e}')
            results[port] = False
    
    return results

def test_ssl_connection():
    """Test 2: Connessione SSL"""
    print("\n🔐 TEST 2: Connessione SSL")
    print("=" * 50)
    
    import ssl
    
    host = '100.108.112.117'
    port = 6543  # Porta SSL
    
    try:
        # Test connessione SSL
        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE
        
        with socket.create_connection((host, port), timeout=10) as sock:
            with context.wrap_socket(sock, server_hostname=host) as ssock:
                print(f"✅ SSL Connection successful")
                print(f"✅ SSL Version: {ssock.version()}")
                print(f"✅ Cipher: {ssock.cipher()}")
                return True
                
    except Exception as e:
        print(f"❌ SSL Connection failed: {e}")
        return False

def test_raw_postgres_protocol():
    """Test 3: Protocollo PostgreSQL Raw"""
    print("\n🐘 TEST 3: Protocollo PostgreSQL Raw")
    print("=" * 50)
    
    host = '100.108.112.117'
    port = 6432  # Porta non-SSL
    
    try:
        # Crea un messaggio PostgreSQL StartupMessage
        # https://www.postgresql.org/docs/current/protocol-message-formats.html
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(10)
        sock.connect((host, port))
        
        # Startup message per PostgreSQL
        # Formato: length(4 bytes) + protocol_version(4 bytes) + parameters + null terminator
        username = "ninvendo_user"
        database = "ninvendo_db"
        
        # Protocol version 3.0 = 196608 (0x00030000)
        protocol_version = (3 << 16) + 0
        
        # Costruisci il messaggio
        message = b''
        message += f"user\x00{username}\x00".encode('utf-8')
        message += f"database\x00{database}\x00".encode('utf-8')
        message += b'\x00'  # Terminatore
        
        # Aggiungi lunghezza totale (4 bytes per lunghezza + 4 per versione + messaggio)
        total_length = 4 + 4 + len(message)
        startup_packet = total_length.to_bytes(4, 'big') + protocol_version.to_bytes(4, 'big') + message
        
        print(f"📤 Sending PostgreSQL startup packet ({len(startup_packet)} bytes)")
        sock.send(startup_packet)
        
        # Leggi la risposta
        response = sock.recv(1024)
        print(f"📥 Received {len(response)} bytes")
        
        if len(response) > 0:
            # Il primo byte indica il tipo di messaggio
            msg_type = chr(response[0]) if response[0] < 128 else 'Unknown'
            print(f"✅ Message type: {msg_type}")
            
            if msg_type == 'R':  # Authentication message
                print("✅ PostgreSQL responded with Authentication request")
                return True
            elif msg_type == 'E':  # Error message
                print("⚠️ PostgreSQL responded with Error")
                # Leggi il messaggio di errore
                error_length = int.from_bytes(response[1:5], 'big')
                error_msg = response[5:5+error_length-4].decode('utf-8', errors='ignore')
                print(f"Error: {error_msg}")
                return False
        
        sock.close()
        return True
        
    except Exception as e:
        print(f"❌ PostgreSQL protocol test failed: {e}")
        return False

def test_psql_command():
    """Test 4: Test con psql command"""
    print("\n💻 TEST 4: Test psql Command")
    print("=" * 50)
    
    # Definisci possibili percorsi psql
    psql_paths = [
        r"C:\Program Files\PostgreSQL\17\bin\psql.exe",
        r"C:\Program Files\PostgreSQL\16\bin\psql.exe", 
        r"C:\Program Files\PostgreSQL\15\bin\psql.exe",
        r"C:\Program Files\PostgreSQL\14\bin\psql.exe",
        "psql",  # Se è nel PATH
    ]
    
    psql_cmd = None
    for path in psql_paths:
        if os.path.exists(path) or path == "psql":
            psql_cmd = path
            break
    
    if not psql_cmd:
        print("❌ psql not found")
        return False
    
    print(f"📍 Using psql: {psql_cmd}")
    
    # Testa diverse combinazioni
    test_configs = [
        {"host": "100.108.112.117", "port": 6432, "ssl": "disable"},
        {"host": "100.108.112.117", "port": 6432, "ssl": "prefer"},
        {"host": "100.108.112.117", "port": 6543, "ssl": "require"},
        {"host": "100.108.112.117", "port": 6543, "ssl": "disable"},
    ]
    
    for i, config in enumerate(test_configs):
        print(f"\n🔸 Test {i+1}: Port {config['port']}, SSL {config['ssl']}")
        
        env = os.environ.copy()
        env['PGPASSWORD'] = 'NinV3nd0_S3cur3_P4ss!'
        
        cmd = [
            psql_cmd,
            '-h', config['host'],
            '-p', str(config['port']),
            '-U', 'ninvendo_user',
            '-d', 'ninvendo_db',
            '-c', "SELECT 'Proxy PostgreSQL funziona!' as test;",
            '--no-password'
        ]
        
        if config['ssl']:
            env['PGSSLMODE'] = config['ssl']
        
        try:
            result = subprocess.run(
                cmd,
                env=env,
                capture_output=True,
                text=True,
                timeout=15
            )
            
            if result.returncode == 0:
                print(f"✅ Success: {result.stdout.strip()}")
                return True
            else:
                print(f"❌ Failed (code {result.returncode})")
                print(f"   Error: {result.stderr.strip()}")
                
        except subprocess.TimeoutExpired:
            print("❌ Timeout (15s)")
        except Exception as e:
            print(f"❌ Exception: {e}")
    
    return False

def test_django_connection():
    """Test 5: Test connessione Django"""
    print("\n🐍 TEST 5: Test Django Connection")
    print("=" * 50)
    
    database_configs = [
        {
            'ENGINE': 'django.db.backends.postgresql',
            'HOST': '100.108.112.117',
            'PORT': '6432',
            'NAME': 'ninvendo_db',
            'USER': 'ninvendo_user',
            'PASSWORD': 'NinV3nd0_S3cur3_P4ss!',
            'OPTIONS': {
                'sslmode': 'disable',
            }
        },
        {
            'ENGINE': 'django.db.backends.postgresql',
            'HOST': '100.108.112.117', 
            'PORT': '6543',
            'NAME': 'ninvendo_db',
            'USER': 'ninvendo_user',
            'PASSWORD': 'NinV3nd0_S3cur3_P4ss!',
            'OPTIONS': {
                'sslmode': 'require',
            }
        }
    ]
    
    for i, db_config in enumerate(database_configs):
        print(f"\n🔸 Django Test {i+1}: Port {db_config['PORT']}")
        
        try:
            import psycopg2
            
            conn = psycopg2.connect(
                host=db_config['HOST'],
                port=db_config['PORT'],
                database=db_config['NAME'],
                user=db_config['USER'],
                password=db_config['PASSWORD'],
                sslmode=db_config['OPTIONS']['sslmode'],
                connect_timeout=10
            )
            
            cursor = conn.cursor()
            cursor.execute("SELECT 'Django PostgreSQL funziona!' as test;")
            result = cursor.fetchone()
            
            print(f"✅ Success: {result[0]}")
            conn.close()
            return True
            
        except ImportError:
            print("❌ psycopg2 not installed")
        except Exception as e:
            print(f"❌ Failed: {e}")
    
    return False

def suggest_fixes():
    """Suggerimenti per risolvere i problemi"""
    print("\n🔧 SUGGERIMENTI PER RISOLVERE I PROBLEMI")
    print("=" * 60)
    
    print("\n📋 1. VERIFICA CONFIGURAZIONE STUNNEL")
    print("Sul server proxy, esegui:")
    print("sudo cat /etc/stunnel/stunnel.conf")
    print("sudo systemctl status stunnel")
    print("sudo journalctl -u stunnel -n 50")
    
    print("\n📋 2. CONFIGURAZIONE CORRETTA STUNNEL")
    print("Il file /etc/stunnel/stunnel.conf dovrebbe essere:")
    print("""
# NINVENDO PostgreSQL Proxy
pid = /var/run/stunnel/stunnel.pid
debug = 4

# PostgreSQL con SSL
[postgresql-ssl]
accept = 6543
connect = localhost:5432
cert = /etc/stunnel/server.pem
key = /etc/stunnel/server.key

# PostgreSQL senza SSL (tunnel TCP)
[postgresql-tcp]
accept = 6432
connect = localhost:5432
""")
    
    print("\n📋 3. VERIFICA POSTGRESQL LOCALE")
    print("Sul server proxy, testa il PostgreSQL locale:")
    print("sudo -u postgres psql -c \"SELECT 'Local PostgreSQL OK!' as test;\"")
    
    print("\n📋 4. VERIFICA FIREWALL")
    print("Sul server proxy:")
    print("sudo iptables -L | grep 643")
    print("sudo firewall-cmd --list-ports")
    
    print("\n📋 5. TEST CONNESSIONE DIRETTA")
    print("Dal server proxy, testa:")
    print("telnet localhost 5432")
    
    print("\n📋 6. CONFIGURAZIONE RENDER")
    print("Per Render, usa questa DATABASE_URL:")
    print("postgresql://ninvendo_user:NinV3nd0_S3cur3_P4ss!@100.108.112.117:6432/ninvendo_db?sslmode=disable")

def main():
    """Esegui tutti i test"""
    print("🚀 NINVENDO PostgreSQL Proxy Test Suite")
    print("=" * 60)
    
    # Esegui tutti i test
    test_basic_connectivity()
    test_ssl_connection()
    test_raw_postgres_protocol() 
    test_psql_command()
    test_django_connection()
    
    # Suggerimenti
    suggest_fixes()
    
    print("\n" + "=" * 60)
    print("🏁 Test completati!")

if __name__ == "__main__":
    main()