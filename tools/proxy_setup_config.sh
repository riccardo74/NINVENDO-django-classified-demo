#!/usr/bin/env python3
"""
PostgreSQL Proxy Test Suite
===========================

Script per testare l'efficacia e la sicurezza del proxy PostgreSQL
per il marketplace NINVENDO.

Testa:
- Connessione attraverso il proxy
- Autenticazione SSL/TLS
- Performance delle query
- Sicurezza delle connessioni
- Failover e resilienza
- Monitoring delle metriche

Requisiti:
- psycopg2-binary
- requests
- cryptography (per SSL testing)
- concurrent.futures
"""

import os
import sys
import time
import json
import socket
import ssl
import subprocess
import threading
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Dict, List, Tuple, Optional, Any

try:
    import psycopg2
    from psycopg2 import sql
    import requests
    from cryptography import x509
    from cryptography.hazmat.backends import default_backend
except ImportError as e:
    print(f"❌ Missing required package: {e}")
    print("Install with: pip install psycopg2-binary requests cryptography")
    sys.exit(1)

class Colors:
    """ANSI color codes for console output"""
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class ProxyTester:
    def __init__(self):
        self.results = {
            'timestamp': datetime.now().isoformat(),
            'tests': {},
            'summary': {
                'total_tests': 0,
                'passed': 0,
                'failed': 0,
                'warnings': 0
            }
        }
        
        # Configurazione dai file di ambiente o parametri
        self.config = {
            'proxy_host': os.getenv('PROXY_HOST', 'proxy.your-oracle-cloud.com'),
            'proxy_port': int(os.getenv('PROXY_PORT', '5432')),
            'db_host': os.getenv('DB_HOST', 'localhost'),  # Host reale dietro il proxy
            'db_port': int(os.getenv('DB_PORT', '5432')),
            'db_name': os.getenv('DB_NAME', 'ninvendo_dev'),
            'db_user': os.getenv('DB_USER', 'ninvendo'),
            'db_password': os.getenv('DB_PASSWORD', ''),
            'ssl_mode': os.getenv('PGSSLMODE', 'require'),
            'tailscale_ip': os.getenv('TAILSCALE_IP', '100.x.x.x'),
            'stunnel_port': int(os.getenv('STUNNEL_PORT', '6543')),
            'test_timeout': int(os.getenv('TEST_TIMEOUT', '30'))
        }

    def print_header(self, text: str):
        """Stampa un header colorato"""
        print(f"\n{Colors.HEADER}{Colors.BOLD}{'='*50}{Colors.ENDC}")
        print(f"{Colors.HEADER}{Colors.BOLD}{text:^50}{Colors.ENDC}")
        print(f"{Colors.HEADER}{Colors.BOLD}{'='*50}{Colors.ENDC}\n")

    def print_test(self, name: str, status: str, details: str = ""):
        """Stampa il risultato di un test"""
        if status == "PASS":
            color = Colors.OKGREEN
            symbol = "✅"
        elif status == "FAIL":
            color = Colors.FAIL
            symbol = "❌"
        elif status == "WARN":
            color = Colors.WARNING
            symbol = "⚠️"
        else:
            color = Colors.OKCYAN
            symbol = "ℹ️"
            
        print(f"{symbol} {color}{name}: {status}{Colors.ENDC}")
        if details:
            print(f"   {details}")

    def record_test(self, test_name: str, passed: bool, details: Dict[str, Any] = None, warning: bool = False):
        """Registra il risultato di un test"""
        self.results['tests'][test_name] = {
            'passed': passed,
            'warning': warning,
            'details': details or {},
            'timestamp': datetime.now().isoformat()
        }
        
        self.results['summary']['total_tests'] += 1
        if passed:
            if warning:
                self.results['summary']['warnings'] += 1
            else:
                self.results['summary']['passed'] += 1
        else:
            self.results['summary']['failed'] += 1

    def test_basic_connectivity(self) -> bool:
        """Test 1: Connettività di base al proxy"""
        self.print_header("Test 1: Connettività di Base")
        
        try:
            # Test connessione TCP
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(self.config['test_timeout'])
            
            start_time = time.time()
            result = sock.connect_ex((self.config['proxy_host'], self.config['proxy_port']))
            connect_time = (time.time() - start_time) * 1000
            sock.close()
            
            if result == 0:
                self.print_test("TCP Connection", "PASS", f"Connect time: {connect_time:.2f}ms")
                self.record_test("tcp_connection", True, {"connect_time_ms": connect_time})
                return True
            else:
                self.print_test("TCP Connection", "FAIL", f"Error code: {result}")
                self.record_test("tcp_connection", False, {"error_code": result})
                return False
                
        except Exception as e:
            self.print_test("TCP Connection", "FAIL", str(e))
            self.record_test("tcp_connection", False, {"error": str(e)})
            return False

    def test_ssl_certificate(self) -> bool:
        """Test 2: Verifica certificato SSL (se stunnel è attivo)"""
        self.print_header("Test 2: Certificato SSL")
        
        try:
            # Prova prima sulla porta stunnel se configurata
            test_port = self.config['stunnel_port'] if self.config['stunnel_port'] != self.config['proxy_port'] else self.config['proxy_port']
            
            context = ssl.create_default_context()
            context.check_hostname = False  # Per testing
            
            with socket.create_connection((self.config['proxy_host'], test_port), timeout=self.config['test_timeout']) as sock:
                with context.wrap_socket(sock, server_hostname=self.config['proxy_host']) as ssock:
                    cert = ssock.getpeercert(binary_form=True)
                    cert_obj = x509.load_der_x509_certificate(cert, default_backend())
                    
                    # Verifica validità
                    now = datetime.now()
                    not_before = cert_obj.not_valid_before
                    not_after = cert_obj.not_valid_after
                    
                    days_to_expire = (not_after - now).days
                    
                    details = {
                        "subject": cert_obj.subject.rfc4514_string(),
                        "issuer": cert_obj.issuer.rfc4514_string(),
                        "not_before": not_before.isoformat(),
                        "not_after": not_after.isoformat(),
                        "days_to_expire": days_to_expire
                    }
                    
                    if days_to_expire < 30:
                        self.print_test("SSL Certificate", "WARN", f"Expires in {days_to_expire} days")
                        self.record_test("ssl_certificate", True, details, warning=True)
                    else:
                        self.print_test("SSL Certificate", "PASS", f"Valid for {days_to_expire} days")
                        self.record_test("ssl_certificate", True, details)
                    
                    return True
                    
        except ssl.SSLError as e:
            self.print_test("SSL Certificate", "FAIL", f"SSL Error: {e}")
            self.record_test("ssl_certificate", False, {"ssl_error": str(e)})
            return False
        except Exception as e:
            # Potrebbe non essere configurato SSL
            self.print_test("SSL Certificate", "WARN", f"SSL not configured or accessible: {e}")
            self.record_test("ssl_certificate", True, {"warning": str(e)}, warning=True)
            return True

    def test_postgresql_connection(self) -> bool:
        """Test 3: Connessione PostgreSQL attraverso il proxy"""
        self.print_header("Test 3: Connessione PostgreSQL")
        
        # Prova diverse configurazioni di connessione
        connection_configs = [
            {
                "name": "Direct Proxy",
                "host": self.config['proxy_host'],
                "port": self.config['proxy_port'],
                "sslmode": self.config['ssl_mode']
            },
            {
                "name": "Stunnel Proxy",
                "host": self.config['proxy_host'],
                "port": self.config['stunnel_port'],
                "sslmode": "disable"  # stunnel gestisce SSL
            },
            {
                "name": "Tailscale Direct",
                "host": self.config['tailscale_ip'],
                "port": self.config['db_port'],
                "sslmode": self.config['ssl_mode']
            }
        ]
        
        successful_connections = []
        
        for config in connection_configs:
            try:
                conn_string = (
                    f"postgresql://{self.config['db_user']}:{self.config['db_password']}"
                    f"@{config['host']}:{config['port']}/{self.config['db_name']}"
                    f"?sslmode={config['sslmode']}&connect_timeout={self.config['test_timeout']}"
                )
                
                start_time = time.time()
                conn = psycopg2.connect(conn_string)
                connect_time = (time.time() - start_time) * 1000
                
                # Test semplice query
                with conn.cursor() as cur:
                    cur.execute("SELECT version(), current_timestamp, current_user")
                    result = cur.fetchone()
                    
                conn.close()
                
                details = {
                    "connect_time_ms": connect_time,
                    "version": result[0] if result else "Unknown",
                    "timestamp": str(result[1]) if result else "Unknown",
                    "user": result[2] if result else "Unknown"
                }
                
                self.print_test(f"PostgreSQL Connection ({config['name']})", "PASS", 
                              f"Connect time: {connect_time:.2f}ms")
                self.record_test(f"postgresql_connection_{config['name'].lower().replace(' ', '_')}", 
                               True, details)
                successful_connections.append(config['name'])
                
            except psycopg2.Error as e:
                self.print_test(f"PostgreSQL Connection ({config['name']})", "FAIL", str(e))
                self.record_test(f"postgresql_connection_{config['name'].lower().replace(' ', '_')}", 
                               False, {"error": str(e)})
            except Exception as e:
                self.print_test(f"PostgreSQL Connection ({config['name']})", "FAIL", str(e))
                self.record_test(f"postgresql_connection_{config['name'].lower().replace(' ', '_')}", 
                               False, {"error": str(e)})
        
        return len(successful_connections) > 0

    def test_performance_metrics(self) -> bool:
        """Test 4: Metriche di performance"""
        self.print_header("Test 4: Performance Metrics")
        
        try:
            # Connessione per test performance
            conn_string = (
                f"postgresql://{self.config['db_user']}:{self.config['db_password']}"
                f"@{self.config['proxy_host']}:{self.config['proxy_port']}"
                f"/{self.config['db_name']}?sslmode={self.config['ssl_mode']}"
            )
            
            conn = psycopg2.connect(conn_string)
            
            # Test latenza query semplici
            simple_queries = [
                "SELECT 1",
                "SELECT current_timestamp",
                "SELECT version()",
                "SELECT COUNT(*) FROM information_schema.tables"
            ]
            
            latencies = []
            
            for query in simple_queries:
                times = []
                for _ in range(5):  # 5 esecuzioni per query
                    start_time = time.time()
                    with conn.cursor() as cur:
                        cur.execute(query)
                        cur.fetchall()
                    query_time = (time.time() - start_time) * 1000
                    times.append(query_time)
                
                avg_time = sum(times) / len(times)
                latencies.append(avg_time)
                
            avg_latency = sum(latencies) / len(latencies)
            
            # Test throughput con query concorrenti
            def run_concurrent_query():
                with conn.cursor() as cur:
                    cur.execute("SELECT pg_sleep(0.1), current_timestamp")
                    return cur.fetchall()
            
            # Test con 10 query concorrenti
            start_time = time.time()
            with ThreadPoolExecutor(max_workers=10) as executor:
                futures = [executor.submit(run_concurrent_query) for _ in range(10)]
                results = [future.result() for future in as_completed(futures)]
            
            concurrent_time = (time.time() - start_time) * 1000
            
            conn.close()
            
            details = {
                "average_latency_ms": avg_latency,
                "concurrent_queries_time_ms": concurrent_time,
                "query_latencies": latencies
            }
            
            # Valutazione performance
            if avg_latency < 50:
                status = "PASS"
            elif avg_latency < 200:
                status = "WARN"
            else:
                status = "FAIL"
            
            self.print_test("Query Latency", status, f"Avg latency: {avg_latency:.2f}ms")
            self.print_test("Concurrent Queries", "PASS", f"10 queries in {concurrent_time:.2f}ms")
            
            self.record_test("performance_metrics", status != "FAIL", details, 
                           warning=(status == "WARN"))
            
            return status != "FAIL"
            
        except Exception as e:
            self.print_test("Performance Metrics", "FAIL", str(e))
            self.record_test("performance_metrics", False, {"error": str(e)})
            return False

    def test_security_checks(self) -> bool:
        """Test 5: Controlli di sicurezza"""
        self.print_header("Test 5: Security Checks")
        
        security_tests = []
        
        # Test 1: Verifica che non si possa connettere senza autenticazione
        try:
            conn_string = (
                f"postgresql://wrong_user:wrong_pass"
                f"@{self.config['proxy_host']}:{self.config['proxy_port']}"
                f"/{self.config['db_name']}?sslmode={self.config['ssl_mode']}&connect_timeout=5"
            )
            conn = psycopg2.connect(conn_string)
            conn.close()
            
            self.print_test("Authentication Check", "FAIL", "Connected with wrong credentials!")
            security_tests.append(False)
            
        except psycopg2.Error:
            self.print_test("Authentication Check", "PASS", "Properly rejected invalid credentials")
            security_tests.append(True)
        
        # Test 2: Verifica connessione SSL se richiesta
        if self.config['ssl_mode'] in ['require', 'verify-ca', 'verify-full']:
            try:
                conn_string = (
                    f"postgresql://{self.config['db_user']}:{self.config['db_password']}"
                    f"@{self.config['proxy_host']}:{self.config['proxy_port']}"
                    f"/{self.config['db_name']}?sslmode=disable&connect_timeout=5"
                )
                conn = psycopg2.connect(conn_string)
                conn.close()
                
                self.print_test("SSL Enforcement", "FAIL", "Connected without SSL when SSL required!")
                security_tests.append(False)
                
            except psycopg2.Error:
                self.print_test("SSL Enforcement", "PASS", "Properly enforcing SSL connection")
                security_tests.append(True)
        
        # Test 3: Verifica limitazioni query (se configurate)
        try:
            conn_string = (
                f"postgresql://{self.config['db_user']}:{self.config['db_password']}"
                f"@{self.config['proxy_host']}:{self.config['proxy_port']}"
                f"/{self.config['db_name']}?sslmode={self.config['ssl_mode']}"
            )
            conn = psycopg2.connect(conn_string)
            
            # Test query potenzialmente pericolose
            dangerous_queries = [
                "SELECT * FROM pg_stat_activity",  # Info sistema
                "SHOW ALL",  # Configurazione
                "SELECT current_setting('data_directory')"  # Path sistema
            ]
            
            blocked_queries = 0
            for query in dangerous_queries:
                try:
                    with conn.cursor() as cur:
                        cur.execute(query)
                        cur.fetchall()
                except psycopg2.Error:
                    blocked_queries += 1
            
            conn.close()
            
            if blocked_queries > 0:
                self.print_test("Query Restrictions", "PASS", f"Blocked {blocked_queries}/{len(dangerous_queries)} dangerous queries")
                security_tests.append(True)
            else:
                self.print_test("Query Restrictions", "WARN", "No query restrictions detected")
                security_tests.append(True)  # Non è necessariamente un errore
                
        except Exception as e:
            self.print_test("Query Restrictions", "WARN", f"Could not test: {e}")
            security_tests.append(True)
        
        all_passed = all(security_tests)
        self.record_test("security_checks", all_passed, 
                        {"tests_passed": sum(security_tests), "total_tests": len(security_tests)})
        
        return all_passed

    def test_failover_resilience(self) -> bool:
        """Test 6: Test di resilienza e failover"""
        self.print_header("Test 6: Failover & Resilience")
        
        try:
            # Test connessioni multiple simultanee
            def create_connection():
                conn_string = (
                    f"postgresql://{self.config['db_user']}:{self.config['db_password']}"
                    f"@{self.config['proxy_host']}:{self.config['proxy_port']}"
                    f"/{self.config['db_name']}?sslmode={self.config['ssl_mode']}"
                )
                conn = psycopg2.connect(conn_string)
                time.sleep(2)  # Mantieni connessione per 2 secondi
                conn.close()
                return True
            
            # Test con 20 connessioni concorrenti
            start_time = time.time()
            with ThreadPoolExecutor(max_workers=20) as executor:
                futures = [executor.submit(create_connection) for _ in range(20)]
                successful = sum(1 for future in as_completed(futures) if future.result())
            
            total_time = (time.time() - start_time) * 1000
            
            if successful >= 18:  # Almeno 90% successo
                self.print_test("Concurrent Connections", "PASS", 
                              f"{successful}/20 successful in {total_time:.2f}ms")
            else:
                self.print_test("Concurrent Connections", "FAIL", 
                              f"Only {successful}/20 successful")
            
            # Test riconnessione dopo interruzione simulata
            try:
                # Connessione normale
                conn = psycopg2.connect(
                    f"postgresql://{self.config['db_user']}:{self.config['db_password']}"
                    f"@{self.config['proxy_host']}:{self.config['proxy_port']}"
                    f"/{self.config['db_name']}?sslmode={self.config['ssl_mode']}"
                )
                
                # Simula interruzione (chiudendo forzatamente)
                conn.close()
                
                # Riconnessione immediata
                time.sleep(1)
                conn = psycopg2.connect(
                    f"postgresql://{self.config['db_user']}:{self.config['db_password']}"
                    f"@{self.config['proxy_host']}:{self.config['proxy_port']}"
                    f"/{self.config['db_name']}?sslmode={self.config['ssl_mode']}"
                )
                
                with conn.cursor() as cur:
                    cur.execute("SELECT 1")
                    cur.fetchone()
                
                conn.close()
                
                self.print_test("Connection Recovery", "PASS", "Successfully reconnected after interruption")
                
            except Exception as e:
                self.print_test("Connection Recovery", "FAIL", f"Failed to reconnect: {e}")
            
            details = {
                "concurrent_success_rate": successful / 20,
                "concurrent_time_ms": total_time
            }
            
            self.record_test("failover_resilience", successful >= 18, details)
            return successful >= 18
            
        except Exception as e:
            self.print_test("Failover & Resilience", "FAIL", str(e))
            self.record_test("failover_resilience", False, {"error": str(e)})
            return False

    def test_tailscale_connectivity(self) -> bool:
        """Test 7: Connettività Tailscale"""
        self.print_header("Test 7: Tailscale Network")
        
        try:
            # Test ping a IP Tailscale
            if self.config['tailscale_ip'].startswith('100.'):
                result = subprocess.run(['ping', '-c', '3', '-W', '5', self.config['tailscale_ip']], 
                                      capture_output=True, text=True, timeout=15)
                
                if result.returncode == 0:
                    # Estrai statistiche ping
                    output = result.stdout
                    if "3 packets transmitted, 3 received" in output:
                        self.print_test("Tailscale Ping", "PASS", "All packets received")
                    else:
                        self.print_test("Tailscale Ping", "WARN", "Some packet loss detected")
                else:
                    self.print_test("Tailscale Ping", "FAIL", "Cannot reach Tailscale IP")
                    return False
            else:
                self.print_test("Tailscale Ping", "WARN", "Tailscale IP not configured")
            
            # Test connessione diretta se possibile
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(10)
                result = sock.connect_ex((self.config['tailscale_ip'], self.config['db_port']))
                sock.close()
                
                if result == 0:
                    self.print_test("Tailscale DB Connection", "PASS", "Direct connection available")
                else:
                    self.print_test("Tailscale DB Connection", "FAIL", f"Cannot connect directly (code: {result})")
                    
            except Exception as e:
                self.print_test("Tailscale DB Connection", "FAIL", str(e))
            
            self.record_test("tailscale_connectivity", True)  # Non bloccante
            return True
            
        except Exception as e:
            self.print_test("Tailscale Connectivity", "WARN", f"Cannot test Tailscale: {e}")
            self.record_test("tailscale_connectivity", True, {"warning": str(e)}, warning=True)
            return True

    def test_monitoring_endpoints(self) -> bool:
        """Test 8: Endpoint di monitoring (se disponibili)"""
        self.print_header("Test 8: Monitoring Endpoints")
        
        # Lista di possibili endpoint di monitoring
        monitoring_endpoints = [
            f"http://{self.config['proxy_host']}:8080/health",
            f"https://{self.config['proxy_host']}:8080/health",
            f"http://{self.config['proxy_host']}:9090/metrics",  # Prometheus
            f"https://{self.config['proxy_host']}:9090/metrics"
        ]
        
        available_endpoints = []
        
        for endpoint in monitoring_endpoints:
            try:
                response = requests.get(endpoint, timeout=10, verify=False)
                if response.status_code == 200:
                    available_endpoints.append(endpoint)
                    self.print_test(f"Monitoring Endpoint", "PASS", f"{endpoint} - Status: {response.status_code}")
                else:
                    self.print_test(f"Monitoring Endpoint", "WARN", f"{endpoint} - Status: {response.status_code}")
                    
            except requests.RequestException:
                # Endpoint non disponibile, normale
                pass
        
        if available_endpoints:
            self.print_test("Monitoring Available", "PASS", f"Found {len(available_endpoints)} endpoints")
        else:
            self.print_test("Monitoring Available", "WARN", "No monitoring endpoints found")
        
        self.record_test("monitoring_endpoints", True, 
                        {"available_endpoints": available_endpoints}, 
                        warning=(len(available_endpoints) == 0))
        return True

    def generate_report(self) -> str:
        """Genera un report completo dei test"""
        report = []
        report.append(f"\n{Colors.BOLD}{'='*60}{Colors.ENDC}")
        report.append(f"{Colors.BOLD}{Colors.HEADER}NINVENDO PostgreSQL Proxy Test Report{Colors.ENDC}")
        report.append(f"{Colors.BOLD}{'='*60}{Colors.ENDC}\n")
        
        # Summary
        summary = self.results['summary']
        total = summary['total_tests']
        passed = summary['passed']
        failed = summary['failed']
        warnings = summary['warnings']
        
        report.append(f"📊 {Colors.BOLD}Test Summary:{Colors.ENDC}")
        report.append(f"   Total Tests: {total}")
        report.append(f"   {Colors.OKGREEN}✅ Passed: {passed}{Colors.ENDC}")
        report.append(f"   {Colors.FAIL}❌ Failed: {failed}{Colors.ENDC}")
        report.append(f"   {Colors.WARNING}⚠️  Warnings: {warnings}{Colors.ENDC}")
        
        success_rate = (passed / total * 100) if total > 0 else 0
        if success_rate >= 90:
            color = Colors.OKGREEN
        elif success_rate >= 70:
            color = Colors.WARNING
        else:
            color = Colors.FAIL
            
        report.append(f"   {color}Success Rate: {success_rate:.1f}%{Colors.ENDC}\n")
        
        # Raccomandazioni
        report.append(f"💡 {Colors.BOLD}Recommendations:{Colors.ENDC}")
        
        if failed > 0:
            report.append(f"   {Colors.FAIL}• Critical issues detected - investigate failed tests{Colors.ENDC}")
        
        if warnings > 0:
            report.append(f"   {Colors.WARNING}• Review warnings for potential improvements{Colors.ENDC}")
        
        if success_rate == 100:
            report.append(f"   {Colors.OKGREEN}• Proxy configuration looks excellent!{Colors.ENDC}")
        elif success_rate >= 90:
            report.append(f"   {Colors.OKGREEN}• Proxy configuration is solid with minor issues{Colors.ENDC}")
        else:
            report.append(f"   {Colors.FAIL}• Proxy configuration needs attention{Colors.ENDC}")
        
        # Configurazione testata
        report.append(f"\n🔧 {Colors.BOLD}Configuration Tested:{Colors.ENDC}")
        report.append(f"   Proxy: {self.config['proxy_host']}:{self.config['proxy_port']}")
        report.append(f"   Database: {self.config['db_name']} as {self.config['db_user']}")
        report.append(f"   SSL Mode: {self.config['ssl_mode']}")
        report.append(f"   Tailscale: {self.config['tailscale_ip']}")
        
        report_text = "\n".join(report)
        
        # Salva report su file
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_file = f"proxy_test_report_{timestamp}.json"
        
        with open(report_file, 'w') as f:
            json.dump(self.results, f, indent=2)
        
        report_text += f"\n\n📄 Detailed report saved to: {report_file}\n"
        
        return report_text

    def run_all_tests(self):
        """Esegue tutti i test in sequenza"""
        print(f"{Colors.BOLD}{Colors.HEADER}NINVENDO PostgreSQL Proxy Test Suite{Colors.ENDC}")
        print(f"{Colors.OKCYAN}Testing proxy at {self.config['proxy_host']}:{self.config['proxy_port']}{Colors.ENDC}\n")
        
        # Lista test da eseguire
        tests = [
            ("Basic Connectivity", self.test_basic_connectivity),
            ("SSL Certificate", self.test_ssl_certificate),
            ("PostgreSQL Connection", self.test_postgresql_connection),
            ("Performance Metrics", self.test_performance_metrics),
            ("Security Checks", self.test_security_checks),
            ("Failover & Resilience", self.test_failover_resilience),
            ("Tailscale Connectivity", self.test_tailscale_connectivity),
            ("Monitoring Endpoints", self.test_monitoring_endpoints)
        ]
        
        start_time = time.time()
        
        # Esegui tutti i test
        for test_name, test_func in tests:
            try:
                test_func()
            except KeyboardInterrupt:
                print(f"\n{Colors.WARNING}Test interrupted by user{Colors.ENDC}")
                break
            except Exception as e:
                self.print_test(test_name, "FAIL", f"Unexpected error: {e}")
                self.record_test(test_name.lower().replace(' ', '_'), False, {"unexpected_error": str(e)})
        
        total_time = time.time() - start_time
        
        # Genera e mostra report
        print(self.generate_report())
        print(f"⏱️  Total test time: {total_time:.2f} seconds")


def main():
    """Funzione principale"""
    import argparse
    
    parser = argparse.ArgumentParser(description='NINVENDO PostgreSQL Proxy Test Suite')
    parser.add_argument('--proxy-host', help='Proxy hostname')
    parser.add_argument('--proxy-port', type=int, help='Proxy port')
    parser.add_argument('--db-name', help='Database name')
    parser.add_argument('--db-user', help='Database user')
    parser.add_argument('--db-password', help='Database password')
    parser.add_argument('--ssl-mode', help='SSL mode (disable, require, verify-ca, verify-full)')
    parser.add_argument('--tailscale-ip', help='Tailscale IP address')
    parser.add_argument('--stunnel-port', type=int, help='Stunnel port (if different from proxy port)')
    parser.add_argument('--timeout', type=int, help='Test timeout in seconds')
    parser.add_argument('--config-file', help='Load configuration from JSON file')
    parser.add_argument('--test-only', nargs='+', help='Run only specific tests', 
                       choices=['connectivity', 'ssl', 'postgresql', 'performance', 
                               'security', 'failover', 'tailscale', 'monitoring'])
    parser.add_argument('--verbose', '-v', action='store_true', help='Verbose output')
    
    args = parser.parse_args()
    
    # Crea tester
    tester = ProxyTester()
    
    # Override configurazione da argomenti
    if args.proxy_host:
        tester.config['proxy_host'] = args.proxy_host
    if args.proxy_port:
        tester.config['proxy_port'] = args.proxy_port
    if args.db_name:
        tester.config['db_name'] = args.db_name
    if args.db_user:
        tester.config['db_user'] = args.db_user
    if args.db_password:
        tester.config['db_password'] = args.db_password
    if args.ssl_mode:
        tester.config['ssl_mode'] = args.ssl_mode
    if args.tailscale_ip:
        tester.config['tailscale_ip'] = args.tailscale_ip
    if args.stunnel_port:
        tester.config['stunnel_port'] = args.stunnel_port
    if args.timeout:
        tester.config['test_timeout'] = args.timeout
    
    # Carica configurazione da file se specificato
    if args.config_file:
        try:
            with open(args.config_file, 'r') as f:
                file_config = json.load(f)
                tester.config.update(file_config)
        except Exception as e:
            print(f"{Colors.FAIL}Error loading config file: {e}{Colors.ENDC}")
            sys.exit(1)
    
    # Verifica configurazione minima
    required_config = ['proxy_host', 'db_name', 'db_user', 'db_password']
    missing_config = [key for key in required_config if not tester.config[key]]
    
    if missing_config:
        print(f"{Colors.FAIL}Missing required configuration: {', '.join(missing_config)}{Colors.ENDC}")
        print(f"{Colors.OKCYAN}Set environment variables or use command line arguments{Colors.ENDC}")
        print(f"{Colors.OKCYAN}Example: export DB_PASSWORD='your_password'{Colors.ENDC}")
        sys.exit(1)
    
    # Esegui test specifici se richiesto
    if args.test_only:
        test_mapping = {
            'connectivity': tester.test_basic_connectivity,
            'ssl': tester.test_ssl_certificate,
            'postgresql': tester.test_postgresql_connection,
            'performance': tester.test_performance_metrics,
            'security': tester.test_security_checks,
            'failover': tester.test_failover_resilience,
            'tailscale': tester.test_tailscale_connectivity,
            'monitoring': tester.test_monitoring_endpoints
        }
        
        print(f"{Colors.BOLD}{Colors.HEADER}Running specific tests: {', '.join(args.test_only)}{Colors.ENDC}\n")
        
        for test_name in args.test_only:
            if test_name in test_mapping:
                test_mapping[test_name]()
        
        print(tester.generate_report())
    else:
        # Esegui tutti i test
        tester.run_all_tests()


if __name__ == "__main__":
    main()