from PIL import Image, ImageDraw, ImageFont
import os

os.makedirs('photos', exist_ok=True)
os.makedirs('roles', exist_ok=True)

# Шрифт по умолчанию
try:
    font = ImageFont.truetype("arial.ttf", 40)
except:
    font = ImageFont.load_default()

# Фото игроков 185x150 px
for i in range(1, 11):
    img = Image.new('RGB', (185, 150), color=(50, 100, 150))
    d = ImageDraw.Draw(img)
    d.text((70, 50), str(i), font=font, fill=(255, 255, 255))
    img.save(f'photos/{i}.png')

# Значки ролей 16x16 px
roles = ['don','sheriff','mafia','peaceful']
colors = [(200,0,0),(0,200,0),(0,0,200),(200,200,0)]
for r,c in zip(roles, colors):
    img = Image.new('RGB', (16,16), color=c)
    img.save(f'roles/{r}.png')
