@echo off
echo ============================================================
echo   👤 CRIAÇÃO AUTOMÁTICA DE SUPERUSUÁRIO DJANGO
echo ============================================================
echo.
echo 🎯 Este script cria um superusuário automaticamente
echo    usando variáveis de ambiente ou valores padrão.
echo.

REM Verificar se estamos no diretório correto
if not exist "manage.py" (
    echo ❌ ERRO: Arquivo manage.py não encontrado!
    echo    Certifique-se de estar na pasta gestao_demandas_projeto
    echo    Diretório atual: %CD%
    pause
    exit /b 1
)

echo 📁 Diretório do projeto: %CD%
echo.

REM Ativar ambiente virtual se existir
if exist "..\\.venv\\Scripts\\activate.bat" (
    echo 🔧 Ativando ambiente virtual...
    call "..\\.venv\\Scripts\\activate.bat"
    echo ✅ Ambiente virtual ativado
    echo.
)

echo 📋 Configurações do superusuário:
echo ----------------------------------------
echo Username: %DJANGO_SUPERUSER_USERNAME% (padrão: admin)
echo Email:    %DJANGO_SUPERUSER_EMAIL% (padrão: admin@example.com)
echo Password: %DJANGO_SUPERUSER_PASSWORD% (padrão: admin123)
echo.

echo 💡 Para personalizar, defina as variáveis de ambiente:
echo    set DJANGO_SUPERUSER_USERNAME=meuadmin
echo    set DJANGO_SUPERUSER_EMAIL=admin@meusite.com
echo    set DJANGO_SUPERUSER_PASSWORD=minhasenha123
echo.

echo ⚠️  IMPORTANTE: Este script só funciona após executar migrações!
echo    Se necessário: python manage.py migrate
echo.

set /p continuar="Continuar com a criação do superusuário? (S/N): "
if /I not "%continuar%"=="S" (
    echo ❌ Operação cancelada pelo usuário.
    pause
    exit /b 0
)

echo.
echo 🚀 Criando superusuário...
echo ----------------------------------------

python create_superuser.py

if errorlevel 1 (
    echo.
    echo ❌ ERRO na criação do superusuário!
    echo.
    echo 🔍 Possíveis causas:
    echo    • Migrações não executadas: python manage.py migrate
    echo    • Ambiente virtual não ativado
    echo    • Django não instalado: pip install django
    echo    • Problema na configuração do banco de dados
    echo.
    echo 🛠️  Comandos para resolver:
    echo    python manage.py migrate
    echo    python manage.py check
    echo.
) else (
    echo.
    echo ✅ OPERAÇÃO CONCLUÍDA!
    echo.
    echo 🎉 Agora você pode fazer login no admin:
    echo    • URL: http://localhost:8000/admin/
    echo    • Username: %DJANGO_SUPERUSER_USERNAME%
    echo    • Password: %DJANGO_SUPERUSER_PASSWORD%
    echo.
    echo 💡 Para iniciar o servidor:
    echo    python manage.py runserver
    echo    # ou use os scripts de porta alternativa:
    echo    start_8080.bat, start_3000.bat, start_server.bat
    echo.
)

echo ============================================================
echo   📊 INFORMAÇÕES DO SCRIPT
echo ============================================================
echo.
echo 📄 Arquivo usado: create_superuser.py
echo 🔧 Configurações: Variáveis de ambiente ou padrões
echo 🎯 Comportamento: Não recria se usuário já existir
echo ⚙️  Compatível: Desenvolvimento local e Railway
echo.
echo Pressione qualquer tecla para sair...
pause >nul