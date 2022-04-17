# Библиотеки
from Window import FONT_TEXT, colors
from Characteristics_of_planets import planets_info

def write(planet, window, x, y):
        
    current_name = planet.name
    
    text_list = []
    
    for parameter in planets_info[current_name]:
        
        # Окончания
        if parameter == 'mass': end = ' kg'
        elif parameter == 'density': end = ' kg/m^3'
        elif parameter == 'radius': end = ' m'
        elif parameter == 'gravity': end = ' m/s^2'
        elif parameter == 'velocity': end = ' m/s'
        else: end = ''

        text_list.append(FONT_TEXT.render(parameter + ': ' + str(planets_info[current_name][parameter]) + end, 1, colors['WHITE']))
    
    text_list.append(FONT_TEXT.render('distance to sun' + ': ' + str(round(planet.distance_to_sun / 1_000, 1)) + ' km', 1, colors['WHITE']))
    
    # Отрисовка данных
    for text in text_list:
        
        window.blit(text, (x, y))
        y += 30