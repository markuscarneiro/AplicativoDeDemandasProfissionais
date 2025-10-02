# 🚀 AMBIENTE DJANGO CONFIGURADO COM SUCESSO!

## 📁 ESTRUTURA CRIADA

```
c:\Users\u8178\app-demandas\
├── .venv/                          # Ambiente virtual Python
└── gestao_demandas_projeto/        # Projeto Django
    ├── gestao_demandas/            # Configurações do projeto
    ├── demandas/                   # App principal
    ├── media/                      # Arquivos de upload
    ├── static/                     # Arquivos estáticos
    ├── manage.py                   # Script de gerenciamento
    ├── db.sqlite3                  # Banco de dados
    ├── requirements.txt            # Dependências
    ├── COMANDOS.md                 # Comandos úteis
    └── CHECKLIST.md                # Checklist de verificação
```

## ⚡ COMO USAR

### 1. Ativar o ambiente virtual:
```powershell
# Windows
.venv\Scripts\activate
```

### 2. Navegar para o projeto:
```powershell
cd gestao_demandas_projeto
```

### 3. Executar o servidor:
```powershell
python manage.py runserver
```

### 4. Acessar no navegador:
- **Aplicação:** http://127.0.0.1:8000/
- **Admin:** http://127.0.0.1:8000/admin/

## 🌐 ACESSO NA REDE LOCAL

### 🚀 Como tornar o sistema acessível para colegas na rede:

#### 1. Iniciar servidor para rede local:
```powershell
# Executar no diretório do projeto
python manage.py runserver 0.0.0.0:8000
```

#### 2. URL de acesso para outros usuários:
```
http://10.1.25.101:8000
```

#### 3. Verificar IP atual da máquina:
```powershell
# Windows
ipconfig | findstr "IPv4"

# Ou usar o script automatizado (ver seção Scripts)
```

### ⚠️ REQUISITOS IMPORTANTES:

- ✅ **Máquina precisa estar ligada** e conectada na rede
- ✅ **Não fechar o terminal** onde o servidor está rodando
- ✅ **Porta 8000** deve estar liberada no Firewall do Windows
- ⚠️ **IP pode mudar** se DHCP estiver ativo

### 🔥 FIREWALL DO WINDOWS:

#### Liberar porta 8000:
```powershell
# Executar como Administrador
netsh advfirewall firewall add rule name="Django Server Port 8000" dir=in action=allow protocol=TCP localport=8000
```

#### Verificar se porta está liberada:
```powershell
netsh advfirewall firewall show rule name="Django Server Port 8000"
```

### 🛠️ TROUBLESHOOTING:

#### Se colegas não conseguem acessar:

1. **Verificar se servidor está rodando:**
   ```powershell
   netstat -an | findstr :8000
   ```

2. **Testar conectividade (do computador do colega):**
   ```cmd
   ping 10.1.25.101
   telnet 10.1.25.101 8000
   ```

3. **Se IP mudou, verificar novo IP:**
   ```powershell
   ipconfig | findstr "IPv4"
   ```

4. **Verificar firewall:**
   - Painel de Controle → Sistema e Segurança → Firewall do Windows
   - Verificar se regra para porta 8000 existe

#### Scripts automatizados (ver seção Scripts abaixo)

### 🔀 PORTAS ALTERNATIVAS (para contornar firewall)

Se a porta padrão 8000 estiver bloqueada pelo firewall corporativo, você pode usar portas alternativas que geralmente estão liberadas:

#### 🎯 Portas recomendadas:
- **8080** - Porta HTTP alternativa (quase sempre liberada)
- **3000** - Porta de desenvolvimento web (raramente bloqueada)
- **8000** - Porta padrão do Django

#### 📋 Comandos para portas alternativas:
```powershell
# Servidor na porta 8080 (recomendado para corporativo)
python manage.py runserver 0.0.0.0:8080

# Servidor na porta 3000 (desenvolvimento web)
python manage.py runserver 0.0.0.0:3000

# Servidor na porta 8000 (padrão)
python manage.py runserver 0.0.0.0:8000
```

#### 🌐 URLs de acesso correspondentes:
```
# Porta 8080:
http://10.1.25.101:8080

# Porta 3000:
http://10.1.25.101:3000

# Porta 8000:
http://10.1.25.101:8000
```

#### 🚀 Scripts prontos por porta:
```powershell
# Executar servidor na porta específica:
start_8080.bat   # Porta 8080 (mais compatível com firewall)
start_3000.bat   # Porta 3000 (desenvolvimento web)
start_server.bat # Porta 8000 (padrão)
```

#### 💡 Dica importante:
**Use as portas 8080 ou 3000 se tiver problemas com firewall!** Estas portas geralmente não precisam de permissões de administrador para serem liberadas.

## 🔧 COMANDOS ESSENCIAIS (dentro da pasta do projeto)

```powershell
# Verificar se está tudo OK
python manage.py check

# Criar superusuário
python manage.py createsuperuser

# Criar migrações
python manage.py makemigrations

# Aplicar migrações
python manage.py migrate

# Executar servidor LOCAL
python manage.py runserver

# Executar servidor para REDE LOCAL
python manage.py runserver 0.0.0.0:8000
```

## 📜 SCRIPTS AUTOMATIZADOS

### Windows - start_server.bat
Execute o arquivo `start_server.bat` para:
- ✅ Ativar ambiente virtual automaticamente
- ✅ Verificar e exibir IP atual da máquina
- ✅ Iniciar servidor acessível na rede (0.0.0.0:8000)
- ✅ Exibir URL completa para compartilhar

```batch
# Simplesmente execute:
start_server.bat
```

### Linux/Mac - start_server.sh
Execute o arquivo `start_server.sh` para a mesma funcionalidade no Linux/Mac.

```bash
# Tornar executável (primeira vez):
chmod +x start_server.sh

# Executar:
./start_server.sh
```

## 🛠️ TROUBLESHOOTING DETALHADO

### 🔥 Configuração do Firewall do Windows

#### Método 1 - Linha de comando (Recomendado):
```powershell
# Executar PowerShell como Administrador
netsh advfirewall firewall add rule name="Django Server Port 8000" dir=in action=allow protocol=TCP localport=8000

# Verificar se regra foi criada:
netsh advfirewall firewall show rule name="Django Server Port 8000"

# Remover regra (se necessário):
netsh advfirewall firewall delete rule name="Django Server Port 8000"
```

#### Método 2 - Interface Gráfica:
1. Abrir **Painel de Controle** → **Sistema e Segurança** → **Firewall do Windows Defender**
2. Clicar em **Configurações avançadas**
3. Clicar em **Regras de Entrada** → **Nova Regra**
4. Selecionar **Porta** → **Avançar**
5. Selecionar **TCP** e **Portas locais específicas**: `8000`
6. Selecionar **Permitir a conexão** → **Avançar**
7. Marcar **Domínio**, **Particular** e **Público** → **Avançar**
8. Nome: `Django Server Port 8000` → **Concluir**

### 🌐 Verificação de Conectividade

#### Do seu computador:
```powershell
# Verificar se servidor está rodando
netstat -an | findstr :8000

# Verificar IP atual
ipconfig | findstr "IPv4"

# Testar acesso local
curl http://localhost:8000
```

#### Do computador do colega:
```cmd
# Testar conectividade de rede
ping 10.1.25.101

# Testar se porta está acessível
telnet 10.1.25.101 8000

# Ou usar PowerShell (Windows 10+):
Test-NetConnection -ComputerName 10.1.25.101 -Port 8000
```

### 📱 Problemas Comuns e Soluções

#### 1. "Este site não pode ser acessado"
- ✅ Verificar se servidor está rodando (`netstat -an | findstr :8000`)
- ✅ Verificar se IP está correto (`ipconfig`)
- ✅ Verificar firewall (regra para porta 8000)
- ✅ Tentar acesso local primeiro (`http://localhost:8000`)

#### 2. "Connection refused" ou "Timeout"
- ✅ Máquina host pode estar desligada
- ✅ Servidor Django pode ter parado (verificar terminal)
- ✅ Firewall bloqueando conexão
- ✅ IP pode ter mudado (DHCP)

#### 3. Erro 403 Forbidden
- ✅ Verificar `ALLOWED_HOSTS` no `settings.py`
- ✅ Verificar `CSRF_TRUSTED_ORIGINS`

#### 4. IP mudou (DHCP ativo)
```powershell
# Verificar novo IP
ipconfig | findstr "IPv4"

# Atualizar settings.py se necessário
# Reiniciar servidor com novo IP
```

#### 5. Múltiplas interfaces de rede
```powershell
# Verificar todas as interfaces
ipconfig /all

# Usar IP da interface correta (geralmente Ethernet ou Wi-Fi)
```

### 🔄 Script de Diagnóstico Rápido

Crie um arquivo `diagnostico.bat`:
```batch
@echo off
echo === DIAGNÓSTICO DO SERVIDOR DJANGO ===
echo.
echo 1. Verificando IP atual:
ipconfig | findstr "IPv4"
echo.
echo 2. Verificando se servidor está rodando:
netstat -an | findstr :8000
echo.
echo 3. Verificando regra de firewall:
netsh advfirewall firewall show rule name="Django Server Port 8000"
echo.
pause
```

# Criar migrações
python manage.py makemigrations

# Aplicar migrações
python manage.py migrate

# Executar servidor
python manage.py runserver
```

## ✅ CONFIGURAÇÕES APLICADAS

- ✅ **Idioma:** Português Brasileiro (pt-br)
- ✅ **Timezone:** America/Sao_Paulo
- ✅ **Banco:** SQLite configurado
- ✅ **Apps:** demandas adicionado
- ✅ **Media:** /media/ configurado
- ✅ **Static:** /static/ configurado
- ✅ **Login:** URLs configuradas
- ✅ **Segurança:** Configurações básicas aplicadas
- ✅ **Rede Local:** ALLOWED_HOSTS configurado para 10.1.25.101
- ✅ **CSRF:** CSRF_TRUSTED_ORIGINS configurado
- ✅ **Scripts:** start_server.bat e start_server.sh criados
- ✅ **Diagnóstico:** diagnostico.bat para troubleshooting

## 📦 DEPENDÊNCIAS INSTALADAS

- Django 4.2.25
- Pillow (manipulação de imagens)
- openpyxl (arquivos Excel)
- reportlab (geração de PDFs)
- python-dateutil (manipulação de datas)

## 🎯 TESTE REALIZADO

✅ **Servidor testado com sucesso!**
- Sistema funcionando em http://127.0.0.1:8001/
- Resposta: "Sistema de Gestão de Demandas - Configuração realizada com sucesso!"
- Nenhum erro encontrado no `python manage.py check`

## 📚 ARQUIVOS DE AJUDA CRIADOS

- **COMANDOS.md** - Lista completa de comandos Django
- **CHECKLIST.md** - Checklist detalhado de verificação
- **README.md** - Este arquivo com instruções gerais

## 🔄 PRÓXIMOS PASSOS

1. **Criar superusuário:** `python manage.py createsuperuser`
2. **Desenvolver models** em `demandas/models.py`
3. **Criar templates** em `demandas/templates/`
4. **Implementar views** em `demandas/views.py`
5. **Configurar formulários** em `demandas/forms.py`

---

**🎉 Ambiente de desenvolvimento Django totalmente configurado e funcional!**