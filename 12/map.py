from pico2d import *
import game_world

image = None
img_hei = 1685
img_wid = 5172
canvas_width = 0
canvas_height = 0
class background:
    def __init__(self):#x,y,wid,hei
        self.object = [2,67,300,200]

        pass

    def exit(self):
        return True

    def update(self):
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
        game_world.add_object(Object([[2,694,564,40,282,20],[2,694+66,564,40,282,20],[2,694+66*2,564,40,282,20],[2,694+66*3,564,40,282,20],[2,694+66*4,564,40,282,20],[2,694+66*5,564,40,282,20],[2,694+66*6,564,40,282,20],[2,694+66*7,564,40,282,20]],8), 4)
        pass

    def exit(self):
        return True

    def update(self):
        pass

    def draw(self):
        global image
        x, y, wid, hei = self.object
        image.clip_draw(x, 1685 - y - hei, wid, hei, 450, 300, 900, 600)
        pass
    def get_bb(self):
        pass
    def handle_collision(self,other,group):
        pass

class Object:
    def __init__(self,list, max_frame):
        self.list = list
        self.max_frame = max_frame
        self.frame = 0

        pass
    def exit(self):
        return True

    def update(self):
        self.frame += 1
        if self.frame >= self.max_frame:
            self.frame = 0
        pass

    def draw(self):
        global image
        x, y, wid, hei, sx,sy= self.list[self.frame]
        image.clip_draw(x, 1685-y-hei, wid, hei,sx*3,sy*3,wid*3,hei*3)
        pass
    def get_bb(self):
        pass
    def handle_collision(self,other,group):
        pass

class barrigate1:
    def __init__(self, list, max_frame):
        self.list = list
        self.max_frame = max_frame
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

    canvas_width = get_canvas_width()
    canvas_height = get_canvas_height()

    game_world.add_object(background(), 0)
    game_world.add_object(stage_1_1(),1)
    pass

