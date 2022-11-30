from pico2d import *
import game_world
import server
import game_framework

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

        pass

    def exit(self):
        return True

    def update(self):
        global window_bottom, window_left
        if window_left < int(server.character.x) - 300:
            window_left =int(server.character.x) - 300
        if window_bottom < int(server.character.y) - 400:
            window_bottom =int(server.character.y) - 400
        pass

    def draw(self):
        global image
        x,y,wid,hei = self.object
        image.clip_draw(x, 1685-y-hei, wid, hei, 450, 300,900,600)
        pass
    def get_bb(self):
        pass
    def handle_collision(self,other,group):
        pass
class stage_1_1:
    def __init__(self):#x,y,wid,hei
        self.object =[1,1217,300,200]
        game_world.add_object(Object([[2,669,564,24,282,52],[2,669+66,564,24,282,52],[2,669+66*2,564,24,282,52],[2,669+66*3,564,24,282,52],[2,669+66*4,564,24,282,52],[2,669+66*5,564,24,282,52],[2,669+66*6,564,24,282,52],[2,669+66*7,564,24,282,52]],8), 2)
        self.layer_1_object = 2
        game_world.add_object(Object([[2,694,564,40,282,20],[2,694+66,564,40,282,20],[2,694+66*2,564,40,282,20],[2,694+66*3,564,40,282,20],[2,694+66*4,564,40,282,20],[2,694+66*5,564,40,282,20],[2,694+66*6,564,40,282,20],[2,694+66*7,564,40,282,20]],8), 4)
        self.layer_2_object = 2

        box_list = []
        pass

    def exit(self):
        return True

    def update(self):
        pass

    def draw(self):
        global image
        x, y, wid, hei = self.object
        image.clip_draw(x+int(window_left/3), 1685 - y - hei, wid, hei, 450, 300, 900, 600)
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
        self.frame = (self.frame+FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % self.frame_max
        pass

    def draw(self):
        global image
        x, y, wid, hei, sx,sy= self.list[int(self.frame)]
        image.clip_draw(x, 1685-y-hei, wid, hei,sx*3-window_left,sy*3,wid*3,hei*3)
        pass

class barrigate1:
    def __init__(self, list, max_frame):
        self.list = list
        self.frame_max = max_frame
        self.frame = 0

        pass

    def exit(self):
        return True

    def update(self):
        self.frame += 1
        self.frame = clamp(0, self.frame, self.max_frame)
        pass

    def draw(self):
        global image
        x, y, wid, hei = self.object[self.frame]
        image.clip_draw(x, 1685 - y - hei, wid, hei, 450, 300, 900, 600)
        pass

    def get_bb(self):
        pass

    def handle_collision(self, other, group):
        pass
def enter():
    global image, img_hei, img_wid,canvas_width,canvas_height
    if image == None:
        image = load_image("sprites/object.png")

    img_hei = image.h
    img_wid = image.w

    canvas_width = 900
    canvas_height = 600

    game_world.add_object(background(), 0)
    game_world.add_object(stage_1_1(),1)
    pass

