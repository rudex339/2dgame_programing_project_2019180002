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


        self.speed = 0
    def draw(self):
        self.img.clip_draw(img_hei-self.screen_x-self.screen_wid,
                           img_wid - self.screen_y -
                           self.screen_hei, self.screen_wid, self.screen_hei, 0, 0,600,300)
        self.player.draw()
    def win_update(self):
        #캐릭터 x위치에 맞춰 화면 이동
        if self.player.player_x>200:
            self.screen_x+=1#플레이어 속도에 맞춤
        pass
    def update(self):
        self.player.update()
        self.win_update()

    def key_update(self, type, key):
        self.player.key_update()