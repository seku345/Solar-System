# Библиотеки
import pygame as pg

# Параметры
from Window import window, background, colors, H, V, FONT_DATE
from Characteristics_of_planets import planets_info

# Дата
from Time import date

# Классы
from Planet_class import Planet
from Table_class import  Table

# Главная функция
def main():

    # Часы
    clock = pg.time.Clock()
    
    # Создание планет
    sun = Planet(planets_info['Sun']['name'], 0, 0, 2.5, 'Sprites/Sun.png', colors['YELLOW'], planets_info['Sun']['mass'], sun= True)

    mercury = Planet(planets_info['Mercury']['name'], -0.387 * Planet.AU, 0, 0.5, 'Sprites/Mercury.png', colors['BROWN'], planets_info['Mercury']['mass'], planets_info['Mercury']['velocity'])

    venus = Planet(planets_info['Venus']['name'], -0.723 * Planet.AU, 0, 1, 'Sprites/Venus.png', colors['WHITE'], planets_info['Venus']['mass'], planets_info['Venus']['velocity'])

    earth = Planet(planets_info['Earth']['name'], -1 * Planet.AU, 0, 1, 'Sprites/Earth.png', colors['BLUE'], planets_info['Earth']['mass'], planets_info['Earth']['velocity'])
    
    mars = Planet(planets_info['Mars']['name'], -1.524 * Planet.AU, 0, 1, 'Sprites/Mars.png', colors['RED'], planets_info['Mars']['mass'], planets_info['Mars']['velocity'])
    
    jupiter = Planet(planets_info['Jupiter']['name'], -5.2 * Planet.AU, 0, 1.75, 'Sprites/Jupiter.png', colors['BEIGE'], planets_info['Jupiter']['mass'], planets_info['Jupiter']['velocity'])

    saturn = Planet(planets_info['Saturn']['name'], -9.54 * Planet.AU, 0, 1.5, 'Sprites/Saturn.png', colors['ORANGE'], planets_info['Saturn']['mass'], planets_info['Saturn']['velocity'], saturn= True)
    
    uranus = Planet(planets_info['Uranus']['name'], -19.2 * Planet.AU, 0, 1.5, 'Sprites/Uranus.png', colors['ICE'], planets_info['Uranus']['mass'], planets_info['Uranus']['velocity'])

    neptune = Planet(planets_info['Neptune']['name'], -30 * Planet.AU, 0, 1.5, 'Sprites/Neptune.png', colors['LIGHT_BLUE'], planets_info['Neptune']['mass'], planets_info['Neptune']['velocity'])

    pluto = Planet(planets_info['Pluto']['name'], -39.53 * Planet.AU, 0, 1, 'Sprites/Pluto.png', colors['DARK_GREY'], planets_info['Pluto']['mass'], planets_info['Pluto']['velocity'])
    
    planets = [sun, mercury, venus, earth, mars, jupiter, saturn, uranus, neptune, pluto]
    
    # Табло
    table = Table(500, 400)
    
    # Переменные
    plus_pressed = False
    minus_pressed = False
    index = 0
    start_date = '9.03.1982'
    pause = False
    
    # Основной цикл
    run = True
    while run:

        # Кадры в секунду
        clock.tick(60)
        pg.display.update()

        # Фон
        window.blit(background, (0, 0))

        # Обработка событий
        for e in pg.event.get():

            # Закрытие окна
            if e.type == pg.KEYDOWN:
                
                if e.key == pg.K_ESCAPE:
                    run = False
                
                # Пауза
                elif e.key == pg.K_SPACE and not pause:
                    pause = True
                elif e.key == pg.K_SPACE and pause:
                    pause = False
                    
            # Проверка нажатия на планеты
            elif e.type == pg.MOUSEBUTTONDOWN and e.button == 1:
                click_coor = list(pg.mouse.get_pos())

                for p in planets:
                    
                    x = p.x * p.SCALE + H/2 - p.radius/2
                    y = p.y * p.SCALE + V/2 - p.radius/2
                    
                    if x <= click_coor[0] <= x + p.radius and y <= click_coor[1] <= y + p.radius:
                        index = planets.index(p)
                        break
                    else:
                        index = -1
            # Изменение масштаба  
            elif e.type == pg.MOUSEWHEEL:
                if e.y >= 1:
                    plus_pressed = True
                elif e.y <= -1:
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
                planet.image = pg.transform.scale(pg.image.load(planet.planet_image), (planet.radius, planet.radius))
            else:
                planet.image = pg.transform.scale(pg.image.load(planet.planet_image), (planet.radius, int(planet.radius/2)))
            if not planet.sun:
                if not pause:
                    planet.update_position(planets)
   
            if planet == earth:
                if not pause:
                    start_date = date(start_date)
                    
            planet.draw()    
            
        plus_pressed = False
        minus_pressed = False
        
        # Отрисовка табло
        if index != -1:
            table.draw(planets, index)
        
        # Отрисовка даты
        date_text = FONT_DATE.render(date(start_date), 1, colors['WHITE'])
        window.blit(date_text, (30, V-100))
        
    quit()

# Запуск
if __name__ == '__main__':
    main()