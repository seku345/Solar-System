# Библиотеки
from time import time

from pygame import *

# Параметры
from Window import window, background, colors, H, V
from Characteristics_of_planets import planets_info

# Классы
from Planet_class import Planet
from Table_class import  Table

# Главная функция
def main():

    clock = time.Clock()

    # Создание планет
    sun = Planet(planets_info['Sun']['name'], 0, 0, 2.5, 'Sprites/Sun.png', colors['YELLOW'], planets_info['Sun']['mass'])
    sun.sun = True

    mercury = Planet(planets_info['Mercury']['name'], -0.387 * Planet.AU, 0, 0.5, 'Sprites/Mercury.png', colors['BROWN'], planets_info['Mercury']['mass'])
    mercury.y_vel = planets_info['Mercury']['velocity']

    venus = Planet(planets_info['Venus']['name'], -0.723 * Planet.AU, 0, 1, 'Sprites/Venus.png', colors['WHITE'], planets_info['Venus']['mass'])
    venus.y_vel = -planets_info['Venus']['velocity']

    earth = Planet(planets_info['Earth']['name'], -1 * Planet.AU, 0, 1, 'Sprites/Earth.png', colors['BLUE'], planets_info['Earth']['mass'])
    earth.y_vel = planets_info['Earth']['velocity']
    
    mars = Planet(planets_info['Mars']['name'], -1.524 * Planet.AU, 0, 1, 'Sprites/Mars.png', colors['RED'], planets_info['Mars']['mass'])
    mars.y_vel = planets_info['Mars']['velocity']
    
    jupiter = Planet(planets_info['Jupiter']['name'], -5.2 * Planet.AU, 0, 1.75, 'Sprites/Jupiter.png', colors['BEIGE'], planets_info['Jupiter']['mass'])
    jupiter.y_vel = planets_info['Jupiter']['velocity']

    saturn = Planet(planets_info['Saturn']['name'], -9.54 * Planet.AU, 0, 1.5, 'Sprites/Saturn.png', colors['ORANGE'], planets_info['Saturn']['mass'], saturn= True)
    saturn.y_vel = planets_info['Saturn']['velocity']
    
    uranus = Planet(planets_info['Uranus']['name'], -19.2 * Planet.AU, 0, 1.5, 'Sprites/Uranus.png', colors['ICE'], planets_info['Uranus']['mass'])
    uranus.y_vel = -planets_info['Uranus']['velocity']

    neptune = Planet(planets_info['Neptune']['name'], -30 * Planet.AU, 0, 1.5, 'Sprites/Neptune.png', colors['LIGHT_BLUE'], planets_info['Neptune']['mass'])
    neptune.y_vel = planets_info['Neptune']['velocity']

    pluto = Planet(planets_info['Pluto']['name'], -39.53 * Planet.AU, 0, 1, 'Sprites/Pluto.png', colors['DARK_GREY'], planets_info['Pluto']['mass'])
    pluto.y_vel = planets_info['Pluto']['velocity']
    
    planets = [sun, mercury, venus, earth, mars, jupiter, saturn, uranus, neptune, pluto]
    
    # Табло
    table = Table(500, 400)
    
    # Переключатели
    plus_pressed = False
    minus_pressed = False
    index = 0
    
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
                    
            # Проверка нажатия на планеты
            elif e.type == MOUSEBUTTONDOWN:
                click_coor = list(mouse.get_pos())

                for p in planets:
                    
                    x = p.x * p.SCALE + H/2 - p.radius/2
                    y = p.y * p.SCALE + V/2 - p.radius/2
                    
                    if x <= click_coor[0] <= x + p.radius and y <= click_coor[1] <= y + p.radius:
                        index = planets.index(p)
                        
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
        table.draw(planets, index)
        
    quit()

# Запуск
if __name__ == '__main__':
    main()