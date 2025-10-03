# INSTRUÇÕES PARA ADICIONAR IMAGEM DE FUNDO

## Opção 1: Imagem Personalizada (Recomendado)

1. **Encontre uma imagem adequada:**
   - Resolução: 1920x1080 ou superior
   - Formato: JPG, PNG ou WebP
   - Tamanho: Máximo 2MB
   - Estilo: Preferencialmente com pouco detalhe no centro

2. **Baixe e renomeie:**
   - Renomeie para: `background-login.jpg`
   - Coloque neste diretório: `demandas/static/demandas/images/`

3. **Sugestões de sites para imagens gratuitas:**
   - [Unsplash](https://unsplash.com/s/photos/corporate-background)
   - [Pexels](https://www.pexels.com/search/office%20background/)
   - [Pixabay](https://pixabay.com/images/search/business%20background/)

## Opção 2: Gerar Imagem com Python (Se disponível)

```bash
# Instale a biblioteca Pillow
pip install Pillow

# Execute o script
python create_background_image.py
```

## Opção 3: Usar Apenas Gradiente

Se preferir não usar imagem, você pode usar apenas gradientes:

1. **Edite o template** `templates/registration/login.html`
2. **Substitua** a linha:
   ```html
   <div class="login-page-body">
   ```
3. **Por uma destas opções:**
   ```html
   <!-- Gradiente profissional -->
   <div class="login-page-body gradient-only gradient-professional">
   
   <!-- Gradiente moderno -->
   <div class="login-page-body gradient-only gradient-modern">
   
   <!-- Gradiente animado -->
   <div class="login-page-body gradient-only gradient-animated">
   ```

## Opção 4: URLs de Imagens de Exemplo

Você pode baixar uma dessas imagens como exemplo:

1. **Corporate Blue**: https://images.unsplash.com/photo-1557804506-669a67965ba0?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80

2. **Modern Office**: https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80

3. **Abstract Tech**: https://images.unsplash.com/photo-1451187580459-43490279c0fa?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80

4. **Minimal Gradient**: https://images.unsplash.com/photo-1506905925346-21bda4d32df4?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80

**Para baixar:**
1. Clique com botão direito na URL
2. "Salvar como..." ou "Save image as..."
3. Renomeie para `background-login.jpg`
4. Coloque em `demandas/static/demandas/images/`

## Status Atual

🔄 **Aguardando**: Imagem de fundo personalizada
✅ **Pronto**: Sistema de CSS e templates
✅ **Funcionando**: Fallback com gradiente

O sistema já está funcionando com gradiente de fallback. 
Quando você adicionar a imagem, ela será carregada automaticamente!