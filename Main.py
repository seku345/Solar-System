# Библиотеки
from math import *

from pygame import *

# Параметры окна
from Window import window, background, colors

# Классы
from Planet_class import Planet
from Table_class import  Table

# Главная функция
def main():

    clock = time.Clock()

    # Создание планет
    sun = Planet(0, 0, 2.5, 'Sprites/Sun.png', colors['YELLOW'], 1.98892 * 10**30)
    sun.sun = True

    mercury = Planet(0.387 * Planet.AU, 0, 0.5, 'Sprites/Mercury.png', colors['BROWN'], 3.30 * 10**23)
    mercury.y_vel = -48 * 1000

    venus = Planet(-0.723 * Planet.AU, 0, 1, 'Sprites/Venus.png', colors['WHITE'], 4.8685 * 10**24)
    venus.y_vel = -35.02 * 1000

    earth = Planet(-1 * Planet.AU, 0, 1, 'Sprites/Earth.png', colors['BLUE'], 5.9742 * 10**24)
    earth.y_vel = 29.783 * 1000
    
    mars = Planet(-1.524 * Planet.AU, 0, 1, 'Sprites/Mars.png', colors['RED'], 6.39 * 10**23)
    mars.y_vel = 24.077 * 1000
    
    jupiter = Planet(-5.2 * Planet.AU, 0, 1.5, 'Sprites/Jupiter.png', colors['BEIGE'], 1.8986 * 10**27)
    jupiter.y_vel = 13.1 * 1000

    saturn = Planet(-9.54 * Planet.AU, 0, 1.75, 'Sprites/Saturn.png', colors['ORANGE'], 5.68 * 10**26, saturn= True)
    saturn.y_vel = 9.68 * 1000
    
    uranus = Planet(-19.2 * Planet.AU, 0, 1.5, 'Sprites/Uranus.png', colors['ICE'], 8.68 * 10**25)
    uranus.y_vel = -6.8 * 1000

    neptune = Planet(30 * Planet.AU, 0, 1.5, 'Sprites/Neptune.png', colors['LIGHT_BLUE'], 1.02 * 10**26)
    neptune.y_vel = -5.44 * 1000

    pluto = Planet(-39.53 * Planet.AU, 0, 0.5, 'Sprites/Pluto.png', colors['DARK_GREY'], 1.305 * 10**22)
    pluto.y_vel = 4.74 * 1000
    
    planets = [sun, mercury, venus, earth, mars, jupiter, saturn, uranus, neptune, pluto]
    
    # Табло
    table = Table(300, 500, planets)
    
    # Переключатели
    plus_pressed = False
    minus_pressed = False
    
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
            if e.type == KEYDOWN:
                
                if e.key == K_ESCAPE:
                    run = False
                    
                elif e.key == K_UP:
                    plus_pressed = True
                elif e.key == K_DOWN:
                    minus_pressed = True
        
        # Отрисовка
        for planet in planets:
                
            if plus_pressed and planet.SCALE_K <= 500:
                planet.SCALE_K += 10
                planet.SCALE = planet.SCALE_K / planet.AU
                if planet in planets[:5]:
                    planet.radius = int(planet.radius_k * planet.SCALE_K/5)
                else:
                    planet.radius = int(planet.radius_k * planet.SCALE_K*2)
                
                
            elif minus_pressed and planet.SCALE_K >= 20:
                planet.SCALE_K -= 10
                planet.SCALE = planet.SCALE_K / planet.AU
                if planet in planets[:5]:
                    planet.radius = int(planet.radius_k * planet.SCALE_K/5)
                else:
                    planet.radius = int(planet.radius_k * planet.SCALE_K*2)
            if not planet.saturn:
                planet.image = transform.scale(image.load(planet.planet_image), (planet.radius, planet.radius))
            else:
                planet.image = transform.scale(image.load(planet.planet_image), (planet.radius, int(planet.radius/2)))
            if not planet.sun:
                planet.update_position(planets)
                            
            planet.draw()    

        plus_pressed = False
        minus_pressed = False
        
        # Отрисовка табло
        table.draw()
        
    quit()

# Запуск
if __name__ == '__main__':
    main()