# 👤 Criação Automática de Superusuário Django

## 📋 **Arquivos Criados**

### **1. `create_superuser.py`**
Script Python para criar superusuário automaticamente usando variáveis de ambiente.

### **2. `criar_superuser.bat`**
Script batch Windows para facilitar o uso do `create_superuser.py`.

### **3. `Procfile` Atualizado**
Procfile agora inclui criação automática de superusuário no deploy Railway.

---

## 🎯 **Como Funciona**

### **Variáveis de Ambiente (Opcionais):**
- `DJANGO_SUPERUSER_USERNAME` - Username do admin (padrão: `admin`)
- `DJANGO_SUPERUSER_EMAIL` - Email do admin (padrão: `admin@example.com`)
- `DJANGO_SUPERUSER_PASSWORD` - Senha do admin (padrão: `admin123`)

### **Comportamento:**
- ✅ **Não recria** se usuário já existir
- ✅ **Usa padrões** se variáveis não estiverem definidas
- ✅ **Compatível** com desenvolvimento local e Railway
- ✅ **Seguro** - não sobrescreve usuários existentes

---

## 🚀 **Como Usar**

### **Desenvolvimento Local:**

#### **Opção 1 - Script Batch (Recomendado):**
```batch
# Na pasta gestao_demandas_projeto:
criar_superuser.bat
```

#### **Opção 2 - Diretamente:**
```bash
cd gestao_demandas_projeto
python create_superuser.py
```

#### **Opção 3 - Com Variáveis Personalizadas:**
```batch
set DJANGO_SUPERUSER_USERNAME=meuadmin
set DJANGO_SUPERUSER_EMAIL=admin@meusite.com
set DJANGO_SUPERUSER_PASSWORD=minhasenha123
python create_superuser.py
```

### **Railway (Automático):**
O superusuário será criado automaticamente no deploy com as variáveis definidas no Railway ou valores padrão.

---

## ⚙️ **Configuração no Railway**

### **1. Definir Variáveis de Ambiente (Opcional):**
No painel do Railway, adicione:
- `DJANGO_SUPERUSER_USERNAME=admin`
- `DJANGO_SUPERUSER_EMAIL=admin@exemplo.com`
- `DJANGO_SUPERUSER_PASSWORD=suasenhasegura123`

### **2. Deploy Automático:**
O `Procfile` agora executa:
1. Migrações (`python manage.py migrate`)
2. **Criação de superusuário** (`python create_superuser.py`)
3. Coleta de estáticos (`python manage.py collectstatic`)
4. Início do servidor (`gunicorn`)

---

## 🔍 **Código do `create_superuser.py`**

```python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gestao_demandas.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')
email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@example.com')
password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', 'admin123')

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print(f'Superusuário {username} criado com sucesso!')
else:
    print(f'Superusuário {username} já existe.')
```

---

## 📊 **Cenários de Uso**

### **Desenvolvimento Local:**
```bash
# Primeiro setup:
python manage.py migrate
python create_superuser.py
# Output: Superusuário admin criado com sucesso!

# Execução posterior:
python create_superuser.py
# Output: Superusuário admin já existe.
```

### **Railway Deploy:**
```
# No deploy, automaticamente:
python manage.py migrate
python create_superuser.py  # <- Novo!
python manage.py collectstatic --noinput
gunicorn gestao_demandas.wsgi
```

### **Personalizado:**
```bash
# Com suas credenciais:
export DJANGO_SUPERUSER_USERNAME=joao
export DJANGO_SUPERUSER_EMAIL=joao@empresa.com
export DJANGO_SUPERUSER_PASSWORD=senhaforte123
python create_superuser.py
# Output: Superusuário joao criado com sucesso!
```

---

## 🛠️ **Troubleshooting**

### **Erro: "no such table: auth_user"**
```bash
# Solução: Execute migrações primeiro
python manage.py migrate
python create_superuser.py
```

### **Erro: ModuleNotFoundError**
```bash
# Solução: Ative ambiente virtual
.venv\Scripts\activate  # Windows
python create_superuser.py
```

### **Script não encontra Django:**
```bash
# Solução: Instale dependências
pip install -r requirements.txt
python create_superuser.py
```

---

## 🔒 **Segurança**

### **⚠️ Importante para Produção:**
1. **Sempre defina** `DJANGO_SUPERUSER_PASSWORD` no Railway
2. **Não use** senha padrão (`admin123`) em produção
3. **Considere** criar usuário específico após deploy
4. **Monitore** logs de criação de usuário

### **Recomendações:**
```bash
# Para produção, use senhas fortes:
DJANGO_SUPERUSER_PASSWORD=MinhaSenh@Segura123!

# Considere email real:
DJANGO_SUPERUSER_EMAIL=admin@suaempresa.com

# Username específico:
DJANGO_SUPERUSER_USERNAME=administrador
```

---

## 🎉 **Benefícios**

### ✅ **Para Desenvolvimento:**
- **Setup rápido** - um comando cria admin
- **Sem interação** - totalmente automatizado
- **Repetível** - pode executar múltiplas vezes
- **Flexível** - usa variáveis ou padrões

### ✅ **Para Produção (Railway):**
- **Deploy automático** - admin criado no deploy
- **Configurável** - via variáveis de ambiente
- **Seguro** - não sobrescreve existentes
- **Logs claros** - mostra se criou ou já existia

---

## 📋 **Status dos Arquivos**

### ✅ **Criados:**
- `gestao_demandas_projeto/create_superuser.py`
- `gestao_demandas_projeto/criar_superuser.bat`

### ✅ **Atualizados:**
- `Procfile` - Inclui `python create_superuser.py`

### 🎯 **Pronto para:**
- ✅ Desenvolvimento local
- ✅ Deploy no Railway
- ✅ Customização via variáveis
- ✅ Uso automatizado

---

**🚀 Agora você tem criação automática de superusuário tanto localmente quanto no Railway!**