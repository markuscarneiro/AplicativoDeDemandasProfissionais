"""
Modelos do sistema de gestão de demandas.

Este módulo define os modelos principais para o sistema:
- Tag: Categorização de demandas
- Demanda: Entidade principal de trabalho
- Comentario: Acompanhamento de demandas
- HistoricoAlteracao: Auditoria de mudanças
- AnexoArquivo: Documentos anexados
"""

from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import datetime
import os


# =============================================================================
# CONSTANTES
# =============================================================================

CODIGO_PREFIX = 'DEM'
CODIGO_DIGITS = 3
MAX_FILE_SIZE_MB = 10


# =============================================================================
# MODELO: TAG
# =============================================================================

class Tag(models.Model):
    """
    Modelo para categorização de demandas através de tags.
    
    Attributes:
        nome: Nome único da tag
        cor: Código hexadecimal para identificação visual
    """
    
    nome = models.CharField(
        max_length=50,
        unique=True,
        verbose_name='Nome'
    )
    cor = models.CharField(
        max_length=7,
        default='#6c757d',
        verbose_name='Cor',
        help_text='Código hexadecimal da cor (ex: #FF5733)'
    )

    class Meta:
        ordering = ['nome']
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self) -> str:
        return self.nome


# =============================================================================
# MODELO: DEMANDA
# =============================================================================

class Demanda(models.Model):
    """
    Modelo principal para gestão de demandas profissionais.
    
    Representa uma unidade de trabalho com rastreamento completo
    de status, prioridade, tempo e responsáveis.
    """
    
    # -------------------------------------------------------------------------
    # CHOICES
    # -------------------------------------------------------------------------
    
    class Status(models.TextChoices):
        PENDENTE = 'pendente', 'Pendente'
        ANDAMENTO = 'andamento', 'Em andamento'
        CONCLUIDA = 'concluida', 'Concluída'
        CANCELADA = 'cancelada', 'Cancelada'
        PAUSA = 'pausa', 'Em pausa'
    
    class Criticidade(models.TextChoices):
        BAIXA = 'baixa', 'Baixa'
        MEDIA = 'media', 'Média'
        ALTA = 'alta', 'Alta'
        CRITICA = 'critica', 'Crítica'
    
    class Prioridade(models.IntegerChoices):
        MUITO_BAIXA = 1, '1 - Muito Baixa'
        BAIXA = 2, '2 - Baixa'
        MEDIA = 3, '3 - Média'
        ALTA = 4, '4 - Alta'
        MUITO_ALTA = 5, '5 - Muito Alta'
    
    # Manter compatibilidade com código existente
    STATUS_CHOICES = Status.choices
    CRITICIDADE_CHOICES = Criticidade.choices
    PRIORIDADE_CHOICES = Prioridade.choices
    
    # -------------------------------------------------------------------------
    # CAMPOS PRINCIPAIS
    # -------------------------------------------------------------------------
    
    codigo = models.CharField(
        max_length=20,
        unique=True,
        editable=False,
        verbose_name='Código',
        help_text='Código único gerado automaticamente (DEM-YYYY-NNN)'
    )
    titulo = models.CharField(
        max_length=200,
        verbose_name='Título'
    )
    descricao = models.TextField(
        verbose_name='Descrição'
    )
    solicitante = models.CharField(
        max_length=100,
        verbose_name='Solicitante'
    )
    responsavel = models.CharField(
        max_length=100,
        verbose_name='Responsável'
    )
    projeto = models.CharField(
        max_length=100,
        verbose_name='Projeto'
    )
    
    # -------------------------------------------------------------------------
    # CAMPOS DE DATA
    # -------------------------------------------------------------------------
    
    data_entrada = models.DateField(
        auto_now_add=True,
        verbose_name='Data de Entrada'
    )
    data_prazo = models.DateField(
        verbose_name='Data de Prazo'
    )
    data_conclusao = models.DateField(
        null=True,
        blank=True,
        verbose_name='Data de Conclusão'
    )
    
    # -------------------------------------------------------------------------
    # CAMPOS DE STATUS E PRIORIZAÇÃO
    # -------------------------------------------------------------------------
    
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.PENDENTE,
        verbose_name='Status'
    )
    criticidade = models.CharField(
        max_length=10,
        choices=Criticidade.choices,
        default=Criticidade.MEDIA,
        verbose_name='Criticidade'
    )
    prioridade = models.IntegerField(
        choices=Prioridade.choices,
        default=Prioridade.MEDIA,
        verbose_name='Prioridade'
    )
    
    # -------------------------------------------------------------------------
    # CAMPOS TÉCNICOS
    # -------------------------------------------------------------------------
    
    riscos = models.TextField(
        blank=True,
        verbose_name='Riscos'
    )
    tempo_estimado = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name='Tempo Estimado',
        help_text='Tempo estimado em horas'
    )
    tempo_realizado = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0,
        verbose_name='Tempo Realizado',
        help_text='Tempo realizado em horas'
    )
    
    # -------------------------------------------------------------------------
    # RELACIONAMENTOS
    # -------------------------------------------------------------------------
    
    tags = models.ManyToManyField(
        Tag,
        blank=True,
        related_name='demandas',
        verbose_name='Tags'
    )
    criado_por = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='demandas_criadas',
        verbose_name='Criado por'
    )
    
    # -------------------------------------------------------------------------
    # TIMESTAMPS
    # -------------------------------------------------------------------------
    
    criado_em = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Criado em'
    )
    atualizado_em = models.DateTimeField(
        auto_now=True,
        verbose_name='Atualizado em'
    )

    class Meta:
        ordering = ['-criado_em']
        verbose_name = 'Demanda'
        verbose_name_plural = 'Demandas'
        indexes = [
            models.Index(fields=['status']),
            models.Index(fields=['prioridade']),
            models.Index(fields=['data_prazo']),
            models.Index(fields=['criado_por']),
        ]

    def __str__(self) -> str:
        return f"{self.codigo} - {self.titulo}"
    
    # -------------------------------------------------------------------------
    # MÉTODOS DE PERSISTÊNCIA
    # -------------------------------------------------------------------------
    
    def save(self, *args, **kwargs):
        """
        Salva a demanda gerando código automático e atualizando status.
        
        - Gera código no formato DEM-YYYY-NNN se não existir
        - Atualiza status para CONCLUÍDA se data_conclusao for preenchida
        """
        if not self.codigo:
            self.codigo = self._gerar_codigo()
        
        # Auto-status: data_conclusao preenchida -> status concluída
        if self.data_conclusao and self.status != self.Status.CONCLUIDA:
            self.status = self.Status.CONCLUIDA
        
        super().save(*args, **kwargs)
    
    def _gerar_codigo(self) -> str:
        """Gera código sequencial no formato DEM-YYYY-NNN."""
        ano_atual = datetime.now().year
        prefix = f'{CODIGO_PREFIX}-{ano_atual}-'
        
        ultimo_codigo = Demanda.objects.filter(
            codigo__startswith=prefix
        ).order_by('codigo').last()
        
        if ultimo_codigo:
            try:
                ultimo_numero = int(ultimo_codigo.codigo.split('-')[-1])
                proximo_numero = ultimo_numero + 1
            except (ValueError, IndexError):
                proximo_numero = 1
        else:
            proximo_numero = 1
        
        return f'{prefix}{proximo_numero:0{CODIGO_DIGITS}d}'
    
    def clean(self):
        """
        Validações customizadas do modelo.
        
        Raises:
            ValidationError: Se data_prazo < data_entrada ou
                           se status = CONCLUIDA sem data_conclusao
        """
        errors = {}
        
        # Validar data_prazo >= data_entrada
        if self.data_prazo and self.data_entrada:
            if self.data_prazo < self.data_entrada:
                errors['data_prazo'] = (
                    'A data de prazo não pode ser anterior à data de entrada.'
                )
        
        # Status CONCLUÍDA requer data_conclusao
        if self.status == self.Status.CONCLUIDA and not self.data_conclusao:
            errors['data_conclusao'] = (
                'A data de conclusão é obrigatória quando o status for "Concluída".'
            )
        
        if errors:
            raise ValidationError(errors)
    
    # -------------------------------------------------------------------------
    # PROPERTIES
    # -------------------------------------------------------------------------
    
    @property
    def esta_atrasada(self) -> bool:
        """
        Verifica se a demanda está atrasada.
        
        Returns:
            True se o prazo já passou e a demanda não está concluída/cancelada
        """
        status_finalizados = {self.Status.CONCLUIDA, self.Status.CANCELADA}
        if self.status in status_finalizados:
            return False
        return timezone.now().date() > self.data_prazo
    
    @property
    def dias_restantes(self) -> int:
        """Retorna o número de dias até o prazo (negativo se atrasado)."""
        return (self.data_prazo - timezone.now().date()).days
    
    @property
    def percentual_tempo(self) -> float:
        """Retorna o percentual de tempo realizado vs estimado."""
        if self.tempo_estimado and self.tempo_estimado > 0:
            return float((self.tempo_realizado / self.tempo_estimado) * 100)
        return 0.0


# =============================================================================
# MODELO: COMENTÁRIO
# =============================================================================

class Comentario(models.Model):
    """
    Modelo para comentários e acompanhamento das demandas.
    
    Permite que usuários adicionem observações e atualizações
    sobre o andamento de uma demanda.
    """
    
    demanda = models.ForeignKey(
        Demanda,
        on_delete=models.CASCADE,
        related_name='comentarios',
        verbose_name='Demanda'
    )
    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Usuário'
    )
    texto = models.TextField(
        verbose_name='Texto'
    )
    criado_em = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Criado em'
    )

    class Meta:
        ordering = ['-criado_em']
        verbose_name = 'Comentário'
        verbose_name_plural = 'Comentários'

    def __str__(self) -> str:
        return f"Comentário de {self.usuario} em {self.demanda}"


# =============================================================================
# MODELO: HISTÓRICO DE ALTERAÇÃO
# =============================================================================

class HistoricoAlteracao(models.Model):
    """
    Modelo para auditoria de alterações nas demandas.
    
    Registra automáticamente as mudanças de campos para
    rastreabilidade completa.
    """
    
    demanda = models.ForeignKey(
        Demanda,
        on_delete=models.CASCADE,
        related_name='historico',
        verbose_name='Demanda'
    )
    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Usuário'
    )
    campo_alterado = models.CharField(
        max_length=100,
        verbose_name='Campo Alterado'
    )
    valor_anterior = models.TextField(
        blank=True,
        verbose_name='Valor Anterior'
    )
    valor_novo = models.TextField(
        blank=True,
        verbose_name='Valor Novo'
    )
    data_alteracao = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Data da Alteração'
    )

    class Meta:
        ordering = ['-data_alteracao']
        verbose_name = 'Histórico de Alteração'
        verbose_name_plural = 'Histórico de Alterações'

    def __str__(self) -> str:
        return f"{self.usuario} alterou {self.campo_alterado}"


# =============================================================================
# MODELO: ANEXO ARQUIVO
# =============================================================================

class AnexoArquivo(models.Model):
    """
    Modelo para arquivos anexados às demandas.
    
    Suporta diversos formatos de arquivo com controle de tamanho
    e rastreamento de quem enviou.
    """
    
    demanda = models.ForeignKey(
        Demanda,
        on_delete=models.CASCADE,
        related_name='anexos',
        verbose_name='Demanda'
    )
    arquivo = models.FileField(
        upload_to='demandas/%Y/%m/%d/',
        verbose_name='Arquivo'
    )
    nome_original = models.CharField(
        max_length=255,
        verbose_name='Nome Original'
    )
    tamanho = models.BigIntegerField(
        verbose_name='Tamanho',
        help_text='Tamanho em bytes'
    )
    enviado_por = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Enviado por'
    )
    enviado_em = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Enviado em'
    )

    class Meta:
        ordering = ['-enviado_em']
        verbose_name = 'Anexo'
        verbose_name_plural = 'Anexos'

    def __str__(self) -> str:
        return self.nome_original
    
    def save(self, *args, **kwargs):
        """Preenche nome_original e tamanho automaticamente."""
        if self.arquivo:
            self.nome_original = os.path.basename(self.arquivo.name)
            if hasattr(self.arquivo, 'size'):
                self.tamanho = self.arquivo.size
        super().save(*args, **kwargs)
    
    @property
    def tamanho_formatado(self) -> str:
        """
        Retorna o tamanho formatado de forma legível.
        
        Returns:
            Tamanho formatado em bytes, KB, MB ou GB
        """
        bytes_size = self.tamanho
        
        if bytes_size < 1024:
            return f"{bytes_size} bytes"
        elif bytes_size < 1024 ** 2:
            return f"{bytes_size / 1024:.1f} KB"
        elif bytes_size < 1024 ** 3:
            return f"{bytes_size / (1024 ** 2):.1f} MB"
        else:
            return f"{bytes_size / (1024 ** 3):.1f} GB"

