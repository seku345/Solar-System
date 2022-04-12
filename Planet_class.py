from math import sqrt, atan2, cos, sin

from pygame import *

from Window import H, V, window

class Planet(sprite.Sprite):

    # Константы
    AU = 149.6e6 * 1000 # Астрономическая единица
    G =  6.7428e-11 # Гравитационная постоянная
    SCALE_K = 250
    SCALE = SCALE_K / AU # 1AU = 100 px
    TIMESTEP = 3600 * 24 # Шаг времени в: 1 секунда равна 1 суткам

    # Инициализация
    def __init__(self, x, y, radius, planet_image, mass, sun= False):
        super().__init__()

        self.planet_image = planet_image
        self.radius = int(radius * self.SCALE_K)
        self.image = transform.scale(image.load(planet_image), (self.radius, self.radius))
        self.x = x
        self.y = y
        self.mass = mass

        self.x_vel = 0
        self.y_vel = 0

        self.distance_to_sun = 0
        self.orbit = []

    # Отрисовка
    def draw(self):
        global H, V
        x = self.x * self.SCALE + H/2 - self.radius/2
        y = self.y * self.SCALE + V/2 - self.radius/2
        
        self.image = transform.scale(image.load(self.planet_image), (self.radius, self.radius))

        window.blit(self.image, (x, y))
