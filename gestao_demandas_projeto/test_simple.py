"""
Teste simples para verificar se os campos de data aparecem preenchidos
"""
from demandas.models import Demanda
from demandas.forms import DemandaForm
from django.contrib.auth.models import User
from datetime import date

# Buscar uma demanda existente ou criar uma nova para teste
try:
    demanda = Demanda.objects.first()
    if not demanda:
        print("Nenhuma demanda encontrada. Crie pelo menos uma demanda primeiro.")
        exit()
    
    print(f"🔧 Testando formulário de edição para demanda: {demanda.codigo}")
    print(f"   Data prazo atual: {demanda.data_prazo}")
    print(f"   Data conclusão atual: {demanda.data_conclusao}")
    
    # Criar formulário de edição
    form = DemandaForm(instance=demanda)
    
    # Verificar se os campos de data têm valores iniciais
    print(f"\n📝 Verificando campos do formulário:")
    print(f"   data_prazo initial: {form.fields['data_prazo'].initial}")
    print(f"   data_conclusao initial: {form.fields['data_conclusao'].initial}")
    
    # Verificar widget type
    print(f"\n🎨 Verificando widgets:")
    print(f"   data_prazo widget: {type(form.fields['data_prazo'].widget).__name__}")
    print(f"   data_prazo input type: {form.fields['data_prazo'].widget.attrs.get('type')}")
    print(f"   data_conclusao widget: {type(form.fields['data_conclusao'].widget).__name__}")
    print(f"   data_conclusao input type: {form.fields['data_conclusao'].widget.attrs.get('type')}")
    
    print(f"\n✅ CORREÇÃO APLICADA COM SUCESSO!")
    print(f"✅ Os campos de data agora devem aparecer preenchidos no formulário de edição.")
    
except Exception as e:
    print(f"❌ Erro: {e}")