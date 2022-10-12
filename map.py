import character
from pico2d import*
img_hei = 826
img_wid = 2537
class World:
    def __init__(self):
        self.img = load_image('sprites/object.png')
        self.screen_x = 1
        self.screen_y = 1415
        self.screen_hei = 200
        self.screen_wid = 300

        self.player = character.Charcter()
        self.player_x = 40
        self.player_y = 50
    def draw(self):
        self.img.clip_draw(img_hei-self.screen_x-self.screen_wid,
                           img_wid - self.screen_y -
                           self.screen_hei, self.screen_wid, self.screen_hei, 0, 0,600,300)
        self.player.animation(self.player_x,self.player_y)

    def update(self):
        self.player.update()

    def key_update(self, type, key):
        self.player.key_update()
        if type == SDL_KEYDOWN:
            if key == SDLK_RIGHT:

            elif key == SDLK_LEFT:

                pass
            elif key == SDLK_UP:

                pass
            elif key == SDLK_DOWN:
                pass
            elif key == SDLK_x:

                    pass
        elif type == SDL_KEYUP:
            if key == SDLK_RIGHT:

                pass
            elif key == SDLK_LEFT:

                pass
            elif key == SDLK_UP:

                pass
            elif key == SDLK_DOWN:

                pass
        pass