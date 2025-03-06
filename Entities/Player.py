from settings import *

class Player(pg.sprite.Sprite):
    def __init__(self,position:vec2, tilemap):
        super().__init__()
        self.image = pg.surface.Surface((32,32))
        self.image.fill('red')
        self.position = position
        self.rect = self.image.get_frect(topleft=position)
        self.move_speed = vec2(5,5)
        self.input = vec2(0,0)
        self.collision_list = []
        self.tilemap = tilemap
    
    def get_input(self):
        input = vec2()
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            input.x -=1
        if keys[pg.K_d]:
            input.x +=1
        if keys[pg.K_w]:
            input.y -=1
        if keys[pg.K_s]:
            input.y +=1
        
        if input.length() != 0:
            input = input.normalize()
    
        return input

    

    def update(self):

        collision_types = {"left": False, "right":False, "bottom": False, "top": False}

        input = self.get_input()
        self.velocity = vec2(0,0)
        self.velocity.x = input.x * self.move_speed.x
        self.velocity.y = input.y * self.move_speed.y

        self.position += self.velocity
        
        self.rect.x = self.position.x
        self.collision_list = self.tilemap.get_collision_with(self)

        for tile in self.collision_list:
            if self.velocity.x > 0:
                self.rect.right = tile.rect.left
                collision_types["right"] = True 
            elif self.velocity.x < 0:
                self.rect.left = tile.rect.right
                collision_types['left'] = True

        self.rect.y = self.position.y
        self.collision_list = self.tilemap.get_collision_with(self)
        for tile in self.collision_list:
            if self.velocity.y > 0:
                self.rect.bottom = tile.rect.top
                collision_types["bottom"] = True 
            elif self.velocity.y < 0:
                self.rect.top = tile.rect.bottom
                collision_types['top'] = True

        

        #self.rect.topleft = self.position
        self.position = self.rect.topleft
        print(collision_types)


