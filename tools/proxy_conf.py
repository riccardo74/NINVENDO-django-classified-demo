#!/usr/bin/env python3
"""
NINVENDO Proxy Configuration Helper
==================================

Script per aiutare a configurare il proxy Oracle Cloud per bypassare
firewall aziendali e permettere connessioni PostgreSQL.

Scenario:
- Macchina W11 dietro firewall aziendale (porta 5432 bloccata)
- Proxy Oracle Cloud su Tailscale (100.108.112.117)
- Connessioni da Render e macchine di sviluppo

Genera configurazioni per:
- Stunnel (TLS tunneling)
- HAProxy (HTTP/TCP proxy)
- SSH tunneling
- Socat (simple relay)
"""

import os
import sys
import json
from datetime import datetime
from pathlib import Path

class ProxyConfigGenerator:
    def __init__(self):
        self.config_templates = {}
        
    def generate_stunnel_config(self, target_host: str, target_port: int = 5432, 
                               listen_port: int = 6543) -> str:
        """Genera configurazione Stunnel per PostgreSQL"""
        
        config = f"""# NINVENDO Stunnel Configuration
# Generated on {datetime.now()}
# Purpose: TLS tunnel for PostgreSQL through firewall

# Global settings
cert = /etc/stunnel/ninvendo.crt
key = /etc/stunnel/ninvendo.key
sslVersion = TLSv1.2

# Security options
options = NO_SSLv2
options = NO_SSLv3
options = CIPHER_SERVER_PREFERENCE
ciphers = ECDHE+AESGCM:ECDHE+CHACHA20:DHE+AESGCM:DHE+CHACHA20:!aNULL:!MD5:!DSS

# Logging
debug = 4
output = /var/log/stunnel/ninvendo.log

# Performance
socket = a:SO_REUSEADDR=1
socket = a:TCP_NODELAY=1

# Service configuration
[ninvendo-postgres]
accept = 0.0.0.0:{listen_port}
connect = {target_host}:{target_port}

# Client authentication (optional but recommended)
verify = 2
CAfile = /etc/stunnel/client-ca.crt

# Advanced options
sessionCacheSize = 1000
sessionCacheTimeout = 300
"""
        return config
    
    def generate_haproxy_config(self, target_host: str, target_port: int = 5432) -> str:
        """Genera configurazione HAProxy per PostgreSQL"""
        
        config = f"""# NINVENDO HAProxy Configuration
# Generated on {datetime.now()}
# Purpose: TCP proxy for PostgreSQL through firewall

global
    daemon
    user haproxy
    group haproxy
    chroot /var/lib/haproxy
    stats socket /run/haproxy/admin.sock mode 660 level admin
    stats timeout 30s
    log 127.0.0.1:514 local0

    # Security
    ssl-default-bind-ciphers ECDHE+AESGCM:ECDHE+CHACHA20:DHE+AESGCM:DHE+CHACHA20:!aNULL:!MD5:!DSS
    ssl-default-bind-options ssl-min-ver TLSv1.2 no-tls-tickets

defaults
    mode tcp
    log global
    timeout connect 5000ms
    timeout client 50000ms
    timeout server 50000ms
    option tcplog
    option log-health-checks

# Statistics interface
listen stats
    bind *:8404
    stats enable
    stats uri /stats
    stats refresh 30s
    stats admin if TRUE

# PostgreSQL proxy on standard port
frontend postgres_frontend_5432
    bind *:5432
    default_backend postgres_backend

# PostgreSQL proxy on alternative port
frontend postgres_frontend_6543
    bind *:6543
    default_backend postgres_backend

# PostgreSQL proxy on HTTP port (firewall bypass)
frontend postgres_frontend_80
    bind *:80
    default_backend postgres_backend

# PostgreSQL proxy on HTTPS port (firewall bypass)
frontend postgres_frontend_443
    bind *:443
    default_backend postgres_backend

# Backend PostgreSQL server
backend postgres_backend
    balance roundrobin
    option tcp-check
    tcp-check connect
    server postgres1 {target_host}:{target_port} check inter 5s rise 2 fall 3

# Health check endpoint
frontend health_check
    bind *:8080
    http-request return status 200 content-type text/plain string "NINVENDO Proxy OK"
"""
        return config
    
    def generate_ssh_tunnel_script(self, target_host: str, target_port: int = 5432,
                                  local_ports: list = [5432, 6543, 8080]) -> str:
        """Genera script SSH tunneling"""
        
        script = f"""#!/bin/bash
# NINVENDO SSH Tunnel Script
# Generated on {datetime.now()}
# Purpose: SSH tunnels for PostgreSQL through firewall

set -euo pipefail

TARGET_HOST="{target_host}"
TARGET_PORT={target_port}
SSH_USER="${{SSH_USER:-ubuntu}}"
SSH_KEY="${{SSH_KEY:-~/.ssh/id_rsa}}"

# Colors for output
RED='\\033[0;31m'
GREEN='\\033[0;32m'
YELLOW='\\033[1;33m'
NC='\\033[0m' # No Color

log_info() {{
    echo -e "${{GREEN}}[INFO]${{NC}} $1"
}}

log_warn() {{
    echo -e "${{YELLOW}}[WARN]${{NC}} $1"
}}

log_error() {{
    echo -e "${{RED}}[ERROR]${{NC}} $1"
}}

# Check if target is reachable via Tailscale
check_target() {{
    log_info "Checking target host $TARGET_HOST..."
    if ping -c 1 -W 5 "$TARGET_HOST" >/dev/null 2>&1; then
        log_info "Target host is reachable"
        return 0
    else
        log_error "Target host is not reachable"
        return 1
    fi
}}

# Setup SSH tunnels
setup_tunnels() {{
    log_info "Setting up SSH tunnels..."
    
    # Kill existing tunnels
    pkill -f "ssh.*$TARGET_HOST" || true
    sleep 2
    
    # Create multiple tunnel endpoints for redundancy
"""
        
        for port in local_ports:
            script += f"""    
    # Tunnel on port {port}
    log_info "Creating tunnel: localhost:{port} -> $TARGET_HOST:$TARGET_PORT"
    ssh -fN -L {port}:$TARGET_HOST:$TARGET_PORT \\
        -o StrictHostKeyChecking=no \\
        -o UserKnownHostsFile=/dev/null \\
        -o ServerAliveInterval=30 \\
        -o ServerAliveCountMax=3 \\
        -o ExitOnForwardFailure=yes \\
        -i "$SSH_KEY" \\
        "$SSH_USER@$TARGET_HOST" || log_warn "Failed to create tunnel on port {port}"
"""
        
        script += f"""
    sleep 2
    
    # Verify tunnels
    log_info "Verifying tunnels..."
    for port in {' '.join(map(str, local_ports))}; do
        if netstat -ln | grep ":$port " >/dev/null; then
            log_info "Tunnel on port $port is active"
        else
            log_warn "Tunnel on port $port failed"
        fi
    done
}}

# Monitor tunnels
monitor_tunnels() {{
    log_info "Monitoring tunnels (Ctrl+C to stop)..."
    while true; do
        for port in {' '.join(map(str, local_ports))}; do
            if ! netstat -ln | grep ":$port " >/dev/null; then
                log_warn "Tunnel on port $port is down, attempting to restart..."
                ssh -fN -L $port:$TARGET_HOST:$TARGET_PORT \\
                    -o StrictHostKeyChecking=no \\
                    -o UserKnownHostsFile=/dev/null \\
                    -o ServerAliveInterval=30 \\
                    -o ServerAliveCountMax=3 \\
                    -o ExitOnForwardFailure=yes \\
                    -i "$SSH_KEY" \\
                    "$SSH_USER@$TARGET_HOST" || log_error "Failed to restart tunnel on port $port"
            fi
        done
        sleep 30
    done
}}

# Cleanup function
cleanup() {{
    log_info "Cleaning up tunnels..."
    pkill -f "ssh.*$TARGET_HOST" || true
    exit 0
}}

# Trap cleanup on exit
trap cleanup EXIT INT TERM

# Main execution
case "${{1:-start}}" in
    start)
        check_target && setup_tunnels && monitor_tunnels
        ;;
    stop)
        cleanup
        ;;
    status)
        log_info "Checking tunnel status..."
        for port in {' '.join(map(str, local_ports))}; do
            if netstat -ln | grep ":$port " >/dev/null; then
                log_info "Port $port: ACTIVE"
            else
                log_warn "Port $port: INACTIVE"
            fi
        done
        ;;
    *)
        echo "Usage: $0 {{start|stop|status}}"
        exit 1
        ;;
esac
"""
        return script
    
    def generate_socat_script(self, target_host: str, target_port: int = 5432) -> str:
        """Genera script Socat per relay semplice"""
        
        script = f"""#!/bin/bash
# NINVENDO Socat Relay Script
# Generated on {datetime.now()}
# Purpose: Simple TCP relay for PostgreSQL

set -euo pipefail

TARGET_HOST="{target_host}"
TARGET_PORT={target_port}

# Port mappings for firewall bypass
declare -A PORT_MAPPINGS=(
    ["5432"]="$TARGET_HOST:$TARGET_PORT"  # Direct PostgreSQL
    ["6543"]="$TARGET_HOST:$TARGET_PORT"  # Alternative port
    ["8080"]="$TARGET_HOST:$TARGET_PORT"  # HTTP bypass
    ["443"]="$TARGET_HOST:$TARGET_PORT"   # HTTPS bypass
)

# Start socat relays
start_relays() {{
    echo "Starting NINVENDO socat relays..."
    
    # Kill existing socat processes
    pkill socat || true
    sleep 2
    
    for local_port in "${{!PORT_MAPPINGS[@]}}"; do
        target="${{PORT_MAPPINGS[$local_port]}}"
        echo "Starting relay: 0.0.0.0:$local_port -> $target"
        
        socat TCP-LISTEN:$local_port,fork,reuseaddr TCP:$target &
        
        # Verify relay started
        sleep 1
        if netstat -ln | grep ":$local_port " >/dev/null; then
            echo "✅ Relay on port $local_port is active"
        else
            echo "❌ Failed to start relay on port $local_port"
        fi
    done
    
    echo "All relays started. Use 'pkill socat' to stop."
}}

# Status check
check_status() {{
    echo "NINVENDO Proxy Status:"
    for local_port in "${{!PORT_MAPPINGS[@]}}"; do
        if netstat -ln | grep ":$local_port " >/dev/null; then
            echo "Port $local_port: ACTIVE"
        else
            echo "Port $local_port: INACTIVE"
        fi
    done
}}

# Test connections
test_connections() {{
    echo "Testing proxy connections..."
    for local_port in "${{!PORT_MAPPINGS[@]}}"; do
        echo -n "Testing port $local_port... "
        if timeout 3 bash -c "</dev/tcp/localhost/$local_port"; then
            echo "OK"
        else
            echo "FAILED"
        fi
    done
}}

case "${{1:-start}}" in
    start)
        start_relays
        ;;
    status)
        check_status
        ;;
    test)
        test_connections
        ;;
    stop)
        pkill socat || true
        echo "All relays stopped"
        ;;
    *)
        echo "Usage: $0 {{start|stop|status|test}}"
        exit 1
        ;;
esac
"""
        return script
    
    def generate_docker_compose(self, target_host: str, target_port: int = 5432) -> str:
        """Genera Docker Compose per proxy containerizzato"""
        
        compose = f"""# NINVENDO Proxy Docker Compose
# Generated on {datetime.now()}
version: '3.8'

services:
  # HAProxy for TCP proxying
  haproxy:
    image: haproxy:2.4-alpine
    container_name: ninvendo-haproxy
    ports:
      - "5432:5432"   # PostgreSQL standard
      - "6543:6543"   # Alternative
      - "8080:8080"   # HTTP bypass
      - "443:443"     # HTTPS bypass
      - "8404:8404"   # Stats interface
    volumes:
      - ./haproxy.cfg:/usr/local/etc/haproxy/haproxy.cfg:ro
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "nc", "-z", "localhost", "8404"]
      interval: 30s
      timeout: 10s
      retries: 3
    networks:
      - ninvendo-net

  # Stunnel for TLS tunneling
  stunnel:
    image: dweomer/stunnel
    container_name: ninvendo-stunnel
    ports:
      - "6543:6543"   # TLS PostgreSQL
    volumes:
      - ./stunnel.conf:/etc/stunnel/stunnel.conf:ro
      - ./certs:/etc/stunnel/certs:ro
    restart: unless-stopped
    depends_on:
      - haproxy
    networks:
      - ninvendo-net

  # Monitoring with simple HTTP server
  monitor:
    image: nginx:alpine
    container_name: ninvendo-monitor
    ports:
      - "9090:80"
    volumes:
      - ./monitor.html:/usr/share/nginx/html/index.html:ro
    restart: unless-stopped
    networks:
      - ninvendo-net

networks:
  ninvendo-net:
    driver: bridge

# To deploy:
# 1. Save configurations to files
# 2. docker-compose up -d
# 3. Test with: docker-compose logs -f
"""
        return compose
    
    def generate_systemd_service(self, service_type: str = "socat") -> str:
        """Genera servizio systemd per il proxy"""
        
        service = f"""# NINVENDO Proxy Systemd Service
# Generated on {datetime.now()}
# Save as: /etc/systemd/system/ninvendo-proxy.service

[Unit]
Description=NINVENDO PostgreSQL Proxy Service
After=network.target
Wants=network.target

[Service]
Type=forking
User=ninvendo
Group=ninvendo
WorkingDirectory=/opt/ninvendo-proxy
ExecStart=/opt/ninvendo-proxy/start-proxy.sh
ExecStop=/opt/ninvendo-proxy/stop-proxy.sh
ExecReload=/bin/kill -HUP $MAINPID
Restart=always
RestartSec=10

# Security
NoNewPrivileges=true
PrivateTmp=true
ProtectSystem=strict
ProtectHome=true
ReadWritePaths=/opt/ninvendo-proxy

# Logging
StandardOutput=journal
StandardError=journal
SyslogIdentifier=ninvendo-proxy

[Install]
WantedBy=multi-user.target

# Installation commands:
# sudo systemctl daemon-reload
# sudo systemctl enable ninvendo-proxy
# sudo systemctl start ninvendo-proxy
# sudo systemctl status ninvendo-proxy
"""
        return service
    
    def generate_installation_script(self, target_host: str, proxy_type: str = "socat") -> str:
        """Genera script di installazione completo"""
        
        script = f"""#!/bin/bash
# NINVENDO Proxy Installation Script
# Generated on {datetime.now()}

set -euo pipefail

TARGET_HOST="{target_host}"
PROXY_TYPE="{proxy_type}"
INSTALL_DIR="/opt/ninvendo-proxy"
USER="ninvendo"

# Colors
RED='\\033[0;31m'
GREEN='\\033[0;32m'
YELLOW='\\033[1;33m'
BLUE='\\033[0;34m'
NC='\\033[0m'

log() {{ echo -e "${{GREEN}}[INFO]${{NC}} $1"; }}
warn() {{ echo -e "${{YELLOW}}[WARN]${{NC}} $1"; }}
error() {{ echo -e "${{RED}}[ERROR]${{NC}} $1"; }}

# Check if running as root
if [[ $EUID -ne 0 ]]; then
   error "This script must be run as root"
   exit 1
fi

# Create user
log "Creating ninvendo user..."
if ! id "$USER" &>/dev/null; then
    useradd -r -s /bin/bash -d "$INSTALL_DIR" "$USER"
    log "User $USER created"
else
    log "User $USER already exists"
fi

# Create installation directory
log "Creating installation directory..."
mkdir -p "$INSTALL_DIR"
chown "$USER:$USER" "$INSTALL_DIR"

# Install dependencies
log "Installing dependencies..."
apt-get update
case "$PROXY_TYPE" in
    "socat")
        apt-get install -y socat netcat-openbsd
        ;;
    "haproxy")
        apt-get install -y haproxy
        ;;
    "stunnel")
        apt-get install -y stunnel4 openssl
        ;;
    "ssh")
        apt-get install -y openssh-client
        ;;
    *)
        apt-get install -y socat haproxy stunnel4 openssh-client
        ;;
esac

# Configure firewall
log "Configuring firewall..."
ufw allow 5432/tcp comment "PostgreSQL direct"
ufw allow 6543/tcp comment "PostgreSQL alternative"
ufw allow 8080/tcp comment "HTTP bypass"
ufw allow 443/tcp comment "HTTPS bypass"
ufw allow 8404/tcp comment "HAProxy stats"

# Generate configurations
log "Generating proxy configurations..."
cd "$INSTALL_DIR"

# This script will generate the appropriate config files
# based on the proxy type selected

log "Installation completed!"
log "Next steps:"
log "1. Configure your target host details"
log "2. Test the proxy: sudo systemctl start ninvendo-proxy"
log "3. Check status: sudo systemctl status ninvendo-proxy"
log "4. View logs: sudo journalctl -u ninvendo-proxy -f"

warn "Remember to:"
warn "- Update firewall rules on Oracle Cloud"
warn "- Configure Tailscale on target machine"
warn "- Test connectivity from all endpoints"
"""
        return script
    
    def save_configurations(self, output_dir: str, target_host: str, 
                           target_port: int = 5432, config_type: str = "all"):
        """Salva tutte le configurazioni generate"""
        
        output_path = Path(output_dir)
        output_path.mkdir(exist_ok=True)
        
        configs = {}
        
        if config_type in ["all", "stunnel"]:
            configs["stunnel.conf"] = self.generate_stunnel_config(target_host, target_port)
        
        if config_type in ["all", "haproxy"]:
            configs["haproxy.cfg"] = self.generate_haproxy_config(target_host, target_port)
        
        if config_type in ["all", "ssh"]:
            configs["ssh-tunnel.sh"] = self.generate_ssh_tunnel_script(target_host, target_port)
        
        if config_type in ["all", "socat"]:
            configs["socat-relay.sh"] = self.generate_socat_script(target_host, target_port)
        
        if config_type in ["all", "docker"]:
            configs["docker-compose.yml"] = self.generate_docker_compose(target_host, target_port)
        
        if config_type in ["all", "systemd"]:
            configs["ninvendo-proxy.service"] = self.generate_systemd_service()
        
        if config_type in ["all", "install"]:
            configs["install.sh"] = self.generate_installation_script(target_host)
        
        # Salva tutti i file
        for filename, content in configs.items():
            file_path = output_path / filename
            with open(file_path, 'w') as f:
                f.write(content)
            
            # Rendi eseguibili gli script
            if filename.endswith('.sh'):
                os.chmod(file_path, 0o755)
            
            print(f"✅ Generated: {file_path}")
        
        # Genera README
        readme_content = f"""# NINVENDO Proxy Configuration Files
Generated on {datetime.now()}

## Target Configuration
- Target Host: {target_host}
- Target Port: {target_port}
- Proxy Types: {config_type}

## Quick Start

### Option 1: Socat (Simple TCP Relay)
```bash
chmod +x socat-relay.sh
./socat-relay.sh start
```

### Option 2: HAProxy (Advanced TCP Proxy)
```bash
sudo cp haproxy.cfg /etc/haproxy/
sudo systemctl restart haproxy
```

### Option 3: Stunnel (TLS Tunnel)
```bash
sudo cp stunnel.conf /etc/stunnel/
sudo systemctl restart stunnel4
```

### Option 4: SSH Tunnel
```bash
chmod +x ssh-tunnel.sh
./ssh-tunnel.sh start
```

### Option 5: Docker Compose
```bash
docker-compose up -d
```

## Testing
After starting any proxy, test with:
```bash
# Test port 5432
telnet localhost 5432

# Test PostgreSQL connection
psql -h localhost -p 5432 -U your_user -d your_db
```

## Monitoring
- HAProxy stats: http://localhost:8404/stats
- Service logs: sudo journalctl -u ninvendo-proxy -f

## Security Notes
- Change default passwords
- Use proper SSL certificates
- Restrict access by IP if possible
- Monitor logs for suspicious activity
"""
        
        readme_path = output_path / "README.md"
        with open(readme_path, 'w') as f:
            f.write(readme_content)
        
        print(f"✅ Generated: {readme_path}")
        print(f"\n🎉 All configuration files saved to: {output_dir}")


def main():
    """Funzione principale"""
    import argparse
    
    parser = argparse.ArgumentParser(description='NINVENDO Proxy Configuration Generator')
    parser.add_argument('--target-host', required=True, help='Target host behind firewall')
    parser.add_argument('--target-port', type=int, default=5432, help='Target PostgreSQL port')
    parser.add_argument('--output-dir', default='./proxy-configs', help='Output directory')
    parser.add_argument('--type', choices=['all', 'stunnel', 'haproxy', 'ssh', 'socat', 'docker'], 
                       default='all', help='Configuration type to generate')
    
    args = parser.parse_args()
    
    print("🔧 NINVENDO Proxy Configuration Generator")
    print("=" * 50)
    print(f"Target: {args.target_host}:{args.target_port}")
    print(f"Output: {args.output_dir}")
    print(f"Type: {args.type}")
    print("=" * 50)
    
    generator = ProxyConfigGenerator()
    generator.save_configurations(
        args.output_dir, 
        args.target_host, 
        args.target_port, 
        args.type
    )


if __name__ == "__main__":
    main()