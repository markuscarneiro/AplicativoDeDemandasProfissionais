@echo off
echo ============================================================
echo   🧪 TESTE - CONFIGURAÇÃO POSTGRESQL RAILWAY
echo ============================================================

REM Ativar ambiente virtual
if exist "..\\.venv\\Scripts\\activate.bat" (
    call "..\\.venv\\Scripts\\activate.bat"
)

echo 🔍 Testando configuração com DATABASE_URL...
echo.

python teste_postgresql_railway.py

echo.
echo 🔍 Testando sem DATABASE_URL (desenvolvimento)...
echo.

REM Remover DATABASE_URL temporariamente
set DATABASE_URL=
python -c "
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gestao_demandas.settings')
import django
django.setup()
from django.conf import settings
db = settings.DATABASES['default']
print('Engine:', db['ENGINE'])
print('SQLite OK' if 'sqlite' in db['ENGINE'] else 'PostgreSQL OK')
"

pause