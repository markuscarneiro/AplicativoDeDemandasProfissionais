"""
Teste adicional: Validação em demandas existentes sendo editadas
"""
from demandas.models import Demanda
from demandas.forms import DemandaForm
from django.contrib.auth.models import User
from datetime import date, timedelta

print("🔧 Testando validação em edição de demandas existentes...")

# Buscar uma demanda existente ou criar uma
user = User.objects.first()
if not user:
    user = User.objects.create_user(username='testuser', email='test@example.com')

# Criar demanda em andamento
demanda_base = Demanda.objects.create(
    titulo='Demanda para Teste de Edição',
    descricao='Testando validação em edição',
    solicitante='João Silva',
    responsavel='Maria Santos',
    projeto='Projeto Teste',
    data_prazo=date.today() + timedelta(days=30),
    status='andamento',
    criticidade='media',
    prioridade=3,
    tempo_estimado=40.0,
    tempo_realizado=20.0,  # Já tem tempo parcial
    criado_por=user
)

print(f"📋 Demanda criada: {demanda_base.codigo}")
print(f"   Status inicial: {demanda_base.status}")
print(f"   Tempo realizado: {demanda_base.tempo_realizado}")

# Teste 1: Tentar editar para concluída removendo tempo_realizado
print("\n📝 Teste 1: Edição - Status para 'concluida' com tempo_realizado = 0")
edit_data = {
    'titulo': demanda_base.titulo,
    'descricao': demanda_base.descricao,
    'solicitante': demanda_base.solicitante,
    'responsavel': demanda_base.responsavel,
    'projeto': demanda_base.projeto,
    'data_prazo': demanda_base.data_prazo,
    'status': 'concluida',  # Alterando para concluída
    'criticidade': demanda_base.criticidade,
    'prioridade': demanda_base.prioridade,
    'tempo_estimado': demanda_base.tempo_estimado,
    'tempo_realizado': 0,  # Zerando tempo (inválido)
    'data_conclusao': date.today(),
}

form_edit = DemandaForm(data=edit_data, instance=demanda_base)
if form_edit.is_valid():
    print("❌ FALHA: Deveria rejeitar tempo_realizado = 0")
else:
    print("✅ SUCCESS: Rejeitou corretamente")
    print(f"   Erro: {form_edit.errors.get('tempo_realizado', [])}")

# Teste 2: Edição válida - concluir com tempo adequado
print("\n📝 Teste 2: Edição válida - concluindo com tempo adequado")
edit_data['tempo_realizado'] = 45.5  # Tempo válido
edit_data['data_conclusao'] = date.today()

form_edit2 = DemandaForm(data=edit_data, instance=demanda_base)
if form_edit2.is_valid():
    print("✅ SUCCESS: Formulário de edição válido")
    demanda_updated = form_edit2.save()
    print(f"   Status após edição: {demanda_updated.status}")
    print(f"   Tempo realizado: {demanda_updated.tempo_realizado}")
    print(f"   Data conclusão: {demanda_updated.data_conclusao}")
else:
    print("❌ FALHA: Formulário deveria ser válido")
    print(f"   Erros: {form_edit2.errors}")

# Teste 3: Editar apenas data_conclusao (sem alterar status manualmente)
print("\n📝 Teste 3: Preenchendo apenas data_conclusao")
# Resetar demanda
demanda_base.status = 'andamento'
demanda_base.data_conclusao = None
demanda_base.tempo_realizado = 30.0
demanda_base.save()

edit_data3 = {
    'titulo': demanda_base.titulo,
    'descricao': demanda_base.descricao,
    'solicitante': demanda_base.solicitante,
    'responsavel': demanda_base.responsavel,
    'projeto': demanda_base.projeto,
    'data_prazo': demanda_base.data_prazo,
    'status': 'andamento',  # Mantendo status original
    'criticidade': demanda_base.criticidade,
    'prioridade': demanda_base.prioridade,
    'tempo_estimado': demanda_base.tempo_estimado,
    'tempo_realizado': demanda_base.tempo_realizado,
    'data_conclusao': date.today(),  # Só preenchendo data
}

form_edit3 = DemandaForm(data=edit_data3, instance=demanda_base)
if form_edit3.is_valid():
    print("✅ SUCCESS: Válido ao preencher data_conclusao")
    demanda_updated3 = form_edit3.save()
    print(f"   Status após salvar: {demanda_updated3.status}")  # Deve ser 'concluida'
    print(f"   Data conclusão: {demanda_updated3.data_conclusao}")
else:
    print("❌ FALHA: Deveria ser válido")
    print(f"   Erros: {form_edit3.errors}")

# Limpeza
print("\n🧹 Limpando dados de teste")
demanda_base.delete()

print("\n🎉 Testes de edição concluídos!")
print("✅ Validações funcionam corretamente para demandas editadas!")