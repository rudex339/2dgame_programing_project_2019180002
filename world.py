import character
from pico2d import*
img_hei = 1685
img_wid = 5172
class World:
    def __init__(self):
        self.img = load_image('sprites/object.png')
        self.screen_x = 1
        self.screen_y = 1217
        self.m_x = 0
        self.m_y = 0
        self.screen_hei = 200
        self.screen_wid = 400

        self.player = character.Charcter()


        self.speed = 0
    def draw(self):
        global img_hei, img_wid
        self.img.clip_draw(self.screen_x + self.m_x,
                           img_hei - self.screen_y- self.m_y- self.screen_hei, self.screen_wid, self.screen_hei, 450, 300,900,600)
        self.player.draw(self.m_x,self.m_y)
    def win_update(self):
        #캐릭터 x위치에 맞춰 화면 이동
        if (self.player.player_x - self.m_x)>200:
            self.m_x+=5#플레이어 속도에 맞춤
        pass
    def update(self):
        self.player.update()
        self.win_update()

    def handle_events(self, type, key):
        self.player.handle_events(type, key)