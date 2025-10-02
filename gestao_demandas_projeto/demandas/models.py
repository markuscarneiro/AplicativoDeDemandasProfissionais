from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime
import os

# Create your models here.

class Tag(models.Model):
    """Model para tags/etiquetas das demandas"""
    nome = models.CharField(max_length=50, unique=True)
    cor = models.CharField(
        max_length=7, 
        default='#6c757d', 
        help_text='Código hexadecimal da cor (ex: #FF5733)'
    )
    
    def __str__(self):
        return self.nome
    
    class Meta:
        ordering = ['nome']
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'


class Demanda(models.Model):
    """Model principal para gestão de demandas"""
    
    # Choices para status
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('andamento', 'Em andamento'),
        ('concluida', 'Concluída'),
        ('cancelada', 'Cancelada'),
        ('pausa', 'Em pausa'),
    ]
    
    # Choices para criticidade
    CRITICIDADE_CHOICES = [
        ('baixa', 'Baixa'),
        ('media', 'Média'),
        ('alta', 'Alta'),
        ('critica', 'Crítica'),
    ]
    
    # Choices para prioridade
    PRIORIDADE_CHOICES = [
        (1, '1 - Muito Baixa'),
        (2, '2 - Baixa'),
        (3, '3 - Média'),
        (4, '4 - Alta'),
        (5, '5 - Muito Alta'),
    ]
    
    # Campos principais
    codigo = models.CharField(
        max_length=20, 
        unique=True, 
        help_text='Código único gerado automaticamente (DEM-YYYY-NNN)'
    )
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    solicitante = models.CharField(max_length=100)
    responsavel = models.CharField(max_length=100)
    projeto = models.CharField(max_length=100)
    
    # Datas
    data_entrada = models.DateField(auto_now_add=True)
    data_prazo = models.DateField()
    data_conclusao = models.DateField(null=True, blank=True)
    
    # Status e priorização
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pendente')
    criticidade = models.CharField(max_length=10, choices=CRITICIDADE_CHOICES, default='media')
    prioridade = models.IntegerField(choices=PRIORIDADE_CHOICES, default=3)
    
    # Detalhes técnicos
    riscos = models.TextField(blank=True)
    tempo_estimado = models.DecimalField(
        max_digits=8, 
        decimal_places=2, 
        help_text='Tempo estimado em horas'
    )
    tempo_realizado = models.DecimalField(
        max_digits=8, 
        decimal_places=2, 
        default=0, 
        help_text='Tempo realizado em horas'
    )
    
    # Relacionamentos
    tags = models.ManyToManyField(Tag, blank=True, related_name='demandas')
    criado_por = models.ForeignKey(User, on_delete=models.CASCADE, related_name='demandas_criadas')
    
    # Timestamps
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        """Gera código único automaticamente se não existir e gerencia status automaticamente"""
        if not self.codigo:
            ano_atual = datetime.now().year
            # Busca o último número sequencial do ano atual
            ultimo_codigo = Demanda.objects.filter(
                codigo__startswith=f'DEM-{ano_atual}-'
            ).order_by('codigo').last()
            
            if ultimo_codigo:
                # Extrai o número sequencial do último código
                try:
                    ultimo_numero = int(ultimo_codigo.codigo.split('-')[-1])
                    proximo_numero = ultimo_numero + 1
                except (ValueError, IndexError):
                    proximo_numero = 1
            else:
                proximo_numero = 1
            
            # Gera o código no formato DEM-YYYY-NNN (com 3 dígitos)
            self.codigo = f'DEM-{ano_atual}-{proximo_numero:03d}'
        
        # Lógica automática: Se data_conclusao foi preenchida, alterar status para 'concluida'
        if self.data_conclusao and self.status != 'concluida':
            self.status = 'concluida'
        
        super().save(*args, **kwargs)
    
    def clean(self):
        """Validações customizadas do modelo"""
        from django.core.exceptions import ValidationError
        errors = {}
        
        # Validar que data_prazo >= data_entrada
        if self.data_prazo and self.data_entrada:
            if self.data_prazo < self.data_entrada:
                errors['data_prazo'] = 'A data de prazo não pode ser anterior à data de entrada.'
        
        # Validar que se status = Concluída, deve ter data_conclusao
        # (Removida validação que impedia preenchimento automático de status)
        if self.status == 'concluida' and not self.data_conclusao:
            errors['data_conclusao'] = 'A data de conclusão é obrigatória quando o status for "Concluída".'
        
        if errors:
            raise ValidationError(errors)
    
    @property
    def esta_atrasada(self):
        """Verifica se a demanda está atrasada baseada no prazo"""
        if self.status in ['concluida', 'cancelada']:
            return False
        return timezone.now().date() > self.data_prazo
    
    def __str__(self):
        return f"{self.codigo} - {self.titulo}"
    
    class Meta:
        ordering = ['-criado_em']
        verbose_name = 'Demanda'
        verbose_name_plural = 'Demandas'


class Comentario(models.Model):
    """Model para comentários nas demandas"""
    demanda = models.ForeignKey(Demanda, on_delete=models.CASCADE, related_name='comentarios')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Comentário de {self.usuario} em {self.demanda}"
    
    class Meta:
        ordering = ['-criado_em']
        verbose_name = 'Comentário'
        verbose_name_plural = 'Comentários'


class HistoricoAlteracao(models.Model):
    """Model para registrar histórico de alterações nas demandas"""
    demanda = models.ForeignKey(Demanda, on_delete=models.CASCADE, related_name='historico')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    campo_alterado = models.CharField(max_length=100)
    valor_anterior = models.TextField(blank=True)
    valor_novo = models.TextField(blank=True)
    data_alteracao = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.usuario} alterou {self.campo_alterado}"
    
    class Meta:
        ordering = ['-data_alteracao']
        verbose_name = 'Histórico de Alteração'
        verbose_name_plural = 'Histórico de Alterações'


class AnexoArquivo(models.Model):
    """Model para anexos de arquivos nas demandas"""
    demanda = models.ForeignKey(Demanda, on_delete=models.CASCADE, related_name='anexos')
    arquivo = models.FileField(upload_to='demandas/%Y/%m/%d/')
    nome_original = models.CharField(max_length=255)
    tamanho = models.BigIntegerField(help_text='Tamanho em bytes')
    enviado_por = models.ForeignKey(User, on_delete=models.CASCADE)
    enviado_em = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        """Preenche nome_original e tamanho automaticamente"""
        if self.arquivo:
            self.nome_original = os.path.basename(self.arquivo.name)
            if hasattr(self.arquivo, 'size'):
                self.tamanho = self.arquivo.size
        super().save(*args, **kwargs)
    
    @property
    def tamanho_formatado(self):
        """Retorna o tamanho formatado em KB, MB, GB"""
        bytes_size = self.tamanho
        if bytes_size < 1024:
            return f"{bytes_size} bytes"
        elif bytes_size < 1024 * 1024:
            return f"{bytes_size / 1024:.1f} KB"
        elif bytes_size < 1024 * 1024 * 1024:
            return f"{bytes_size / (1024 * 1024):.1f} MB"
        else:
            return f"{bytes_size / (1024 * 1024 * 1024):.1f} GB"
    
    def __str__(self):
        return self.nome_original
    
    class Meta:
        ordering = ['-enviado_em']
        verbose_name = 'Anexo'
        verbose_name_plural = 'Anexos'
