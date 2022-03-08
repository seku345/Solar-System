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


    def __init__(self, planet_image, planet_x, planet_y, radius, mass, sun):
        super().__init__()

        self.image = transform_scale(image.load(planet_image), (self.radius, self.radius))
        self.planet_x = planet_x
        self.planet_y = planet_y
        self.radius = radius
        self.mass = mass

        self.x_vel = 0
        self.y_vel = 0

        self.distance_to_sun = 0
        self.orbit = []



        

# Главная функция
def main():
    
    # Настройка экрана
    H = GetSystemMetrics(0)
    V = GetSystemMetrics(1)

    window = display.set_mode((0, 0), FULLSCREEN)
    display.set_caption('Planet Simulation')
    background = transform.scale(image.load('Sprites/Background.jpg'), (H, V))

    clock = time.Clock()

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