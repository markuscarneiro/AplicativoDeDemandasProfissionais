@echo off
echo ===============================================
echo   📥 INSTALADOR AUTOMÁTICO DO GIT PARA WINDOWS
echo ===============================================
echo.
echo 🔍 Este script vai ajudar você a instalar o Git.
echo.

REM Verificar se Git já está instalado
git --version >nul 2>&1
if not errorlevel 1 (
    echo ✅ Git já está instalado!
    git --version
    echo.
    echo Pressione qualquer tecla para sair...
    pause >nul
    exit /b 0
)

echo ❌ Git não encontrado no sistema.
echo.
echo 📋 OPÇÕES DE INSTALAÇÃO:
echo.
echo 1. 🌐 Download Manual (Recomendado)
echo 2. 🔧 Verificar Winget
echo 3. 📊 Mostrar instruções detalhadas
echo.
set /p opcao="Escolha uma opção (1-3): "

if "%opcao%"=="1" goto download_manual
if "%opcao%"=="2" goto verificar_winget
if "%opcao%"=="3" goto instrucoes
goto opcao_invalida

:download_manual
echo.
echo 🌐 DOWNLOAD MANUAL DO GIT:
echo ----------------------------------------
echo.
echo 1. Abra seu navegador
echo 2. Acesse: https://git-scm.com/download/win
echo 3. Baixe: "64-bit Git for Windows Setup"
echo 4. Execute o instalador
echo 5. Use as configurações padrão (Next, Next, Next...)
echo 6. Após instalar, feche e reabra o PowerShell
echo 7. Execute novamente: git --version
echo.
echo 🔗 URL direta:
echo https://github.com/git-for-windows/git/releases/latest
echo.
goto fim

:verificar_winget
echo.
echo 🔧 VERIFICANDO WINGET:
echo ----------------------------------------
winget --version >nul 2>&1
if not errorlevel 1 (
    echo ✅ Winget disponível! Instalando Git...
    echo.
    winget install --id Git.Git -e --source winget
    if not errorlevel 1 (
        echo.
        echo ✅ Git instalado com sucesso!
        echo ⚠️  REINICIE o PowerShell para usar o Git
    ) else (
        echo ❌ Erro na instalação via Winget
        echo 💡 Tente o download manual (opção 1)
    )
) else (
    echo ❌ Winget não disponível
    echo 💡 Use o download manual (opção 1)
)
goto fim

:instrucoes
echo.
echo 📊 INSTRUÇÕES DETALHADAS:
echo ----------------------------------------
echo.
echo 🎯 MÉTODO 1 - Download Manual (RECOMENDADO):
echo    1. Vá para: https://git-scm.com/download/win
echo    2. Clique em "Download for Windows"
echo    3. Execute o arquivo .exe baixado
echo    4. Durante a instalação:
echo       - Use todas as opções padrão
echo       - Mantenha "Git from the command line" selecionado
echo       - Escolha "Use Windows default console window"
echo    5. Após instalar, feche TODOS os terminais
echo    6. Abra novo PowerShell
echo    7. Teste: git --version
echo.
echo 🎯 MÉTODO 2 - Via Microsoft Store:
echo    1. Abra Microsoft Store
echo    2. Pesquise por "Git"
echo    3. Instale "Git for Windows"
echo.
echo 🎯 MÉTODO 3 - Via Chocolatey (se tiver):
echo    1. PowerShell como Admin
echo    2. Execute: choco install git
echo.
echo ⚠️  IMPORTANTE: Após qualquer instalação, REINICIE o PowerShell!
goto fim

:opcao_invalida
echo.
echo ❌ Opção inválida! Escolha 1, 2 ou 3.
echo.
pause
cls
goto :eof

:fim
echo.
echo ===============================================
echo   📝 APÓS INSTALAR O GIT:
echo ===============================================
echo.
echo 1. ✅ Feche este terminal
echo 2. ✅ Abra novo PowerShell  
echo 3. ✅ Navegue até seu projeto:
echo    cd c:\Users\u8178\app-demandas\gestao_demandas_projeto
echo 4. ✅ Configure Git (primeira vez):
echo    git config --global user.name "Seu Nome"
echo    git config --global user.email "seu.email@empresa.com"
echo 5. ✅ Inicialize repositório:
echo    git init
echo    git add .
echo    git commit -m "Primeiro commit - sistema de demandas"
echo.
echo ===============================================
echo.
echo Pressione qualquer tecla para sair...
pause >nul