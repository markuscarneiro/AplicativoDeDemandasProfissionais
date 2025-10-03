@echo off
echo ============================================================
echo   🧪 TESTE LOCAL - CONFIGURAÇÃO RAILWAY
echo ============================================================
echo.
echo 🎯 Este script testa se a configuração do Railway funciona
echo    localmente antes de fazer o deploy.
echo.

cd gestao_demandas_projeto

echo 📋 1. Verificando requirements.txt...
echo ----------------------------------------
type requirements.txt
echo.

echo 🔍 2. Verificando se dependências estão instaladas...
echo ----------------------------------------
python -c "import django; print('✅ Django:', django.get_version())" 2>nul || echo "❌ Django não encontrado"
python -c "import gunicorn; print('✅ Gunicorn instalado')" 2>nul || echo "❌ Gunicorn não encontrado - instale: pip install gunicorn"
python -c "import dj_database_url; print('✅ dj-database-url instalado')" 2>nul || echo "❌ dj-database-url não encontrado - instale: pip install dj-database-url"
python -c "import psycopg2; print('✅ psycopg2-binary instalado')" 2>nul || echo "❌ psycopg2-binary não encontrado - instale: pip install psycopg2-binary"
python -c "import whitenoise; print('✅ whitenoise instalado')" 2>nul || echo "❌ whitenoise não encontrado - instale: pip install whitenoise"
echo.

echo 🔧 3. Testando configurações do settings.py...
echo ----------------------------------------
echo Testando importações...
python -c "from gestao_demandas.settings import *; print('✅ Settings.py carregado com sucesso')" 2>nul || echo "❌ Erro no settings.py"
echo.

echo 🗃️  4. Verificando migrações...
echo ----------------------------------------
python manage.py check --deploy 2>nul
if errorlevel 1 (
    echo ⚠️  Executando check básico...
    python manage.py check
)
echo.

echo 📁 5. Testando coleta de arquivos estáticos...
echo ----------------------------------------
if not exist "staticfiles" mkdir staticfiles
python manage.py collectstatic --noinput --verbosity 0
if errorlevel 1 (
    echo ❌ Erro ao coletar arquivos estáticos
) else (
    echo ✅ Arquivos estáticos coletados com sucesso
)
echo.

echo 🚀 6. Testando inicialização com Gunicorn...
echo ----------------------------------------
echo Testando sintaxe do Gunicorn...
gunicorn --check-config gestao_demandas.wsgi 2>nul
if errorlevel 1 (
    echo ❌ Erro na configuração do Gunicorn
) else (
    echo ✅ Configuração do Gunicorn OK
)
echo.

echo 🌐 7. Verificando variáveis de ambiente...
echo ----------------------------------------
echo DEBUG atual: %DEBUG%
echo SECRET_KEY configurado: %SECRET_KEY%
echo DATABASE_URL: %DATABASE_URL%
echo.

echo ============================================================
echo   📊 RESUMO DO TESTE
echo ============================================================
echo.
echo 📋 ARQUIVOS RAILWAY:
dir ..\Procfile 2>nul && echo ✅ Procfile encontrado || echo ❌ Procfile não encontrado
dir ..\runtime.txt 2>nul && echo ✅ runtime.txt encontrado || echo ❌ runtime.txt não encontrado
dir ..\.railwayignore 2>nul && echo ✅ .railwayignore encontrado || echo ❌ .railwayignore não encontrado
echo.

echo 💡 PRÓXIMOS PASSOS:
echo    1. Se todos os testes passaram: ✅ Pronto para deploy
echo    2. Se há erros: Instale dependências faltantes
echo    3. Comando para instalar tudo: pip install -r requirements.txt
echo    4. Para deploy: git add . && git commit -m "Deploy Railway" && git push
echo.

echo ============================================================
echo   🚀 COMANDO DO PROCFILE (será executado no Railway):
echo ============================================================
echo.
type ..\Procfile
echo.
echo.

echo Pressione qualquer tecla para continuar...
pause >nul

echo.
echo 🔧 QUER TESTAR O GUNICORN LOCALMENTE?
echo ----------------------------------------
set /p testar="Digite 'S' para testar Gunicorn agora ou qualquer tecla para sair: "

if /I "%testar%"=="S" (
    echo.
    echo 🚀 Iniciando Gunicorn localmente...
    echo 📱 Acesse: http://localhost:8000
    echo 🛑 Pressione Ctrl+C para parar
    echo.
    gunicorn gestao_demandas.wsgi --bind 0.0.0.0:8000
)

echo.
echo 👋 Teste finalizado!
pause