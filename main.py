from settings import *
from Entities.Tilemap import Tilemap
from Entities.Player import Player
class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(SCREEN_SIZE, pg.FULLSCREEN)
        self.clock = pg.time.Clock()

        self.tilemap = Tilemap('./Data/Levels/1.tmx')

        
        self.entities_group = pg.sprite.Group()
        self.tilemap.load_tiles()

        self.player = Player(vec2(30,500), self.tilemap)
        
        self.entities_group.add(self.player)


    def exit(self):
        pg.quit()
        exit_process()
    def check_events(self):
        for event in pg.event.get():
            if event == pg.QUIT:
               self.exit()
        self.keys = pg.key.get_pressed()
        if self.keys[pg.K_ESCAPE]:
            self.exit()

    def update(self):
        self.entities_group.update()
        

    def draw(self):
        self.screen.fill(BG_COLOR)
        self.tilemap.draw(self.screen)
        self.entities_group.draw(self.screen)
    def run(self):
        self.runnig = True 
        while self.runnig:
            self.update()
            self.draw()
            self.check_events()


            self.clock.tick(FPS)
            pg.display.update()


if __name__ == '__main__':
    game = Game()
    game.run()