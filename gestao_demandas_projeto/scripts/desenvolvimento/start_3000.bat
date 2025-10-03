@echo off
echo ======================================================
echo    🚀 INICIANDO SERVIDOR DJANGO - PORTA 3000
echo ======================================================
echo.
echo 🎯 Porta de Desenvolvimento: Esta porta é amplamente
echo    utilizada para desenvolvimento web e raramente bloqueada!
echo.

REM Verificar se estamos no diretório correto
if not exist "manage.py" (
    echo ❌ ERRO: Arquivo manage.py não encontrado!
    echo    Certifique-se de estar no diretório do projeto Django.
    echo    Diretório atual: %CD%
    pause
    exit /b 1
)

echo 📁 Diretório do projeto: %CD%
echo.

REM Ativar ambiente virtual
echo 🔧 Ativando ambiente virtual...
if exist "..\\.venv\\Scripts\\activate.bat" (
    call "..\\.venv\\Scripts\\activate.bat"
    echo ✅ Ambiente virtual ativado
) else (
    echo ⚠️  Ambiente virtual não encontrado, tentando executar sem ele...
)
echo.

REM Verificar dependências
echo 🔍 Verificando instalação do Django...
python -c "import django; print('✅ Django versão:', django.get_version())" 2>nul
if errorlevel 1 (
    echo ❌ Django não encontrado! Instalando dependências...
    pip install -r requirements.txt
)
echo.

REM Obter IP atual da máquina
echo 🌐 Verificando IP atual da máquina...
for /f "tokens=2 delims=:" %%a in ('ipconfig ^| findstr /C:"IPv4"') do (
    set "ip=%%a"
    setlocal enabledelayedexpansion
    set "ip=!ip: =!"
    echo ✅ IP encontrado: !ip!
    set CURRENT_IP=!ip!
    goto :found_ip
)
:found_ip
echo.

REM Verificar se o servidor Django está funcionando
echo 🔍 Verificando configuração do Django...
python manage.py check --deploy 2>nul
if errorlevel 1 (
    echo ⚠️  Executando verificação básica...
    python manage.py check
)
echo.

REM Aplicar migrações se necessário
echo 🔄 Verificando migrações...
python manage.py migrate --check 2>nul
if errorlevel 1 (
    echo 📝 Aplicando migrações pendentes...
    python manage.py migrate
)
echo.

REM Informações importantes
echo ======================================================
echo    🎯 INFORMAÇÕES DE ACESSO - PORTA 3000
echo ======================================================
echo.
echo 🖥️  ACESSO LOCAL:
echo    http://localhost:3000
echo    http://127.0.0.1:3000
echo.
echo 🌐 ACESSO REDE LOCAL:
setlocal enabledelayedexpansion
echo    http://!CURRENT_IP!:3000
echo.
echo 📋 COMPARTILHE ESTA URL COM SEUS COLEGAS:
echo    ┌─────────────────────────────────────┐
echo    │  http://!CURRENT_IP!:3000           │
echo    └─────────────────────────────────────┘
echo.
echo ⚠️  REQUISITOS IMPORTANTES:
echo    • Mantenha este terminal aberto
echo    • Máquina deve estar conectada na rede
echo    • Porta 3000 raramente é bloqueada!
echo    • IP pode mudar se DHCP estiver ativo
echo.
echo 🔥 Se necessário, liberar porta no Firewall (como Admin):
echo    netsh advfirewall firewall add rule name="Django Server Port 3000" dir=in action=allow protocol=TCP localport=3000
echo.
echo ======================================================
echo    🚀 INICIANDO SERVIDOR NA PORTA 3000...
echo ======================================================
echo.

REM Iniciar servidor Django na porta 3000
echo 🌟 Servidor iniciando em 0.0.0.0:3000...
echo 📱 Pressione Ctrl+C para parar o servidor
echo.

python manage.py runserver 0.0.0.0:3000

echo.
echo ======================================================
echo    👋 SERVIDOR FINALIZADO
echo ======================================================
echo.
echo Pressione qualquer tecla para fechar...
pause >nul