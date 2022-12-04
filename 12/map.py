from pico2d import *
import game_world
import server
import game_framework
from M_3_Rocket import M_3
import exposion
from mingkong import Mingkong
import random

image = None
img_hei = 1685
img_wid = 5172
canvas_width = 0
canvas_height = 0
window_left = 0
window_bottom = 0


PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 40.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8


class background:
    def __init__(self):#x,y,wid,hei
        self.object = [2,67,300,200]
        self.my=0

        self.bgm = load_music("sound/mission_1.mp3")
        self.bgm.set_volume(32)
        self.bgm.repeat_play()


        pass

    def exit(self):
        return True

    def update(self):
        global window_bottom, window_left
        if window_left < int(server.character.x) - 300:
            if int(server.character.x)-window_left >300:
                window_left += RUN_SPEED_PPS * game_framework.frame_time * 2
            else:
                window_left =int(server.character.x) - 300
        if server.character.x >2818 * 3 - 60:
            if self.my < 20:
                self.my +=RUN_SPEED_PPS * game_framework.frame_time


        pass

    def draw(self):
        global image
        x,y,wid,hei = self.object
        image.clip_draw(x+int(window_left/6), 1685-y-hei-int(self.my), wid, hei, 450, 300,900,600)
        pass
    def get_bb(self):
        pass
    def handle_collision(self,other,group):
        pass

class stage:
    def __init__(self):  # x,y,wid,hei
        self.b_stage = [stage_1()]
        self.timer = 0
        pass

    def exit(self):
        return True

    def update(self):
        for i in self.b_stage:
            op = i.update()
            if  op == 1:
                self.b_stage.append(i.next())
            elif op == 2:
                self.b_stage.pop(0)
        self.timer = (self.timer + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 150
        if int(self.timer) == 0:
            x = random.randrange(0, 900)
            m = Mingkong(x + window_left, 300 * 2, -1)
            game_world.add_object(m, 2)
        pass

    def draw(self):
        for i in self.b_stage:
            i.draw()
        pass
class stage_1:
    def __init__(self):  # x,y,wid,hei
        self.object = [1, 1217, 300, 200]
        self.small_stage = [stage_1_1()]

        pass

    def exit(self):
        return True

    def update(self):
        for st in self.small_stage:
            op = st.update()
            if  op == 1:
                self.small_stage += [st.next()]
            elif op == 2:
                st.delete()
                self.small_stage.pop(0)
            elif op == 3:
                st.delete()
                self.small_stage.pop(0)
                return 2
            elif op == 4:
                return 1
        return 0

    def draw(self):
        global image
        x, y, wid, hei = self.object
        image.clip_draw(x + int(window_left / 3),
                        1685 - y - hei,
                        clamp(0, 1405 - int(window_left / 3), wid)
                        , hei,
                        int(clamp(0, 1405 - int(window_left / 3), wid) * 3 / 2)
                        , 300,
                        clamp(0, 1405 - int(window_left / 3), wid) * 3, 600)
        pass
    def next(self):
        return stage_2()
class stage_1_1:
    def __init__(self):#x,y,wid,hei

        self.object =[1,1217,300,200]
        self.objects = []
        o =Object([[2,669,564,24,282,52],
                   [2,669+66,564,24,282,52],
                   [2,669+66*2,564,24,282,52],
                   [2,669+66*3,564,24,282,52],
                   [2,669+66*4,564,24,282,52],
                   [2,669+66*5,564,24,282,52],
                   [2,669+66*6,564,24,282,52],
                   [2,669+66*7,564,24,282,52]],8)
        game_world.add_object(o, 2)
        self.objects += [o]

        o = Object([[3102, 58, 27, 20, 379, 71]], 1)
        game_world.add_object(o, 2)
        self.objects += [o]

        o = Object([[2959, 37, 85, 41, 500, 50]], 1)
        game_world.add_object(o, 2)

        o=Object([[2,694,564,40,282,20],[2,694+66,564,40,282,20],[2,694+66*2,564,40,282,20],[2,694+66*3,564,40,282,20],[2,694+66*4,564,40,282,20],[2,694+66*5,564,40,282,20],[2,694+66*6,564,40,282,20],[2,694+66*7,564,40,282,20]],8)
        game_world.add_object(o, 4)
        self.objects += [o]

        o=Object([[3045, 40, 55, 38, 514, 48]], 1)
        game_world.add_object(o, 4)
        self.objects += [o]

        o=Object([[3131, 38, 94, 40, 618, 40]], 1)
        game_world.add_object(o, 4)
        self.objects += [o]

        o=Object([[3227, 37, 79, 41, 690, 33]], 1)
        game_world.add_object(o, 4)
        self.objects += [o]

        self.box_list = [game_world.box(40 * 3, 0, 0, 540 * 3),
                       game_world.box(42 * 3, 0, 540*3, 550 * 3),
                       game_world.box(44 * 3, 0, 550*3, 560 * 3),
                       game_world.box(46 * 3, 0, 560*3, 570 * 3),
                       game_world.box(48 * 3, 0, 570*3, 580 * 3),
                       game_world.box(50 * 3, 0, 580 * 3, 590 * 3),
                       game_world.box(52 * 3, 0, 590 * 3, 600 * 3),
                       game_world.box(54 * 3, 0, 600 * 3, 610 * 3),
                       game_world.box(56 * 3, 0, 610 * 3, 620 * 3),
                       game_world.box(58 * 3, 0, 620 * 3, 630 * 3),
                       game_world.box(60 * 3, 0, 630 * 3, 640 * 3),
                       game_world.box(62 * 3, 0, 640 * 3, 650 * 3),
                       game_world.box(64 * 3, 0, 650 * 3, 660 * 3),
                       game_world.box(66 * 3, 0, 660 * 3, 670 * 3),
                       game_world.box(70 * 3, 0, 670 * 3, 680 * 3),
                       game_world.box(72 * 3, 0, 680*3, 740 * 3),
                       game_world.box(70 * 3, 0, 740*3, 750 * 3),
                       game_world.box(68 * 3, 0, 750*3, 760 * 3),
                       game_world.box(66 * 3, 0, 760*3, 770 * 3),
                       game_world.box(64 * 3, 0, 770*3, 780 * 3),
                       game_world.box(62 * 3, 0, 780*3, 790 * 3),
                       game_world.box(60 * 3, 0, 790*3, 800 * 3),
                       game_world.box(58 * 3, 0, 800*3, 810 * 3),
                       game_world.box(56 * 3, 0, 810*3, 820 * 3),
                       game_world.box(54 * 3, 0, 820*3, 830 * 3),
                       game_world.box(52 * 3, 0, 830*3, 840 * 3),
                       game_world.box(50 * 3, 0, 840*3, 850 * 3),
                       game_world.box(48 * 3, 0, 850*3, 860 * 3),
                       game_world.box(46 * 3, 0, 860*3, 870 * 3),
                       game_world.box(44 * 3, 0, 870*3, 880 * 3),
                       game_world.box(42 * 3, 0, 880*3, 890 * 3),
                       game_world.box(40 * 3, 0, 890*3, 900 * 3),
                       game_world.box(38 * 3, 0, 900*3, 920 * 3)]
        for l in self.box_list:
            l.compatible()
        game_world.add_collision_pairs(None, self.box_list, "character:box")

        self.barrigate = Barrigate1()
        pass

    def exit(self):
        del (self.barrigate)
        for l in self.box_list:
            game_world.remove_collision_object(l)
        for l in self.objects:
            game_world.remove_object(l)
        return True

    def update(self):
        global window_left
        for box in self.box_list:
            for other, group in box.all_collision():
                if group == 'character:box':
                    pass
        if self.barrigate.update() == 1:
            return 1
        if window_left > 920*3:
            return 2
        return 0
    def next(self):
        return stage_1_2()

    def delete(self):
        print ("delete")
        del(self)
        pass

class Barrigate1:
    def __init__(self):
        self.hp = 10

        self.layer_1 = Object([[3862, 1, 118, 137, 870, 138]], 1)
        game_world.add_object(self.layer_1,2)

        self.layer_2 = Object([[3989, 1, 103, 137, 880, 138]], 1)
        game_world.add_object(self.layer_2, 4)

        self.box_list = [game_world.box(74 * 3, 0, 720 * 3, 730 * 3),
                    game_world.box(76 * 3, 0, 730 * 3, 740 * 3),
                    game_world.box(78 * 3, 0, 740 * 3, 750 * 3),
                    game_world.box(80 * 3, 0, 760 * 3, 765 * 3),
                    game_world.box(82 * 3, 0, 765 * 3, 770 * 3),
                    game_world.box(84 * 3, 0, 770 * 3, 775 * 3),
                    game_world.box(86 * 3, 0, 775 * 3, 780 * 3),
                    game_world.box(88 * 3, 0, 780 * 3, 785 * 3),
                    game_world.box(90 * 3, 0, 785 * 3, 795 * 3),
                    game_world.box(92 * 3, 0, 795 * 3, 805 * 3),
                    game_world.box(94 * 3, 0, 805 * 3, 860 * 3),
                    game_world.box(500 * 3, 0, 840 * 3, 860 * 3)]
        self.hit_box = game_world.box(500 * 3, 0, 835 * 3, 860 * 3)
        for l in self.box_list:
            l.compatible()
        self.hit_box.compatible()

        game_world.add_collision_pairs(None, self.box_list, "character:box")
        game_world.add_collision_pairs(self.hit_box,None,  "bullet:hitbox")

        pass

    def exit(self):
        game_world.remove_object(self.layer_1)
        game_world.remove_object(self.layer_2)
        return True
    def update(self):
        global window_left
        if self.hp>0 and window_left > 920*3-900:
            window_left =920*3-900

            pass


        for other, group in self.hit_box.all_collision():
            if group == 'bullet:hitbox':
                self.hp -= 1
                print("hpdown")


        if self.hp == 0:
            game_world.remove_object(self.layer_1)
            game_world.remove_object(self.layer_2)
            for l in self.box_list:
                game_world.remove_collision_object(l)
            game_world.remove_collision_object(self.hit_box)

            self.layer_1 =Object([[4095,1,304,166,776,83]],1)
            game_world.add_object(self.layer_1, 2)

            self.layer_2 = Object([[3314, 128, 280,83 , 785, 42]], 1)
            game_world.add_object(self.layer_2, 4)

            exposion.ex_bgm1.set_volume(32)
            exposion.ex_bgm1.play(1)
            self.hp -= 1
            return 1
        return 0
        pass

class stage_1_2:
    def __init__(self):#x,y,wid,hei
        self.box_list = [game_world.box(38 * 3, 0, 920 * 3, 980 * 3),
                       game_world.box(65 * 3, 0, 980 * 3, 1090 * 3),
                       game_world.box(46 * 3, 0, 1090 * 3, 1110 * 3),
                       game_world.box(44 * 3, 0, 1110 * 3, 1130 * 3),
                       game_world.box(42 * 3, 0, 1130 * 3, 1150 * 3),
                       game_world.box(40 * 3, 0, 1150 * 3, 1170 * 3),
                       game_world.box(38 * 3, 0, 1170 * 3, 1190 * 3),
                       game_world.box(36 * 3, 0, 1190 * 3, 1210 * 3),
                       game_world.box(34 * 3, 0, 1210 * 3, 1310 * 3),
                       game_world.box(36 * 3, 0, 1310 * 3, 1330 * 3),
                       game_world.box(38 * 3, 0, 1330 * 3, 1350 * 3),
                       game_world.box(40 * 3, 0, 1350 * 3, 1370 * 3),
                       game_world.box(42 * 3, 0, 1370 * 3, 1390 * 3),
                       game_world.box(44 * 3, 0, 1390 * 3, 1410 * 3),
                       game_world.box(46 * 3, 0, 1410 * 3, 1440 * 3),
                       game_world.box(48 * 3, 0, 1440 * 3, 1480 * 3),
                       game_world.box(50 * 3, 0, 1480 * 3, 1520 * 3),
                       game_world.box(52 * 3, 0, 1520 * 3, 1560 * 3)]
        for l in self.box_list:
            l.compatible()
        game_world.add_collision_pairs(None, self.box_list, "character:box")



        self.barrigate = barrigate2()
        pass

    def exit(self):
        return True

    def update(self):
        global window_left
        for box in self.box_list:
            for other, group in box.all_collision():
                if group == 'character:box':
                    pass
        if self.barrigate.update() == 1:
            return 4
        if window_left > 1560* 3:
            return 3
        return 0


    def next(self):
        pass
    def delete(self):
        pass
class barrigate2:
    def __init__(self):
        self.hp = 10
        self.layer_1 = Object([[1388, 884, 203, 224, 1505, 112]], 1)
        game_world.add_object(self.layer_1, 2)
        self.door = None

        self.layer_2 = Object([[2290,607, 279, 182, 1470, 90]], 1)
        game_world.add_object(self.layer_2, 4)

        self.box_list = [game_world.box(500 * 3, 0, 1565*3, 1570 * 3)]
        self.hit_box = game_world.box(500 * 3, 0, 1560*3, 1570 * 3)
        for l in self.box_list:
            l.compatible()
        self.hit_box.compatible()

        game_world.add_collision_pairs(None, self.box_list, "character:box")
        game_world.add_collision_pairs(self.hit_box,None,  "bullet:hitbox")
        pass

    def exit(self):
        return True
    def update(self):
        global window_left
        if self.hp>0 and window_left > 1570 * 3-900:
            window_left =1570 * 3-900
            pass
        if self.door == None and window_left > 1500 * 3-900:
            self.door = Object([[569, 801, 86, 72, 1545, 95],
                                [658, 805, 89, 68, 1542, 91],
                                [750, 813, 99, 60, 1532, 83],
                                [851, 826, 114, 47, 1517, 70],
                                [968, 847, 131, 26, 1500, 49],
                                [1105, 834, 126, 39, 1505, 45],
                                [1242, 833, 122, 40, 1501, 45]], None)
            game_world.add_object(self.door, 2)

        for other, group in self.hit_box.all_collision():
            if group == 'bullet:hitbox':
                self.hp -= 1


        if self.hp == 0:
            print('del')
            game_world.remove_object(self.layer_1)
            game_world.remove_object(self.layer_2)
            game_world.remove_object(self.door)
            for l in self.box_list:
                game_world.remove_collision_object(l)
            game_world.remove_collision_object(self.hit_box)
            exposion.ex_bgm1.set_volume(32)
            exposion.ex_bgm1.play(1)
            self.hp -= 1
            return 1
        return 0
        pass

class  stage_2:
    def __init__(self):  # x,y,wid,hei 1405
        self.object = [1645, 859, 300, 200]#3411 227
        self.small_stage = [stage_2_1()]
        pass

    def exit(self):
        return True

    def update(self):
        for st in self.small_stage:
            op = st.update()
            if  op == 1:
                self.small_stage += [st.next()]
            elif op == 2:
                st.delete()
                self.small_stage.pop(0)
            elif op == 3:
                st.delete()
                self.small_stage.pop(0)
                return 2
            elif op == 4:
                return 1
        return 0

    def draw(self):
        global image
        x, y, wid, hei = self.object
        if int(window_left/3) - 1405 < 0:
            image.clip_draw(x, 1685 - y - hei -13, wid, hei, (1405 - int(window_left / 3))*3 + 450, 300, 900, 600)
        else:
            image.clip_draw(x + int(window_left / 3)-1405,
                            1685 - y - hei + window_bottom-13,
                            clamp(0, 3411+1305 - int(window_left / 3), wid)
                            , hei,
                            int(clamp(0, 3411+1305 - int(window_left / 3), wid) * 3 / 2)
                            , 300-window_bottom,
                            clamp(0, 3411+1380 - int(window_left / 3), wid) * 3, 600)
        pass
    def next(self):
        return None
    pass

class stage_2_1:

    def __init__(self):#x,y,wid,hei
        self.box_list = [game_world.box(1570 * 3, 0, 1596 * 3-20, 52 * 3),
                       game_world.box(1596 * 3-20, 0, 1617 * 3-20, (101-15) * 3),
                       game_world.box(1617 * 3-20, 0, 1641 * 3-20, (105-15) * 3),
                       game_world.box(1641 * 3-20, 0, 1658 * 3-20, (129-15) * 3),
                       game_world.box(1658 * 3-20, 0, 1665 * 3-20, (132-15) * 3),
                       game_world.box(1665 * 3-20, 0, 1670 * 3-20, (137-15) * 3),
                         game_world.box(1670 * 3-20, 0, 1675 * 3-20, 125 * 3),
                         game_world.box(1675 * 3-20, 0, 1680 * 3-20, 130 * 3),
                       game_world.box(1680 * 3-20, 0, 1690 * 3-20, 135 * 3),
                       game_world.box(1690 * 3-20, 0, 1695 * 3-20, 140 * 3),
                       game_world.box(1695 * 3-20, 0, 1697 * 3-20, 145 * 3),
                       game_world.box(1697 * 3-20, 0, 1727 * 3-20, 150 * 3),
                       game_world.box(1727 * 3-20, 0, 1767 * 3-20, 145 * 3),
                       game_world.box(1767 * 3-20, 0, 1807 * 3-20, 140 * 3),
                       game_world.box(1807 * 3-20, 0, 1847 * 3-20, 135 * 3),
                       game_world.box(1847 * 3-20, 0, 1887 * 3-20, 130 * 3),
                       game_world.box(1887 * 3-20, 0, 1927 * 3-20, 125 * 3),
                       game_world.box(1927 * 3-20, 0, 1967 * 3-20, 120 * 3),
                       game_world.box(1967 * 3-20, 0, 2037 * 3-20, 115 * 3),
                         game_world.box(2037 * 3-20, 0, 2047 * 3-20, 110 * 3),
                         game_world.box(2047 * 3-20, 0, 2087 * 3-20, 105 * 3),
                         game_world.box(2087 * 3-20, 0, 2127 * 3-20, 100 * 3),
                         game_world.box(2127 * 3-20, 0, 2167 * 3-20, 95 * 3),
                         game_world.box(2167 * 3-20, 0, 2207 * 3-20, 90 * 3),
                         game_world.box(2207 * 3-20, 0, 2247 * 3-20, 85 * 3),
                         game_world.box(2247 * 3-20, 0, 2287 * 3-20, 80 * 3),
                         game_world.box(2287 * 3-20, 0, 2327 * 3-20, 75 * 3),
                         game_world.box(2327 * 3-20, 0, 2340 * 3-20, 70 * 3),
                         game_world.box(2340 * 3-20, 0, 2360 * 3-20, 65 * 3),
                         game_world.box(2330 * 3-20, 0, 2371 * 3-20, 63 * 3),
                       game_world.box(2371 * 3-20, 0, 2758 * 3-60, 63 * 3),
                         game_world.box(2758 * 3 - 60, 0, 2768 * 3 - 60, 67 * 3),
                         game_world.box(2768 * 3 - 60, 0, 2778 * 3 - 60, 71 * 3),
                         game_world.box(2778 * 3 - 60, 0, 2788 * 3 - 60, 75 * 3),
                         game_world.box(2788 * 3 - 60, 0, 2798 * 3 - 60, 79 * 3),
                         game_world.box(2798 * 3 - 60, 0, 2808 * 3 - 60, 83 * 3),
                         game_world.box(2808 * 3 - 60, 0, 2818 * 3 - 60, 87 * 3),
                         game_world.box(2818 * 3 - 60, 0, 2828 * 3 - 60, 91 * 3),
                         game_world.box(2828 * 3 - 60, 0, 2842 * 3 - 60, 95 * 3),
                         game_world.box(2842 * 3-60, 0, 2850 * 3-60, 97 * 3)]#2758 79
        game_world.add_collision_pairs(None, self.box_list, "character:box")

        self.object = Object([[1614, 1152, 1289, 131,2000, 18]], 1)
        game_world.add_object(self.object, 4)

        self.boat= Boat()
        self.barrigate1 = M_3(3500*3,40)
        self.barrigate2 = M_3(4000 * 3, 40)
        game_world.add_object(self.barrigate1, 2)
        game_world.add_object(self.barrigate2, 2)
        pass

    def exit(self):
        return True

    def update(self):
        global window_left, window_bottom
        self.boat.update()
        for box in self.box_list:
            for other, group in box.all_collision():
                if group == 'character:box':
                    pass
        return 0


    def next(self):
        pass
    def delete(self):
        pass
class Boat:
    def __init__(self):
        self.speed = 0
        self.layer_1 = Object([[3668,289, 212, 100, 2944, 40]], 1)
        game_world.add_object(self.layer_1, 2)

        self.box_list = [game_world.box(2944 * 3-int(212*3/2), 0, 2944 * int(212*3/2), 40*3)]

        game_world.add_collision_pairs(None, self, "character:boat")
        o =game_world.box(2944 * 3-212*3, 0, 2944 * 3+212*3, 25*3)
        game_world.add_collision_pairs(None, o, "character:box")
        game_world.add_collision_pairs(o, None, "boat:box")
        self.box_list.append((o))
        pass

    def exit(self):
        return True
    def update(self):
        global window_left
        for box in self.box_list:
            for other, group in box.all_collision():
                if group == 'character:box':
                    pass
                elif group == "boat:box":
                    self.speed = 0
        self.layer_1.move(self.speed * game_framework.frame_time, 0)
        for i in self.box_list:
            i.move_box(self.speed * game_framework.frame_time, 0)

        return 0
        pass
    def get_bb(self):
        return self.box_list[0].get_bb()
    def handle_collision(self, other, group):
        if group == 'character:boat':
            self.speed = RUN_SPEED_PPS
        pass
    pass
class Object:
    def __init__(self,list, max_frame):
        self.list = list
        self.frame_max = max_frame
        self.frame = 0

        pass
    def exit(self):
        return True

    def update(self):
        if self.frame_max == None:
            self.frame = clamp(0,(self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time),len(self.list)-1)
            pass
        else:
            self.frame = (self.frame+FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % self.frame_max
        pass

    def draw(self):
        global image
        x, y, wid, hei, sx,sy= self.list[int(self.frame)]
        image.clip_draw(x, 1685-y-hei, wid, hei,sx*3-window_left,sy*3,wid*3,hei*3)
        pass
    def move(self, dx, dy):
        for l in range(len(self.list)):
            self.list[l][4] += (dx/3)
            self.list[l][5] += (dy/3)
def enter():
    global image, img_hei, img_wid,canvas_width,canvas_height
    if image == None:
        image = load_image("sprites/object.png")

    img_hei = image.h
    img_wid = image.w

    canvas_width = 900
    canvas_height = 600

    game_world.add_object(background(), 0)
    game_world.add_object(stage(),1)
    pass

