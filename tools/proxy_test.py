#!/usr/bin/env python3
"""
🔧 NINVENDO Proxy Debug & Security Test
========================================

Script completo per testare:
- Connettività proxy
- Sicurezza TLS/SSL 
- Performance
- Configurazione PostgreSQL
- Debug problemi comuni

Uso:
    python proxy_test.py --full        # Test completo
    python proxy_test.py --quick       # Test rapido
    python proxy_test.py --security    # Solo test sicurezza
"""

import socket
import time
import ssl
import argparse
import sys
import subprocess
import json
from datetime import datetime
from typing import Dict, List, Tuple, Optional

# Configurazione
PROXY_CONFIG = {
    'host': '100.108.112.117',  # IP Oracle Cloud (Tailscale)
    'ports': {
        'postgresql': 5432,
        'postgresql_ssl': 6543,
        'stunnel': 6432,
        'ssh': 22
    },
    'local_pg': {
        'host': 'localhost',
        'port': 5432,
        'user': 'ninvendo_user',
        'database': 'ninvendo_db'
    }
}

class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    BOLD = '\033[1m'
    END = '\033[0m'

def print_header(title: str):
    """Stampa header colorato"""
    print(f"\n{Colors.BOLD}{Colors.BLUE}{'='*60}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.CYAN}🔧 {title}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.BLUE}{'='*60}{Colors.END}")

def print_success(msg: str):
    print(f"{Colors.GREEN}✅ {msg}{Colors.END}")

def print_error(msg: str):
    print(f"{Colors.RED}❌ {msg}{Colors.END}")

def print_warning(msg: str):
    print(f"{Colors.YELLOW}⚠️  {msg}{Colors.END}")

def print_info(msg: str):
    print(f"{Colors.CYAN}ℹ️  {msg}{Colors.END}")

class ProxyTester:
    def __init__(self, config: dict):
        self.config = config
        self.results = {}
        
    def test_port_connectivity(self) -> Dict[str, bool]:
        """Test connettività porte"""
        print_header("Test Connettività Porte")
        
        results = {}
        host = self.config['host']
        
        for service, port in self.config['ports'].items():
            try:
                start_time = time.time()
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(5)
                
                result = sock.connect_ex((host, port))
                connect_time = (time.time() - start_time) * 1000
                
                if result == 0:
                    print_success(f"{service.upper()} (:{port}) - OPEN ({connect_time:.1f}ms)")
                    results[service] = True
                else:
                    print_error(f"{service.upper()} (:{port}) - CLOSED")
                    results[service] = False
                    
                sock.close()
                
            except Exception as e:
                print_error(f"{service.upper()} (:{port}) - ERROR: {e}")
                results[service] = False
                
        return results

    def test_ssl_security(self) -> Dict[str, any]:
        """Test sicurezza SSL/TLS"""
        print_header("Test Sicurezza SSL/TLS")
        
        ssl_results = {}
        host = self.config['host']
        ssl_port = self.config['ports'].get('postgresql_ssl', 6543)
        
        try:
            # Test SSL connection
            context = ssl.create_default_context()
            context.check_hostname = False
            context.verify_mode = ssl.CERT_NONE
            
            with socket.create_connection((host, ssl_port), timeout=10) as sock:
                with context.wrap_socket(sock, server_hostname=host) as ssock:
                    cert = ssock.getpeercert()
                    cipher = ssock.cipher()
                    
                    print_success(f"SSL Connection stabilita")
                    print_info(f"Cipher: {cipher[0] if cipher else 'Unknown'}")
                    print_info(f"SSL Version: {cipher[1] if cipher else 'Unknown'}")
                    
                    ssl_results['connected'] = True
                    ssl_results['cipher'] = cipher[0] if cipher else None
                    ssl_results['ssl_version'] = cipher[1] if cipher else None
                    ssl_results['cert_info'] = cert
                    
        except Exception as e:
            print_error(f"SSL Test failed: {e}")
            ssl_results['connected'] = False
            ssl_results['error'] = str(e)
            
        return ssl_results

    def test_postgresql_connection(self, use_ssl: bool = False) -> Dict[str, any]:
        """Test connessione PostgreSQL"""
        service_name = "PostgreSQL SSL" if use_ssl else "PostgreSQL Plain"
        print_header(f"Test {service_name}")
        
        pg_results = {}
        
        try:
            # Tenta di importare psycopg2
            import psycopg2
            
            # Configura connessione
            host = self.config['host']
            port = self.config['ports']['postgresql_ssl'] if use_ssl else self.config['ports']['postgresql']
            
            # Parametri di connessione per test locale
            conn_params = {
                'host': host,
                'port': port,
                'user': 'postgres',  # User default per test
                'password': 'test123',  # Password test
                'database': 'postgres',  # DB default
                'connect_timeout': 10
            }
            
            if use_ssl:
                conn_params['sslmode'] = 'require'
            
            print_info(f"Tentativo connessione a {host}:{port}")
            
            # Test connessione
            start_time = time.time()
            conn = psycopg2.connect(**conn_params)
            connect_time = (time.time() - start_time) * 1000
            
            # Test query
            cur = conn.cursor()
            cur.execute('SELECT version()')
            version = cur.fetchone()[0]
            
            print_success(f"Connessione riuscita ({connect_time:.1f}ms)")
            print_info(f"PostgreSQL Version: {version}")
            
            cur.close()
            conn.close()
            
            pg_results['connected'] = True
            pg_results['connect_time'] = connect_time
            pg_results['version'] = version
            
        except ImportError:
            print_warning("psycopg2 non installato - Test saltato")
            print_info("Installa con: pip install psycopg2-binary")
            pg_results['skipped'] = True
            
        except Exception as e:
            print_error(f"Connessione fallita: {e}")
            pg_results['connected'] = False
            pg_results['error'] = str(e)
            
        return pg_results

    def test_performance(self) -> Dict[str, any]:
        """Test performance proxy"""
        print_header("Test Performance")
        
        perf_results = {}
        host = self.config['host']
        port = self.config['ports']['stunnel']
        
        # Test latenza
        latencies = []
        successful_pings = 0
        
        print_info("Testing latency (10 pings)...")
        
        for i in range(10):
            try:
                start = time.time()
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(3)
                sock.connect((host, port))
                latency = (time.time() - start) * 1000
                latencies.append(latency)
                successful_pings += 1
                sock.close()
                print(f"  Ping {i+1}: {latency:.1f}ms")
            except:
                print(f"  Ping {i+1}: TIMEOUT")
                
        if latencies:
            avg_latency = sum(latencies) / len(latencies)
            min_latency = min(latencies)
            max_latency = max(latencies)
            
            print_success(f"Latenza media: {avg_latency:.1f}ms")
            print_info(f"Min: {min_latency:.1f}ms, Max: {max_latency:.1f}ms")
            print_info(f"Success rate: {successful_pings}/10 ({successful_pings*10}%)")
            
            perf_results['avg_latency'] = avg_latency
            perf_results['min_latency'] = min_latency
            perf_results['max_latency'] = max_latency
            perf_results['success_rate'] = successful_pings / 10
        else:
            print_error("Nessuna connessione riuscita")
            perf_results['success_rate'] = 0
            
        return perf_results

    def test_firewall_bypass(self) -> Dict[str, any]:
        """Test che il proxy bypassa correttamente il firewall"""
        print_header("Test Firewall Bypass")
        
        firewall_results = {}
        
        # Test connessione diretta alla macchina protetta (dovrebbe fallire)
        protected_host = "192.168.1.100"  # IP macchina dietro firewall
        protected_port = 5432
        
        print_info(f"Test connessione diretta a {protected_host}:{protected_port} (dovrebbe fallire)")
        
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            result = sock.connect_ex((protected_host, protected_port))
            sock.close()
            
            if result == 0:
                print_warning("Connessione diretta riuscita - Firewall potrebbe non essere attivo")
                firewall_results['direct_blocked'] = False
            else:
                print_success("Connessione diretta bloccata (firewall attivo)")
                firewall_results['direct_blocked'] = True
                
        except Exception as e:
            print_success(f"Connessione diretta bloccata: {e}")
            firewall_results['direct_blocked'] = True
            
        # Test connessione via proxy
        proxy_host = self.config['host']
        proxy_port = self.config['ports']['stunnel']
        
        print_info(f"Test connessione via proxy {proxy_host}:{proxy_port}")
        
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            result = sock.connect_ex((proxy_host, proxy_port))
            sock.close()
            
            if result == 0:
                print_success("Connessione via proxy riuscita")
                firewall_results['proxy_works'] = True
            else:
                print_error("Connessione via proxy fallita")
                firewall_results['proxy_works'] = False
                
        except Exception as e:
            print_error(f"Connessione via proxy fallita: {e}")
            firewall_results['proxy_works'] = False
            
        return firewall_results

    def generate_debug_commands(self):
        """Genera comandi di debug per la macchina proxy"""
        print_header("Comandi Debug per Oracle Cloud Proxy")
        
        commands = [
            "# 🔍 Status servizi",
            "sudo systemctl status stunnel",
            "sudo systemctl status socat",
            "",
            "# 📋 Log servizi",
            "sudo journalctl -u stunnel -n 20",
            "sudo journalctl -u socat -n 20",
            "",
            "# 🔧 Configurazioni",
            "sudo cat /etc/stunnel/stunnel.conf",
            "ps aux | grep socat",
            "",
            "# 🌐 Network status", 
            "sudo netstat -tlnp | grep ':643'",
            "sudo netstat -tlnp | grep ':5432'",
            "",
            "# 🔥 Firewall status",
            "sudo iptables -L -n",
            "sudo firewall-cmd --list-all",
            "",
            "# 📡 Tailscale status",
            "sudo tailscale status",
            "sudo tailscale ping 100.108.112.117",
            "",
            "# 🐘 Test PostgreSQL locale",
            "psql -h localhost -p 5432 -U postgres -c 'SELECT version();'",
            "",
            "# 🔌 Test porte manualmente",
            "nc -zv localhost 5432",
            "nc -zv localhost 6432", 
            "nc -zv localhost 6543",
        ]
        
        for cmd in commands:
            if cmd.startswith('#'):
                print(f"{Colors.YELLOW}{cmd}{Colors.END}")
            else:
                print(f"  {cmd}")
        
        print_info("\nCopia e incolla questi comandi nella sessione SSH del proxy Oracle Cloud")

    def generate_setup_commands(self):
        """Genera comandi per completare setup proxy"""
        print_header("Setup Comandi per Oracle Cloud Proxy")
        
        setup_commands = [
            "# 🔧 Installa e configura stunnel",
            "sudo dnf install -y stunnel",
            "",
            "# 📝 Crea configurazione stunnel",
            "sudo mkdir -p /etc/stunnel",
            "sudo tee /etc/stunnel/stunnel.conf << 'EOF'",
            "[postgresql]",
            "accept = 6543",
            "connect = localhost:5432",
            "cert = /etc/stunnel/server.pem",
            "key = /etc/stunnel/server.key",
            "EOF",
            "",
            "# 🔐 Genera certificati SSL self-signed",
            "sudo openssl req -new -x509 -days 365 -nodes \\",
            "  -out /etc/stunnel/server.pem \\", 
            "  -keyout /etc/stunnel/server.key \\",
            "  -subj '/CN=ninvendo-proxy'",
            "",
            "# 🔒 Fix permessi",
            "sudo chmod 600 /etc/stunnel/server.key",
            "sudo chmod 644 /etc/stunnel/server.pem",
            "",
            "# 🚀 Abilita e avvia stunnel",
            "sudo systemctl enable stunnel",
            "sudo systemctl start stunnel",
            "",
            "# 🔌 Setup socat per proxy TCP plain",
            "sudo tee /etc/systemd/system/socat-postgres.service << 'EOF'",
            "[Unit]",
            "Description=Socat PostgreSQL Proxy",
            "After=network.target",
            "",
            "[Service]",
            "Type=simple",
            "User=nobody",
            "ExecStart=/usr/bin/socat TCP-LISTEN:6432,fork,reuseaddr TCP:localhost:5432",
            "Restart=always",
            "RestartSec=5",
            "",
            "[Install]",
            "WantedBy=multi-user.target",
            "EOF",
            "",
            "sudo systemctl enable socat-postgres",
            "sudo systemctl start socat-postgres",
            "",
            "# 🔥 Configura firewall",
            "sudo firewall-cmd --permanent --add-port=6432/tcp",
            "sudo firewall-cmd --permanent --add-port=6543/tcp", 
            "sudo firewall-cmd --reload",
        ]
        
        for cmd in setup_commands:
            if cmd.startswith('#'):
                print(f"{Colors.YELLOW}{cmd}{Colors.END}")
            else:
                print(f"  {cmd}")

    def run_full_test(self) -> Dict[str, any]:
        """Esegue test completo"""
        print_header("NINVENDO Proxy - Test Completo")
        print_info(f"Target: {self.config['host']}")
        print_info(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        all_results = {}
        
        # Test connettività
        all_results['connectivity'] = self.test_port_connectivity()
        
        # Test performance
        all_results['performance'] = self.test_performance()
        
        # Test SSL
        all_results['ssl'] = self.test_ssl_security()
        
        # Test PostgreSQL
        all_results['postgresql_plain'] = self.test_postgresql_connection(use_ssl=False)
        all_results['postgresql_ssl'] = self.test_postgresql_connection(use_ssl=True)
        
        # Test firewall
        all_results['firewall'] = self.test_firewall_bypass()
        
        return all_results

    def print_summary(self, results: Dict[str, any]):
        """Stampa riassunto risultati"""
        print_header("Riassunto Test")
        
        # Connectivity Summary
        conn_results = results.get('connectivity', {})
        working_ports = sum(1 for status in conn_results.values() if status)
        total_ports = len(conn_results)
        
        if working_ports == total_ports:
            print_success(f"Connettività: {working_ports}/{total_ports} porte funzionanti")
        elif working_ports > 0:
            print_warning(f"Connettività: {working_ports}/{total_ports} porte funzionanti")
        else:
            print_error(f"Connettività: {working_ports}/{total_ports} porte funzionanti")
        
        # Performance Summary
        perf_results = results.get('performance', {})
        if 'success_rate' in perf_results:
            success_rate = perf_results['success_rate'] * 100
            if success_rate >= 90:
                print_success(f"Performance: {success_rate:.0f}% success rate")
            elif success_rate >= 70:
                print_warning(f"Performance: {success_rate:.0f}% success rate")
            else:
                print_error(f"Performance: {success_rate:.0f}% success rate")
        
        # SSL Summary
        ssl_results = results.get('ssl', {})
        if ssl_results.get('connected'):
            print_success("SSL: Configurazione sicura attiva")
        else:
            print_warning("SSL: Non configurato o non funzionante")
        
        # PostgreSQL Summary  
        pg_plain = results.get('postgresql_plain', {})
        pg_ssl = results.get('postgresql_ssl', {})
        
        if pg_plain.get('connected') or pg_ssl.get('connected'):
            print_success("PostgreSQL: Connessione disponibile")
        else:
            print_error("PostgreSQL: Nessuna connessione funzionante")
        
        # Overall Status
        print("\n" + "="*60)
        critical_checks = [
            conn_results.get('stunnel', False),
            perf_results.get('success_rate', 0) > 0.5
        ]
        
        if all(critical_checks):
            print_success("🎉 PROXY FUNZIONANTE - Pronto per produzione")
        elif any(critical_checks):
            print_warning("⚠️  PROXY PARZIALE - Richiede configurazione aggiuntiva")
        else:
            print_error("❌ PROXY NON FUNZIONANTE - Richiede debug")

def main():
    parser = argparse.ArgumentParser(description='NINVENDO Proxy Debug & Security Test')
    parser.add_argument('--full', action='store_true', help='Esegui test completo')
    parser.add_argument('--quick', action='store_true', help='Test rapido connettività')
    parser.add_argument('--security', action='store_true', help='Solo test sicurezza')
    parser.add_argument('--setup', action='store_true', help='Mostra comandi setup')
    parser.add_argument('--debug', action='store_true', help='Mostra comandi debug')
    
    args = parser.parse_args()
    
    tester = ProxyTester(PROXY_CONFIG)
    
    if args.setup:
        tester.generate_setup_commands()
    elif args.debug:
        tester.generate_debug_commands()
    elif args.security:
        results = {}
        results['ssl'] = tester.test_ssl_security()
        results['firewall'] = tester.test_firewall_bypass()
        tester.print_summary(results)
    elif args.quick:
        results = {}
        results['connectivity'] = tester.test_port_connectivity()
        results['performance'] = tester.test_performance()
        tester.print_summary(results)
    elif args.full:
        results = tester.run_full_test()
        tester.print_summary(results)
        
        # Salva risultati in JSON
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f'ninvendo_proxy_test_{timestamp}.json'
        with open(filename, 'w') as f:
            json.dump(results, f, indent=2, default=str)
        print_info(f"Risultati salvati in: {filename}")
    else:
        # Default: quick test
        results = {}
        results['connectivity'] = tester.test_port_connectivity()
        results['performance'] = tester.test_performance()
        tester.print_summary(results)
        
        print_info("\nUsa --help per vedere tutte le opzioni disponibili")

if __name__ == '__main__':
    main()