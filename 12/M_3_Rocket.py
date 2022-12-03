import map
from pico2d import *
import game_world
import game_framework
import server

AT, WAIT= 1, 2

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 40.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

class IDLE:
    list = [[26,44,128,132],
            [172,44,128,132],
            [326,45,128,131],
            [477,44,128,132]]
    def enter(self):
        self.frame = 0
        self.frame_max = len(IDLE.list)
        self.timer = 0
        pass

    def exit(self):
        return True

    def do(self):
        self.timer += 1
        self.frame = ((self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % self.frame_max)
        if self.timer == 10000 and self.ready == True:
            self.add_event(AT)
        pass

    def draw(self):
        x, y, wid, hei = IDLE.list[int(self.frame)]
        M_3.image.clip_draw(x, 1024 - y - hei, wid, hei, self.x - server.background.window_left,self.y+int(hei *3/2), wid * 3, hei * 3)
class ATTACK:
    list = [[26, 266, 128, 134],
            [171, 265, 128, 135],
            [328, 231, 128, 169],
            [482, 217, 128, 183],
            [638, 215, 128, 185],
            [782, 213, 128, 187],
            [29, 717, 128, 187],
            [181, 417, 128, 187],
            [337, 418, 128, 186],
            [484, 429, 128, 175],
            [637, 452, 128, 152],
            [785, 473, 128, 131]
            ]
    def enter(self):
        self.frame = 0
        self.frame_max = len(ATTACK.list)
        pass

    def exit(self):
        return True

    def do(self):
        self.frame = ((self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time))
        if int(self.frame) >= self.frame_max-1:
            self.add_event(WAIT)
        pass

    def draw(self):
        x, y, wid, hei = ATTACK.list[int(self.frame)]
        M_3.image.clip_draw(x, 1024  - y - hei, wid, hei, self.x - server.background.window_left, self.y + int(hei *3/2) , wid * 3,
                            hei * 3)
        pass
state = {
    IDLE:  {AT: ATTACK,WAIT:IDLE},
    ATTACK:   {AT: ATTACK,WAIT:IDLE}
}
class M_3:
    image = None
    def __init__(self, x, y):
        self.hp = 10
        if M_3.image == None:
            M_3.image = load_image("sprites/M-3 Rocket Launch Support Van.png")
        self.x, self.y = x, y
        self. cur_state = IDLE
        self.cur_state.enter(self)
        self.event_que = []
        self.ready= False

        self.object = map.Object([[2879,1087,204,80, int(self.x/3), int(self.y/3)]],1)
        game_world.add_object(self.object,2)

        self.box_list = [game_world.box(x-100, 0, x+100, y-5)]
        hit_box = game_world.box(x-100, y-5, x+100, y+400)

        game_world.add_collision_pairs(None, self.box_list, "character:box")
        game_world.add_collision_pairs(None, self.box_list, "boat:box")
        game_world.add_collision_pairs(None, hit_box, "bullet:hitbox")

        self.box_list.append(hit_box)
        pass

    def exit(self):

        return True

    def update(self):
        for box in self.box_list:
            for other, group in box.all_collision():
                if group == 'character:boat':
                    pass
                elif group == 'boat:box':
                    self.ready = True
                    pass
                elif group == "bullet:hitbox":
                    print("hit")
                    self.hp -= 1

        self.cur_state.do(self)

        if self.event_que:
            event = self.event_que.pop()
            if self.cur_state.exit(self):
                try:
                    self.cur_state = state[self.cur_state][event]
                except KeyError:
                    print(self.cur_state, event)
                self.cur_state.enter(self)


        if self.hp == 0:
            for box in self.box_list:
                game_world.remove_collision_object(box)
            game_world.remove_object(self.object)
            game_world.remove_object(self)
        pass
    def add_event(self, event):
        self.event_que.insert(0, event)

    def draw(self):
        self.cur_state.draw(self)