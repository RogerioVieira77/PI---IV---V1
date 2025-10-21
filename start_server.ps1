# ========================================
# CEU TRES PONTES - INICIANDO SERVIDOR
# ========================================

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "CEU TRES PONTES - INICIANDO SERVIDOR" -ForegroundColor Cyan
Write-Host "========================================`n" -ForegroundColor Cyan

# Ir para o diretório do projeto
Set-Location "C:\PI - IV - V1"

Write-Host "[1/3] Ativando ambiente virtual..." -ForegroundColor Yellow
& .\venv\Scripts\Activate.ps1

Write-Host "[2/3] Configurando Flask..." -ForegroundColor Yellow
$env:FLASK_APP = "backend/app.py"
$env:FLASK_ENV = "development"
$env:FLASK_DEBUG = "1"

Write-Host "[3/3] Iniciando servidor Flask...`n" -ForegroundColor Yellow

Write-Host "========================================" -ForegroundColor Green
Write-Host "SERVIDOR RODANDO EM:" -ForegroundColor Green
Write-Host "  - http://localhost:5000" -ForegroundColor White
Write-Host "  - http://127.0.0.1:5000" -ForegroundColor White
Write-Host "========================================`n" -ForegroundColor Green

Write-Host "Pressione CTRL+C para parar o servidor`n" -ForegroundColor Yellow

# Iniciar servidor
flask run --host=0.0.0.0 --port=5000
