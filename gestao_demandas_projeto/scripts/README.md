# 🔧 Scripts - Sistema de Gestão de Demandas

Esta pasta contém todos os scripts automatizados organizados por categoria.

## 📁 Estrutura dos Scripts

```
scripts/
├── 📁 desenvolvimento/    # Scripts para desenvolvimento local
├── 📁 testes/           # Scripts de teste e diagnóstico
└── 📁 deploy/           # Scripts para deploy e produção
```

## 🔧 Scripts de Desenvolvimento

### **desenvolvimento/**
- `CONFIGURACAO_COMPLETA.bat` - Setup completo do ambiente
- `gerenciar.bat` - Menu interativo com comandos Django
- `instalar_git.bat` - Instalação automática do Git
- `start_server.bat` - Iniciar servidor na porta padrão (8000)
- `start_3000.bat` - Iniciar servidor na porta 3000
- `start_8080.bat` - Iniciar servidor na porta 8080
- `start_server.sh` - Script Unix para iniciar servidor

## 🧪 Scripts de Teste

### **testes/**
- `diagnostico.bat` - Diagnóstico completo do sistema
- `PORTAS_STATUS.bat` - Status das portas disponíveis
- `SUPERUSER_STATUS.bat` - Status do superusuário
- `teste_banco_config.bat` - Teste de configuração do banco
- `teste_final_corrigido.bat` - Teste final após correções
- `teste_postgresql.bat` - Teste específico PostgreSQL
- `teste_railway.bat` - Teste para deploy Railway
- `teste_railway_subpasta.bat` - Teste Railway com subpastas
- `demo_auto_status.py` - Demonstração de status automático
- `railway_diagnostico.py` - Diagnóstico específico Railway
- `teste_postgresql_railway.py` - Teste PostgreSQL Railway

## 🚀 Scripts de Deploy

### **deploy/**
- `criar_superuser.bat` - Criação automática de superusuário

## 🎯 Como Usar

### Para Desenvolvimento:
1. Execute `desenvolvimento/CONFIGURACAO_COMPLETA.bat` para setup inicial
2. Use `desenvolvimento/gerenciar.bat` para comandos frequentes
3. Inicie o servidor com `desenvolvimento/start_server.bat`

### Para Testes:
1. Execute `testes/diagnostico.bat` para verificação geral
2. Use scripts específicos para testes direcionados
3. Verifique status com `testes/*_STATUS.bat`

### Para Deploy:
1. Configure variáveis de ambiente
2. Execute `deploy/criar_superuser.bat` se necessário
3. Deploy automático via Procfile

## ⚠️ Requisitos

- Windows PowerShell/CMD
- Ambiente virtual Python ativado
- Django configurado
- Dependências instaladas (`requirements.txt`)

## 📝 Manutenção

Para adicionar novos scripts:
1. Coloque na pasta apropriada
2. Use nomenclatura descritiva
3. Adicione comentários explicativos
4. Atualize este índice

---

**Todos os scripts foram testados e validados no ambiente Windows.**