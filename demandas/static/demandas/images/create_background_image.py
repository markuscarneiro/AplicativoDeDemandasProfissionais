"""
Script para criar uma imagem de fundo de exemplo para o login.
Execute este script para gerar a imagem background-login.jpg
"""

try:
    from PIL import Image, ImageDraw, ImageFont
    import os
    
    def create_background_image():
        # Dimensões da imagem
        width, height = 1920, 1080
        
        # Criar uma nova imagem
        image = Image.new('RGB', (width, height))
        draw = ImageDraw.Draw(image)
        
        # Criar gradiente
        for y in range(height):
            # Gradiente de azul para roxo
            ratio = y / height
            
            # Cores do gradiente
            r1, g1, b1 = 102, 126, 234  # #667eea
            r2, g2, b2 = 118, 75, 162   # #764ba2
            
            r = int(r1 + (r2 - r1) * ratio)
            g = int(g1 + (g2 - g1) * ratio)
            b = int(b1 + (b2 - b1) * ratio)
            
            draw.line([(0, y), (width, y)], fill=(r, g, b))
        
        # Adicionar elementos decorativos
        # Círculos semitransparentes
        overlay = Image.new('RGBA', (width, height), (0, 0, 0, 0))
        overlay_draw = ImageDraw.Draw(overlay)
        
        # Círculo 1
        overlay_draw.ellipse([200, 100, 500, 400], fill=(255, 255, 255, 20))
        
        # Círculo 2
        overlay_draw.ellipse([1400, 200, 1800, 600], fill=(255, 255, 255, 15))
        
        # Círculo 3
        overlay_draw.ellipse([1300, 600, 1700, 1000], fill=(255, 255, 255, 25))
        
        # Círculo 4
        overlay_draw.ellipse([100, 700, 400, 1000], fill=(255, 255, 255, 18))
        
        # Combinar imagem base com overlay
        image = Image.alpha_composite(image.convert('RGBA'), overlay).convert('RGB')
        
        # Caminho para salvar
        output_path = os.path.join(
            os.path.dirname(__file__), 
            '..', 'images', 'background-login.jpg'
        )
        
        # Criar diretório se não existir
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        # Salvar imagem
        image.save(output_path, 'JPEG', quality=85, optimize=True)
        print(f"Imagem criada com sucesso: {output_path}")
        
    if __name__ == "__main__":
        create_background_image()
        
except ImportError:
    print("""
    Para criar a imagem de fundo, instale a biblioteca Pillow:
    
    pip install Pillow
    
    Depois execute:
    python create_background_image.py
    
    Alternativamente, você pode:
    1. Baixar uma imagem de 1920x1080 da internet
    2. Renomear para background-login.jpg
    3. Colocar em: demandas/static/demandas/images/background-login.jpg
    """)
except Exception as e:
    print(f"Erro ao criar imagem: {e}")
    print("""
    Você pode substituir por uma imagem personalizada:
    1. Encontre uma imagem de fundo (1920x1080 recomendado)
    2. Renomeie para background-login.jpg
    3. Coloque em: demandas/static/demandas/images/background-login.jpg
    """)