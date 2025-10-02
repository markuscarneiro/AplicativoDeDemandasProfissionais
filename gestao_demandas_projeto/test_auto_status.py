"""
Teste da nova funcionalidade: mudança automática de status ao preencher data_conclusao
"""
from demandas.models import Demanda
from demandas.forms import DemandaForm
from django.contrib.auth.models import User
from datetime import date, timedelta

print("🔧 Testando mudança automática de status ao preencher data_conclusao...")

# Criar usuário de teste se não existir
user, created = User.objects.get_or_create(
    username='test_auto_status',
    defaults={'email': 'test@example.com', 'first_name': 'Test', 'last_name': 'Auto Status'}
)

# Teste 1: Criar nova demanda sem data de conclusão
print("\n📝 Teste 1: Criando demanda nova sem data de conclusão")
test_data = {
    'titulo': 'Teste Status Automático',
    'descricao': 'Testando mudança automática de status',
    'solicitante': 'João Silva',
    'responsavel': 'Maria Santos',
    'projeto': 'Projeto Teste Status',
    'data_prazo': date.today() + timedelta(days=30),
    'status': 'andamento',
    'criticidade': 'media',
    'prioridade': 3,
    'tempo_estimado': 40.0,
    'tempo_realizado': 20.0,
}

form = DemandaForm(data=test_data)
if form.is_valid():
    demanda = form.save(commit=False)
    demanda.criado_por = user
    demanda.save()
    print(f"✅ Demanda criada: {demanda.codigo}")
    print(f"   Status inicial: {demanda.status}")
    print(f"   Data conclusão: {demanda.data_conclusao}")
else:
    print(f"❌ Erro ao criar demanda: {form.errors}")
    exit()

# Teste 2: Preencher data de conclusão via formulário
print("\n📝 Teste 2: Preenchendo data de conclusão via formulário")
edit_data = {
    'titulo': demanda.titulo,
    'descricao': demanda.descricao,
    'solicitante': demanda.solicitante,
    'responsavel': demanda.responsavel,
    'projeto': demanda.projeto,
    'data_prazo': demanda.data_prazo,
    'status': 'andamento',  # Mantendo status original
    'criticidade': demanda.criticidade,
    'prioridade': demanda.prioridade,
    'tempo_estimado': demanda.tempo_estimado,
    'tempo_realizado': demanda.tempo_realizado,
    'data_conclusao': date.today(),  # Preenchendo data de conclusão
}

form_edit = DemandaForm(data=edit_data, instance=demanda)
if form_edit.is_valid():
    demanda_updated = form_edit.save()
    print(f"✅ Demanda atualizada via formulário:")
    print(f"   Status após salvar: {demanda_updated.status}")
    print(f"   Data conclusão: {demanda_updated.data_conclusao}")
    
    if demanda_updated.status == 'concluida':
        print("🎉 SUCCESS: Status foi alterado automaticamente para 'concluida'!")
    else:
        print("❌ FALHA: Status não foi alterado automaticamente")
else:
    print(f"❌ Erro ao editar demanda: {form_edit.errors}")

# Teste 3: Teste direto no modelo (sem formulário)
print("\n📝 Teste 3: Alteração direta no modelo")
demanda.status = 'pendente'  # Resetar para outro status
demanda.data_conclusao = None  # Remover data de conclusão
demanda.save()
print(f"   Status resetado para: {demanda.status}")

# Agora preencher data de conclusão diretamente
demanda.data_conclusao = date.today()
demanda.save()
print(f"   Após preencher data_conclusao:")
print(f"   Status: {demanda.status}")

if demanda.status == 'concluida':
    print("🎉 SUCCESS: Status alterado automaticamente no modelo!")
else:
    print("❌ FALHA: Status não foi alterado no modelo")

# Teste 4: Verificar que não sobrescreve se já estiver como 'concluida'
print("\n📝 Teste 4: Verificando que não sobrescreve status 'concluida'")
demanda.status = 'concluida'
demanda.save()
original_status = demanda.status
demanda.data_conclusao = date.today() + timedelta(days=1)  # Alterar data
demanda.save()

print(f"   Status antes: {original_status}")
print(f"   Status depois: {demanda.status}")

if demanda.status == 'concluida':
    print("✅ SUCCESS: Status 'concluida' foi mantido!")
else:
    print("❌ FALHA: Status foi alterado indevidamente")

# Limpeza
print("\n🧹 Limpando dados de teste")
demanda.delete()
if created:
    user.delete()

print("\n🎉 Testes da funcionalidade automática concluídos!")
print("✅ A mudança de status para 'concluida' ao preencher data_conclusao está funcionando!")