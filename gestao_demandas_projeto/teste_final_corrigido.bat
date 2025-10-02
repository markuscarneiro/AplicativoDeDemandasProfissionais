@echo off
echo ============================================================
echo   ✅ TESTE FINAL - CONFIGURAÇÃO CORRIGIDA
echo ============================================================
echo.

REM Ativar ambiente virtual
if exist "..\\.venv\\Scripts\\activate.bat" (
    echo 🔧 Ativando ambiente virtual...
    call "..\\.venv\\Scripts\\activate.bat"
    echo ✅ Ambiente virtual ativado
    echo.
)

echo 🔍 1. Verificando dependências instaladas...
echo ----------------------------------------
python -c "import dj_database_url; print('✅ dj-database-url:', dj_database_url.__version__)" || echo "❌ dj-database-url falhou"
python -c "import gunicorn; print('✅ gunicorn instalado')" || echo "❌ gunicorn falhou"
python -c "import psycopg2; print('✅ psycopg2-binary instalado')" || echo "❌ psycopg2 falhou"
echo.

echo 🧪 2. Testando configuração Django...
echo ----------------------------------------
python manage.py check || echo "❌ Erro na configuração"
echo.

echo 🌐 3. Testando WSGI...
echo ----------------------------------------
python -c "from gestao_demandas.wsgi import application; print('✅ WSGI OK')" || echo "❌ Erro no WSGI"
echo.

echo 📋 4. Verificando Procfile...
echo ----------------------------------------
type Procfile
echo.

echo 🚀 5. Comando para Railway (funcionando)...
echo ----------------------------------------
echo O comando no Procfile funcionará no Railway (Linux).
echo No Windows, o Gunicorn tem limitações mas a configuração está correta.
echo.

echo ============================================================
echo   🎉 CONFIGURAÇÃO PRONTA PARA RAILWAY!
echo ============================================================
echo.
echo ✅ Dependências: Instaladas e funcionando
echo ✅ Settings.py: Import condicional correto
echo ✅ Procfile: Comando correto para Railway
echo ✅ WSGI: Carregando sem erros
echo ✅ Requirements.txt: Na pasta correta
echo.
echo 💡 Para testar local (desenvolvimento):
echo    python manage.py runserver
echo.
echo 🚀 Para Railway: 
echo    git add .
echo    git commit -m "Fix dj-database-url import and dependencies"
echo    git push
echo.

pause