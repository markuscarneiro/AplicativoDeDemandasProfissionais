#!/usr/bin/env python3
"""
Script de diagnóstico para Railway
Verifica configurações e variáveis de ambiente
"""
import os
import sys

print("🔍 DIAGNÓSTICO RAILWAY - Configuração do Banco")
print("=" * 50)

# Verificar variáveis de ambiente
print("📋 VARIÁVEIS DE AMBIENTE:")
railway_vars = [
    'DATABASE_URL', 
    'RAILWAY_ENVIRONMENT', 
    'RAILWAY_PUBLIC_DOMAIN',
    'PGDATABASE', 'PGUSER', 'PGPASSWORD', 'PGHOST', 'PGPORT',
    'SECRET_KEY', 'DEBUG'
]

for var in railway_vars:
    value = os.environ.get(var)
    if value:
        if 'PASSWORD' in var or 'SECRET' in var:
            print(f"  ✅ {var}: ***DEFINIDA***")
        else:
            print(f"  ✅ {var}: {value}")
    else:
        print(f"  ❌ {var}: NÃO DEFINIDA")

print("\n🗃️ CONFIGURAÇÃO DO BANCO:")

# Tentar importar Django settings
try:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gestao_demandas.settings')
    import django
    django.setup()
    
    from django.conf import settings
    
    db_config = settings.DATABASES['default']
    print(f"  🎯 Engine: {db_config['ENGINE']}")
    
    if 'postgresql' in db_config['ENGINE']:
        print(f"  ✅ PostgreSQL configurado")
        print(f"  📍 Host: {db_config.get('HOST', 'N/A')}")
        print(f"  🔌 Port: {db_config.get('PORT', 'N/A')}")
        print(f"  🗂️  Database: {db_config.get('NAME', 'N/A')}")
        print(f"  👤 User: {db_config.get('USER', 'N/A')}")
    elif 'sqlite' in db_config['ENGINE']:
        print(f"  ⚠️  SQLite configurado (problemático no Railway)")
        print(f"  📁 Arquivo: {db_config.get('NAME', 'N/A')}")
    
    print(f"\n⚙️  DEBUG: {settings.DEBUG}")
    print(f"🌐 ALLOWED_HOSTS: {settings.ALLOWED_HOSTS}")
    
except Exception as e:
    print(f"  ❌ Erro ao carregar settings: {e}")

print("\n🚀 RECOMENDAÇÕES:")
if not os.environ.get('DATABASE_URL') and not os.environ.get('PGHOST'):
    print("  ⚠️  Nenhuma configuração PostgreSQL encontrada!")
    print("  💡 AÇÃO: Configure PostgreSQL service no Railway")
    print("  💡 AÇÃO: Ou defina variáveis PG* manualmente")

print("=" * 50)