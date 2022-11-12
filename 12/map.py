from pico2d import *
import game_world

image = None
img_hei = 1685
img_wid = 5172
class stage_1_1:
    def __init__(self,layer):
        if layer == 1:#x,y,wid,hei
            self.object = [[2,67,300,200],
                           [1,1217,300,200]]
            self.box = [[0, 0, 300, 300]]
            pass
        elif layer == 2:
            self.object = [[],
                           []]
            pass
        self.ID = layer
        pass

    def exit(self):
        return True

    def update(self):
        if self.ID == 1:
            pass
        elif self.ID == 2:
            pass
        pass

    def draw(self):
        global image
        for x,y,wid,hei in self.object:
            image.clip_draw(x, 1685-y-hei, wid, hei, 450, 300,900,600)
        pass
    def get_bb(self):
        return self.box
    def handle_collision(self,other,group):
        pass
def enter():
    global image
    if image == None:
        image = load_image("sprites/object.png")
    game_world.add_object(stage_1_1(1),0)
    #game_world.add_object(stage_1_1(2), 1)
    pass

