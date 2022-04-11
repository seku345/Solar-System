# Библиотеки
from pygame import *
from math import *
from win32api import GetSystemMetrics

# Класс планет
class Planet(sprite.Sprite):

    # Константы
    AU = 149.6e6 * 1000 # Астрономическая единица
    G =  6.7428e-11 # Гравитационная постоянная
    SCALE = 250 / AU # 1AU = 100 px
    TIMESTEP = 3600 * 24 # Шаг времени в: 1 секунда равна 1 суткам

    # Инициализация
    def __init__(self, x, y, radius, planet_image, mass, sun= False):
        super().__init__()

        self.image = transform.scale(image.load(planet_image), (self.radius, self.radius))
        self.x = x
        self.y = y
        self.radius = radius
        self.mass = mass

        self.x_vel = 0
        self.y_vel = 0

        self.distance_to_sun = 0
        self.orbit = []

    # Отрисовка
    def update(self, win):
        global H, V
        x = self.x * self.SCALE + H/2
        y = self.y * self.SCALE + V/2

        draw.circle(win, (255, 255, 255), (x, y), self.radius)

        

# Главная функция
def main():
    
    # Настройка экрана
    H = GetSystemMetrics(0)
    V = GetSystemMetrics(1)

    window = display.set_mode((0, 0), FULLSCREEN)
    display.set_caption('Planet Simulation')
    background = transform.scale(image.load('Sprites/Background.jpg'), (H, V))

    clock = time.Clock()

    # Создание планет
    sun = Planet(0, 0, 30, 'Sprites/Sun.png', 1.98892 * 10**30, True)

    mercury = Planet(0.387 * Planet.AU, 0, 8, 'Sprites/Mercury.png', 3.30 * 10**23)
    mercury.y_vel = -47.4 * 1000

    venus = Planet(0.723 * Planet.AU, 0, 14, 'Sprites/Venus.png', 4.8685 * 10**24)
    venus.y_vel = -35.02 * 1000

    earth = Planet(-1 * Planet.AU, 0, 16, 'Sprites/Earth.png', 5.9742 * 10**24)
    earth.y_vel = 29.783 * 1000
    
    mars = Planet(-1.524 * Planet.AU, 0, 12, 'Sprites/Mars.png', 6.39 * 10**23)
    mars.y_vel = 24.077 * 1000
    
    jupiter = Planet(5.204 * Planet.AU, 0, 14, 'Sprites/Jupiter.png', 4.8685 * 10**24)
    jupiter.y_vel = -35.02 * 1000

    saturn = Planet(9.54 * Planet.AU, 0, 14, 'Sprites/Saturn.png', 4.8685 * 10**24)
    saturn.y_vel = -35.02 * 1000
    
    uranus = Planet(18.4 * Planet.AU, 0, 14, 'Sprites/Uranus.png', 4.8685 * 10**24)
    uranus.y_vel = -35.02 * 1000

    neptune = Planet(30 * Planet.AU, 0, 14, 'Sprites/Neptune.png', 4.8685 * 10**24)
    neptune .y_vel = -35.02 * 1000

    pluto = Planet(39.53 * Planet.AU, 0, 14, 'Sprites/Pluto.png', 4.8685 * 10**24)
    pluto.y_vel = -35.02 * 1000
    
    # Основной цикл
    run = True
    while run:

        # Кадры в секунду
        clock.tick(60)
        display.update()

        # Фон
        window.blit(background, (0, 0))

        # Обработка событий
        for e in event.get():

            # Закрытие окна
            if e.type == KEYDOWN and e.key == K_ESCAPE:
                run = False

    quit()

# Запуск
if __name__ == '__main__':
    main()