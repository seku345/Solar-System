from win32api import GetSystemMetrics
from pygame import  *

# Получение размеров окна
H = GetSystemMetrics(0)
V = GetSystemMetrics(1)

# Шрифты
font.init()
FONT = font.Font("Font.ttf", 16)
FONT_TEXT = font.Font("Font.ttf", 32)
FONT_DATE = font.Font("Font.ttf", 100)

# Окно
window = display.set_mode((0, 0), FULLSCREEN)
display.set_caption('Planet Simulation')
background = transform.scale(image.load('Sprites/Background.jpg'), (H, V))

# Цвета
colors = {
        'WHITE': (255, 255, 255),
        'YELLOW': (255, 255, 0),
        'BLUE': (100, 149, 237),
        'RED': (188, 39, 50),
        'DARK_GREY': (80, 78, 81),
        'BEIGE': (233, 182, 136),
        'ORANGE': (237, 140, 44),
        'LIGHT_BLUE': (65, 153, 234),
        'ICE': (95, 231, 233),
        'BROWN': (202, 84, 19)
        }