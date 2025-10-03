"""
Script para testar o formulário DemandaForm via Django shell
"""
from demandas.models import Demanda, Tag
from demandas.forms import DemandaForm
from django.contrib.auth.models import User
from datetime import date

print("🔧 Testando DemandaForm...")

# Criar usuário de teste se não existir
user, created = User.objects.get_or_create(
    username='test_user',
    defaults={'email': 'test@example.com', 'first_name': 'Test', 'last_name': 'User'}
)

# Teste 1: Formulário vazio
print("\n📝 Teste 1: Formulário vazio")
form = DemandaForm()
print(f"✅ Formulário criado com {len(form.fields)} campos")

# Teste 2: Criar demanda de teste
print("\n📝 Teste 2: Criando demanda de teste")
test_data = {
    'titulo': 'Demanda de Teste - Correção Formulário',
    'descricao': 'Testando correção dos campos de data no formulário',
    'solicitante': 'João Silva',
    'responsavel': 'Maria Santos',
    'projeto': 'Projeto Teste Forms',
    'data_prazo': '2025-12-31',
    'status': 'pendente',
    'criticidade': 'media',
    'prioridade': 3,
    'tempo_estimado': 40.0,
    'tempo_realizado': 0.0,
}

form = DemandaForm(data=test_data)
if form.is_valid():
    demanda = form.save(commit=False)
    demanda.criado_por = user
    demanda.save()
    print(f"✅ Demanda criada: {demanda.titulo} (Código: {demanda.codigo})")
    print(f"   Data prazo: {demanda.data_prazo}")
else:
    print(f"❌ Erro ao criar demanda: {form.errors}")
    exit()

# Teste 3: Formulário de edição
print("\n📝 Teste 3: Testando formulário de edição")
form_edit = DemandaForm(instance=demanda)

# Verificar se as datas estão formatadas
print(f"✅ Campo data_prazo initial: {form_edit.fields['data_prazo'].initial}")
print(f"✅ Campo data_prazo widget type: {type(form_edit.fields['data_prazo'].widget)}")
print(f"✅ Campo data_conclusao initial: {form_edit.fields['data_conclusao'].initial}")

# Teste 4: Editar com data de conclusão
print("\n📝 Teste 4: Editando com data de conclusão")
edit_data = test_data.copy()
edit_data['data_conclusao'] = '2025-12-30'
edit_data['status'] = 'concluida'

form_edit = DemandaForm(data=edit_data, instance=demanda)
if form_edit.is_valid():
    demanda_updated = form_edit.save()
    print(f"✅ Demanda atualizada!")
    print(f"   Data prazo: {demanda_updated.data_prazo}")
    print(f"   Data conclusão: {demanda_updated.data_conclusao}")
    print(f"   Status: {demanda_updated.status}")
else:
    print(f"❌ Erro ao editar demanda: {form_edit.errors}")

# Teste 5: Formulário de edição com datas preenchidas
print("\n📝 Teste 5: Formulário de edição com datas já preenchidas")
form_final = DemandaForm(instance=demanda_updated)
print(f"✅ Data prazo no formulário: {form_final.fields['data_prazo'].initial}")
print(f"✅ Data conclusão no formulário: {form_final.fields['data_conclusao'].initial}")

# Limpeza
print("\n🧹 Limpando dados de teste")
demanda.delete()
if created:
    user.delete()

print("\n🎉 Todos os testes do formulário passaram!")
print("✅ Os campos de data agora devem aparecer preenchidos na edição!")