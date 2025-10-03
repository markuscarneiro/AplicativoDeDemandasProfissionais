# ⚙️ Configurações de Deploy

Esta pasta contém arquivos de configuração para deploy em produção.

## 📁 Arquivos de Configuração

### **Procfile**
Arquivo de configuração para Railway/Heroku que define:
- Comandos de release (migrações, collectstatic)
- Comando web (gunicorn)
- Processo de criação de superusuário

### **runtime.txt**
Define a versão do Python para o ambiente de produção.
- Versão atual: Python 3.11.x

## 🚀 Deploy Automático

### Railway
1. Conecte o repositório
2. Configure variáveis de ambiente:
   - `DATABASE_URL` (automático)
   - `SECRET_KEY`
   - `DEBUG=False`
   - `DJANGO_SUPERUSER_*` (opcional)

### Heroku
1. Crie app: `heroku create nome-app`
2. Configure add-ons: `heroku addons:create heroku-postgresql:hobby-dev`
3. Configure variáveis: `heroku config:set SECRET_KEY=...`
4. Deploy: `git push heroku main`

## 🔧 Variáveis de Ambiente

### Obrigatórias:
- `DATABASE_URL` - URL do banco PostgreSQL
- `SECRET_KEY` - Chave secreta Django

### Opcionais:
- `DEBUG` - Modo debug (default: False)
- `ALLOWED_HOSTS` - Hosts permitidos
- `DJANGO_SUPERUSER_USERNAME` - Username do admin
- `DJANGO_SUPERUSER_EMAIL` - Email do admin
- `DJANGO_SUPERUSER_PASSWORD` - Senha do admin

## 📋 Processo de Deploy

1. **Build:** Instala dependências (`requirements.txt`)
2. **Release:** 
   - Executa migrações (`migrate`)
   - Cria superusuário (`create_superuser.py`)
   - Coleta estáticos (`collectstatic`)
3. **Web:** Inicia servidor (`gunicorn`)

## 🔍 Verificação

Após deploy, verifique:
- ✅ Site carregando
- ✅ Admin acessível
- ✅ Banco conectado
- ✅ Arquivos estáticos servindo

## 🛠️ Troubleshooting

### Problemas Comuns:
1. **Erro 500:** Verifique `DEBUG=True` temporariamente
2. **Banco não conecta:** Verifique `DATABASE_URL`
3. **Estáticos não carregam:** Execute `collectstatic`
4. **Admin não acessa:** Verifique superusuário criado

### Logs:
```bash
# Railway
railway logs

# Heroku
heroku logs --tail
```

---

**Configurações testadas e validadas para produção.**