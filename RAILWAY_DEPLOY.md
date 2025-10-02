# 🚀 Deploy no Railway - Configuração Completa

## ✅ **Arquivos Criados/Configurados para Railway**

### 📋 **Estrutura do Deploy:**
```
app-demandas/
├── Procfile                     # Comando de inicialização do Railway
├── runtime.txt                  # Versão do Python (3.11.0)
├── .railwayignore              # Arquivos ignorados no deploy
└── gestao_demandas_projeto/
    ├── requirements.txt         # Dependências atualizadas
    ├── gestao_demandas/
    │   └── settings.py         # Configurações dinâmicas
    └── manage.py
```

---

## ⚙️ **Configurações Implementadas**

### 1. **`Procfile`** (Raiz do repositório)
```
web: cd gestao_demandas_projeto && python manage.py migrate && python manage.py collectstatic --noinput && gunicorn gestao_demandas.wsgi --bind 0.0.0.0:$PORT
```
- ✅ Navega para a pasta do projeto Django
- ✅ Executa migrações automaticamente
- ✅ Coleta arquivos estáticos
- ✅ Inicia Gunicorn na porta fornecida pelo Railway

### 2. **`runtime.txt`** (Raiz do repositório)
```
python-3.11.0
```
- ✅ Especifica Python 3.11 para o Railway

### 3. **`settings.py`** Atualizado
**Configurações Dinâmicas:**
- ✅ **DEBUG** baseado em variável de ambiente
- ✅ **SECRET_KEY** da variável de ambiente (com fallback)
- ✅ **ALLOWED_HOSTS** dinâmico para Railway
- ✅ **DATABASE_URL** automático para PostgreSQL
- ✅ **WhiteNoise** para arquivos estáticos
- ✅ **Configurações de segurança** para produção

### 4. **`requirements.txt`** Atualizado
```
django>=4.2,<5.0
pillow
openpyxl
reportlab
python-dateutil
gunicorn           # Servidor WSGI para produção
dj-database-url    # Parse de DATABASE_URL
psycopg2-binary    # Driver PostgreSQL
whitenoise         # Servir arquivos estáticos
```

### 5. **`.railwayignore`**
- ✅ Exclui arquivos desnecessários do deploy
- ✅ Remove scripts de desenvolvimento local
- ✅ Ignora documentação de rede local
- ✅ Exclui cache e arquivos temporários

---

## 🚀 **Como Fazer Deploy no Railway**

### **Passo 1: Commit das Alterações**
```bash
git add .
git commit -m "Configure project for Railway deployment"
git push
```

### **Passo 2: Conectar ao Railway**
1. **Acesse:** https://railway.app
2. **Login** com GitHub
3. **New Project** → **Deploy from GitHub repo**
4. **Selecione:** `app-demandas`

### **Passo 3: Configurar Variáveis de Ambiente** (Opcional)
No painel do Railway, adicione:
- `SECRET_KEY` - Chave secreta do Django
- `DEBUG` - `False` para produção
- `RAILWAY_PUBLIC_DOMAIN` - Será detectado automaticamente

### **Passo 4: Deploy Automático**
- ✅ Railway detecta o `Procfile` automaticamente
- ✅ Instala dependências do `requirements.txt`
- ✅ Executa migrações e coleta estáticos
- ✅ Inicia aplicação com Gunicorn

---

## 🔧 **Funcionalidades Mantidas**

### **✅ Compatibilidade Local:**
- ✅ Desenvolvimento local continua funcionando
- ✅ SQLite para desenvolvimento
- ✅ Scripts de porta alternativa preservados
- ✅ Configurações de rede local mantidas

### **✅ Funcionalidades Railway:**
- ✅ PostgreSQL automático em produção
- ✅ SSL/HTTPS automático
- ✅ Domínio `.railway.app` automático
- ✅ Escalabilidade automática
- ✅ Deploy contínuo do GitHub

---

## 📊 **Configurações Dinâmicas**

| Configuração | Desenvolvimento | Produção (Railway) |
|-------------|-----------------|-------------------|
| **DEBUG** | `True` | `False` |
| **Banco** | SQLite | PostgreSQL |
| **ALLOWED_HOSTS** | `*` | Domínio Railway |
| **Arquivos Estáticos** | Django dev server | WhiteNoise |
| **Segurança** | Básica | SSL + HSTS |

---

## 🛠️ **Comandos Úteis Pós-Deploy**

### **No Railway Dashboard:**
```bash
# Executar migrações manualmente:
python gestao_demandas_projeto/manage.py migrate

# Criar superuser:
python gestao_demandas_projeto/manage.py createsuperuser

# Ver logs:
# Use o painel do Railway
```

### **Localmente (para testar):**
```bash
# Simular produção localmente:
cd gestao_demandas_projeto
pip install -r requirements.txt
export DEBUG=False
export SECRET_KEY="sua-chave-secreta"
python manage.py collectstatic
gunicorn gestao_demandas.wsgi
```

---

## 🎯 **URLs de Acesso**

### **Desenvolvimento Local:**
- `http://localhost:8000` (padrão)
- `http://localhost:8080` (alternativa)
- `http://localhost:3000` (alternativa)

### **Produção Railway:**
- `https://seu-projeto.railway.app`
- Admin: `https://seu-projeto.railway.app/admin/`

---

## 🔍 **Troubleshooting**

### **Se o deploy falhar:**
1. **Verifique logs** no Railway Dashboard
2. **Confirme estrutura** de pastas correta
3. **Verifique requirements.txt** está atualizado
4. **Teste localmente** com as mesmas configurações

### **Se aplicação não carregar:**
1. **Verifique variáveis** de ambiente
2. **Confirme migrações** foram executadas
3. **Verifique ALLOWED_HOSTS** no Railway
4. **Check logs** para erros específicos

---

## 🎉 **Status da Configuração**

### ✅ **DEPLOY PRONTO:**
- ✅ **Procfile** criado e configurado
- ✅ **Runtime** especificado (Python 3.11)
- ✅ **Settings.py** configurado dinamicamente
- ✅ **Requirements.txt** atualizado
- ✅ **RailwayIgnore** configurado
- ✅ **Compatibilidade local** mantida
- ✅ **Documentação** completa

**🚀 Faça commit e push para deployar no Railway!**