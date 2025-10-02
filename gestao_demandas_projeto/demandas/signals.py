from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Demanda, HistoricoAlteracao
import json


@receiver(pre_save, sender=Demanda)
def capture_demanda_changes(sender, instance, **kwargs):
    """Captura as alterações antes de salvar para registrar no histórico"""
    if instance.pk:  # Se é uma alteração (não criação)
        try:
            # Busca o objeto original
            original = Demanda.objects.get(pk=instance.pk)
            
            # Lista de campos a monitorar
            campos_monitorados = [
                'titulo', 'descricao', 'solicitante', 'responsavel', 'projeto',
                'data_prazo', 'data_conclusao', 'status', 'criticidade', 'prioridade',
                'riscos', 'tempo_estimado', 'tempo_realizado'
            ]
            
            # Armazena as alterações temporariamente no objeto
            instance._alteracoes_pendentes = []
            
            for campo in campos_monitorados:
                valor_original = getattr(original, campo)
                valor_novo = getattr(instance, campo)
                
                # Converte valores para string para comparação
                if valor_original != valor_novo:
                    # Converte valores especiais para exibição
                    if campo in ['status', 'criticidade']:
                        valor_original_display = getattr(original, f'get_{campo}_display')() if valor_original else ''
                        valor_novo_display = getattr(instance, f'get_{campo}_display')() if valor_novo else ''
                    else:
                        valor_original_display = str(valor_original) if valor_original is not None else ''
                        valor_novo_display = str(valor_novo) if valor_novo is not None else ''
                    
                    instance._alteracoes_pendentes.append({
                        'campo': campo,
                        'valor_anterior': valor_original_display,
                        'valor_novo': valor_novo_display
                    })
                    
        except Demanda.DoesNotExist:
            # Objeto não existe ainda (primeira criação)
            instance._alteracoes_pendentes = []


@receiver(post_save, sender=Demanda)
def register_demanda_changes(sender, instance, created, **kwargs):
    """Registra as alterações no histórico após salvar"""
    if not created and hasattr(instance, '_alteracoes_pendentes'):
        # Busca o usuário atual (se disponível no contexto)
        # Nota: Em um contexto real, você precisaria passar o usuário via thread local ou contexto
        try:
            # Para fins de demonstração, vamos usar o criador da demanda
            # Em produção, você implementaria thread local storage para capturar o usuário atual
            usuario_alteracao = instance.criado_por
            
            for alteracao in instance._alteracoes_pendentes:
                HistoricoAlteracao.objects.create(
                    demanda=instance,
                    usuario=usuario_alteracao,
                    campo_alterado=alteracao['campo'],
                    valor_anterior=alteracao['valor_anterior'],
                    valor_novo=alteracao['valor_novo']
                )
        except Exception as e:
            # Em caso de erro, registra uma alteração genérica
            HistoricoAlteracao.objects.create(
                demanda=instance,
                usuario=instance.criado_por,
                campo_alterado='sistema',
                valor_anterior='',
                valor_novo=f'Demanda alterada automaticamente: {str(e)}'
            )
        
        # Limpa as alterações pendentes
        delattr(instance, '_alteracoes_pendentes')


# Funções auxiliares para obter display dos campos choices
def get_field_display(instance, field_name):
    """Retorna o display name de um campo choice"""
    try:
        return getattr(instance, f'get_{field_name}_display')()
    except AttributeError:
        return getattr(instance, field_name, '')


# Thread Local Storage para capturar usuário atual (implementação opcional)
import threading

_thread_locals = threading.local()

def get_current_user():
    """Retorna o usuário atual do thread local"""
    return getattr(_thread_locals, 'user', None)

def set_current_user(user):
    """Define o usuário atual no thread local"""
    _thread_locals.user = user


class CurrentUserMiddleware:
    """Middleware para capturar o usuário atual"""
    
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if hasattr(request, 'user') and request.user.is_authenticated:
            set_current_user(request.user)
        else:
            set_current_user(None)
            
        response = self.get_response(request)
        
        # Limpa o usuário após a requisição
        set_current_user(None)
        
        return response