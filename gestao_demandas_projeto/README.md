# 🚀 Quasar Cronos - Sistema de Gestão de Demandas

<div align="center">

![Django](https://img.shields.io/badge/Django-4.2+-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![Status](https://img.shields.io/badge/Status-Produção-success?style=for-the-badge)

**Sistema completo para gestão estratégica de demandas organizacionais**

[Instalação](#-instalação) • [Funcionalidades](#-funcionalidades) • [Tecnologias](#-tecnologias) • [Documentação](#-documentação)

</div>

---

## � Visão Geral

**Quasar Cronos** é um sistema web robusto desenvolvido em Django para gestão completa de demandas organizacionais. Projetado para equipes que precisam de **rastreabilidade total**, **priorização inteligente** e **análise estratégica** de suas demandas.

### 🎯 **Público-Alvo**
- **Gestores de Projeto** - Controle total do portfólio
- **Equipes de TI** - Rastreamento de tickets e melhorias
- **Departamentos Corporativos** - Organização de solicitações
- **Analistas** - Relatórios e métricas de performance

### 🏗️ **Stack Tecnológica**
- **Backend:** Django 4.2+ (Python)
- **Banco:** SQLite (desenvolvimento) / PostgreSQL (produção)
- **Frontend:** Bootstrap 5.3 + JavaScript ES6
- **Relatórios:** ReportLab (PDF) + OpenPyXL (Excel)

---

## 🔧 Tecnologias - Explicação Didática

### 🖥️ **Backend (Servidor)**

**Django - O "Cérebro" do Sistema**
```python
# Django = Cozinha de um restaurante
# - Recebe pedidos (requests HTTP)
# - Processa receitas (views + models)  
# - Entrega pratos prontos (HTML renderizado)
```

**Vantagens:**
- ✅ **ORM Integrado:** Trabalha com banco sem SQL manual
- ✅ **Admin Automático:** Interface administrativa pronta
- ✅ **Segurança Built-in:** CSRF, autenticação, validações
- ✅ **Signals:** Eventos automáticos (auditoria sem esforço)

**SQLite/PostgreSQL - O "Arquivo" do Sistema**
```sql
-- SQLite: Arquivo único (.db) 
-- PostgreSQL: Servidor robusto para produção
-- Django ORM traduz Python para SQL automaticamente
```

### 🎨 **Frontend (Interface)**

**Bootstrap - O "Designer Profissional"**
```html
<!-- Bootstrap = Kit de móveis IKEA -->
<!-- Componentes prontos: navbar, cards, botões, formulários -->
<div class="card">          <!-- Card pronto -->
<div class="btn btn-primary"> <!-- Botão profissional -->
<div class="row col-md-6">   <!-- Grid responsivo -->
```

**Por que Bootstrap?**
- ✅ **Visual profissional** em minutos
- ✅ **Responsivo automático** (mobile-first)
- ✅ **Consistência** em todos os navegadores
- ✅ **Menos CSS customizado** para manter

**JavaScript - O "Garçom Interativo"**
```javascript
// JavaScript = Garçom que reage após o prato ser servido
// Django entrega a página, JS adiciona interatividade

// Confirmações inteligentes
if (confirm('Tem certeza que deseja excluir?')) { ... }

// Validações em tempo real  
document.getElementById('campo').addEventListener('input', validar);

// Ajax para dados dinâmicos sem recarregar página
fetch('/api/dados').then(response => response.json());
```

**Por que JavaScript?**
- ✅ **Django é estático** após renderizar
- ✅ **JS reage** a cliques, digitação, eventos
- ✅ **UX moderna** sem recarregamentos constantes

### 🔄 **Fluxo de Integração**

```
� Usuário clica → 🌐 Django recebe → 🧠 View processa → 🗄️ Model consulta banco 
→ 📄 Template gera HTML → 🎨 Bootstrap estiliza → ⚡ JavaScript adiciona interatividade 
→ �️ Usuário vê resultado
```

**Analogia Completa:**
- **Django** = Cozinha (processa pedidos)
- **HTML** = Prato (estrutura básica)
- **CSS/Bootstrap** = Decoração (apresentação)
- **JavaScript** = Garçom (interação pós-entrega)
- **SQLite** = Despensa (armazena ingredientes)

---

## ⚡ Funcionalidades

### � **Autenticação & Segurança**
- ✅ Login moderno com background personalizável
- ✅ Controle de acesso por usuário
- ✅ Sessões seguras com timeout automático
- ✅ Proteção CSRF em todos os formulários

### � **Gestão de Demandas**
- ✅ **Código único automático:** `DEM-2025-001` (rastreabilidade total)
- ✅ **CRUD completo:** Criar, listar, editar, excluir
- ✅ **Status inteligente:** Pendente → Andamento → Concluída
- ✅ **Priorização:** Matriz Eisenhower (Urgente/Importante)
- ✅ **Criticidade:** Baixa, Média, Alta, Crítica
- ✅ **Tags coloridas:** Categorização visual
- ✅ **Anexos ilimitados:** Upload de qualquer arquivo
- ✅ **Histórico automático:** Rastreamento de todas as alterações

### 📈 **Dashboard & Analytics**
- ✅ **Matriz Eisenhower visual:** Quadrantes interativos
- ✅ **Gráficos em tempo real:** Status, prioridades, prazos
- ✅ **Métricas-chave:** Demandas em atraso, concluídas, pendentes
- ✅ **Timeline:** Visualização temporal de entregas

### 🔍 **Busca & Filtros**
- ✅ **Busca global:** Por código, título, solicitante
- ✅ **Filtros avançados:** Status, data, responsável, projeto
- ✅ **Ordenação inteligente:** Por prazo, prioridade, atualização
- ✅ **Paginação otimizada:** Performance em grandes volumes

### 📋 **Relatórios & Exportação**
- ✅ **PDF profissional:** Relatórios formatados com ReportLab
- ✅ **Excel completo:** Todas as colunas exportáveis
- ✅ **Filtros aplicados:** Exporta apenas dados filtrados
- ✅ **Metadados inclusos:** Data geração, usuário, critérios

### 🔔 **Notificações & Validações**
- ✅ **Alertas visuais:** Prazos vencidos, status críticos
- ✅ **Validações automáticas:** Datas, campos obrigatórios
- ✅ **Feedback em tempo real:** Confirmações, erros, sucessos
- ✅ **Auditoria completa:** Quem, quando, o que alterou

---

## 🚀 Instalação

### 📋 **Pré-requisitos**
- **Python 3.8+** instalado
- **Git** para clonagem do repositório
- **Rede corporativa** com acesso à porta 8501

### 1️⃣ **Clone do Repositório**
```bash
git clone https://github.com/markuscarneiro/app-demandas.git
cd app-demandas/gestao_demandas_projeto
```

### 2️⃣ **Ambiente Virtual**
```bash
# Windows
python -m venv .venv
.venv\\Scripts\\activate

# Linux/Mac
python3 -m venv .venv
source .venv/bin/activate
```

### 3️⃣ **Dependências**
```bash
pip install -r requirements.txt
```

### 4️⃣ **Configuração do Banco**
```bash
# Criar estrutura do banco
python manage.py makemigrations
python manage.py migrate

# Criar usuário administrador
python manage.py createsuperuser
```

### 5️⃣ **Inicialização**
```bash
# Servidor local (desenvolvimento)
python manage.py runserver 127.0.0.1:8501

# Servidor rede (produção local)
python manage.py runserver 0.0.0.0:8501
```

### 6️⃣ **Acesso ao Sistema**
- **URL Principal:** `http://10.1.25.101:8501`
- **Admin Django:** `http://10.1.25.101:8501/admin`
- **Login:** Use credenciais criadas no passo 4

### 🔧 **Scripts Prontos**
```bash
# Desenvolvimento
scripts/desenvolvimento/start_server.bat

# Diagnóstico
scripts/testes/diagnostico.bat

# Status das portas
scripts/testes/PORTAS_STATUS.bat
```
- **Aplicação:** http://127.0.0.1:8000/
- **Admin:** http://127.0.0.1:8000/admin/

## 🎨 Personalização da Tela de Login

O sistema possui uma tela de login moderna com suporte a imagem de fundo personalizada:

### 🖼️ Configurar Imagem de Fundo

1. **Adicionar sua imagem:**
   ```
   demandas/static/demandas/images/background-login.jpg
   ```

2. **Características recomendadas:**
   - **Resolução:** 1920x1080 ou superior
   - **Formatos:** JPG, PNG, WebP
   - **Tamanho:** Máximo 2MB
   - **Estilo:** Imagens com pouco detalhe no centro

3. **Criar imagem de exemplo:**
   ```powershell
   cd demandas/static/demandas/images/
   python create_background_image.py
   ```

### 🎨 Alternativas com Gradiente

Se preferir usar apenas gradientes (sem imagem), edite o template:

1. **Gradientes disponíveis:**
   - `gradient-professional` - Azul corporativo
   - `gradient-modern` - Cores vibrantes
   - `gradient-dark` - Tons escuros
   - `gradient-ocean` - Azul oceano
   - `gradient-animated` - Gradiente animado

2. **Aplicar gradiente:**
   ```html
   <div class="login-page-body gradient-only gradient-professional">
   ```

3. **CSS adicional:**
   ```css
   @import 'demandas/css/login-gradients.css';
   ```

### 📱 Funcionalidades da Tela de Login

- ✅ **Background responsivo** - Adapta a diferentes telas
- ✅ **Overlay semitransparente** - Melhora legibilidade
- ✅ **Animações suaves** - Efeitos visuais modernos
- ✅ **Fallback automático** - Gradiente se imagem falhar
- ✅ **Dark mode** - Suporte automático
- ✅ **Acessibilidade** - Foco automático e navegação por teclado

### 📄 Documentação Detalhada

Para mais detalhes sobre personalização:
- `demandas/static/demandas/images/README.md` - Guia de imagens
- `demandas/static/demandas/css/login-background.css` - Estilos principais
- `demandas/static/demandas/css/login-gradients.css` - Gradientes alternativos

## 📜 Scripts Disponíveis

### 🔧 Desenvolvimento
- `scripts/desenvolvimento/start_server.bat` - Iniciar servidor local
- `scripts/desenvolvimento/start_3000.bat` - Servidor na porta 3000
- `scripts/desenvolvimento/start_8080.bat` - Servidor na porta 8080
- `scripts/desenvolvimento/gerenciar.bat` - Menu de comandos Django

### 🧪 Testes e Diagnóstico
- `scripts/testes/diagnostico.bat` - Diagnóstico completo
- `scripts/testes/PORTAS_STATUS.bat` - Status das portas
- `scripts/testes/teste_*.bat` - Scripts de teste específicos

### 🚀 Deploy
- `scripts/deploy/criar_superuser.bat` - Criar superusuário

## 🛠️ Tecnologias

- **Backend:** Django 4.2.25
- **Banco:** SQLite (desenvolvimento) / PostgreSQL (produção)
- **Frontend:** Bootstrap 5, HTML5, CSS3
- **Autenticação:** Django Auth
- **Deploy:** Railway/Heroku

## 📖 Documentação

Para informações detalhadas, consulte:
- `docs/DOCUMENTACAO_COMPLETA.md` - Guia completo do sistema
- `docs/COMANDOS.md` - Comandos Django essenciais
- `docs/CHECKLIST.md` - Checklist de verificação
- `docs/IMPLEMENTACAO_COMPLETA_PORTAS.md` - Configuração de portas
- `docs/POSTGRESQL_CONFIG.md` - Configuração PostgreSQL

## 🔧 Configurações Aplicadas

- ✅ **Idioma:** Português Brasileiro (pt-br)
- ✅ **Timezone:** America/Sao_Paulo
- ✅ **Banco:** SQLite/PostgreSQL configurado
- ✅ **Apps:** demandas adicionado
- ✅ **Media/Static:** Configurados
- ✅ **Autenticação:** Sistema completo
- ✅ **Rede Local:** ALLOWED_HOSTS configurado
- ✅ **Deploy:** Railway/Heroku ready

## 📦 Dependências Principais

- Django >=4.2,<5.0
- Pillow (manipulação de imagens)
- openpyxl (arquivos Excel)
- reportlab (geração de PDFs)
- python-dateutil (manipulação de datas)
- dj-database-url (PostgreSQL)
- psycopg2-binary (PostgreSQL driver)
- gunicorn (servidor WSGI)

## 🚀 Deploy

O projeto está configurado para deploy automático no Railway/Heroku:
1. Configure as variáveis de ambiente
2. Faça push para o repositório
3. O deploy é automático via `config/Procfile`

---

**Desenvolvido com ❤️ usando Django**