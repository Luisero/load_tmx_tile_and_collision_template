from settings import *
import time
from Entities.Tilemap import Tilemap
from Entities.Player import Player

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(SCREEN_SIZE, pg.FULLSCREEN)
        self.clock = pg.time.Clock()
        self.font = pg.font.Font(None, 36)  # Fonte para exibir o FPS

        self.tilemap = Tilemap('./Data/Levels/1.tmx', vec2(0,-255))
        
        self.entities_group = pg.sprite.Group()
        self.tilemap.load_tiles()

        self.prev_time = time.time()
        self.dt = 0
        self.target_fps = TARGET_FPS
        self.fps = FPS
        self.player = Player(vec2(30,200), self.tilemap)
        self.entities_group.add(self.player)

    def exit(self):
        pg.quit()
        exit_process()
    
    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.exit()
            
        #FPS = 60
        self.fps = 60
        self.keys = pg.key.get_pressed()
        if self.keys[pg.K_ESCAPE]:
            self.exit()
        if self.keys[pg.K_g]:
            self.fps = 30
        
    def update(self):
        now= time.time()
        self.dt = now - self.prev_time
        self.dt *= self.target_fps
        self.prev_time = now
        self.entities_group.update(self.dt)
        
    def draw(self):
        self.screen.fill(BG_COLOR)
        self.tilemap.draw(self.screen)
        self.entities_group.draw(self.screen)

        # Exibir FPS na tela
        fps_text = self.font.render(f"FPS: {int(self.clock.get_fps())}", True, (255, 255, 255))
        self.screen.blit(fps_text, (10, 10))
        
    def run(self):
        self.runnig = True 
        while self.runnig:
            self.update()
            self.draw()
            self.check_events()

            self.clock.tick(self.fps)
            pg.display.update()

if __name__ == '__main__':
    game = Game()
    game.run()
