# 📋 Aplicativo de Demandas Profissionais

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.2-green.svg)](https://www.djangoproject.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Railway](https://img.shields.io/badge/Deploy-Railway-purple.svg)](https://railway.app/)

Sistema completo de gestão de demandas profissionais desenvolvido em Django, com dashboard interativo, matriz de Eisenhower, exportação de relatórios e muito mais.

![Dashboard Preview](docs/images/dashboard-preview.png)

---

## 📑 Índice

- [✨ Funcionalidades](#-funcionalidades)
- [🚀 Início Rápido](#-início-rápido)
- [📋 Pré-requisitos](#-pré-requisitos)
- [🔧 Instalação](#-instalação)
- [⚙️ Configuração](#️-configuração)
- [🏃 Executando o Projeto](#-executando-o-projeto)
- [🧪 Testes](#-testes)
- [📁 Estrutura do Projeto](#-estrutura-do-projeto)
- [🛠️ Tecnologias](#️-tecnologias)
- [📊 Modelos de Dados](#-modelos-de-dados)
- [🔐 Segurança](#-segurança)
- [🚢 Deploy](#-deploy)
- [🤝 Contribuindo](#-contribuindo)
- [📄 Licença](#-licença)

---

## ✨ Funcionalidades

### 📊 Dashboard Interativo
- Visão geral das demandas por status
- Gráficos de distribuição
- Alertas de demandas atrasadas ou próximas do prazo
- Métricas de desempenho (tempo médio de conclusão, taxa no prazo)
- Top solicitantes e responsáveis

### 📝 Gestão de Demandas
- CRUD completo de demandas
- Código automático sequencial (DEM-YYYY-NNN)
- Status: Pendente, Em Andamento, Concluída, Cancelada, Em Pausa
- Criticidade: Baixa, Média, Alta, Crítica
- Prioridade: 1 a 5 (Muito Baixa a Muito Alta)
- Controle de tempo estimado vs realizado
- Sistema de tags para categorização
- Comentários e histórico de alterações
- Upload de anexos

### 📐 Matriz de Eisenhower
- Organização visual por urgência x importância
- 4 quadrantes para priorização
- Filtros dinâmicos

### 📤 Exportação de Relatórios
- **Excel (.xlsx)**: Planilha formatada com todos os campos
- **PDF**: Relatório profissional com tabela e filtros aplicados

### 🏷️ Gestão de Tags
- Criação de tags coloridas
- Associação múltipla por demanda
- Filtros por tag

### 🔔 Sistema de Notificações
- Alertas de demandas atrasadas
- Notificação de prazos próximos (7 dias)
- API JSON para integração

### 🔐 Autenticação e Segurança
- Sistema de login completo
- Controle de permissões
- Proteção CSRF e XSS
- Suporte a HTTPS em produção

---

## 🚀 Início Rápido

```bash
# Clone o repositório
git clone https://github.com/markuscarneiro/AplicativoDeDemandasProfissionais.git
cd AplicativoDeDemandasProfissionais

# Crie um ambiente virtual
python -m venv venv
venv\Scripts\activate  # Windows
# ou: source venv/bin/activate  # Linux/Mac

# Instale as dependências
pip install -r requirements.txt

# Entre na pasta do projeto
cd gestao_demandas_projeto

# Execute as migrações
python manage.py migrate

# Crie um superusuário
python manage.py createsuperuser

# Inicie o servidor
python manage.py runserver
```

Acesse: http://localhost:8000

---

## 📋 Pré-requisitos

- **Python** 3.10 ou superior
- **pip** (gerenciador de pacotes Python)
- **Git** (para clonar o repositório)
- **Banco de dados**: SQLite (desenvolvimento) ou PostgreSQL (produção)

---

## 🔧 Instalação

### 1. Clone o Repositório

```bash
git clone https://github.com/markuscarneiro/AplicativoDeDemandasProfissionais.git
cd AplicativoDeDemandasProfissionais
```

### 2. Crie um Ambiente Virtual

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/macOS
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as Dependências

```bash
pip install -r requirements.txt
```

### 4. Configure as Variáveis de Ambiente (Opcional)

Crie um arquivo `.env` na raiz do projeto:

```env
SECRET_KEY=sua-chave-secreta-aqui
DEBUG=True
DATABASE_URL=postgres://user:password@host:port/dbname  # Para PostgreSQL
```

---

## ⚙️ Configuração

### Banco de Dados

**Desenvolvimento (SQLite):**
O projeto usa SQLite por padrão. Nenhuma configuração adicional é necessária.

**Produção (PostgreSQL):**
Configure a variável de ambiente `DATABASE_URL`:

```bash
DATABASE_URL=postgres://usuario:senha@host:porta/nome_banco
```

### Variáveis de Ambiente

| Variável | Descrição | Padrão |
|----------|-----------|--------|
| `SECRET_KEY` | Chave secreta do Django | Chave de desenvolvimento |
| `DEBUG` | Modo de debug | `True` |
| `DATABASE_URL` | URL de conexão PostgreSQL | SQLite local |
| `RAILWAY_PUBLIC_DOMAIN` | Domínio do Railway | - |

---

## 🏃 Executando o Projeto

### Desenvolvimento Local

```bash
cd gestao_demandas_projeto

# Aplicar migrações
python manage.py migrate

# Criar superusuário (primeira vez)
python manage.py createsuperuser

# Coletar arquivos estáticos
python manage.py collectstatic --noinput

# Iniciar servidor
python manage.py runserver
```

### Portas Alternativas

```bash
# Porta 8080
python manage.py runserver 8080

# Porta 3000
python manage.py runserver 3000

# Acessível na rede local
python manage.py runserver 0.0.0.0:8000
```

---

## 🧪 Testes

```bash
cd gestao_demandas_projeto

# Executar todos os testes
python manage.py test

# Executar testes específicos
python manage.py test tests.test_forms
python manage.py test tests.test_auto_status

# Com cobertura de código
pip install coverage
coverage run manage.py test
coverage report
```

---

## 📁 Estrutura do Projeto

```
AplicativoDeDemandasProfissionais/
├── 📄 README.md                    # Este arquivo
├── 📄 requirements.txt             # Dependências do projeto
├── 📄 Procfile                     # Configuração para Railway
├── 📄 runtime.txt                  # Versão do Python
│
└── 📂 gestao_demandas_projeto/     # Projeto Django principal
    ├── 📄 manage.py                # CLI do Django
    ├── 📄 db.sqlite3               # Banco de dados local
    │
    ├── 📂 gestao_demandas/         # Configurações do projeto
    │   ├── 📄 settings.py          # Configurações principais
    │   ├── 📄 urls.py              # URLs principais
    │   ├── 📄 wsgi.py              # WSGI para produção
    │   └── 📄 asgi.py              # ASGI (async)
    │
    ├── 📂 demandas/                # App principal
    │   ├── 📄 models.py            # Modelos de dados
    │   ├── 📄 views.py             # Views e lógica
    │   ├── 📄 forms.py             # Formulários
    │   ├── 📄 urls.py              # URLs do app
    │   ├── 📄 admin.py             # Configuração do admin
    │   ├── 📄 signals.py           # Signals (histórico)
    │   │
    │   ├── 📂 templates/           # Templates HTML
    │   ├── 📂 static/              # CSS, JS, Imagens
    │   └── 📂 migrations/          # Migrações do banco
    │
    ├── 📂 templates/               # Templates globais
    │   ├── 📄 base.html            # Template base
    │   └── 📂 registration/        # Templates de login
    │
    ├── 📂 static/                  # Arquivos estáticos globais
    ├── 📂 media/                   # Uploads de usuários
    ├── 📂 tests/                   # Testes automatizados
    ├── 📂 scripts/                 # Scripts auxiliares
    └── 📂 docs/                    # Documentação adicional
```

---

## 🛠️ Tecnologias

### Backend
- **Django 4.2** - Framework web Python
- **Python 3.10+** - Linguagem de programação
- **SQLite / PostgreSQL** - Bancos de dados

### Frontend
- **Bootstrap 5** - Framework CSS
- **Chart.js** - Gráficos interativos
- **JavaScript** - Interatividade

### Bibliotecas Python
- **openpyxl** - Geração de arquivos Excel
- **reportlab** - Geração de PDFs
- **Pillow** - Processamento de imagens
- **python-dateutil** - Manipulação de datas
- **whitenoise** - Servir arquivos estáticos
- **gunicorn** - Servidor WSGI
- **dj-database-url** - Configuração de banco de dados
- **psycopg2-binary** - Driver PostgreSQL

---

## 📊 Modelos de Dados

### Demanda
| Campo | Tipo | Descrição |
|-------|------|-----------|
| `codigo` | CharField | Código único (DEM-YYYY-NNN) |
| `titulo` | CharField | Título da demanda |
| `descricao` | TextField | Descrição detalhada |
| `solicitante` | CharField | Nome do solicitante |
| `responsavel` | CharField | Nome do responsável |
| `projeto` | CharField | Projeto associado |
| `data_entrada` | DateField | Data de criação (auto) |
| `data_prazo` | DateField | Data limite |
| `data_conclusao` | DateField | Data de conclusão |
| `status` | CharField | Status atual |
| `criticidade` | CharField | Nível de criticidade |
| `prioridade` | IntegerField | Prioridade (1-5) |
| `tempo_estimado` | DecimalField | Horas estimadas |
| `tempo_realizado` | DecimalField | Horas realizadas |
| `riscos` | TextField | Riscos identificados |
| `tags` | ManyToMany | Tags associadas |
| `criado_por` | ForeignKey | Usuário criador |

### Tag
| Campo | Tipo | Descrição |
|-------|------|-----------|
| `nome` | CharField | Nome da tag (único) |
| `cor` | CharField | Cor hexadecimal (#RRGGBB) |

### Comentario
| Campo | Tipo | Descrição |
|-------|------|-----------|
| `demanda` | ForeignKey | Demanda associada |
| `usuario` | ForeignKey | Autor do comentário |
| `texto` | TextField | Conteúdo do comentário |
| `criado_em` | DateTimeField | Data/hora de criação |

### AnexoArquivo
| Campo | Tipo | Descrição |
|-------|------|-----------|
| `demanda` | ForeignKey | Demanda associada |
| `arquivo` | FileField | Arquivo enviado |
| `nome_original` | CharField | Nome original |
| `tamanho` | BigIntegerField | Tamanho em bytes |
| `enviado_por` | ForeignKey | Usuário que enviou |
| `enviado_em` | DateTimeField | Data/hora do envio |

---

## 🔐 Segurança

O projeto implementa diversas medidas de segurança:

- ✅ **Proteção CSRF** em todos os formulários
- ✅ **Proteção XSS** contra scripts maliciosos
- ✅ **Clickjacking Protection** (X-Frame-Options: DENY)
- ✅ **Content-Type Sniffing Protection**
- ✅ **HTTPS Redirect** em produção
- ✅ **HSTS** (HTTP Strict Transport Security)
- ✅ **Cookies Seguros** em produção
- ✅ **Validação de senha** robusta

### Recomendações para Produção

1. Gere uma nova `SECRET_KEY`:
   ```python
   from django.core.management.utils import get_random_secret_key
   print(get_random_secret_key())
   ```

2. Configure `DEBUG=False`

3. Use HTTPS com certificado SSL válido

4. Configure o banco de dados PostgreSQL

---

## 🚢 Deploy

### Railway (Recomendado)

1. Crie uma conta no [Railway](https://railway.app/)

2. Conecte seu repositório GitHub

3. Configure as variáveis de ambiente:
   - `SECRET_KEY`
   - `DATABASE_URL` (criado automaticamente com PostgreSQL)

4. O deploy será automático a cada push

### Outras Plataformas

O projeto é compatível com:
- **Heroku**
- **Render**
- **DigitalOcean App Platform**
- **AWS Elastic Beanstalk**
- **VPS tradicional** (com Nginx + Gunicorn)

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Siga os passos:

1. Faça um Fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/NovaFeature`)
3. Commit suas mudanças (`git commit -m 'Adiciona NovaFeature'`)
4. Push para a branch (`git push origin feature/NovaFeature`)
5. Abra um Pull Request

### Padrões de Código

- Siga o **PEP 8** para código Python
- Use **type hints** quando possível
- Adicione **docstrings** em funções e classes
- Escreva **testes** para novas funcionalidades

---

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

---

## 👨‍💻 Autor

**Markus Carneiro**

- GitHub: [@markuscarneiro](https://github.com/markuscarneiro)

---

## 🙏 Agradecimentos

- Django Software Foundation
- Bootstrap Team
- Comunidade Open Source

---

<p align="center">
  Feito com ❤️ em Python/Django
</p>
