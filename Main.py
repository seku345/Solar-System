# Библиотеки
from math import *

from pygame import *

# Параметры окна
from Window import window, background

# Класс планет
from Planet_class import Planet

# Главная функция
def main():

    clock = time.Clock()

    # Создание планет
    sun = Planet(0, 0, 150, 'Sprites/Sun.png', 1.98892 * 10**30, True)

    mercury = Planet(0.387 * Planet.AU, 0, 50, 'Sprites/Mercury.png', 3.30 * 10**23)
    mercury.y_vel = -47.4 * 1000

    venus = Planet(0.723 * Planet.AU, 0, 14, 'Sprites/Venus.png', 4.8685 * 10**24)
    venus.y_vel = -35.02 * 1000

    earth = Planet(-1 * Planet.AU, 0, 16, 'Sprites/Earth.png', 5.9742 * 10**24)
    earth.y_vel = 29.783 * 1000
    
    mars = Planet(-1.524 * Planet.AU, 0, 12, 'Sprites/Mars.png', 6.39 * 10**23)
    mars.y_vel = 24.077 * 1000
    
    jupiter = Planet(5.204 * Planet.AU, 0, 14, 'Sprites/Jupiter.png', 1.8986 * 10**27)
    jupiter.y_vel = 13.1 * 1000

    saturn = Planet(9.54 * Planet.AU, 0, 14, 'Sprites/Saturn.png', 5.68 * 10**26)
    saturn.y_vel = 9.68 * 1000
    
    uranus = Planet(18.4 * Planet.AU, 0, 14, 'Sprites/Uranus.png', 8.68 * 10**25)
    uranus.y_vel = -6.8 * 1000

    neptune = Planet(30 * Planet.AU, 0, 14, 'Sprites/Neptune.png', 1.02 * 10**26)
    neptune .y_vel = -5.44 * 1000

    pluto = Planet(39.53 * Planet.AU, 0, 14, 'Sprites/Pluto.png', 1.305 * 10**22)
    pluto.y_vel = 4.74 * 1000
    
    planets = [sun, mercury, venus, earth, mars, jupiter, saturn, uranus, neptune, pluto]
    
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
        
        # Отрисовка
        for planet in planets:
            planet.draw(window)

    quit()

# Запуск
if __name__ == '__main__':
    main()