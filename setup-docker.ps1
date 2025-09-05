# Script PowerShell per setup Docker NINVENDO
Write-Host "🐳 NINVENDO Docker Setup" -ForegroundColor Blue
Write-Host "========================" -ForegroundColor Blue

# Verifica Docker
if (-not (Get-Command "docker" -ErrorAction SilentlyContinue)) {
    Write-Host "❌ Docker non installato. Installa Docker Desktop prima." -ForegroundColor Red
    exit 1
}

if (-not (Get-Command "docker-compose" -ErrorAction SilentlyContinue)) {
    Write-Host "❌ Docker Compose non installato." -ForegroundColor Red
    exit 1
}

# Verifica file .env
if (-not (Test-Path ".env")) {
    Write-Host "❌ File .env non trovato!" -ForegroundColor Red
    Write-Host "Il file .env deve contenere DATABASE_URL e altre variabili." -ForegroundColor Yellow
    exit 1
}

# Verifica DATABASE_URL nel .env
$envContent = Get-Content ".env" -Raw
if ($envContent -notmatch "DATABASE_URL.*render\.com") {
    Write-Host "⚠️  Verifica che DATABASE_URL nel .env punti a Render PostgreSQL" -ForegroundColor Yellow
}

Write-Host "✅ Configurazione verificata!" -ForegroundColor Green

# Build immagine Docker
Write-Host "🏗️  Building Docker image..." -ForegroundColor Blue
docker-compose build

if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Errore durante il build Docker!" -ForegroundColor Red
    exit 1
}

# Avvia i container
Write-Host "🚀 Starting containers..." -ForegroundColor Blue
docker-compose up -d

if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Errore durante l'avvio dei container!" -ForegroundColor Red
    exit 1
}

# Attendi che i servizi siano pronti
Write-Host "⏳ Waiting for services to be ready..." -ForegroundColor Blue
Start-Sleep -Seconds 15

# Mostra status
Write-Host "📋 Container status:" -ForegroundColor Blue
docker-compose ps

Write-Host ""
Write-Host "🎉 Setup completato!" -ForegroundColor Green
Write-Host ""
Write-Host "📊 Per vedere i logs:" -ForegroundColor Yellow
Write-Host "   docker-compose logs -f web" -ForegroundColor White
Write-Host ""
Write-Host "🌐 L'applicazione è disponibile su:" -ForegroundColor Yellow
Write-Host "   http://localhost:8000" -ForegroundColor White
Write-Host ""
Write-Host "🛑 Per fermare i container:" -ForegroundColor Yellow
Write-Host "   docker-compose down" -ForegroundColor White
Write-Host ""
Write-Host "🔧 Per accedere al container:" -ForegroundColor Yellow
Write-Host "   docker-compose exec web bash" -ForegroundColor White