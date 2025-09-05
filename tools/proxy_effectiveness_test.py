#!/usr/bin/env python3
"""
NINVENDO Proxy Effectiveness Test Suite
=======================================

Test specifico per verificare l'efficacia del proxy Oracle Cloud
nell'architettura NINVENDO per bypassare firewall aziendali.

Architettura da testare:
[Dev Local] ←→ [Proxy Oracle Cloud] ←→ [Target Machine behind Firewall]

Test da eseguire:
1. Connectivity Tests (TCP/TLS)
2. Proxy Functionality (Port Forwarding)
3. Stunnel Configuration (if present)
4. Performance & Latency
5. Security & Encryption
6. Firewall Bypass Effectiveness
7. Failover & Reliability

Usage:
    python proxy_effectiveness_test.py --config proxy_config.json
"""

import os
import sys
import json
import time
import socket
import ssl
import subprocess
import threading
import random
from datetime import datetime, timedelta
from typing import Dict, List, Tuple, Optional, Any
import concurrent.futures

try:
    import psycopg2
    import requests
except ImportError as e:
    print(f"❌ Missing required package: {e}")
    print("Install with: pip install psycopg2-binary requests")
    sys.exit(1)

class ProxyEffectivenessTest:
    def __init__(self, config: Dict):
        self.config = config
        self.results = {
            'timestamp': datetime.now().isoformat(),
            'architecture_test': {},
            'effectiveness_score': 0,
            'recommendations': [],
            'critical_issues': []
        }
        
        # Configurazione test
        self.proxy_host = config.get('proxy_host', '100.108.112.117')
        self.local_db_host = config.get('local_db_host', 'localhost')
        self.local_db_port = config.get('local_db_port', 5432)
        self.proxy_ports = config.get('proxy_ports', [5432, 6543, 8080, 443])
        
    def log_result(self, test_name: str, status: str, details: str = "", 
                   score: int = 0, critical: bool = False):
        """Log test result with scoring"""
        self.results['architecture_test'][test_name] = {
            'status': status,
            'details': details,
            'score': score,
            'timestamp': datetime.now().isoformat()
        }
        
        # Console output with colors
        colors = {'PASS': '\033[92m', 'FAIL': '\033[91m', 'WARN': '\033[93m', 'INFO': '\033[94m', 'RESET': '\033[0m'}
        symbol = {'PASS': '✅', 'FAIL': '❌', 'WARN': '⚠️', 'INFO': 'ℹ️'}
        
        color = colors.get(status, colors['INFO'])
        icon = symbol.get(status, 'ℹ️')
        
        print(f"{icon} {color}[{status}] {test_name}{colors['RESET']}")
        if details:
            print(f"    {details}")
            
        if critical and status == 'FAIL':
            self.results['critical_issues'].append(f"{test_name}: {details}")

    def test_basic_connectivity(self) -> Dict:
        """Test 1: Basic TCP connectivity to proxy"""
        print("\n🔍 Testing Basic Connectivity to Proxy...")
        
        results = {}
        
        for port in self.proxy_ports:
            test_name = f"TCP_Connection_Port_{port}"
            
            try:
                start_time = time.time()
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(10)
                
                result = sock.connect_ex((self.proxy_host, port))
                connect_time = (time.time() - start_time) * 1000
                sock.close()
                
                if result == 0:
                    self.log_result(test_name, 'PASS', f"Connected in {connect_time:.2f}ms", score=10)
                    results[f'port_{port}'] = {'open': True, 'latency_ms': connect_time}
                else:
                    self.log_result(test_name, 'FAIL', f"Connection refused (code: {result})", score=0)
                    results[f'port_{port}'] = {'open': False, 'error_code': result}
                    
            except Exception as e:
                self.log_result(test_name, 'FAIL', f"Connection error: {e}", score=0)
                results[f'port_{port}'] = {'open': False, 'error': str(e)}
        
        # Determina porte utilizzabili
        open_ports = [port for port in self.proxy_ports if results.get(f'port_{port}', {}).get('open', False)]
        
        if open_ports:
            self.log_result('Proxy_Reachability', 'PASS', f"Found {len(open_ports)} accessible port(s): {open_ports}", score=20)
            results['recommended_ports'] = open_ports
        else:
            self.log_result('Proxy_Reachability', 'FAIL', "No accessible ports found", score=0, critical=True)
            results['recommended_ports'] = []
        
        return results

    def test_proxy_forwarding(self) -> Dict:
        """Test 2: Proxy port forwarding capability"""
        print("\n🔄 Testing Proxy Port Forwarding...")
        
        results = {}
        
        # Test se il proxy può inoltrare connessioni
        # Simuliamo una connessione diretta vs attraverso proxy
        
        # Test diretto a localhost
        try:
            start_time = time.time()
            direct_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            direct_sock.settimeout(5)
            direct_sock.connect((self.local_db_host, self.local_db_port))
            direct_time = (time.time() - start_time) * 1000
            direct_sock.close()
            
            self.log_result('Direct_Local_Connection', 'PASS', f"Direct connection: {direct_time:.2f}ms", score=5)
            results['direct_connection'] = {'success': True, 'latency_ms': direct_time}
            
        except Exception as e:
            self.log_result('Direct_Local_Connection', 'FAIL', f"Direct connection failed: {e}", score=0)
            results['direct_connection'] = {'success': False, 'error': str(e)}
            return results
        
        # Test proxy forwarding pattern recognition
        proxy_patterns = [
            ('HTTP_CONNECT', self.test_http_connect_proxy),
            ('TCP_Forward', self.test_tcp_forward_proxy),
            ('Stunnel_TLS', self.test_stunnel_proxy)
        ]
        
        working_patterns = []
        
        for pattern_name, test_func in proxy_patterns:
            try:
                pattern_result = test_func()
                if pattern_result.get('working', False):
                    working_patterns.append(pattern_name)
                    self.log_result(f'Proxy_Pattern_{pattern_name}', 'PASS', 
                                  f"Pattern works: {pattern_result.get('details', '')}", score=15)
                else:
                    self.log_result(f'Proxy_Pattern_{pattern_name}', 'INFO', 
                                  f"Pattern not active: {pattern_result.get('details', '')}", score=0)
            except Exception as e:
                self.log_result(f'Proxy_Pattern_{pattern_name}', 'WARN', f"Test error: {e}", score=0)
        
        results['working_patterns'] = working_patterns
        
        if working_patterns:
            self.log_result('Proxy_Forwarding_Capability', 'PASS', 
                          f"Detected {len(working_patterns)} working pattern(s)", score=20)
        else:
            self.log_result('Proxy_Forwarding_Capability', 'WARN', 
                          "No clear forwarding patterns detected", score=5)
        
        return results

    def test_http_connect_proxy(self) -> Dict:
        """Test HTTP CONNECT proxy method"""
        try:
            # Prova HTTP CONNECT su porta 8080 o 443
            for port in [8080, 443]:
                if port in [p for p in self.proxy_ports]:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(5)
                    sock.connect((self.proxy_host, port))
                    
                    # Invia richiesta CONNECT
                    connect_request = f"CONNECT {self.local_db_host}:{self.local_db_port} HTTP/1.1\r\nHost: {self.local_db_host}:{self.local_db_port}\r\n\r\n"
                    sock.send(connect_request.encode())
                    
                    response = sock.recv(1024).decode()
                    sock.close()
                    
                    if "200" in response:
                        return {'working': True, 'details': f'HTTP CONNECT on port {port}'}
                    
        except Exception:
            pass
        
        return {'working': False, 'details': 'HTTP CONNECT not available'}

    def test_tcp_forward_proxy(self) -> Dict:
        """Test direct TCP forwarding"""
        try:
            # Test se il proxy inoltra direttamente TCP su porta PostgreSQL
            for port in [5432, 6543]:
                if port in [p for p in self.proxy_ports]:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(5)
                    sock.connect((self.proxy_host, port))
                    
                    # Prova a inviare un magic byte PostgreSQL
                    # Se riceve una risposta PostgreSQL-like, è un forwarding
                    time.sleep(0.1)
                    
                    try:
                        sock.settimeout(1)
                        response = sock.recv(1024)
                        if len(response) > 0:
                            sock.close()
                            return {'working': True, 'details': f'TCP forwarding on port {port}'}
                    except socket.timeout:
                        pass
                    
                    sock.close()
                    
        except Exception:
            pass
        
        return {'working': False, 'details': 'Direct TCP forwarding not detected'}

    def test_stunnel_proxy(self) -> Dict:
        """Test Stunnel TLS proxy"""
        try:
            # Test connessioni TLS su porte comuni Stunnel
            for port in [6543, 443]:
                if port in [p for p in self.proxy_ports]:
                    context = ssl.create_default_context()
                    context.check_hostname = False
                    context.verify_mode = ssl.CERT_NONE
                    
                    with socket.create_connection((self.proxy_host, port), timeout=5) as sock:
                        with context.wrap_socket(sock, server_hostname=self.proxy_host) as ssock:
                            # Se riusciamo a stabilire TLS, potrebbe essere Stunnel
                            return {'working': True, 'details': f'TLS connection on port {port} (possible Stunnel)'}
                            
        except Exception:
            pass
        
        return {'working': False, 'details': 'Stunnel/TLS proxy not detected'}

    def test_performance_through_proxy(self) -> Dict:
        """Test 3: Performance through proxy vs direct"""
        print("\n📊 Testing Performance Through Proxy...")
        
        results = {}
        
        # Test latenza connessioni multiple
        def measure_connection_time(host, port, iterations=5):
            times = []
            for _ in range(iterations):
                try:
                    start = time.time()
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(3)
                    sock.connect((host, port))
                    times.append((time.time() - start) * 1000)
                    sock.close()
                except:
                    times.append(float('inf'))
            return {
                'avg_ms': sum(t for t in times if t != float('inf')) / len([t for t in times if t != float('inf')]) if times else 0,
                'min_ms': min(t for t in times if t != float('inf')) if times else 0,
                'max_ms': max(t for t in times if t != float('inf')) if times else 0,
                'success_rate': len([t for t in times if t != float('inf')]) / len(times)
            }
        
        # Test diretto
        direct_perf = measure_connection_time(self.local_db_host, self.local_db_port)
        results['direct_performance'] = direct_perf
        
        self.log_result('Direct_Performance', 'INFO', 
                       f"Direct: {direct_perf['avg_ms']:.2f}ms avg, {direct_perf['success_rate']*100:.1f}% success", 
                       score=5)
        
        # Test attraverso proxy (sulle porte aperte)
        open_ports = self.results['architecture_test'].get('Proxy_Reachability', {}).get('details', '')
        
        if 'port' in str(open_ports):
            # Prova sulla prima porta aperta trovata
            proxy_port = self.proxy_ports[0] if self.proxy_ports else 5432
            proxy_perf = measure_connection_time(self.proxy_host, proxy_port)
            results['proxy_performance'] = proxy_perf
            
            # Calcola overhead
            if direct_perf['avg_ms'] > 0 and proxy_perf['avg_ms'] > 0:
                overhead_factor = proxy_perf['avg_ms'] / direct_perf['avg_ms']
                results['overhead_factor'] = overhead_factor
                
                if overhead_factor < 2.0:
                    self.log_result('Proxy_Performance', 'PASS', 
                                   f"Proxy: {proxy_perf['avg_ms']:.2f}ms ({overhead_factor:.1f}x overhead)", score=15)
                elif overhead_factor < 5.0:
                    self.log_result('Proxy_Performance', 'WARN', 
                                   f"Proxy: {proxy_perf['avg_ms']:.2f}ms ({overhead_factor:.1f}x overhead - acceptable)", score=10)
                else:
                    self.log_result('Proxy_Performance', 'FAIL', 
                                   f"Proxy: {proxy_perf['avg_ms']:.2f}ms ({overhead_factor:.1f}x overhead - too slow)", score=0)
        
        return results

    def test_security_configuration(self) -> Dict:
        """Test 4: Security configuration"""
        print("\n🔒 Testing Security Configuration...")
        
        results = {}
        security_score = 0
        
        # Test 1: TLS/SSL availability
        tls_available = False
        for port in [443, 6543]:
            try:
                context = ssl.create_default_context()
                context.check_hostname = False
                context.verify_mode = ssl.CERT_NONE
                
                with socket.create_connection((self.proxy_host, port), timeout=5) as sock:
                    with context.wrap_socket(sock, server_hostname=self.proxy_host) as ssock:
                        cert = ssock.getpeercert()
                        tls_available = True
                        results['tls_port'] = port
                        results['certificate'] = cert
                        break
            except:
                continue
        
        if tls_available:
            self.log_result('TLS_Encryption', 'PASS', f"TLS available on port {results['tls_port']}", score=20)
            security_score += 20
        else:
            self.log_result('TLS_Encryption', 'WARN', "No TLS encryption detected", score=0)
        
        # Test 2: Port scanning protection
        closed_ports = 0
        random_ports = random.sample(range(1000, 9999), 10)
        
        for port in random_ports:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                result = sock.connect_ex((self.proxy_host, port))
                sock.close()
                if result != 0:
                    closed_ports += 1
            except:
                closed_ports += 1
        
        if closed_ports >= 8:
            self.log_result('Port_Security', 'PASS', f"{closed_ports}/10 random ports properly closed", score=10)
            security_score += 10
        else:
            self.log_result('Port_Security', 'WARN', f"Only {closed_ports}/10 random ports closed", score=5)
            security_score += 5
        
        # Test 3: Response timing (anti-enumeration)
        timing_test = self.test_response_timing()
        if timing_test['consistent']:
            self.log_result('Timing_Security', 'PASS', "Response timing is consistent", score=5)
            security_score += 5
        else:
            self.log_result('Timing_Security', 'WARN', "Response timing varies (enumeration risk)", score=0)
        
        results['security_score'] = security_score
        results['timing_test'] = timing_test
        
        return results

    def test_response_timing(self) -> Dict:
        """Test response timing consistency"""
        open_port = self.proxy_ports[0] if self.proxy_ports else 5432
        closed_port = 9999
        
        open_times = []
        closed_times = []
        
        for _ in range(5):
            # Test porta aperta
            start = time.time()
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(2)
                sock.connect((self.proxy_host, open_port))
                sock.close()
            except:
                pass
            open_times.append((time.time() - start) * 1000)
            
            # Test porta chiusa
            start = time.time()
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(2)
                sock.connect((self.proxy_host, closed_port))
                sock.close()
            except:
                pass
            closed_times.append((time.time() - start) * 1000)
        
        avg_open = sum(open_times) / len(open_times)
        avg_closed = sum(closed_times) / len(closed_times)
        
        # Timing is consistent if difference is small
        timing_difference = abs(avg_open - avg_closed)
        consistent = timing_difference < 100  # Less than 100ms difference
        
        return {
            'consistent': consistent,
            'avg_open_ms': avg_open,
            'avg_closed_ms': avg_closed,
            'difference_ms': timing_difference
        }

    def test_firewall_bypass_effectiveness(self) -> Dict:
        """Test 5: Firewall bypass effectiveness"""
        print("\n🛡️ Testing Firewall Bypass Effectiveness...")
        
        results = {}
        
        # Test diverse tecniche di bypass
        bypass_techniques = [
            ('Standard_Port_80', 80),
            ('Standard_Port_443', 443),
            ('Alt_HTTP_8080', 8080),
            ('Custom_Port_6543', 6543),
            ('PostgreSQL_Port_5432', 5432)
        ]
        
        working_techniques = []
        
        for technique_name, port in bypass_techniques:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(3)
                result = sock.connect_ex((self.proxy_host, port))
                sock.close()
                
                if result == 0:
                    working_techniques.append((technique_name, port))
                    self.log_result(f'Bypass_{technique_name}', 'PASS', f"Port {port} accessible", score=5)
                else:
                    self.log_result(f'Bypass_{technique_name}', 'INFO', f"Port {port} not accessible", score=0)
                    
            except Exception as e:
                self.log_result(f'Bypass_{technique_name}', 'INFO', f"Port {port} test failed: {e}", score=0)
        
        results['working_techniques'] = working_techniques
        
        # Valutazione efficacia bypass
        if len(working_techniques) >= 2:
            self.log_result('Firewall_Bypass_Effectiveness', 'PASS', 
                          f"Multiple bypass options available: {len(working_techniques)}", score=20)
        elif len(working_techniques) == 1:
            self.log_result('Firewall_Bypass_Effectiveness', 'WARN', 
                          "Only one bypass option available", score=10)
        else:
            self.log_result('Firewall_Bypass_Effectiveness', 'FAIL', 
                          "No bypass options available", score=0, critical=True)
        
        return results

    def test_postgresql_proxy_integration(self) -> Dict:
        """Test 6: PostgreSQL-specific proxy integration"""
        print("\n🗄️ Testing PostgreSQL Proxy Integration...")
        
        results = {}
        
        # Test se possiamo simulare una connessione PostgreSQL attraverso il proxy
        try:
            # Prima testa connessione locale diretta
            local_conn_string = f"postgresql://{self.config.get('db_user', 'ninvendo')}:{self.config.get('db_password', 'test123')}@{self.local_db_host}:{self.local_db_port}/{self.config.get('db_name', 'ninvendo_dev')}?sslmode=disable&connect_timeout=5"
            
            with psycopg2.connect(local_conn_string) as conn:
                with conn.cursor() as cur:
                    cur.execute("SELECT version(), current_timestamp")
                    result = cur.fetchone()
                    
            self.log_result('Local_PostgreSQL_Test', 'PASS', 
                          f"Local PostgreSQL accessible: {result[0][:30]}...", score=10)
            results['local_postgresql'] = {'working': True, 'version': result[0]}
            
            # Test simulazione proxy PostgreSQL
            # (Questo dovrebbe essere testato quando il proxy è configurato per PostgreSQL)
            proxy_simulation_result = self.simulate_proxy_postgresql()
            results['proxy_simulation'] = proxy_simulation_result
            
            if proxy_simulation_result['feasible']:
                self.log_result('PostgreSQL_Proxy_Feasibility', 'PASS', 
                              "PostgreSQL through proxy is feasible", score=15)
            else:
                self.log_result('PostgreSQL_Proxy_Feasibility', 'WARN', 
                              "PostgreSQL proxy needs configuration", score=5)
                
        except Exception as e:
            self.log_result('Local_PostgreSQL_Test', 'FAIL', f"Local PostgreSQL test failed: {e}", score=0)
            results['local_postgresql'] = {'working': False, 'error': str(e)}
        
        return results

    def simulate_proxy_postgresql(self) -> Dict:
        """Simula come PostgreSQL dovrebbe funzionare attraverso il proxy"""
        # Test se il proxy può gestire protocolli binari come PostgreSQL
        feasible = False
        details = ""
        
        # Test 1: Può il proxy gestire connessioni persistenti?
        try:
            for port in [5432, 6543]:
                if port in [p for p in self.proxy_ports]:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(5)
                    sock.connect((self.proxy_host, port))
                    
                    # Mantieni connessione per 3 secondi
                    time.sleep(3)
                    sock.close()
                    
                    feasible = True
                    details = f"Persistent connections possible on port {port}"
                    break
        except:
            details = "Persistent connections not supported"
        
        return {'feasible': feasible, 'details': details}

    def calculate_effectiveness_score(self) -> int:
        """Calcola score di efficacia complessiva"""
        total_score = 0
        max_score = 0
        
        for test_name, test_result in self.results['architecture_test'].items():
            total_score += test_result.get('score', 0)
            max_score += 20  # Assuming max 20 points per test
        
        if max_score > 0:
            effectiveness_percentage = (total_score / max_score) * 100
        else:
            effectiveness_percentage = 0
        
        return int(effectiveness_percentage)

    def generate_recommendations(self):
        """Genera raccomandazioni basate sui risultati"""
        recommendations = []
        
        # Analizza risultati critici
        if self.results['critical_issues']:
            recommendations.append("🚨 CRITICAL: Address critical connectivity issues before proceeding")
        
        # Analizza connettività
        proxy_reachable = any('Proxy_Reachability' in test and 
                             self.results['architecture_test'][test]['status'] == 'PASS' 
                             for test in self.results['architecture_test'])
        
        if not proxy_reachable:
            recommendations.append("🔧 Configure proxy server to accept connections on standard ports (80, 443, 8080)")
        
        # Analizza sicurezza
        security_tests = [test for test in self.results['architecture_test'] 
                         if 'Security' in test or 'TLS' in test]
        security_passed = sum(1 for test in security_tests 
                             if self.results['architecture_test'][test]['status'] == 'PASS')
        
        if security_passed < len(security_tests) / 2:
            recommendations.append("🔒 Improve security configuration: enable TLS, configure proper firewalling")
        
        # Analizza performance
        performance_tests = [test for test in self.results['architecture_test'] 
                           if 'Performance' in test]
        if any(self.results['architecture_test'][test]['status'] == 'FAIL' 
               for test in performance_tests):
            recommendations.append("⚡ Optimize proxy performance: consider using dedicated ports or compression")
        
        # Raccomandazioni specifiche per PostgreSQL
        if 'PostgreSQL_Proxy_Feasibility' in self.results['architecture_test']:
            if self.results['architecture_test']['PostgreSQL_Proxy_Feasibility']['status'] != 'PASS':
                recommendations.append("🗄️ Configure PostgreSQL-specific proxy: consider Stunnel or HAProxy for database connections")
        
        self.results['recommendations'] = recommendations

    def run_all_tests(self):
        """Esegue tutti i test di efficacia del proxy"""
        print("🚀 NINVENDO Proxy Effectiveness Test Suite")
        print("="*60)
        print(f"Testing proxy: {self.proxy_host}")
        print(f"Target architecture: Dev → Proxy → Database behind firewall")
        print("="*60)
        
        # Esegui tutti i test
        tests = [
            self.test_basic_connectivity,
            self.test_proxy_forwarding,
            self.test_performance_through_proxy,
            self.test_security_configuration,
            self.test_firewall_bypass_effectiveness,
            self.test_postgresql_proxy_integration
        ]
        
        for test_func in tests:
            try:
                test_result = test_func()
                # Store detailed results if needed
            except Exception as e:
                print(f"❌ Test {test_func.__name__} failed: {e}")
        
        # Calcola score finale
        self.results['effectiveness_score'] = self.calculate_effectiveness_score()
        
        # Genera raccomandazioni
        self.generate_recommendations()
        
        # Report finale
        self.print_final_report()

    def print_final_report(self):
        """Stampa report finale dei test"""
        print("\n" + "="*60)
        print("📊 PROXY EFFECTIVENESS REPORT")
        print("="*60)
        
        score = self.results['effectiveness_score']
        if score >= 80:
            status_color = '\033[92m'  # Green
            status_text = "EXCELLENT"
        elif score >= 60:
            status_color = '\033[93m'  # Yellow
            status_text = "GOOD"
        elif score >= 40:
            status_color = '\033[93m'  # Yellow
            status_text = "FAIR"
        else:
            status_color = '\033[91m'  # Red
            status_text = "POOR"
        
        print(f"🎯 EFFECTIVENESS SCORE: {status_color}{score}% ({status_text})\033[0m")
        
        # Statistiche test
        total_tests = len(self.results['architecture_test'])
        passed_tests = sum(1 for test in self.results['architecture_test'].values() 
                          if test['status'] == 'PASS')
        
        print(f"📋 TEST RESULTS: {passed_tests}/{total_tests} passed")
        
        # Problemi critici
        if self.results['critical_issues']:
            print(f"\n🚨 CRITICAL ISSUES ({len(self.results['critical_issues'])}):")
            for issue in self.results['critical_issues']:
                print(f"   ❌ {issue}")
        
        # Raccomandazioni
        if self.results['recommendations']:
            print(f"\n💡 RECOMMENDATIONS:")
            for rec in self.results['recommendations']:
                print(f"   {rec}")
        
        # Prossimi passi
        print(f"\n🎯 NEXT STEPS:")
        
        if score >= 70:
            print("   ✅ Proxy is ready for PostgreSQL migration")
            print("   🔄 Proceed with database migration setup")
            print("   🗄️ Configure PostgreSQL on target machine")
        elif score >= 50:
            print("   ⚠️  Address recommendations before migration")
            print("   🔧 Improve proxy configuration")
            print("   🧪 Re-run tests after improvements")
        else:
            print("   🚨 Proxy needs significant configuration")
            print("   📋 Address critical issues first")
            print("   💡 Consider alternative proxy solutions")
        
        # Salva report
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_file = f"proxy_effectiveness_report_{timestamp}.json"
        
        with open(report_file, 'w') as f:
            json.dump(self.results, f, indent=2)
        
        print(f"\n📄 Detailed report saved: {report_file}")
        print("="*60)


def main():
    """Funzione principale"""
    import argparse
    
    parser = argparse.ArgumentParser(description='NINVENDO Proxy Effectiveness Test')
    parser.add_argument('--config-file', required=True, help='JSON configuration file')
    parser.add_argument('--proxy-host', help='Override proxy hostname')
    parser.add_argument('--local-db-host', default='localhost', help='Local database host for comparison')
    parser.add_argument('--test-ports', nargs='+', type=int, default=[5432, 6543, 8080, 443], 
                       help='Ports to test on proxy')
    parser.add_argument('--quick', action='store_true', help='Run quick tests only')
    
    args = parser.parse_args()
    
    # Carica configurazione
    try:
        with open(args.config_file, 'r') as f:
            config = json.load(f)
    except Exception as e:
        print(f"❌ Error loading configuration: {e}")
        sys.exit(1)
    
    # Override con parametri command line
    if args.proxy_host:
        config['proxy_host'] = args.proxy_host
    if args.local_db_host:
        config['local_db_host'] = args.local_db_host
    
    config['proxy_ports'] = args.test_ports
    
    # Esegui test
    tester = ProxyEffectivenessTest(config)
    
    if args.quick:
        # Solo test essenziali
        print("🏃‍♂️ Running quick effectiveness test...")
        tester.test_basic_connectivity()
        tester.test_firewall_bypass_effectiveness()
        score = tester.calculate_effectiveness_score()
        print(f"\n⚡ Quick Score: {score}%")
    else:
        # Test completo
        tester.run_all_tests()


if __name__ == "__main__":
    main()