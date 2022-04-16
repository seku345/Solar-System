from pygame import *

from Window import H, V, window, FONT
from Table_text import write

class Table:
    
    def __init__(self, scale_x, scale_y):
        
        self.scale_x = scale_x
        self.scale_y = scale_y
        self.x = H - self.scale_x - 30
        self.y = 20

        self.image = transform.scale(image.load('Sprites/Table.png'), (self.scale_x, self.scale_y))
        
    def draw(self, planets, index):
        
        self.index = index
        self.planet = planets[self.index]
        
        window.blit(self.image, (self.x, self.y))
        
        write(self.planet, window, self.x + 20, self.y + 40)