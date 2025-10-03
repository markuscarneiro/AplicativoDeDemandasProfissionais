#!/usr/bin/env python3
"""
Teste de configuração do banco Railway
"""
import os

print("🔍 TESTE - PostgreSQL Railway")
print("=" * 40)

# Simular DATABASE_URL do Railway
test_database_url = "postgresql://postgres:password@localhost:5432/railway"
os.environ['DATABASE_URL'] = test_database_url

print(f"📋 DATABASE_URL (simulada): {test_database_url}")

try:
    # Testar configuração
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gestao_demandas.settings')
    import django
    django.setup()
    
    from django.conf import settings
    
    db_config = settings.DATABASES['default']
    print("\n🗃️ CONFIGURAÇÃO DETECTADA:")
    print(f"  Engine: {db_config['ENGINE']}")
    print(f"  Name: {db_config['NAME']}")
    print(f"  Host: {db_config['HOST']}")
    print(f"  Port: {db_config['PORT']}")
    print(f"  User: {db_config['USER']}")
    
    if 'postgresql' in db_config['ENGINE']:
        print("\n✅ PostgreSQL configurado corretamente!")
    else:
        print("\n❌ Ainda usando SQLite!")
        
except Exception as e:
    print(f"\n❌ ERRO: {e}")

print("=" * 40)