@echo off
echo ======================================================
echo    🔍 DIAGNÓSTICO DO SERVIDOR DJANGO
echo ======================================================
echo.

echo 📡 1. Verificando IP atual da máquina:
echo ----------------------------------------
for /f "tokens=2 delims=:" %%a in ('ipconfig ^| findstr /C:"IPv4"') do (
    set "ip=%%a"
    setlocal enabledelayedexpansion
    set "ip=!ip: =!"
    echo ✅ IP encontrado: !ip!
)
echo.

echo 🌐 2. Verificando servidores Django nas portas disponíveis:
echo ----------------------------------------
echo Verificando porta 8000 (padrão):
netstat -an | findstr :8000
if errorlevel 1 (
    echo ❌ Nenhum servidor na porta 8000
) else (
    echo ✅ Servidor ativo na porta 8000
)

echo.
echo Verificando porta 8080 (alternativa):
netstat -an | findstr :8080
if errorlevel 1 (
    echo ❌ Nenhum servidor na porta 8080
) else (
    echo ✅ Servidor ativo na porta 8080
)

echo.
echo Verificando porta 3000 (desenvolvimento):
netstat -an | findstr :3000
if errorlevel 1 (
    echo ❌ Nenhum servidor na porta 3000
) else (
    echo ✅ Servidor ativo na porta 3000
)
echo.

echo 🔥 3. Verificando regras de firewall para todas as portas:
echo ----------------------------------------
echo Verificando firewall para porta 8000:
netsh advfirewall firewall show rule name="Django Server Port 8000" 2>nul
if errorlevel 1 (
    echo ❌ Regra para porta 8000 não encontrada
) else (
    echo ✅ Porta 8000 liberada no firewall
)

echo.
echo Verificando firewall para porta 8080:
netsh advfirewall firewall show rule name="Django Port 8080" 2>nul
if errorlevel 1 (
    echo ❌ Regra para porta 8080 não encontrada
) else (
    echo ✅ Porta 8080 liberada no firewall
)

echo.
echo Verificando firewall para porta 3000:
netsh advfirewall firewall show rule name="Django Port 3000" 2>nul
if errorlevel 1 (
    echo ❌ Regra para porta 3000 não encontrada
) else (
    echo ✅ Porta 3000 liberada no firewall
)

echo.
echo 💡 Para liberar portas (executar como Administrador):
echo    netsh advfirewall firewall add rule name="Django Port 8080" dir=in action=allow protocol=TCP localport=8080
echo    netsh advfirewall firewall add rule name="Django Port 3000" dir=in action=allow protocol=TCP localport=3000
echo    netsh advfirewall firewall add rule name="Django Server Port 8000" dir=in action=allow protocol=TCP localport=8000
echo.

echo 🖥️ 4. Testando acesso local:
echo ----------------------------------------
echo Testando http://localhost:8000...
curl -s -o nul -w "%%{http_code}" http://localhost:8000 2>nul
if errorlevel 1 (
    echo ❌ Não foi possível testar (curl não disponível)
    echo 💡 Teste manualmente: http://localhost:8000
) else (
    echo ✅ Teste de conectividade local realizado
)
echo.

echo 📋 5. Informações do sistema:
echo ----------------------------------------
echo Usuário atual: %USERNAME%
echo Computador: %COMPUTERNAME%
echo Data/Hora: %DATE% %TIME%
echo.

echo ======================================================
echo    💡 DICAS RÁPIDAS
echo ======================================================
echo.
echo 🚀 Para iniciar servidor:
echo    start_server.bat
echo.
echo 🌐 Para compartilhar:
echo    1. Execute start_server.bat
echo    2. Compartilhe a URL exibida
echo    3. Certifique-se que firewall está liberado
echo.
echo 🔧 Para configurar firewall (como Admin):
echo    netsh advfirewall firewall add rule name="Django Server Port 8000" dir=in action=allow protocol=TCP localport=8000
echo.
echo ======================================================

echo.
echo Pressione qualquer tecla para fechar...
pause >nul