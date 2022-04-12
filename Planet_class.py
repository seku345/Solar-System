from math import sqrt, atan2, cos, sin

from pygame import *

from Window import H, V, window

font.init()
FONT = font.Font("Font.ttf", 16)

class Planet(sprite.Sprite):

    # Константы
    AU = 149.6e6 * 1000 # Астрономическая единица
    G =  6.7428e-11 # Гравитационная постоянная
    SCALE_K = 250
    SCALE = SCALE_K / AU # 1AU = 100 px
    TIMESTEP = 3600 * 24 # Шаг времени: 1 секунда равна 1 суткам

    # Инициализация
    def __init__(self, x, y, radius, planet_image, color, mass, sun= False):
        super().__init__()

        self.planet_image = planet_image
        self.radius = radius
        self.image = transform.scale(image.load(planet_image), (self.radius, self.radius))
        self.x = x
        self.y = y
        self.mass = mass
        self.color = color

        self.x_vel = 0
        self.y_vel = 0

        self.distance_to_sun = 0
        self.orbit = []
        
        self.sun = sun

    # Отрисовка
    def draw(self):
        
        x = self.x * self.SCALE + H/2 - self.radius/2
        y = self.y * self.SCALE + V/2 - self.radius/2
        
        if len(self.orbit) > 2:
            updated_points = []
            for point in self.orbit:
                x, y = point
                x = x * self.SCALE + H / 2
                y = y * self.SCALE + V / 2
                updated_points.append((x, y))

            draw.lines(window, self.color, False, updated_points, 2)
            
        window.blit(self.image, (x, y))    
            
        if not self.sun:
            distance_text = FONT.render(f'{round(self.distance_to_sun/1000, 1)}km', 1, (255, 255, 255))
            window.blit(distance_text, (x - distance_text.get_width()/2, y - distance_text.get_height()/2))

    def attraction(self, other):
        other_x, other_y = other.x, other.y
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance = sqrt(distance_x ** 2 + distance_y ** 2)
        
        if other.sun:
            self.distance_to_sun = distance
        
        force = self.G * self.mass * other.mass / distance**2
        theta = atan2(distance_y, distance_x)
        force_x = cos(theta) * force
        force_y = sin(theta) * force
        return force_x, force_y
    
    def update_position(self, planets):
        total_fx = total_fy = 0
        for planet in planets:
            if self == planet:
                continue
        
            fx, fy = self.attraction(planet)
            total_fx += fx
            total_fy = fy
        
        self.x_vel += total_fx / self.mass * self.TIMESTEP
        self.y_vel += total_fy / self.mass * self.TIMESTEP
        
        self.x += self.x_vel * self.TIMESTEP
        self.y += self.y_vel * self.TIMESTEP
        self.orbit.append((self.x, self.y))