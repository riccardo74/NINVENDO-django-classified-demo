# NINVENDO PostgreSQL Proxy Setup - Windows PowerShell
# ====================================================

param(
    [string]$ConfigPath = "$env:USERPROFILE\.ninvendo",
    [switch]$TestOnly,
    [switch]$Verbose
)

# Colors for output
$Colors = @{
    Red = 'Red'
    Green = 'Green' 
    Yellow = 'Yellow'
    Blue = 'Blue'
    Magenta = 'Magenta'
    Cyan = 'Cyan'
}

function Write-ColorOutput($Message, $Color = 'White') {
    Write-Host $Message -ForegroundColor $Color
}

function Write-Header($Text) {
    Write-Host ""
    Write-ColorOutput ("=" * 50) $Colors.Magenta
    Write-ColorOutput $Text.PadLeft(([Math]::Floor((50 + $Text.Length) / 2))) $Colors.Magenta
    Write-ColorOutput ("=" * 50) $Colors.Magenta
    Write-Host ""
}

function Write-Success($Message) {
    Write-ColorOutput "[OK] $Message" $Colors.Green
}

function Write-Warning($Message) {
    Write-ColorOutput "[WARN] $Message" $Colors.Yellow
}

function Write-Error($Message) {
    Write-ColorOutput "[ERROR] $Message" $Colors.Red
}

function Write-Info($Message) {
    Write-ColorOutput "[INFO] $Message" $Colors.Blue
}

Write-Header "NINVENDO PostgreSQL Proxy Setup - Windows"

# Crea directory configurazione
if (-not (Test-Path $ConfigPath)) {
    New-Item -ItemType Directory -Path $ConfigPath -Force | Out-Null
    Write-Success "Created config directory: $ConfigPath"
}

# Rileva ambiente
Write-Header "Environment Detection"

# Check Tailscale
$TailscaleStatus = ""
$TailscaleIP = ""

try {
    $TailscaleOutput = tailscale status 2>$null
    if ($LASTEXITCODE -eq 0) {
        Write-Success "Tailscale is running"
        
        # Trova IP del proxy
        $ProxyLine = $TailscaleOutput | Where-Object { $_ -match "proxy-ninv.*100\.108\.112\.117" }
        if ($ProxyLine) {
            $TailscaleIP = "100.108.112.117"
            Write-Success "Found proxy server: $TailscaleIP"
        }
        
        # Mostra dispositivi online
        $OnlineDevices = $TailscaleOutput | Where-Object { $_ -notmatch "offline" -and $_ -match "100\." }
        Write-Info "Online devices:"
        $OnlineDevices | ForEach-Object { Write-Info "  $_" }
    } else {
        Write-Warning "Tailscale not running or not accessible"
    }
} catch {
    Write-Warning "Tailscale command not found"
}

# Check Python
$PythonVersion = ""
try {
    $PythonOutput = python --version 2>$null
    if ($LASTEXITCODE -eq 0) {
        $PythonVersion = $PythonOutput
        Write-Success "Python available: $PythonVersion"
    } else {
        Write-Warning "Python not found in PATH"
    }
} catch {
    Write-Warning "Python not available"
}

# Check Git
try {
    $GitOutput = git --version 2>$null
    if ($LASTEXITCODE -eq 0) {
        Write-Success "Git available: $GitOutput"
    }
} catch {
    Write-Warning "Git not available"
}

# Test porte prima della configurazione
Write-Header "Port Discovery"

function Test-TcpConnection($Hostname, $Port, $Timeout = 5000) {
    try {
        $TcpClient = New-Object System.Net.Sockets.TcpClient
        $Connect = $TcpClient.BeginConnect($Hostname, $Port, $null, $null)
        $Wait = $Connect.AsyncWaitHandle.WaitOne($Timeout, $false)
        
        if ($Wait) {
            $TcpClient.EndConnect($Connect)
            $TcpClient.Close()
            return $true
        } else {
            $TcpClient.Close()
            return $false
        }
    } catch {
        return $false
    }
}

# Test porte comuni PostgreSQL
$ProxyHost = "100.108.112.117"
$PortsToTest = @(5432, 6543, 5433, 5434)
$OpenPorts = @()

Write-Info "Testing common PostgreSQL ports on $ProxyHost..."

foreach ($Port in $PortsToTest) {
    Write-Host "  Testing port $Port..." -NoNewline
    if (Test-TcpConnection $ProxyHost $Port 3000) {
        Write-Host " OPEN" -ForegroundColor Green
        $OpenPorts += $Port
    } else {
        Write-Host " CLOSED" -ForegroundColor Red
    }
}

if ($OpenPorts.Count -gt 0) {
    Write-Success "Found $($OpenPorts.Count) open port(s): $($OpenPorts -join ', ')"
    $RecommendedPort = $OpenPorts[0]
} else {
    Write-Warning "No open ports found. Will use default 5432"
    $RecommendedPort = 5432
}

# Configurazione interattiva
Write-Header "Configuration Setup"

# Carica configurazione esistente se disponibile
$ConfigFile = Join-Path $ConfigPath "proxy.json"
$ExistingConfig = @{}

if (Test-Path $ConfigFile) {
    try {
        $ExistingConfig = Get-Content $ConfigFile | ConvertFrom-Json -AsHashtable
        Write-Info "Loading existing configuration from $ConfigFile"
    } catch {
        Write-Warning "Could not load existing configuration"
    }
}

# Funzione per input con default - VERSIONE CORRETTA
function Read-ConfigValue($Prompt, $DefaultValue, $CurrentValue) {
    $Value = if ($CurrentValue) { $CurrentValue } else { $DefaultValue }
    
    Write-Host -NoNewline "$Prompt"
    if ($Value) {
        Write-Host -NoNewline " [$Value]" -ForegroundColor Cyan
    }
    Write-Host -NoNewline ": "
    
    $Input = Read-Host
    if ([string]::IsNullOrWhiteSpace($Input) -and $Value) {
        return $Value
    }
    
    # CORREZIONE: Sintassi PowerShell corretta
    if ($Input) { 
        return $Input 
    } else { 
        return $DefaultValue 
    }
}

# Configurazione principale
Write-ColorOutput "Proxy Server Configuration" $Colors.Cyan

$Config = @{}
$Config.proxy_host = Read-ConfigValue "Proxy hostname" $ProxyHost $ExistingConfig.proxy_host
$Config.proxy_port = [int](Read-ConfigValue "Proxy port" $RecommendedPort $ExistingConfig.proxy_port)

Write-ColorOutput "`nDatabase Configuration" $Colors.Cyan
$Config.db_host = Read-ConfigValue "Database host (behind proxy)" "localhost" $ExistingConfig.db_host
$Config.db_port = [int](Read-ConfigValue "Database port" "5432" $ExistingConfig.db_port)
$Config.db_name = Read-ConfigValue "Database name" "ninvendo_dev" $ExistingConfig.db_name
$Config.db_user = Read-ConfigValue "Database user" "ninvendo" $ExistingConfig.db_user

# Password
if (-not $ExistingConfig.db_password) {
    Write-Host -NoNewline "Database password: " -ForegroundColor Blue
    $SecurePassword = Read-Host -AsSecureString
    $Config.db_password = [Runtime.InteropServices.Marshal]::PtrToStringAuto([Runtime.InteropServices.Marshal]::SecureStringToBSTR($SecurePassword))
} else {
    Write-ColorOutput "Database password: [configured]" $Colors.Green
    $Config.db_password = $ExistingConfig.db_password
}

Write-ColorOutput "`nSSL Configuration" $Colors.Cyan
$Config.ssl_mode = Read-ConfigValue "SSL mode (disable/require/verify-ca/verify-full)" "require" $ExistingConfig.ssl_mode

Write-ColorOutput "`nNetwork Configuration" $Colors.Cyan
$Config.tailscale_ip = Read-ConfigValue "Tailscale IP" $TailscaleIP $ExistingConfig.tailscale_ip
$Config.test_timeout = [int](Read-ConfigValue "Test timeout (seconds)" "30" $ExistingConfig.test_timeout)

# Mostra riepilogo
Write-Header "Configuration Summary"

Write-Host "Proxy: $($Config.proxy_host):$($Config.proxy_port)"
Write-Host "Database: $($Config.db_name) on $($Config.db_host):$($Config.db_port)"
Write-Host "User: $($Config.db_user)"
Write-Host "SSL Mode: $($Config.ssl_mode)"
Write-Host "Tailscale: $($Config.tailscale_ip)"
Write-Host "Timeout: $($Config.test_timeout)s"

Write-Host ""
$Confirm = Read-Host "Save this configuration? (y/n)"
if ($Confirm -notmatch "^[Yy]") {
    Write-Error "Configuration cancelled"
    exit 1
}

# Salva configurazione
Write-Header "Saving Configuration"

try {
    # JSON configuration
    $Config | ConvertTo-Json -Depth 10 | Out-File -FilePath $ConfigFile -Encoding UTF8
    Write-Success "Configuration saved to $ConfigFile"
    
    # PowerShell environment file
    $EnvFile = Join-Path $ConfigPath "proxy.ps1"
    $EnvContent = @"
# NINVENDO PostgreSQL Proxy Configuration
# Generated on $(Get-Date)

`$env:PROXY_HOST = "$($Config.proxy_host)"
`$env:PROXY_PORT = "$($Config.proxy_port)"
`$env:DB_HOST = "$($Config.db_host)" 
`$env:DB_PORT = "$($Config.db_port)"
`$env:DB_NAME = "$($Config.db_name)"
`$env:DB_USER = "$($Config.db_user)"
`$env:DB_PASSWORD = "$($Config.db_password)"
`$env:PGSSLMODE = "$($Config.ssl_mode)"
`$env:TAILSCALE_IP = "$($Config.tailscale_ip)"
`$env:TEST_TIMEOUT = "$($Config.test_timeout)"

Write-Host "NINVENDO proxy environment loaded" -ForegroundColor Green
"@
    
    $EnvContent | Out-File -FilePath $EnvFile -Encoding UTF8
    Write-Success "PowerShell environment saved to $EnvFile"
    
} catch {
    Write-Error "Failed to save configuration: $_"
    exit 1
}

# Test connessione di base
Write-Header "Basic Connection Test"

# Test TCP connection
Write-Info "Testing TCP connection to $($Config.proxy_host):$($Config.proxy_port)..."

$StartTime = Get-Date
$TcpSuccess = Test-TcpConnection $Config.proxy_host $Config.proxy_port 10000
$ConnectTime = (Get-Date) - $StartTime

if ($TcpSuccess) {
    $ConnectMs = $ConnectTime.TotalMilliseconds.ToString('F2')
    Write-Success "TCP connection successful ($ConnectMs ms)"
} else {
    Write-Error "TCP connection failed"
    Write-Warning "Check that:"
    Write-Warning "  1. Proxy server is running"
    Write-Warning "  2. Tailscale is connected"
    Write-Warning "  3. Firewall allows connection"
    Write-Warning "  4. Port $($Config.proxy_port) is correct"
}

# Test PostgreSQL se Python disponibile
if ($PythonVersion -and $TcpSuccess) {
    Write-Info "Testing PostgreSQL connection..."
    
    # Crea script Python temporaneo per test
    $TempPyScript = Join-Path $env:TEMP "test_pg_connection.py"
    $PyScript = @"
import sys
try:
    import psycopg2
    
    conn_string = "postgresql://$($Config.db_user):$($Config.db_password)@$($Config.proxy_host):$($Config.proxy_port)/$($Config.db_name)?sslmode=$($Config.ssl_mode)&connect_timeout=30"
    
    conn = psycopg2.connect(conn_string)
    cur = conn.cursor()
    cur.execute("SELECT version(), current_timestamp, current_user")
    result = cur.fetchone()
    
    print("SUCCESS")
    print("Version: " + result[0][:50] + "...")
    print("Time: " + str(result[1]))
    print("User: " + result[2])
    
    conn.close()
    
except ImportError:
    print("ERROR: psycopg2 not installed")
    print("Install with: pip install psycopg2-binary")
    sys.exit(1)
except Exception as e:
    print("ERROR: " + str(e))
    sys.exit(1)
"@

    $PyScript | Out-File -FilePath $TempPyScript -Encoding UTF8
    
    try {
        $PgResult = python $TempPyScript 2>&1
        Remove-Item $TempPyScript -Force
        
        if ($PgResult[0] -eq "SUCCESS") {
            Write-Success "PostgreSQL connection successful!"
            $PgResult[1..($PgResult.Count-1)] | ForEach-Object { Write-Info "  $_" }
        } else {
            Write-Warning "PostgreSQL connection failed:"
            $PgResult | ForEach-Object { Write-Warning "  $_" }
        }
    } catch {
        Write-Warning "Could not test PostgreSQL connection: $_"
        Remove-Item $TempPyScript -Force -ErrorAction SilentlyContinue
    }
}

# Crea script di test rapido
Write-Header "Creating Test Scripts"

# Test rapido PowerShell
$QuickTestScript = Join-Path $ConfigPath "quick-test.ps1"
$QuickTestContent = @"
# NINVENDO Quick Connection Test
# Load configuration
. "$EnvFile"

Write-Host "Testing NINVENDO PostgreSQL proxy..." -ForegroundColor Cyan
Write-Host "Host: `$env:PROXY_HOST:`$env:PROXY_PORT"
Write-Host "Database: `$env:DB_NAME"
Write-Host ""

# TCP Test
`$TcpClient = New-Object System.Net.Sockets.TcpClient
try {
    `$TcpClient.Connect(`$env:PROXY_HOST, `$env:PROXY_PORT)
    Write-Host "TCP connection successful" -ForegroundColor Green
    `$TcpClient.Close()
} catch {
    Write-Host "TCP connection failed: `$_" -ForegroundColor Red
    exit 1
}

# PostgreSQL Test (if Python available)
if (Get-Command python -ErrorAction SilentlyContinue) {
    Write-Host "Testing PostgreSQL..."
    `$DatabaseUrl = "postgresql://`$env:DB_USER:`$env:DB_PASSWORD@`$env:PROXY_HOST:`$env:PROXY_PORT/`$env:DB_NAME?sslmode=`$env:PGSSLMODE"
    Write-Host "Database URL: `$DatabaseUrl"
} else {
    Write-Host "Python not available for PostgreSQL test" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "Quick test completed!" -ForegroundColor Green
"@

$QuickTestContent | Out-File -FilePath $QuickTestScript -Encoding UTF8
Write-Success "Quick test script created: $QuickTestScript"

# Script per Django
$DjangoTestScript = Join-Path $ConfigPath "test-django-connection.ps1"
$DjangoContent = @"
# NINVENDO Django Database Connection Test
# Load configuration
. "$EnvFile"

Write-Host "Django PostgreSQL Connection Test" -ForegroundColor Cyan

# Set Django database URL
`$DatabaseUrl = "postgresql://`$env:DB_USER:`$env:DB_PASSWORD@`$env:PROXY_HOST:`$env:PROXY_PORT/`$env:DB_NAME?sslmode=`$env:PGSSLMODE"
`$env:DATABASE_URL = `$DatabaseUrl

Write-Host "Database URL: `$DatabaseUrl"
Write-Host ""

# Change to Django project directory
if (Test-Path "manage.py") {
    Write-Host "Found Django project, testing connection..."
    
    try {
        # Test database connection
        python manage.py shell --command="from django.db import connection; connection.ensure_connection(); print('Django database connection successful!')"
        
        Write-Host ""
        Write-Host "Running Django checks..."
        python manage.py check --database default
        
    } catch {
        Write-Host "Django database test failed: `$_" -ForegroundColor Red
    }
} else {
    Write-Host "No Django project found in current directory" -ForegroundColor Yellow
    Write-Host "Navigate to your Django project directory and run this script again"
}

Write-Host ""
Write-Host "To use this database in Django, add to your .env file:" -ForegroundColor Yellow
Write-Host "DATABASE_URL=`$DatabaseUrl" -ForegroundColor Cyan
"@

$DjangoContent | Out-File -FilePath $DjangoTestScript -Encoding UTF8
Write-Success "Django test script created: $DjangoTestScript"

# Istruzioni finali
Write-Header "Next Steps"

Write-ColorOutput "Configuration complete! Here's what to do next:" $Colors.Green
Write-Host ""

Write-ColorOutput "1. Run quick connection test:" $Colors.Yellow
Write-Host "   PowerShell $QuickTestScript"
Write-Host ""

Write-ColorOutput "2. Install Python dependencies (if not already done):" $Colors.Yellow
Write-Host "   pip install psycopg2-binary requests cryptography"
Write-Host ""

Write-ColorOutput "3. Test Django connection:" $Colors.Yellow
Write-Host "   PowerShell $DjangoTestScript"
Write-Host ""

Write-ColorOutput "Configuration files saved in: $ConfigPath" $Colors.Blue
Write-ColorOutput "Keep your credentials secure!" $Colors.Red

Write-Host ""
Write-ColorOutput "Setup completed successfully!" $Colors.Green

# Offri di eseguire test rapido
$RunTest = Read-Host "Run quick connection test now? (y/n)"
if ($RunTest -match "^[Yy]") {
    Write-Host ""
    & $QuickTestScript
}
