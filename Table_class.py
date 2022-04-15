from pygame import *

from Window import H, V, window, FONT

class Table:
    
    def __init__(self, scale_x, scale_y, planets):
        
        self.scale_x = scale_x
        self.scale_y = scale_y
        self.x = H - self.scale_x - 30
        self.y = 20
        
        self.planets = planets
        
        self.image = transform.scale(image.load('Sprites/Table.png'), (self.scale_x, self.scale_y))
        
    def draw(self):
        
        window.blit(self.image, (self.x, self.y))