from pico2d import *
import object
img_hei = 1685
img_wid = 5172
class barricade_1:
    def __init__(self):
        self.x = 922
        self.hp = 0#=hp
        self.box = [object.Box(74 * 3, 0, 720*3, 730 * 3, 'ground'),
                    object.Box(76 * 3, 0, 730*3, 740 * 3, 'ground'),
                    object.Box(78 * 3, 0, 740*3, 750 * 3, 'ground'),
                    object.Box(80 * 3, 0, 760*3, 765 * 3, 'ground'),
                    object.Box(82 * 3, 0, 765*3, 770 * 3, 'ground'),
                    object.Box(84 * 3, 0, 770*3, 775 * 3, 'ground'),
                    object.Box(86 * 3, 0, 775*3, 780 * 3, 'ground'),
                    object.Box(88 * 3, 0, 780*3, 785 * 3, 'ground'),
                    object.Box(90 * 3, 0, 785*3, 795 * 3, 'ground'),
                    object.Box(92 * 3, 0, 795*3, 805 * 3, 'ground'),
                    object.Box(94 * 3, 0, 805*3, 860 * 3, 'ground'),
                    object.Box(500 * 3, 0, 840*3, 860 * 3, 'wall')]
    def spawn_enemy(self):
        pass
    def check_barrigate(self,m_x):
        if self.hp>0 and m_x+300 >= self.x:
            return 1
        return 0
    def draw_1(self,img,m_x,m_y):
        if self.hp <= 0:
            img.clip_draw(4095, img_hei - 1 - 166, 304, 166, (776 - m_x) * 3, 250 - m_y * 3, 304 * 3, 166 * 3)
        else :
            img.clip_draw(3862, img_hei - 1 - 137, 118, 137, (870 - m_x) * 3, 415 - m_y * 3, 118 * 3, 137 * 3)
            pass
    def draw_2(self,img,m_x,m_y):
        if self.hp <= 0:
            img.clip_draw(3314, img_hei - 128 - 83, 280, 83, (785 - m_x) * 3, 126 - m_y * 3, 280 * 3, 83 * 3)
        else:
            img.clip_draw(3989, img_hei - 1 - 137, 103, 137, (880 - m_x) * 3, 415 - m_y * 3, 103 * 3, 137 * 3)
            pass

class barricade_2:
    def __init__(self):
        self.sprite_1 = [3862,1,118,137]
        self.sprite_2 = [3989,1,103,137]
        self.x = 1608
        self.hp = 10#=hp
        self.box = [object.Box(500 * 3, 0, 1560*3, 1570 * 3, 'wall')]
    def spawn_enemy(self):
        pass
    def check_barrigate(self,m_x):
        if self.hp>0 and m_x+300 >= self.x:
            return 1
        return 0
    def draw_1(self,img,m_x,m_y):
        if self.hp <= 0:
            #img.clip_draw(2290, img_hei -607 - 182, 279, 182, (1700 - m_x) * 3, 250 - m_y * 3, 304 * 3, 166 * 3)
            pass
        else :
            img.clip_draw(3862, img_hei - 1 - 137, 118, 137, (870 - m_x) * 3, 415 - m_y * 3, 118 * 3, 137 * 3)
            pass
    def draw_2(self,img,m_x,m_y):
        if self.hp <= 0:
            img.clip_draw(2290, img_hei -607 - 182, 279, 182, (1700 - m_x) * 3, 250 - m_y * 3, 279 * 3, 182 * 3)
        else:
            img.clip_draw(2290, img_hei -607 - 182, 279, 182, (1470 - m_x) * 3, 270 - m_y * 3, 279 * 3, 182 * 3)
            pass