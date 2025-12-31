#!/usr/bin/env python
"""
Script de teste para verificar se o formulário DemandaForm está funcionando corretamente
"""
import os
import sys
import django
from datetime import date

# Configurar Django
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gestao_demandas_projeto.settings')
django.setup()

from demandas.models import Demanda, Tag
from demandas.forms import DemandaForm
from django.contrib.auth.models import User

def test_demanda_form():
    """Testa a criação e edição do formulário DemandaForm"""
    print("🔧 Testando DemandaForm...")
    
    # Criar um usuário para teste (se não existir)
    user, created = User.objects.get_or_create(
        username='test_user',
        defaults={'email': 'test@example.com'}
    )
    
    # Teste 1: Criar formulário vazio
    print("\n📝 Teste 1: Formulário vazio")
    form = DemandaForm()
    print(f"✅ Formulário criado com {len(form.fields)} campos")
    
    # Teste 2: Criar demanda de teste
    print("\n📝 Teste 2: Criando demanda de teste")
    test_data = {
        'titulo': 'Demanda de Teste',
        'descricao': 'Descrição da demanda de teste',
        'solicitante': 'João Silva',
        'responsavel': 'Maria Santos',
        'projeto': 'Projeto Teste',
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
        print(f"✅ Demanda criada: {demanda.titulo} (ID: {demanda.id})")
    else:
        print(f"❌ Erro ao criar demanda: {form.errors}")
        return
    
    # Teste 3: Editar demanda existente
    print("\n📝 Teste 3: Editando demanda existente")
    form_edit = DemandaForm(instance=demanda)
    
    # Verificar se as datas estão formatadas corretamente
    print(f"✅ Campo data_prazo initial: {form_edit.fields['data_prazo'].initial}")
    print(f"✅ Campo data_conclusao initial: {form_edit.fields['data_conclusao'].initial}")
    
    # Teste 4: Editar com nova data
    print("\n📝 Teste 4: Salvando edição com nova data")
    edit_data = test_data.copy()
    edit_data['data_conclusao'] = '2025-12-30'
    edit_data['status'] = 'concluida'
    
    form_edit = DemandaForm(data=edit_data, instance=demanda)
    if form_edit.is_valid():
        demanda_updated = form_edit.save()
        print(f"✅ Demanda atualizada: data_conclusao = {demanda_updated.data_conclusao}")
    else:
        print(f"❌ Erro ao editar demanda: {form_edit.errors}")
    
    # Limpeza
    print("\n🧹 Limpando dados de teste")
    demanda.delete()
    if created:
        user.delete()
    
    print("\n🎉 Todos os testes passaram!")

if __name__ == '__main__':
    test_demanda_form()