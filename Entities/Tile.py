import pygame as pg
import math
from settings import *
class Tile(pg.sprite.Sprite):
    def __init__(self,position, surface:pg.Surface, group) -> None:
        super().__init__(group)
        self.image = surface
        #self.original_position = [position[0], position[1]]
        #self.position = [position[0], position[1]+200]
        self.position = position
        self.type = 'Tile'
        
        
        self.rect = self.image.get_frect(topleft =self.position)
        

        
    def draw(self, surface:pg.Surface, scroll=vec2(0,0)):
        surface.blit(self.image,self.rect.topleft-scroll)
        

    def update(self):
       
        pass
