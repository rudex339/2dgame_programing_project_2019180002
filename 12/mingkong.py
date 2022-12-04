import map
from pico2d import *
import game_world
import game_framework
import server

AT, WAIT, move, DIE= 0, 1, 2,3

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 40.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

image = None

class IDLE:
    list = [[15,27,51,45],
            [82,27,50,45],
            [147,27,50,45],
            [211,28,52,44],
            [279,28,53,44],
            [347,28,53,44],
            [415,27,50,44]]
    def enter(self):
        self.frame = 0
        self.frame_max = len(IDLE.list)
        self.speed_x = 0
        pass

    def exit(self):
        return True

    def do(self):
        self.frame = ((self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % self.frame_max)
        for other, group in self.check_box1.all_collision():
            if group == "character:check_box":
                print("2")

                if  self.hit_box.top + self.hit_box.bottom < other.bottom + other.top :
                    self.dir = -1

                else:
                    self.dir = 1
                self.add_event(AT)
                return
        for other, group in self.check_box2.all_collision():
            if group == "character:check_box":
                print("1")
                if self.hit_box.top + self.hit_box.bottom < other.bottom + other.top:
                    self.dir = 1

                else:
                    self.dir = -1
                self.add_event(move)

                return
        pass



        pass


    def draw(self):
        global image
        x, y, wid, hei = IDLE.list[int(self.frame)]
        sx, sy = self.x - server.background.window_left, self.y - server.background.window_bottom
        if self.dir == -1:
            image.clip_composite_draw(x, 1943 - y - hei, wid, hei, 0.0, 'h', sx, sy,
                                           2 * wid, 2 * hei)
        else:
            image.clip_composite_draw(x, 1943 - y - hei, wid, hei, 0.0, ' ', sx, sy,
                                           2 * wid, 2 * hei)
class ATTACK:
    list = [[18, 414, 52, 44],
            [83, 414, 52, 44],
            [147, 415, 53, 43],
            [212, 416, 55, 42],
            [289, 416, 56, 43],
            [355, 414, 57, 44],
            [425, 413, 57, 45],
            [495, 413, 54, 45],
            [564, 414, 53, 44],
            [16, 477, 56, 46],
            [87, 478, 53, 45],
            [148, 477, 54, 46],
            [217, 478, 55, 45]
            ]
    def enter(self):
        self.frame = 0
        self.frame_max = len(ATTACK.list)
        pass

    def exit(self):
        return True

    def do(self):
        self.frame = ((self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time))

        if int(self.frame) == 9:
            bubble = Bubble(self.x + self.dir * 33, self.y + 32, self.dir)
            game_world.add_object(bubble, 2)

        if int(self.frame) >= self.frame_max-1:
            self.add_event(WAIT)
        pass

    def draw(self):
        global image
        x, y, wid, hei = ATTACK.list[int(self.frame)]
        sx, sy = self.x - server.background.window_left, self.y - server.background.window_bottom
        if self.dir == -1:
            image.clip_composite_draw(x, 1943 - y - hei, wid, hei, 0.0, 'h', sx, sy,
                                           2 * wid, 2 * hei)
        else:
            image.clip_composite_draw(x, 1943 - y - hei, wid, hei, 0.0, ' ', sx, sy,
                                           2 * wid, 2 * hei)
        pass

class WALK:
    list = [[15,90,51,44],
            [82,90,48,45],
            [150,90,49,45],
            [210,91,49,44],
            [275,91,48,44],
            [349,91,51,44],
            [415,91,50,44]]
    def enter(self):
        self.frame = 0
        self.frame_max = len(WALK.list)
        self.speed_x += self.dir*RUN_SPEED_PPS/2
        pass

    def exit(self):
        return True

    def do(self):
        self.frame = ((self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time))
        if int(self.frame) >= self.frame_max-1:
            print("stop")
            self.add_event(WAIT)
        pass

    def draw(self):
        global image
        x, y, wid, hei = WALK.list[int(self.frame)]
        sx, sy = self.x - server.background.window_left, self.y - server.background.window_bottom
        if self.dir == -1:
            image.clip_composite_draw(x, 1943 - y - hei, wid, hei, 0.0, 'h', sx, sy,
                                           2 * wid, 2 * hei)
        else:
            image.clip_composite_draw(x, 1943 - y - hei, wid, hei, 0.0, ' ', sx, sy,
                                           2 * wid, 2 * hei)
class DEAD:
    list = [[42, 1173, 53, 44],
            [107, 1168, 52, 49],
            [42, 1173, 53, 44],
            [170, 1198, 52, 49],
            [42, 1173, 53, 44],
            [42, 1173, 53, 44],
            [170, 1198, 52, 49]]

    def enter(self):
        self.frame = 0
        self.frame_max = len(DEAD.list)
        pass

    def exit(self):
        return True

    def do(self):
        self.frame = ((self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % self.frame_max)
        if int(self.frame) >= self.frame_max - 1:
            self.exit()
        pass

    def draw(self):
        global image
        x, y, wid, hei = DEAD.list[int(self.frame)]
        sx, sy = self.x - server.background.window_left, self.y - server.background.window_bottom
        if self.dir == -1:
            image.clip_composite_draw(x, 1943 - y - hei, wid, hei, 0.0, 'h', sx, sy,
                                      2 * wid, 2 * hei)
        else:
            image.clip_composite_draw(x, 1943 - y - hei, wid, hei, 0.0, ' ', sx, sy,
                                      2 * wid, 2 * hei)
state = {
    IDLE:  {AT: ATTACK,WAIT:IDLE, move:WALK,  DIE: DEAD},
    ATTACK:   {AT: ATTACK,WAIT:IDLE, move:WALK,  DIE: DEAD},
    WALK:{AT: ATTACK,WAIT:IDLE, move:WALK,  DIE: DEAD},
    DEAD :{AT: ATTACK,WAIT:IDLE, move:WALK,  DIE: DEAD}
}
class Mingkong:

    def __init__(self, x, y, dir):
        self.hp = 1
        global image
        if image == None:
            image = load_image("sprites/Neo Geo NGCD - Metal Slug 3 - Chowmein Conga.png")
        self.x, self.y, self.dir = x, y, dir
        self.speed_x, self.speed_y = 0,0
        self. cur_state = IDLE
        self.cur_state.enter(self)
        self.event_que = []
        self.ready= False



        self.check_box1 = game_world.box(x-200, y-200, x+200, y+200)
        self.check_box2 = game_world.box(x - 80, y - 200, x + 80, y + 200)
        game_world.add_collision_pairs(None, self.check_box1, "character:check_box")
        game_world.add_collision_pairs(None, self.check_box2, "character:check_box")
        self.hit_box = game_world.box(x-50, y-40, x+50, y+40)
        game_world.add_collision_pairs(self.hit_box,None,  "character:box")
        game_world.add_collision_pairs(self.hit_box,None,  "bullet:hitbox")
        pass

    def exit(self):
        game_world.remove_collision_object(self.hit_box)
        game_world.remove_collision_object(self.check_box1)
        game_world.remove_collision_object(self.check_box2)
        game_world.remove_object(self)
        return True

    def update(self):

        for other, group in self.hit_box.all_collision():
                if group == 'character:box':
                    if abs(other.bottom - self.hit_box.top) < 50 or abs(other.top - self.hit_box.bottom) < 50:
                        if self.hit_box.bottom + self.hit_box.top < other.top + other.bottom:
                            self.y += other.bottom - self.hit_box.top
                            self.hit_box.move_box(0, other.bottom - self.hit_box.top)
                            self.check_box1.move_box(0, other.bottom - self.hit_box.top)
                            self.check_box2.move_box(0, other.bottom - self.hit_box.top)
                            self.speed_y = 0
                        else:
                            self.y += other.top - self.hit_box.bottom
                            self.hit_box.move_box(0, other.top - self.hit_box.bottom)
                            self.check_box1.move_box(0, other.top - self.hit_box.bottom)
                            self.check_box2.move_box(0, other.top - self.hit_box.bottom)
                            self.speed_y = 0

                    else:
                        if self.hit_box.left + self.hit_box.right < other.left + other.right:
                            self.x += other.left - self.hit_box.right
                            self.hit_box.move_box(other.left - self.hit_box.right, 0)
                            self.check_box1.move_box(other.left - self.hit_box.right, 0)
                            self.check_box2.move_box(other.left - self.hit_box.right, 0)
                        else:
                            self.x += other.right - self.hit_box.left
                            self.hit_box.move_box(other.right - self.hit_box.left, 0)
                            self.check_box1.move_box(other.right - self.hit_box.left, 0)
                            self.check_box2.move_box(other.right - self.hit_box.left, 0)
                elif group == "bullet:hitbox":
                    self.hp -= 1

        self.speed_y -= RUN_SPEED_PPS / 20

        self.cur_state.do(self)

        if self.hp == 0 or self.x < server.background.window_left or self.y < server.background.window_bottom:
            self.add_event(DIE)
            self.hp -= 1

        if self.event_que:
            event = self.event_que.pop()
            if self.cur_state.exit(self):
                try:
                    self.cur_state = state[self.cur_state][event]
                except KeyError:
                    print(self.cur_state, event)
                self.cur_state.enter(self)

        self.x += self.dir*(self.speed_x) * game_framework.frame_time
        self.y += (self.speed_y) * game_framework.frame_time
        self.hit_box.move_box(self.dir*(self.speed_x ) * game_framework.frame_time,
                             (self.speed_y) * game_framework.frame_time)
        self.check_box1.move_box(self.dir * (self.speed_x) * game_framework.frame_time,
                              (self.speed_y) * game_framework.frame_time)
        self.check_box2.move_box(self.dir * (self.speed_x) * game_framework.frame_time,
                                 (self.speed_y) * game_framework.frame_time)

        pass
    def add_event(self, event):
        self.event_que.insert(0, event)

    def draw(self):
        self.cur_state.draw(self)

class Bubble:

        def __init__(self, x=800, y=300, dir=1):

            self.x, self.y, self.dir = x, y, -dir
            game_world.add_collision_pairs(self, None, "character:box")
            game_world.add_collision_pairs(None, self, "character:enemy")

        def draw(self):
            global image
            sx, sy = self.x - server.background.window_left, self.y - server.background.window_bottom
            if self.dir == -1:
                image.clip_composite_draw(43, 1943-1571-16, 16, 16, 0.0, 'h', sx, sy,
                                               32, 32)
            else:
                image.clip_composite_draw(43, 1943-1571-16, 16, 16, 0.0, ' ', sx, sy,
                                          32, 32)

        def update(self):
            self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time

            if self.x - server.background.window_left < -10 or self.x - server.background.window_left > 910:
                print("bullet delete")
                game_world.remove_object(self)
                game_world.remove_collision_object(self)

        def get_bb(self):
            return self.x - 27 / 2, self.y - 5 / 2, self.x + 27 / 2, self.y + 5 / 2

        def handle_collision(self, other, group):
            if group == 'character:box':
                pass
            elif group == "character:enemy":
                print("bullet hit")
                pass
            game_world.remove_collision_object(self)
            game_world.remove_object(self)

            pass