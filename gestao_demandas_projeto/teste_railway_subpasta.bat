@echo off
echo ============================================================
echo   🧪 TESTE LOCAL - CONFIGURAÇÃO RAILWAY SUBPASTA
echo ============================================================
echo.
echo 🎯 Testando configuração para Railway com subpasta como root
echo.

if not exist "manage.py" (
    echo ❌ ERRO: Execute este script na pasta gestao_demandas_projeto
    echo    Diretório atual: %CD%
    pause
    exit /b 1
)

echo 📁 Pasta atual: %CD%
echo.

echo 🔍 1. Verificando arquivos necessários...
echo ----------------------------------------
if exist "Procfile" (
    echo ✅ Procfile encontrado
    type Procfile
) else (
    echo ❌ Procfile não encontrado
)
echo.

if exist "requirements.txt" (
    echo ✅ requirements.txt encontrado
) else (
    echo ❌ requirements.txt não encontrado
)
echo.

if exist "runtime.txt" (
    echo ✅ runtime.txt encontrado
    type runtime.txt
) else (
    echo ❌ runtime.txt não encontrado
)
echo.

echo 🔧 2. Verificando dependências...
echo ----------------------------------------
python -c "import django; print('✅ Django:', django.get_version())" 2>nul || echo "❌ Django não encontrado"
python -c "import gunicorn; print('✅ Gunicorn instalado')" 2>nul || echo "❌ Gunicorn não encontrado"
python -c "from gestao_demandas.wsgi import application; print('✅ WSGI OK')" 2>nul || echo "❌ Erro no WSGI"
echo.

echo 🌐 3. Testando comando do Procfile...
echo ----------------------------------------
echo Comando que será executado no Railway:
type Procfile
echo.
echo.

echo 💡 4. Para testar gunicorn localmente:
echo ----------------------------------------
echo set PORT=8000
echo gunicorn gestao_demandas.wsgi:application --bind 0.0.0.0:8000
echo.
echo Depois acesse: http://localhost:8000
echo.

echo ============================================================
echo   🚀 CONFIGURAÇÃO PARA RAILWAY
echo ============================================================
echo.
echo No painel do Railway:
echo 1. ✅ Root Directory: gestao_demandas_projeto
echo 2. ✅ Build Command: (deixe vazio, usará requirements.txt)
echo 3. ✅ Start Command: (deixe vazio, usará Procfile)
echo 4. ✅ Variáveis de ambiente:
echo    - DEBUG=False
echo    - SECRET_KEY=sua-chave-secreta
echo.

set /p testar="Testar gunicorn agora? (S/N): "
if /I "%testar%"=="S" (
    echo.
    echo 🚀 Iniciando Gunicorn na porta 8000...
    echo 📱 Acesse: http://localhost:8000
    echo 🛑 Pressione Ctrl+C para parar
    echo.
    set PORT=8000
    gunicorn gestao_demandas.wsgi:application --bind 0.0.0.0:8000
)

echo.
echo ✅ Teste concluído!
pause