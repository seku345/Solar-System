from pygame import *

from Window import FONT_TEXT, colors
from Characteristics_of_planets import planets_info

def write(planet, window):

        
    current_name = planet.name
    
    text_list = []
    
    for parameter in planets_info[current_name]:

        text_list.append(FONT_TEXT.render(parameter + ': ' + str(planets_info[current_name][parameter]), 1, colors['WHITE']))

    # name_text = FONT_TEXT.render(planets_info[current_name]['name'], 1, colors['WHITE'])
    # mass_text = FONT_TEXT.render(planets_info[current_name]['mass'], 1, colors['WHITE'])
    # density_text = FONT_TEXT.render(planets_info[current_name]['density'], 1, colors['WHITE'])
    # radius_text = FONT_TEXT.render(planets_info[current_name]['radius'], 1, colors['WHITE'])
    # gravity_text = FONT_TEXT.render(planets_info[current_name]['gravity'], 1, colors['WHITE'])
    # velocity_text = FONT_TEXT.render(planets_info[current_name]['velocity'], 1, colors['WHITE'])
    # distance_to_sun_text = FONT_TEXT.render(planets[i].distance_to_sun, 1, colors['WHITE'])
    # atmospere_text = FONT_TEXT.render(planets_info[current_name]['atmospere'], 1, colors['WHITE'])
    # period_text = FONT_TEXT.render(planets_info[current_name]['period'], 1, colors['WHITE'])
    # day_text = FONT_TEXT.render(planets_info[current_name]['day'], 1, colors['WHITE'])
    # temperature_text = FONT_TEXT.render(planets_info[current_name]['temperature'], 1, colors['WHITE'])
    
    text_list.append(FONT_TEXT.render('distance to sun' + ': ' + str(planet.distance_to_sun), 1, colors['WHITE']))
    
    x = 100
    for text in text_list:
        
        window.blit(text, (100, x))
        x += 20