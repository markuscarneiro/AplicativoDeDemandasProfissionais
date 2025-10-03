@echo off
REM Script para executar comandos Django sem privilégios de administrador
REM Desenvolvido para Windows com ExecutionPolicy restrito

echo ====================================
echo    Sistema de Gestao de Demandas
echo ====================================
echo.

REM Definir variaveis
set PROJECT_DIR=c:\Users\u8178\app-demandas\gestao_demandas_projeto
set PYTHON_EXE=C:\Users\u8178\app-demandas\.venv\Scripts\python.exe

echo Navegando para o diretorio do projeto...
cd /d %PROJECT_DIR%

:menu
echo.
echo ====== MENU DE OPCOES ======
echo 1. Executar servidor (runserver)
echo 2. Criar superusuario
echo 3. Verificar projeto (check)
echo 4. Gerar migracoes
echo 5. Aplicar migracoes
echo 6. Abrir shell Django
echo 7. Sair
echo.
set /p opcao=Escolha uma opcao (1-7): 

if "%opcao%"=="1" goto runserver
if "%opcao%"=="2" goto createsuperuser
if "%opcao%"=="3" goto check
if "%opcao%"=="4" goto makemigrations
if "%opcao%"=="5" goto migrate
if "%opcao%"=="6" goto shell
if "%opcao%"=="7" goto fim
echo Opcao invalida!
goto menu

:runserver
echo.
echo Iniciando servidor Django...
echo Acesse: http://127.0.0.1:8000/
echo Pressione Ctrl+C para parar o servidor
echo.
%PYTHON_EXE% manage.py runserver
goto menu

:createsuperuser
echo.
echo Criando superusuario...
%PYTHON_EXE% manage.py createsuperuser
echo.
pause
goto menu

:check
echo.
echo Verificando projeto...
%PYTHON_EXE% manage.py check
echo.
pause
goto menu

:makemigrations
echo.
echo Gerando migracoes...
%PYTHON_EXE% manage.py makemigrations
echo.
pause
goto menu

:migrate
echo.
echo Aplicando migracoes...
%PYTHON_EXE% manage.py migrate
echo.
pause
goto menu

:shell
echo.
echo Abrindo shell Django...
%PYTHON_EXE% manage.py shell
echo.
pause
goto menu

:fim
echo.
echo Saindo...
pause
exit