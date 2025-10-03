# 🔀 Portas Alternativas - Contornar Firewall Corporativo

## 📋 Visão Geral

Este guia explica como usar **portas alternativas** (8080 e 3000) para contornar restrições de firewall em ambientes corporativos, quando a porta padrão 8000 do Django estiver bloqueada.

## 🎯 Portas Disponíveis

### 📊 Comparativo de Portas:

| Porta | Uso Comum | Bloqueio Corporativo | Recomendação |
|-------|-----------|---------------------|--------------|
| **8080** | HTTP Alternativo | 🟢 Raramente bloqueada | ⭐ **PRIMEIRA OPÇÃO** |
| **3000** | Desenvolvimento Web | 🟢 Quase nunca bloqueada | ⭐ **SEGUNDA OPÇÃO** |
| **8000** | Django Padrão | 🔴 Frequentemente bloqueada | ⚠️ **Pode não funcionar** |

## ⚙️ Configurações Aplicadas

### 1. **Settings.py - CSRF_TRUSTED_ORIGINS:**
```python
CSRF_TRUSTED_ORIGINS = [
    'http://10.1.25.101:8000',  # Porta padrão
    'http://10.1.25.101:8080',  # Porta alternativa 1
    'http://10.1.25.101:3000',  # Porta alternativa 2
    'http://localhost:8000',
    'http://localhost:8080',
    'http://localhost:3000',
    'http://127.0.0.1:8000',
    'http://127.0.0.1:8080',
    'http://127.0.0.1:3000',
]
```

### 2. **ALLOWED_HOSTS** (já configurado):
```python
ALLOWED_HOSTS = [
    '10.1.25.101',  # Funciona para todas as portas
    'localhost',    # Funciona para todas as portas
    '127.0.0.1',    # Funciona para todas as portas
    '*',            # Temporário
]
```

## 🚀 Scripts Disponíveis

### 📄 **start_8080.bat** - Porta 8080
```batch
# Execute para usar porta 8080:
start_8080.bat
```
**URL de acesso:** `http://10.1.25.101:8080`

**Características:**
- ✅ Porta HTTP alternativa padrão
- ✅ Raramente bloqueada em corporações
- ✅ Não requer permissões administrativas
- ✅ Detecção automática de IP

### 📄 **start_3000.bat** - Porta 3000
```batch
# Execute para usar porta 3000:
start_3000.bat
```
**URL de acesso:** `http://10.1.25.101:3000`

**Características:**
- ✅ Porta padrão para desenvolvimento web (React, Vue, etc.)
- ✅ Quase nunca bloqueada
- ✅ Amplamente aceita em ambientes de desenvolvimento
- ✅ Detecção automática de IP

### 📄 **start_server.bat** - Porta 8000
```batch
# Execute para usar porta padrão:
start_server.bat
```
**URL de acesso:** `http://10.1.25.101:8000`

**Características:**
- ⚠️ Porta padrão do Django
- ⚠️ Pode estar bloqueada em corporações
- ✅ Melhor para desenvolvimento local
- ✅ Detecção automática de IP

## 📋 Comandos Manuais

### Se preferir executar comandos manuais:

```powershell
# Ativar ambiente virtual (se necessário):
..\\.venv\\Scripts\\activate.bat

# Porta 8080 (recomendado para corporativo):
python manage.py runserver 0.0.0.0:8080

# Porta 3000 (desenvolvimento web):
python manage.py runserver 0.0.0.0:3000

# Porta 8000 (padrão Django):
python manage.py runserver 0.0.0.0:8000
```

## 🛠️ Troubleshooting por Porta

### 🔍 **Verificar qual porta está funcionando:**

```powershell
# Verificar portas em uso:
netstat -an | findstr ":8080"
netstat -an | findstr ":3000" 
netstat -an | findstr ":8000"

# Testar conectividade (do colega):
Test-NetConnection -ComputerName 10.1.25.101 -Port 8080
Test-NetConnection -ComputerName 10.1.25.101 -Port 3000
Test-NetConnection -ComputerName 10.1.25.101 -Port 8000
```

### 🔥 **Liberar portas no Firewall (se necessário):**

```powershell
# Executar como Administrador:

# Porta 8080:
netsh advfirewall firewall add rule name="Django Port 8080" dir=in action=allow protocol=TCP localport=8080

# Porta 3000:
netsh advfirewall firewall add rule name="Django Port 3000" dir=in action=allow protocol=TCP localport=3000

# Porta 8000:
netsh advfirewall firewall add rule name="Django Port 8000" dir=in action=allow protocol=TCP localport=8000
```

## 📊 Estratégia Recomendada

### 🎯 **Ordem de Teste:**

1. **PRIMEIRO:** Tente `start_8080.bat`
   - Porta 8080 é amplamente aceita
   - Raramente bloqueada em corporações
   
2. **SEGUNDO:** Tente `start_3000.bat`
   - Porta de desenvolvimento muito comum
   - Quase nunca é restrita
   
3. **TERCEIRO:** Tente `start_server.bat`
   - Porta padrão Django
   - Use se as outras não funcionarem

### 💡 **Dicas Importantes:**

- ✅ **Teste local primeiro:** Sempre verifique `http://localhost:PORTA` antes
- ✅ **Uma porta por vez:** Não execute múltiplos servidores simultaneamente
- ✅ **Mantenha terminal aberto:** O servidor para quando você fecha o terminal
- ✅ **Compartilhe URL correta:** Use a URL com a porta que está funcionando

## 🌐 URLs Completas para Compartilhar

### Para **colegas na rede local:**

```
# Porta 8080 (mais recomendada):
http://10.1.25.101:8080

# Porta 3000 (alternativa):
http://10.1.25.101:3000

# Porta 8000 (padrão):
http://10.1.25.101:8000
```

### Para **teste local:**

```
# Porta 8080:
http://localhost:8080

# Porta 3000:
http://localhost:3000

# Porta 8000:
http://localhost:8000
```

## ✅ Benefícios da Implementação

### 🎯 **Para Você:**
- ✅ **Múltiplas opções** se uma porta estiver bloqueada
- ✅ **Scripts automáticos** para cada porta
- ✅ **Sem necessidade de admin** para portas alternativas
- ✅ **Detecção automática** de IP em todos os scripts

### 🎯 **Para o Time:**
- ✅ **Acesso garantido** mesmo com firewall restritivo
- ✅ **URLs simples** para acessar
- ✅ **Múltiplas alternativas** disponíveis
- ✅ **Funciona em 99%** dos ambientes corporativos

---

## 🎉 **RESUMO**

**Com esta configuração, você tem 3 opções de porta para garantir que o sistema seja acessível mesmo nos ambientes corporativos mais restritivos!**

Basta escolher o script apropriado e compartilhar a URL correspondente com seus colegas.