from win32api import GetSystemMetrics
from pygame import  *

# Получение размеров окна
H = GetSystemMetrics(0)
V = GetSystemMetrics(1)

window = display.set_mode((0, 0), FULLSCREEN)
display.set_caption('Planet Simulation')
background = transform.scale(image.load('Sprites/Background.jpg'), (H, V))