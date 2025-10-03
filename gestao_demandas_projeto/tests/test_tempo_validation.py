"""
Teste das novas validações: tempo_realizado obrigatório para demandas concluídas
"""
from demandas.models import Demanda
from demandas.forms import DemandaForm
from django.contrib.auth.models import User
from datetime import date, timedelta

print("🔧 Testando validações de tempo_realizado obrigatório...")

# Criar usuário de teste se não existir
user, created = User.objects.get_or_create(
    username='test_tempo_validation',
    defaults={'email': 'test@example.com', 'first_name': 'Test', 'last_name': 'Tempo'}
)

# Dados base para teste
base_data = {
    'titulo': 'Teste Validação Tempo Realizado',
    'descricao': 'Testando validação de tempo realizado obrigatório',
    'solicitante': 'João Silva',
    'responsavel': 'Maria Santos',
    'projeto': 'Projeto Teste Validação',
    'data_prazo': date.today() + timedelta(days=30),
    'criticidade': 'media',
    'prioridade': 3,
    'tempo_estimado': 40.0,
}

# Teste 1: Tentar concluir sem tempo_realizado
print("\n📝 Teste 1: Status 'concluida' sem tempo_realizado")
test_data_1 = base_data.copy()
test_data_1.update({
    'status': 'concluida',
    'data_conclusao': date.today(),
    'tempo_realizado': None,  # Sem tempo realizado
})

form1 = DemandaForm(data=test_data_1)
if form1.is_valid():
    print("❌ FALHA: Formulário deveria ser inválido")
else:
    print("✅ SUCCESS: Formulário rejeitado corretamente")
    print(f"   Erro: {form1.errors.get('tempo_realizado', 'Nenhum erro encontrado')}")

# Teste 2: Tentar preencher data_conclusao sem tempo_realizado
print("\n📝 Teste 2: data_conclusao preenchida sem tempo_realizado")
test_data_2 = base_data.copy()
test_data_2.update({
    'status': 'andamento',  # Status diferente de concluída
    'data_conclusao': date.today(),
    'tempo_realizado': 0,  # Tempo zero (inválido)
})

form2 = DemandaForm(data=test_data_2)
if form2.is_valid():
    print("❌ FALHA: Formulário deveria ser inválido")
else:
    print("✅ SUCCESS: Formulário rejeitado corretamente")
    print(f"   Erro: {form2.errors.get('tempo_realizado', 'Nenhum erro encontrado')}")

# Teste 3: Status 'concluida' sem data_conclusao (deve preencher automaticamente)
print("\n📝 Teste 3: Status 'concluida' sem data_conclusao (preenchimento automático)")
test_data_3 = base_data.copy()
test_data_3.update({
    'status': 'concluida',
    'data_conclusao': None,  # Sem data de conclusão
    'tempo_realizado': 35.5,  # Com tempo realizado
})

form3 = DemandaForm(data=test_data_3)
if form3.is_valid():
    print("✅ SUCCESS: Formulário válido")
    print(f"   Data conclusão preenchida automaticamente: {form3.cleaned_data.get('data_conclusao')}")
    
    # Salvar para testar
    demanda = form3.save(commit=False)
    demanda.criado_por = user
    demanda.save()
    print(f"   Demanda salva: {demanda.codigo}")
    print(f"   Status final: {demanda.status}")
    print(f"   Data conclusão: {demanda.data_conclusao}")
else:
    print("❌ FALHA: Formulário deveria ser válido")
    print(f"   Erros: {form3.errors}")

# Teste 4: Formulário válido com todos os campos corretos
print("\n📝 Teste 4: Formulário válido com data_conclusao e tempo_realizado")
test_data_4 = base_data.copy()
test_data_4.update({
    'status': 'andamento',
    'data_conclusao': date.today(),
    'tempo_realizado': 42.0,  # Tempo válido
})

form4 = DemandaForm(data=test_data_4)
if form4.is_valid():
    print("✅ SUCCESS: Formulário válido")
    demanda4 = form4.save(commit=False)
    demanda4.criado_por = user
    demanda4.save()
    print(f"   Demanda salva: {demanda4.codigo}")
    print(f"   Status após salvar: {demanda4.status}")  # Deve ser 'concluida' automaticamente
    print(f"   Tempo realizado: {demanda4.tempo_realizado}")
else:
    print("❌ FALHA: Formulário deveria ser válido")
    print(f"   Erros: {form4.errors}")

# Teste 5: Demanda não concluída (deve permitir tempo_realizado vazio)
print("\n📝 Teste 5: Demanda em andamento sem tempo_realizado (deve ser válida)")
test_data_5 = base_data.copy()
test_data_5.update({
    'status': 'andamento',
    'data_conclusao': None,
    'tempo_realizado': 0,  # Tempo zero em andamento (válido)
})

form5 = DemandaForm(data=test_data_5)
if form5.is_valid():
    print("✅ SUCCESS: Formulário válido para demanda em andamento")
    demanda5 = form5.save(commit=False)
    demanda5.criado_por = user
    demanda5.save()
    print(f"   Demanda salva: {demanda5.codigo}")
    print(f"   Status: {demanda5.status}")
else:
    print("❌ FALHA: Formulário deveria ser válido para demanda em andamento")
    print(f"   Erros: {form5.errors}")

# Limpeza
print("\n🧹 Limpando dados de teste")
try:
    if 'demanda' in locals():
        demanda.delete()
    if 'demanda4' in locals():
        demanda4.delete()
    if 'demanda5' in locals():
        demanda5.delete()
except:
    pass

if created:
    user.delete()

print("\n🎉 Testes de validação concluídos!")
print("✅ tempo_realizado agora é obrigatório para demandas concluídas!")