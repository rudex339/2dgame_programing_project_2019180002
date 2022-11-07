import object
import enemy
from pico2d import*

img_hei = 1685
img_wid = 5172

img = None
screen_x = 1
screen_y = 1217
m_x = 0
m_y = 0
screen_hei = 200
screen_wid = 300

stack_stage = None
def enter():
    global img, stack_stage
    img = load_image('sprites/object.png')
    stack_stage = [stage1_1()]

def draw_1():
    global stack_stage
    img.clip_draw(screen_x + m_x, img_hei - screen_y - m_y - screen_hei, screen_wid, screen_hei, 450, 300, 900, 600)
    for st in stack_stage:
        st.draw_layer1()
    pass
def draw_2():
    global stack_stage
    for st in stack_stage:
        st.draw_layer2()

def check_object(player, x, y):
    global  stack_stage
    mx, my = 0,0
    for st in stack_stage:
        for gou in st.ground:
            mx, my = gou.hit_check(player, x, y)
            x += mx
            y += my
        if st.barrigate.hp > 0:
            for gou in st.barrigate.box:
                mx, my = gou.hit_check(player, x, y)
                x += mx
                y += my
    return x , y

def focus_player(player):
    global m_x
    for st in stack_stage:
        if st.barrigate.check_barrigate(m_x):
            return
        pass
    if (player.player_x - m_x * 3) >= 300:
        m_x += 4  # 플레이어 속도에 맞춤
    return
    pass
def push_state(state):
    stack_stage.append(state)

def del_zero():
    global stack_stage
    if (len(stack_stage) > 0):
            # remove the current state
        stack_stage.pop(0)
def update():
    global stack_stage
    for st in stack_stage:
        st.next()
        pass


class stage1_1:
    ground = None
    def __init__(self):
        if stage1_1.ground == None:
            stage1_1.ground = [object.Box(40 * 3, 0, 0, 540 * 3, 'ground'),
                       object.Box(42 * 3, 0, 540*3, 550 * 3, 'ground'),
                       object.Box(44 * 3, 0, 550*3, 560 * 3, 'ground'),
                       object.Box(46 * 3, 0, 560*3, 570 * 3, 'ground'),
                       object.Box(48 * 3, 0, 570*3, 580 * 3, 'ground'),
                       object.Box(50 * 3, 0, 580 * 3, 590 * 3, 'ground'),
                       object.Box(52 * 3, 0, 590 * 3, 600 * 3, 'ground'),
                       object.Box(54 * 3, 0, 600 * 3, 610 * 3, 'ground'),
                       object.Box(56 * 3, 0, 610 * 3, 620 * 3, 'ground'),
                       object.Box(58 * 3, 0, 620 * 3, 630 * 3, 'ground'),
                       object.Box(60 * 3, 0, 630 * 3, 640 * 3, 'ground'),
                       object.Box(62 * 3, 0, 640 * 3, 650 * 3, 'ground'),
                       object.Box(64 * 3, 0, 650 * 3, 660 * 3, 'ground'),
                       object.Box(66 * 3, 0, 660 * 3, 670 * 3, 'ground'),
                       object.Box(70 * 3, 0, 670 * 3, 680 * 3, 'ground'),
                       object.Box(72 * 3, 0, 680*3, 740 * 3, 'ground'),
                       object.Box(70 * 3, 0, 740*3, 750 * 3, 'ground'),
                       object.Box(68 * 3, 0, 750*3, 760 * 3, 'ground'),
                       object.Box(66 * 3, 0, 760*3, 770 * 3, 'ground'),
                       object.Box(64 * 3, 0, 770*3, 780 * 3, 'ground'),
                       object.Box(62 * 3, 0, 780*3, 790 * 3, 'ground'),
                       object.Box(60 * 3, 0, 790*3, 800 * 3, 'ground'),
                       object.Box(58 * 3, 0, 800*3, 810 * 3, 'ground'),
                       object.Box(56 * 3, 0, 810*3, 820 * 3, 'ground'),
                       object.Box(54 * 3, 0, 820*3, 830 * 3, 'ground'),
                       object.Box(52 * 3, 0, 830*3, 840 * 3, 'ground'),
                       object.Box(50 * 3, 0, 840*3, 850 * 3, 'ground'),
                       object.Box(48 * 3, 0, 850*3, 860 * 3, 'ground'),
                       object.Box(46 * 3, 0, 860*3, 870 * 3, 'ground'),
                       object.Box(44 * 3, 0, 870*3, 880 * 3, 'ground'),
                       object.Box(42 * 3, 0, 880*3, 890 * 3, 'ground'),
                       object.Box(40 * 3, 0, 890*3, 900 * 3, 'ground'),
                       object.Box(38 * 3, 0, 900*3, 920 * 3, 'ground'),]
        self.wave_frame = 0
        self.barrigate = enemy.barricade_1()
        pass
    def draw_layer1(self):
        img.clip_draw(2, img_hei - 669 - 24 - (66*self.wave_frame), 564, 24, (282 - m_x) * 3, (52-m_y)*3, 564 * 3, 24 * 3)
        #바리게이트 파괴
        self.barrigate.draw_1(img,m_x, m_y)

        img.clip_draw(3102, img_hei - 58 - 20, 27, 20, (379 - m_x) * 3, 213-m_y*3, 27 * 3, 20 * 3)
        img.clip_draw(2959, img_hei - 37 - 41, 85, 41, (500-m_x)*3, 150-m_y*3, 85*3, 41*3)

    def draw_layer2(self):
        img.clip_draw(2, img_hei - 694 - 40 - (66 * self.wave_frame), 564, 40, (282 - m_x) * 3, 60-m_y*3, 564 * 3, 40 * 3)
        self.wave_frame += 1
        self.wave_frame = self.wave_frame % 8
        # 바리게이트 파괴
        self.barrigate.draw_2(img,m_x, m_y)

        img.clip_draw(3045, img_hei - 40 - 38, 55, 38, (514 - m_x) * 3, 145-m_y*3, 55 * 3, 38 * 3)
        img.clip_draw(3131, img_hei - 38 - 40, 94, 40, (618 - m_x) * 3, 120-m_y*3, 94 * 3, 40 * 3)
        img.clip_draw(3227, img_hei - 37 - 41, 79, 41, (690 - m_x) * 3, 100-m_y*3, 79 * 3, 41 * 3)
    def next(self):
        if m_x + 300 > 922:
            push_state(stage1_2())
            pass
        if m_x > 922:
            del_zero()
            pass

class stage1_2:
    def __init__(self):

        self.ground = [object.Box(38 * 3, 0, 920*3, 980 * 3, 'ground'),
                       object.Box(48 * 3, 0, 980*3, 990 * 3, 'wall'),
                       object.Box(65 * 3, 48*3, 980*3, 1090 * 3, 'ground'),
                       object.Box(63 * 3, 0, 1090*3, 1010 * 3, 'ground'),
                       object.Box(60 * 3, 0, 1010*3, 1020 * 3, 'ground'),
                       object.Box(58 * 3, 0, 1020 * 3, 1030 * 3, 'ground'),
                       object.Box(56 * 3, 0, 1030 * 3, 1040 * 3, 'ground'),
                       object.Box(54 * 3, 0, 1040 * 3, 1050 * 3, 'ground'),
                       object.Box(52 * 3, 0, 1050 * 3, 1060 * 3, 'ground'),
                       object.Box(50 * 3, 0, 1060 * 3, 1070 * 3, 'ground'),
                       object.Box(48 * 3, 0, 1070 * 3, 1090 * 3, 'ground'),
                       object.Box(46 * 3, 0, 1090 * 3, 1110 * 3, 'ground'),
                       object.Box(44 * 3, 0, 1110 * 3, 1130 * 3, 'ground'),
                       object.Box(42 * 3, 0, 1130 * 3, 1150 * 3, 'ground'),
                       object.Box(40 * 3, 0, 1150 * 3, 1170 * 3, 'ground'),
                       object.Box(38 * 3, 0, 1170*3, 1190 * 3, 'ground'),
                       object.Box(36 * 3, 0, 1190*3, 1210 * 3, 'ground'),
                       object.Box(34 * 3, 0, 1210*3, 1310 * 3, 'ground'),
                       object.Box(36 * 3, 0, 1310*3, 1330 * 3, 'ground'),
                       object.Box(38 * 3, 0, 1330*3, 1350 * 3, 'ground'),
                       object.Box(40 * 3, 0, 1350*3, 1370 * 3, 'ground'),
                       object.Box(42 * 3, 0, 1370*3, 1390 * 3, 'ground'),
                       object.Box(44 * 3, 0, 1390*3, 1410 * 3, 'ground'),
                       object.Box(46 * 3, 0, 1410*3, 1440 * 3, 'ground'),
                       object.Box(48 * 3, 0, 1440*3, 1480 * 3, 'ground'),
                       object.Box(50 * 3, 0, 1480*3, 1520 * 3, 'ground'),
                       object.Box(52 * 3, 0, 1520*3, 1560 * 3, 'ground')]
        self.barrigate = enemy.barricade_2()
        pass
    def draw_layer1(self):
        pass

    def draw_layer2(self):
        self.barrigate.draw_2(img, m_x, m_y)
        pass

    def next(self):

            pass

