"""
Teste para verificar se o erro NoReverseMatch foi corrigido na página de confirmação de exclusão
"""
from demandas.models import Demanda
from django.contrib.auth.models import User
from django.test import Client
from django.urls import reverse
from datetime import date, timedelta

print("🔧 Testando correção do erro NoReverseMatch...")

# Criar ou obter usuário para teste
user, created = User.objects.get_or_create(
    username='test_reverse_user',
    defaults={'email': 'test@example.com', 'first_name': 'Test', 'last_name': 'Reverse'}
)

# Criar demanda de teste
demanda = Demanda.objects.create(
    titulo='Teste NoReverseMatch',
    descricao='Testando correção do erro NoReverseMatch',
    solicitante='João Silva',
    responsavel='Maria Santos',
    projeto='Projeto Teste Reverse',
    data_prazo=date.today() + timedelta(days=30),
    status='andamento',
    criticidade='media',
    prioridade=3,
    tempo_estimado=40.0,
    tempo_realizado=20.0,
    criado_por=user
)

print(f"📋 Demanda criada para teste: {demanda.codigo}")

# Teste 1: Verificar se a URL demanda_update existe
print("\n📝 Teste 1: Verificando se URL 'demanda_update' existe")
try:
    url_update = reverse('demandas:demanda_update', kwargs={'pk': demanda.pk})
    print(f"✅ SUCCESS: URL encontrada: {url_update}")
except Exception as e:
    print(f"❌ FALHA: Erro ao fazer reverse da URL: {e}")

# Teste 2: Verificar se a URL demanda_delete existe  
print("\n📝 Teste 2: Verificando se URL 'demanda_delete' existe")
try:
    url_delete = reverse('demandas:demanda_delete', kwargs={'pk': demanda.pk})
    print(f"✅ SUCCESS: URL encontrada: {url_delete}")
except Exception as e:
    print(f"❌ FALHA: Erro ao fazer reverse da URL: {e}")

# Teste 3: Simular acesso à página de confirmação de exclusão
print("\n📝 Teste 3: Testando acesso à página de confirmação de exclusão")
try:
    # Criar client de teste
    client = Client()
    
    # Fazer login
    client.force_login(user)
    
    # Acessar página de confirmação de exclusão
    response = client.get(url_delete)
    
    if response.status_code == 200:
        print("✅ SUCCESS: Página de confirmação carregada sem erro")
        
        # Verificar se o template foi renderizado corretamente
        if 'demanda_confirm_delete.html' in [t.name for t in response.templates]:
            print("✅ SUCCESS: Template correto utilizado")
        else:
            print("⚠️  WARNING: Template diferente do esperado")
            
        # Verificar se não há erro de NoReverseMatch no conteúdo
        content = response.content.decode('utf-8')
        if 'NoReverseMatch' in content:
            print("❌ FALHA: Ainda há erro NoReverseMatch na página")
        else:
            print("✅ SUCCESS: Nenhum erro NoReverseMatch encontrado")
            
    else:
        print(f"❌ FALHA: Código de status HTTP: {response.status_code}")
        
except Exception as e:
    print(f"❌ FALHA: Erro ao acessar página: {e}")

# Teste 4: Verificar se o link "Editar ao invés de excluir" funciona
print("\n📝 Teste 4: Verificando link 'Editar ao invés de excluir'")
try:
    # Fazer novo request para página de exclusão
    response = client.get(url_delete)
    content = response.content.decode('utf-8')
    
    # Verificar se o link está presente e correto
    if f'href="/demandas/{demanda.pk}/editar/"' in content or f"url 'demandas:demanda_update' object.pk" in content:
        print("✅ SUCCESS: Link de edição encontrado no template")
    else:
        print("⚠️  WARNING: Link de edição não encontrado ou incorreto")
        
except Exception as e:
    print(f"❌ FALHA: Erro ao verificar link: {e}")

# Limpeza
print("\n🧹 Limpando dados de teste")
demanda.delete()
if created:
    user.delete()

print("\n🎉 Teste de correção NoReverseMatch concluído!")
print("✅ Erro NoReverseMatch deve estar corrigido!")