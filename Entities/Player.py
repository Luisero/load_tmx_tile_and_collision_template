from settings import *

class Player(pg.sprite.Sprite):
    def __init__(self,position:vec2, tilemap):
        super().__init__()
        self.image = pg.surface.Surface((32,64))
        self.image.fill('red')
        self.position = position
        self.rect = self.image.get_frect(topleft=position)


        self.move_speed = vec2(5,5)
        self.input = vec2(0,0)
        self.gravity = 2
        self.acceleration = vec2(0,self.gravity)
        self.JUMP_FORCE = -30
        self.velocity = vec2(0,0)


        self.collision_list = []
        self.tilemap = tilemap
        self.ground = False
        self.collision_types = {"left": False, "right":False, "bottom": False, "top": False}
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

    def is_grounded(self):
        if self.ground:
            return True 
        return False
    def check_jump(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_SPACE] and self.is_grounded():
            self.velocity.y = self.JUMP_FORCE
        else: 
            self.acceleration.y =self.gravity
    def update(self,dt):
        self.check_jump()
        self.ground = False

        input = self.get_input()
        #self.velocity = vec2(0,0)
        self.velocity.x = input.x * self.move_speed.x
        #self.velocity.y = input.y * self.move_speed.y
        if not(self.collision_types['left'] or self.collision_types['right']) :

            self.velocity.y += self.acceleration.y * dt
        

        self.collision_types = {"left": False, "right":False, "bottom": False, "top": False}

        self.position += self.velocity * dt 
        
        self.rect.x = self.position.x
        self.collision_list = self.tilemap.get_collision_with(self)

        for tile in self.collision_list:
            if self.velocity.x > 0:
                self.rect.right = tile.rect.left
                self.collision_types["right"] = True 
                self.acceleration.y =self.gravity/4 * dt 
            elif self.velocity.x < 0:
                self.rect.left = tile.rect.right
                self.collision_types['left'] = True
                self.acceleration.y =self.gravity/4 * dt 

        self.rect.y = self.position.y
        self.collision_list = self.tilemap.get_collision_with(self)
        for tile in self.collision_list:
            if self.velocity.y > 0:
                self.rect.bottom = tile.rect.top
                self.collision_types["bottom"] = True 
                self.velocity.y = 0
                self.ground = True
            elif self.velocity.y < 0:
                self.rect.top = tile.rect.bottom
                self.collision_types['top'] = True
                self.velocity.y = 0

        

        #self.rect.topleft = self.position
        self.position = self.rect.topleft
        


