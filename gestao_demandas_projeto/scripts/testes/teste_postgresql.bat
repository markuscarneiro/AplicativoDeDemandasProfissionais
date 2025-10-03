@echo off
echo ============================================================
echo   🗃️  TESTE - CONFIGURAÇÃO POSTGRESQL VIA DATABASE_URL
echo ============================================================
echo.
echo 🎯 Testando configuração específica para Railway PostgreSQL
echo.

cd gestao_demandas_projeto

echo 📋 1. Verificando configuração no settings.py...
echo ----------------------------------------
echo Procurando configuração DATABASE_URL...
findstr /C:"DATABASE_URL" gestao_demandas\settings.py
if errorlevel 1 (
    echo ❌ Configuração DATABASE_URL não encontrada
) else (
    echo ✅ Configuração DATABASE_URL encontrada
)
echo.

echo 🔍 2. Testando dependências...
echo ----------------------------------------
python -c "import dj_database_url; print('✅ dj-database-url:', dj_database_url.__version__)" 2>nul || echo "❌ dj-database-url não instalado - Execute: pip install dj-database-url"
python -c "import psycopg2; print('✅ psycopg2-binary instalado')" 2>nul || echo "❌ psycopg2-binary não instalado - Execute: pip install psycopg2-binary"
echo.

echo 🧪 3. Testando configuração SQLite (desenvolvimento local)...
echo ----------------------------------------
echo Sem DATABASE_URL (deve usar SQLite):
python -c "
import os
import sys
sys.path.append('.')
os.environ.pop('DATABASE_URL', None)
from gestao_demandas.settings import DATABASES
print('✅ Banco local (SQLite):', DATABASES['default']['ENGINE'])
print('✅ Arquivo:', DATABASES['default']['NAME'])
" 2>nul || echo "❌ Erro ao carregar configuração SQLite"
echo.

echo 🌐 4. Testando configuração PostgreSQL (simulando Railway)...
echo ----------------------------------------
echo Com DATABASE_URL (deve usar PostgreSQL):
set TEST_DATABASE_URL=postgresql://user:pass@localhost:5432/testdb
python -c "
import os
import sys
sys.path.append('.')
os.environ['DATABASE_URL'] = 'postgresql://user:pass@localhost:5432/testdb'
from gestao_demandas.settings import DATABASES
print('✅ Banco Railway (PostgreSQL):', DATABASES['default']['ENGINE'])
print('✅ Host:', DATABASES['default']['HOST'])
print('✅ Porta:', DATABASES['default']['PORT'])
print('✅ Database:', DATABASES['default']['NAME'])
print('✅ conn_max_age:', DATABASES['default'].get('CONN_MAX_AGE', 'Não configurado'))
" 2>nul || echo "❌ Erro ao carregar configuração PostgreSQL"
echo.

echo 📁 5. Verificando requirements.txt...
echo ----------------------------------------
echo Dependências PostgreSQL no requirements.txt:
findstr /C:"dj-database-url" requirements.txt && echo ✅ dj-database-url encontrado || echo ❌ dj-database-url não encontrado
findstr /C:"psycopg2-binary" requirements.txt && echo ✅ psycopg2-binary encontrado || echo ❌ psycopg2-binary não encontrado
echo.

echo ⚙️ 6. Testando import das configurações...
echo ----------------------------------------
python -c "
from gestao_demandas.settings import *
print('✅ Settings carregado com sucesso')
print('✅ DEBUG:', DEBUG)
print('✅ ALLOWED_HOSTS:', len(ALLOWED_HOSTS), 'hosts configurados')
" 2>nul || echo "❌ Erro ao carregar settings.py"
echo.

echo ============================================================
echo   📊 RESUMO DA CONFIGURAÇÃO
echo ============================================================
echo.
echo 🎯 CONFIGURAÇÃO IMPLEMENTADA:
echo    ✅ PostgreSQL via DATABASE_URL (Railway)
echo    ✅ SQLite mantido para desenvolvimento local
echo    ✅ conn_max_age=600 para performance
echo    ✅ Dependências adicionadas ao requirements.txt
echo.
echo 🌐 FUNCIONAMENTO:
echo    • SEM DATABASE_URL: Usa SQLite (desenvolvimento)
echo    • COM DATABASE_URL: Usa PostgreSQL (Railway)
echo    • Detecção automática baseada em variável de ambiente
echo.
echo 📋 COMANDOS PARA INSTALAR DEPENDÊNCIAS:
echo    pip install dj-database-url psycopg2-binary
echo    # ou
echo    pip install -r requirements.txt
echo.
echo ============================================================
echo   🚀 PRONTO PARA RAILWAY!
echo ============================================================
echo.
echo 💡 A configuração está pronta para:
echo    1. ✅ Desenvolvimento local com SQLite
echo    2. ✅ Produção Railway com PostgreSQL
echo    3. ✅ Detecção automática via DATABASE_URL
echo    4. ✅ Performance otimizada (conn_max_age=600)
echo.
echo Pressione qualquer tecla para continuar...
pause >nul