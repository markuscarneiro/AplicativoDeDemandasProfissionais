from django.contrib import admin
from .models import Demanda, Tag, Comentario, HistoricoAlteracao, AnexoArquivo

# Register your models here.

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cor']
    search_fields = ['nome']
    ordering = ['nome']


@admin.register(Demanda)
class DemandaAdmin(admin.ModelAdmin):
    list_display = [
        'codigo', 'titulo', 'status', 'prioridade', 
        'data_prazo', 'responsavel', 'criado_por'
    ]
    list_filter = [
        'status', 'prioridade', 'criticidade', 'projeto', 
        'data_entrada', 'data_prazo'
    ]
    search_fields = [
        'codigo', 'titulo', 'descricao', 'solicitante', 
        'responsavel', 'projeto'
    ]
    date_hierarchy = 'data_prazo'
    filter_horizontal = ['tags']
    readonly_fields = ['codigo', 'criado_em', 'atualizado_em']
    
    fieldsets = (
        ('Identificação', {
            'fields': ('codigo', 'titulo', 'descricao')
        }),
        ('Responsabilidades', {
            'fields': ('solicitante', 'responsavel', 'projeto', 'criado_por')
        }),
        ('Datas', {
            'fields': ('data_prazo', 'data_conclusao')
        }),
        ('Status e Priorização', {
            'fields': ('status', 'criticidade', 'prioridade')
        }),
        ('Detalhes Técnicos', {
            'fields': ('riscos', 'tempo_estimado', 'tempo_realizado')
        }),
        ('Tags', {
            'fields': ('tags',)
        }),
        ('Metadados', {
            'fields': ('criado_em', 'atualizado_em'),
            'classes': ('collapse',)
        })
    )
    
    def save_model(self, request, obj, form, change):
        """Define o usuário criador automaticamente se for uma nova demanda"""
        if not change:  # Se é uma nova demanda
            obj.criado_por = request.user
        super().save_model(request, obj, form, change)


@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ['demanda', 'usuario', 'texto_truncado', 'criado_em']
    list_filter = ['demanda', 'usuario', 'criado_em']
    search_fields = ['texto', 'demanda__codigo', 'demanda__titulo']
    readonly_fields = ['criado_em']
    
    def texto_truncado(self, obj):
        """Retorna o texto truncado para exibição na lista"""
        return obj.texto[:50] + "..." if len(obj.texto) > 50 else obj.texto
    texto_truncado.short_description = 'Texto'
    
    def save_model(self, request, obj, form, change):
        """Define o usuário automaticamente se for um novo comentário"""
        if not change:  # Se é um novo comentário
            obj.usuario = request.user
        super().save_model(request, obj, form, change)


@admin.register(HistoricoAlteracao)
class HistoricoAlteracaoAdmin(admin.ModelAdmin):
    list_display = ['demanda', 'usuario', 'campo_alterado', 'data_alteracao']
    list_filter = ['demanda', 'usuario', 'campo_alterado', 'data_alteracao']
    search_fields = ['campo_alterado', 'valor_anterior', 'valor_novo']
    readonly_fields = [
        'demanda', 'usuario', 'campo_alterado', 
        'valor_anterior', 'valor_novo', 'data_alteracao'
    ]
    
    def has_add_permission(self, request):
        """Remove permissão de adicionar (deve ser criado automaticamente)"""
        return False
    
    def has_change_permission(self, request, obj=None):
        """Remove permissão de editar (registro histórico)"""
        return False


@admin.register(AnexoArquivo)
class AnexoArquivoAdmin(admin.ModelAdmin):
    list_display = [
        'demanda', 'nome_original', 'tamanho_formatado', 
        'enviado_por', 'enviado_em'
    ]
    list_filter = ['demanda', 'enviado_por', 'enviado_em']
    search_fields = ['nome_original', 'demanda__codigo', 'demanda__titulo']
    readonly_fields = ['nome_original', 'tamanho', 'enviado_em']
    
    def save_model(self, request, obj, form, change):
        """Define o usuário que enviou automaticamente"""
        if not change:  # Se é um novo anexo
            obj.enviado_por = request.user
        super().save_model(request, obj, form, change)
