@echo off
echo ========================================
echo    TESTE DE LOGIN COM BACKGROUND
echo ========================================
echo.

echo 1. Verificando estrutura de arquivos...
if exist "demandas\static\demandas\images\background-login.jpg" (
    echo ✅ Imagem encontrada: background-login.jpg
) else (
    echo ❌ Imagem NÃO encontrada!
    echo    Esperado: demandas\static\demandas\images\background-login.jpg
)

if exist "demandas\static\demandas\css\login-background.css" (
    echo ✅ CSS encontrado: login-background.css
) else (
    echo ❌ CSS NÃO encontrado!
)

if exist "templates\registration\login.html" (
    echo ✅ Template encontrado: login.html
) else (
    echo ❌ Template NÃO encontrado!
)

echo.
echo 2. Iniciando servidor de desenvolvimento...
echo    URL de teste: http://127.0.0.1:8000/admin/login/
echo.
echo INSTRUÇÕES:
echo - Abra o navegador em: http://127.0.0.1:8000/admin/login/
echo - Abra o Console do desenvolvedor (F12)
echo - Verifique as mensagens de debug no console
echo - Se aparecer uma borda verde = imagem carregou
echo - Se aparecer uma borda vermelha = erro no carregamento
echo.
echo Pressione Ctrl+C para parar o servidor
echo ========================================
echo.

python manage.py runserver