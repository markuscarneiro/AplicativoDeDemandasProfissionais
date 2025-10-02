# INSTRUÇÕES DE COMANDOS - DJANGO GESTÃO DE DEMANDAS

## ATIVAÇÃO DO AMBIENTE VIRTUAL
### Windows:
```bash
.venv\Scripts\activate
```

### Linux/Mac:
```bash
source .venv/bin/activate
```

## COMANDOS DJANGO ESSENCIAIS

### Verificar projeto:
```bash
python manage.py check
```

### Executar o servidor de desenvolvimento:
```bash
python manage.py runserver
```

### Criar migrações:
```bash
python manage.py makemigrations
```

### Aplicar migrações:
```bash
python manage.py migrate
```

### Criar superusuário:
```bash
python manage.py createsuperuser
```

### Coletar arquivos estáticos:
```bash
python manage.py collectstatic
```

## COMANDOS ÚTEIS PARA DESENVOLVIMENTO

### Shell do Django:
```bash
python manage.py shell
```

### Executar testes:
```bash
python manage.py test
```

### Ver SQL das migrações:
```bash
python manage.py sqlmigrate demandas 0001
```

## ESTRUTURA DO PROJETO CRIADA:

```
gestao_demandas_projeto/
├── .venv/                          # Ambiente virtual Python
├── gestao_demandas/                # Configurações do projeto Django
│   ├── __init__.py
│   ├── settings.py                 # Configurações principais
│   ├── urls.py                     # URLs principais
│   ├── wsgi.py
│   └── asgi.py
├── demandas/                       # App principal
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py                     # URLs do app
│   ├── views.py                    # Views do app
│   └── migrations/
├── media/                          # Arquivos de upload
├── static/                         # Arquivos estáticos
├── manage.py                       # Script de gerenciamento Django
├── db.sqlite3                      # Banco de dados SQLite
└── requirements.txt                # Dependências do projeto
```