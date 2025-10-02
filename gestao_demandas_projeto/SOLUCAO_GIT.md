# 🔧 Solução: Git Init não funciona

## ❌ **Problema Identificado**
O comando `git init` não funciona porque **o Git não está instalado** no seu sistema Windows.

## ✅ **Solução Rápida**

### **Passo 1: Instalar o Git**
Execute o script que criei para você:
```powershell
# No diretório do projeto:
instalar_git.bat
```

### **Passo 2: Download Manual (Recomendado)**
1. 🌐 Acesse: **https://git-scm.com/download/win**
2. 📥 Baixe: **"64-bit Git for Windows Setup"**
3. ▶️ Execute o instalador
4. ✅ Use **todas as configurações padrão** (Next, Next, Next...)
5. 🔄 **Feche e reabra** o PowerShell após instalar

### **Passo 3: Verificar Instalação**
```powershell
# Teste se o Git foi instalado:
git --version
```

### **Passo 4: Configurar Git (primeira vez)**
```powershell
# Configure seu nome e email:
git config --global user.name "Seu Nome"
git config --global user.email "seu.email@empresa.com"
```

### **Passo 5: Inicializar Repositório**
```powershell
# No diretório do projeto:
cd c:\Users\u8178\app-demandas\gestao_demandas_projeto

# Inicializar repositório:
git init

# Adicionar arquivos:
git add .

# Primeiro commit:
git commit -m "Primeiro commit - sistema de demandas com portas alternativas"
```

## 🎯 **Alternativas de Instalação**

### **Opção 1: Microsoft Store**
1. Abra a **Microsoft Store**
2. Pesquise por **"Git"**
3. Instale **"Git for Windows"**

### **Opção 2: Via Winget (se disponível)**
```powershell
# Execute como Administrador:
winget install --id Git.Git -e --source winget
```

### **Opção 3: Via Chocolatey (se tiver)**
```powershell
# Execute como Administrador:
choco install git
```

## ⚠️ **Importante Após Instalar**

1. **SEMPRE reinicie** o PowerShell após instalar o Git
2. **Verifique** se funcionou: `git --version`
3. **Configure** nome e email antes do primeiro uso
4. **Navegue** até o diretório do projeto antes de `git init`

## 🚀 **Próximos Passos Após Instalar Git**

```powershell
# 1. Navegar para o projeto:
cd c:\Users\u8178\app-demandas\gestao_demandas_projeto

# 2. Inicializar Git:
git init

# 3. Adicionar todos os arquivos:
git add .

# 4. Criar primeiro commit:
git commit -m "Sistema de demandas - configuração completa com portas alternativas"

# 5. Verificar status:
git status

# 6. Ver histórico:
git log --oneline
```

## 📋 **Arquivos que Serão Versionados**
- ✅ Código Django (models, views, forms, templates)
- ✅ Scripts de inicialização (start_8080.bat, start_3000.bat, start_server.bat)
- ✅ Documentação completa (README.md, PORTAS_ALTERNATIVAS.md)
- ✅ Configurações (settings.py, requirements.txt)
- ✅ Scripts de diagnóstico e utilitários

---

## 🎉 **Resumo**
**O `git init` não funciona porque o Git não está instalado. Execute `instalar_git.bat` ou faça download manual do Git em https://git-scm.com/download/win, depois reinicie o PowerShell e tente novamente!**