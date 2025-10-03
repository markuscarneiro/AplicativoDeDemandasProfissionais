# 🧪 Testes - Sistema de Gestão de Demandas

Esta pasta contém todos os testes automatizados do sistema.

## 📁 Organização dos Testes

### 🔍 Testes Funcionais
- `test_auto_status.py` - Testes de status automático
- `test_edit_validation.py` - Validação de edição
- `test_forms.py` - Testes de formulários
- `test_reverse_fix.py` - Correções de URL reverse
- `test_shell.py` - Testes via shell Django
- `test_simple.py` - Testes básicos
- `test_tempo_validation.py` - Validação de campos de tempo
- `test_urls_simple.py` - Testes simples de URLs

## 🎯 Como Executar

### Todos os Testes:
```powershell
python manage.py test
```

### Teste Específico:
```powershell
python manage.py test tests.test_forms
```

### Com Verbosidade:
```powershell
python manage.py test --verbosity=2
```

## 📊 Cobertura dos Testes

Os testes cobrem:
- ✅ Modelos (Models)
- ✅ Formulários (Forms)
- ✅ Views e URLs
- ✅ Validações de dados
- ✅ Status automático
- ✅ Funcionalidades principais

## 🔧 Estrutura de Teste

Cada arquivo de teste segue o padrão:
```python
from django.test import TestCase
from django.contrib.auth.models import User
from demandas.models import Demanda

class TesteExample(TestCase):
    def setUp(self):
        # Configuração inicial
        pass
    
    def test_funcionalidade(self):
        # Teste específico
        pass
```

## 📝 Adicionando Novos Testes

1. Crie arquivo `test_nova_funcionalidade.py`
2. Importe classes necessárias
3. Crie classe herdando de `TestCase`
4. Implemente métodos `test_*`
5. Execute para validar

## ⚠️ Requisitos

- Django Test Framework
- Banco de dados de teste (SQLite)
- Dados de teste (`fixtures` se necessário)
- Ambiente virtual ativado

---

**Executar testes regularmente garante a qualidade do código.**