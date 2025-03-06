import pygame as pg
import math

class Tile(pg.sprite.Sprite):
    def __init__(self,position, surface, group) -> None:
        super().__init__(group)
        self.image = surface
        #self.original_position = [position[0], position[1]]
        #self.position = [position[0], position[1]+200]
        self.position = position
        self.type = 'Tile'
        
        
        self.rect = self.image.get_rect(topleft =self.position)
        

        
    

    def update(self):
       
        pass
