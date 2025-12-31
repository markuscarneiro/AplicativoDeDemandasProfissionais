from django import forms
from django.contrib.auth.models import User
from .models import Demanda, Tag, Comentario, AnexoArquivo


class DemandaForm(forms.ModelForm):
    """Formulário para criação e edição de demandas"""
    
    class Meta:
        model = Demanda
        fields = [
            'titulo', 'descricao', 'solicitante', 'responsavel', 'projeto',
            'data_prazo', 'status', 'criticidade', 'prioridade', 'riscos',
            'tempo_estimado', 'tempo_realizado', 'tags', 'data_conclusao'
        ]
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o título da demanda'
            }),
            'descricao': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Descreva detalhadamente a demanda'
            }),
            'solicitante': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nome do solicitante'
            }),
            'responsavel': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nome do responsável'
            }),
            'projeto': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nome do projeto'
            }),
            'data_prazo': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }, format='%Y-%m-%d'),
            'data_conclusao': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }, format='%Y-%m-%d'),
            'status': forms.Select(attrs={
                'class': 'form-select'
            }),
            'criticidade': forms.Select(attrs={
                'class': 'form-select'
            }),
            'prioridade': forms.Select(attrs={
                'class': 'form-select'
            }),
            'riscos': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Descreva os riscos identificados'
            }),
            'tempo_estimado': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'min': '0',
                'placeholder': 'Horas estimadas'
            }),
            'tempo_realizado': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'min': '0',
                'placeholder': 'Horas realizadas'
            }),
            'tags': forms.CheckboxSelectMultiple(attrs={
                'class': 'form-check-input'
            }),
        }
        labels = {
            'titulo': 'Título *',
            'descricao': 'Descrição *',
            'solicitante': 'Solicitante *',
            'responsavel': 'Responsável *',
            'projeto': 'Projeto *',
            'data_prazo': 'Data Prazo *',
            'data_conclusao': 'Data Conclusão',
            'status': 'Status *',
            'criticidade': 'Criticidade *',
            'prioridade': 'Prioridade *',
            'riscos': 'Riscos',
            'tempo_estimado': 'Tempo Estimado (horas) *',
            'tempo_realizado': 'Tempo Realizado (horas)',
            'tags': 'Tags',
        }
        help_texts = {
            'tempo_estimado': 'Tempo estimado em horas para conclusão',
            'tempo_realizado': 'Tempo já realizado em horas',
            'riscos': 'Identifique possíveis riscos e obstáculos',
            'tags': 'Selecione uma ou mais tags para categorizar a demanda',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Tornar alguns campos obrigatórios
        self.fields['titulo'].required = True
        self.fields['descricao'].required = True
        self.fields['solicitante'].required = True
        self.fields['responsavel'].required = True
        self.fields['projeto'].required = True
        self.fields['data_prazo'].required = True
        self.fields['tempo_estimado'].required = True
        
        # Configurar formatos de entrada para campos de data
        self.fields['data_prazo'].input_formats = ['%Y-%m-%d']
        self.fields['data_conclusao'].input_formats = ['%Y-%m-%d']
        
        # Formatar datas para campos de entrada quando existe uma instância (edição)
        if self.instance and self.instance.pk:
            if self.instance.data_prazo:
                self.fields['data_prazo'].initial = self.instance.data_prazo.strftime('%Y-%m-%d')
            if self.instance.data_conclusao:
                self.fields['data_conclusao'].initial = self.instance.data_conclusao.strftime('%Y-%m-%d')
    
    def clean(self):
        """Validações customizadas do formulário"""
        cleaned_data = super().clean()
        data_entrada = cleaned_data.get('data_entrada')
        data_prazo = cleaned_data.get('data_prazo')
        data_conclusao = cleaned_data.get('data_conclusao')
        status = cleaned_data.get('status')
        tempo_realizado = cleaned_data.get('tempo_realizado')
        
        # Validar que data_prazo >= data_entrada
        if data_prazo and data_entrada:
            if data_prazo < data_entrada:
                raise forms.ValidationError({
                    'data_prazo': 'A data de prazo não pode ser anterior à data de entrada.'
                })
        
        # Se status = Concluída mas data_conclusao estiver vazia, preencher automaticamente
        if status == 'concluida' and not data_conclusao:
            from django.utils import timezone
            cleaned_data['data_conclusao'] = timezone.now().date()
            data_conclusao = cleaned_data['data_conclusao']
        
        # Validar tempo_realizado obrigatório para demandas concluídas
        demanda_sera_concluida = status == 'concluida' or data_conclusao
        
        if demanda_sera_concluida:
            if tempo_realizado is None or tempo_realizado <= 0:
                raise forms.ValidationError({
                    'tempo_realizado': 'O campo Tempo Realizado é obrigatório para concluir a demanda.'
                })
        
        return cleaned_data


class ComentarioForm(forms.ModelForm):
    """Formulário para adicionar comentários"""
    
    class Meta:
        model = Comentario
        fields = ['texto']
        widgets = {
            'texto': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Digite seu comentário...',
                'required': True
            })
        }
        labels = {
            'texto': 'Comentário'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['texto'].required = True


class AnexoForm(forms.ModelForm):
    """Formulário para upload de anexos"""
    
    class Meta:
        model = AnexoArquivo
        fields = ['arquivo']
        widgets = {
            'arquivo': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': '.pdf,.doc,.docx,.xls,.xlsx,.png,.jpg,.jpeg,.gif,.txt,.zip,.rar',
                'required': True
            })
        }
        labels = {
            'arquivo': 'Arquivo'
        }
        help_texts = {
            'arquivo': 'Formatos aceitos: PDF, DOC, DOCX, XLS, XLSX, PNG, JPG, JPEG, GIF, TXT, ZIP, RAR'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['arquivo'].required = True

    def clean_arquivo(self):
        arquivo = self.cleaned_data.get('arquivo')
        if arquivo:
            # Limitar tamanho do arquivo (10MB)
            if arquivo.size > 10 * 1024 * 1024:
                raise forms.ValidationError('O arquivo não pode ser maior que 10MB.')
            
            # Verificar extensão
            extensoes_permitidas = [
                '.pdf', '.doc', '.docx', '.xls', '.xlsx', 
                '.png', '.jpg', '.jpeg', '.gif', '.txt', 
                '.zip', '.rar'
            ]
            nome_arquivo = arquivo.name.lower()
            if not any(nome_arquivo.endswith(ext) for ext in extensoes_permitidas):
                raise forms.ValidationError(
                    'Formato de arquivo não permitido. '
                    'Formatos aceitos: PDF, DOC, DOCX, XLS, XLSX, PNG, JPG, JPEG, GIF, TXT, ZIP, RAR'
                )
        
        return arquivo


class BuscaFiltroForm(forms.Form):
    """Formulário para busca e filtros na listagem"""
    
    search = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Buscar por título, descrição ou código...'
        })
    )
    
    status = forms.ChoiceField(
        choices=[('', 'Todos os status')] + Demanda.STATUS_CHOICES,
        required=False,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    
    prioridade = forms.ChoiceField(
        choices=[('', 'Todas as prioridades')] + Demanda.PRIORIDADE_CHOICES,
        required=False,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    
    projeto = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Projeto...'
        })
    )
    
    responsavel = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Responsável...'
        })
    )
    
    tag = forms.ModelChoiceField(
        queryset=Tag.objects.all(),
        required=False,
        empty_label='Todas as tags',
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    
    data_inicio = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date'
        })
    )
    
    data_fim = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date'
        })
    )
    
    order_by = forms.ChoiceField(
        choices=[
            ('-criado_em', 'Mais recentes'),
            ('criado_em', 'Mais antigas'),
            ('data_prazo', 'Prazo (mais próximo)'),
            ('-data_prazo', 'Prazo (mais distante)'),
            ('-prioridade', 'Prioridade (maior)'),
            ('prioridade', 'Prioridade (menor)'),
            ('status', 'Status (A-Z)'),
            ('-status', 'Status (Z-A)'),
        ],
        required=False,
        initial='-criado_em',
        widget=forms.Select(attrs={'class': 'form-select'})
    )


class TagForm(forms.ModelForm):
    """Formulário para criação e edição de tags"""
    
    class Meta:
        model = Tag
        fields = ['nome', 'cor']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nome da tag'
            }),
            'cor': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'color',
                'title': 'Escolha a cor da tag'
            })
        }
        labels = {
            'nome': 'Nome',
            'cor': 'Cor'
        }
        help_texts = {
            'nome': 'Nome único para identificar a tag',
            'cor': 'Cor que será exibida na tag (formato hexadecimal)'
        }
    
    def clean_nome(self):
        nome = self.cleaned_data.get('nome')
        if nome:
            nome = nome.strip().title()  # Remove espaços e aplica title case
            
            # Verificar se já existe uma tag com este nome (exceto a atual, se for edição)
            qs = Tag.objects.filter(nome__iexact=nome)
            if self.instance.pk:
                qs = qs.exclude(pk=self.instance.pk)
            
            if qs.exists():
                raise forms.ValidationError('Já existe uma tag com este nome.')
                
        return nome
    
    def clean_cor(self):
        cor = self.cleaned_data.get('cor')
        if cor:
            # Validar formato hexadecimal
            import re
            if not re.match(r'^#[0-9A-Fa-f]{6}$', cor):
                raise forms.ValidationError('Formato de cor inválido. Use o formato #RRGGBB (ex: #FF5733)')
        return cor