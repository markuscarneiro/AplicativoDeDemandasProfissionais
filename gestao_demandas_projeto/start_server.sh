#!/bin/bash

echo "======================================================"
echo "   🚀 INICIANDO SERVIDOR DJANGO - REDE LOCAL"
echo "======================================================"
echo

# Verificar se estamos no diretório correto
if [ ! -f "manage.py" ]; then
    echo "❌ ERRO: Arquivo manage.py não encontrado!"
    echo "   Certifique-se de estar no diretório do projeto Django."
    echo "   Diretório atual: $(pwd)"
    read -p "Pressione Enter para continuar..."
    exit 1
fi

echo "📁 Diretório do projeto: $(pwd)"
echo

# Ativar ambiente virtual
echo "🔧 Ativando ambiente virtual..."
if [ -f "../.venv/bin/activate" ]; then
    source "../.venv/bin/activate"
    echo "✅ Ambiente virtual ativado"
elif [ -f "venv/bin/activate" ]; then
    source "venv/bin/activate"
    echo "✅ Ambiente virtual ativado"
else
    echo "⚠️  Ambiente virtual não encontrado, tentando executar sem ele..."
fi
echo

# Verificar dependências
echo "🔍 Verificando instalação do Django..."
python -c "import django; print('✅ Django versão:', django.get_version())" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "❌ Django não encontrado! Instalando dependências..."
    pip install -r requirements.txt
fi
echo

# Obter IP atual da máquina
echo "🌐 Verificando IP atual da máquina..."

# Tentar diferentes métodos para obter IP
if command -v ip >/dev/null 2>&1; then
    # Linux com comando ip
    CURRENT_IP=$(ip route get 1.1.1.1 | awk '{print $7; exit}' 2>/dev/null)
elif command -v ifconfig >/dev/null 2>&1; then
    # macOS ou Linux com ifconfig
    CURRENT_IP=$(ifconfig | grep -E "inet.*broadcast" | awk '{print $2}' | head -1)
elif command -v hostname >/dev/null 2>&1; then
    # Fallback usando hostname
    CURRENT_IP=$(hostname -I | awk '{print $1}' 2>/dev/null)
fi

if [ -n "$CURRENT_IP" ]; then
    echo "✅ IP encontrado: $CURRENT_IP"
else
    echo "⚠️  Não foi possível determinar o IP automaticamente"
    CURRENT_IP="SEU_IP_AQUI"
fi
echo

# Verificar se o servidor Django está funcionando
echo "🔍 Verificando configuração do Django..."
python manage.py check --deploy 2>/dev/null
if [ $? -ne 0 ]; then
    echo "⚠️  Executando verificação básica..."
    python manage.py check
fi
echo

# Aplicar migrações se necessário
echo "🔄 Verificando migrações..."
python manage.py migrate --check 2>/dev/null
if [ $? -ne 0 ]; then
    echo "📝 Aplicando migrações pendentes..."
    python manage.py migrate
fi
echo

# Informações importantes
echo "======================================================"
echo "   🎯 INFORMAÇÕES DE ACESSO"
echo "======================================================"
echo
echo "🖥️  ACESSO LOCAL:"
echo "   http://localhost:8000"
echo "   http://127.0.0.1:8000"
echo
echo "🌐 ACESSO REDE LOCAL:"
echo "   http://$CURRENT_IP:8000"
echo
echo "📋 COMPARTILHE ESTA URL COM SEUS COLEGAS:"
echo "   ┌─────────────────────────────────────┐"
echo "   │  http://$CURRENT_IP:8000           │"
echo "   └─────────────────────────────────────┘"
echo
echo "⚠️  REQUISITOS IMPORTANTES:"
echo "   • Mantenha este terminal aberto"
echo "   • Máquina deve estar conectada na rede"
echo "   • Porta 8000 deve estar liberada no Firewall"
echo "   • IP pode mudar se DHCP estiver ativo"
echo
echo "🔥 Para verificar firewall (Ubuntu/Debian):"
echo "   sudo ufw allow 8000"
echo "   sudo ufw status"
echo
echo "======================================================"
echo "   🚀 INICIANDO SERVIDOR..."
echo "======================================================"
echo
echo "🌟 Servidor iniciando em 0.0.0.0:8000..."
echo "📱 Pressione Ctrl+C para parar o servidor"
echo

# Iniciar servidor Django
python manage.py runserver 0.0.0.0:8000

echo
echo "======================================================"
echo "   👋 SERVIDOR FINALIZADO"
echo "======================================================"
echo
echo "Pressione Enter para continuar..."
read