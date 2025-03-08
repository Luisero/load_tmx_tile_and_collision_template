from settings import *

class Camera(pg.sprite.Group):
    def __init__(self):
        super().__init__()
        self.scroll = vec2(0,0)

    def update_scroll(self, rect:pg.Rect):
        self.scroll.x += (rect.x - self.scroll.x - (SCREEN_WIDTH/2+rect.width))/20
        self.scroll.y += (rect.y - self.scroll.y - (SCREEN_HEIGHT/2))/40
    def custom_draw(self, surface):
        for sprite in self.sprites():
            sprite.draw(surface, self.scroll)