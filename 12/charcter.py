from pico2d import *

import charcter_sheet
import game_framework
import game_world
import server
from bullet import Bullet

RD, LD, RU, LU, UD, UU, DD, DU, X, Z, WAIT, ATK = range(12)
leg_key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RD,
    (SDL_KEYDOWN, SDLK_LEFT): LD,
    (SDL_KEYUP, SDLK_RIGHT): RU,
    (SDL_KEYUP, SDLK_LEFT): LU,
    (SDL_KEYDOWN, SDLK_z): Z
}
body_key_event_table = {
(SDL_KEYDOWN, SDLK_RIGHT): RD,
    (SDL_KEYDOWN, SDLK_LEFT): LD,
    (SDL_KEYUP, SDLK_RIGHT): RU,
    (SDL_KEYUP, SDLK_LEFT): LU,
    (SDL_KEYDOWN, SDLK_UP): UD,
    (SDL_KEYDOWN, SDLK_DOWN): DD,
    (SDL_KEYUP, SDLK_UP): UU,
    (SDL_KEYUP, SDLK_DOWN): DU,
    (SDL_KEYDOWN, SDLK_x): X
}

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 40.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8


class leg_IDLE:
    frame_max = None
    @staticmethod
    def enter(self,event):
        if leg_IDLE.frame_max == None:
            leg_IDLE.frame_max = len(charcter_sheet.waiting_leg)
        self.frame_leg = 0
        pass
    @staticmethod
    def exit(self,event):
        return True
    @staticmethod
    def do(self):
        self.frame_leg = ((self.frame_leg + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % leg_IDLE.frame_max)

        if self.jump:
            self.speed_y -= RUN_SPEED_PPS * 20
            self.add_event(Z, 'leg')
        pass

    @staticmethod
    def draw(self):
        x, y, wid, hei, px, py = charcter_sheet.waiting_leg[(int)(self.frame_leg)]
        sx, sy = self.x-server.background.window_left, self.y-server.background.window_bottom
        if self.dir == -1:
            self.image.clip_composite_draw(x, 2379 - y - hei, wid, hei,0.0, 'h', sx+ 2*px, sy + 2*py, 2*wid, 2*hei)
        else:
            self.image.clip_composite_draw(x, 2379 - y - hei, wid, hei, 0.0, '', sx + 2 * px, sy + 2 * py,2 * wid, 2 * hei)
        pass
class leg_RUN:
    frame_max = None
    def enter(self,event):
        if leg_RUN.frame_max == None:
            leg_RUN.frame_max = len(charcter_sheet.walking_leg)
        self.frame_leg = 0
        pass
    def exit(self,event):
        return True
    def do(self):
        self.frame_leg = ((self.frame_leg + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % leg_RUN.frame_max)

        if self.jump:
            self.speed_y -= RUN_SPEED_PPS * 20
            self.add_event(Z, 'leg')
        pass
    def draw(self):
        x, y, wid, hei, px, py = charcter_sheet.walking_leg[(int)(self.frame_leg)]
        sx, sy = self.x-server.background.window_left, self.y-server.background.window_bottom
        if self.dir == -1:
            self.image.clip_composite_draw(x, 2379 - y - hei, wid, hei, 0.0, 'h', sx + 2 * px, sy + 2 * py,
                                           2 * wid, 2 * hei)
        else:
            self.image.clip_composite_draw(x, 2379 - y - hei, wid, hei, 0.0, '', sx + 2 * px, sy + 2 * py,
                                           2 * wid, 2 * hei)
        pass
class leg_JUMP:
    frame_max = None

    def enter(self,event):
        if leg_JUMP.frame_max == None:
            leg_JUMP.frame_max = len(charcter_sheet.walk_jump_leg)
        self.frame_leg = 0
        if not self.jump:
            self.speed_y += RUN_SPEED_PPS*4
            self.y += 10
            self.legbox.move_box(0, 10)
        pass

    def exit(self,event):
        return True

    def do(self):
        self.frame_leg = ((self.frame_leg + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % leg_JUMP.frame_max)

        if not self.jump:
            self.add_event(WAIT, 'leg')
        pass


    def draw(self):
        x, y, wid, hei, px, py = charcter_sheet.walk_jump_leg[(int)(self.frame_leg)]
        sx, sy = self.x-server.background.window_left, self.y-server.background.window_bottom
        if self.dir == -1:
            self.image.clip_composite_draw(x, 2379 - y - hei, wid, hei,0.0, 'h', sx+ 2*px, sy + 2*py, 2*wid, 2*hei)
        else:
            self.image.clip_composite_draw(x, 2379 - y - hei, wid, hei, 0.0, '', sx + 2 * px, sy + 2 * py,2 * wid, 2 * hei)
        pass
class leg_STOP:
    frame_max = None
    @staticmethod
    def enter(self, event):
        if leg_STOP.frame_max == None:
            leg_STOP.frame_max = len(charcter_sheet.walking_stop_leg)
        self.frame_leg = 0
        pass

    @staticmethod
    def exit(self, event):
        return True

    @staticmethod
    def do(self):

        self.frame_leg = ((self.frame_leg + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time))
        if (int)(self.frame_leg) == leg_STOP.frame_max:
            self.add_event(WAIT, 'leg')
        elif self.jump:
            self.add_event(Z, 'leg')
        elif self.speed_x != 0:
            self.add_event(LD, 'leg')
        pass

    @staticmethod
    def draw(self):
        x, y, wid, hei, px, py = charcter_sheet.walking_stop_leg[(int)(self.frame_leg)]
        sx, sy = self.x-server.background.window_left, self.y-server.background.window_bottom
        if self.dir == -1:
            self.image.clip_composite_draw(x, 2379 - y - hei, wid, hei, 0.0, 'h', sx + 2 * px, sy + 2 * py,
                                           2 * wid, 2 * hei)
        else:
            self.image.clip_composite_draw(x, 2379 - y - hei, wid, hei, 0.0, '', sx + 2 * px, sy + 2 * py,
                                           2 * wid, 2 * hei)
        pass
class body_IDLE:
    frame_max = None
    def enter(self,event):
        if body_IDLE.frame_max == None:
            body_IDLE.frame_max = len(charcter_sheet.handgun_waiting_body)
        self.frame_body = 0
        pass
    def exit(self,event):
        return True
    def do(self):
        self.frame_body = ((self.frame_body + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % body_IDLE.frame_max)
        pass
    def draw(self):
        x, y, wid, hei, px, py = charcter_sheet.handgun_waiting_body[(int)(self.frame_body)]
        sx, sy = self.x-server.background.window_left, self.y-server.background.window_bottom
        if self.dir == -1:
            self.image.clip_composite_draw(x, 2379 - y - hei, wid, hei, 0.0, 'h', sx + 2 * px* -1, sy + 2 * py,
                                           2 * wid, 2 * hei)
        else:
            self.image.clip_composite_draw(x, 2379 - y - hei, wid, hei, 0.0, '', sx + 2 * px, sy + 2 * py,
                                           2 * wid, 2 * hei)
        pass
class body_RUN:
    frame_max = None

    def enter(self, event):
        if body_RUN.frame_max == None:
            body_RUN.frame_max = len(charcter_sheet.handgun_walking_body)
        self.frame_body = 0
        pass

    def exit(self, event):
        return True

    def do(self):
        self.frame_body = ((self.frame_body + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % body_RUN.frame_max)
        pass

    def draw(self):
        x, y, wid, hei, px, py = charcter_sheet.handgun_walking_body[(int)(self.frame_body)]
        sx, sy = self.x-server.background.window_left, self.y-server.background.window_bottom
        if self.dir == -1:
            self.image.clip_composite_draw(x, 2379 - y - hei, wid, hei, 0.0, 'h', sx + 2 * px* -1, sy + 2 * py,
                                           2 * wid, 2 * hei)
        else:
            self.image.clip_composite_draw(x, 2379 - y - hei, wid, hei, 0.0, '', sx + 2 * px, sy + 2 * py,
                                           2 * wid, 2 * hei)
        pass
class body_ATTACK:
    frame_max = None
    bgm = None
    def enter(self, event):
        if body_ATTACK.frame_max == None:
            body_ATTACK.frame_max = len(charcter_sheet.handgun_shot_body)
            body_ATTACK.bgm = load_wav("sound/effect/st1_01.wav")
        self.frame_body = 0
        bullet = Bullet(self.x+self.dir*33,self.y+32,self.dir)
        game_world.add_object(bullet,2)
        body_ATTACK.bgm.set_volume(32)
        body_ATTACK.bgm.play(1)
        pass

    def exit(self, event):
        return True

    def do(self):
        self.frame_body = ((self.frame_body + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time))
        if (int)(self.frame_body) == body_ATTACK.frame_max:
            self.add_event(ATK, 'body')
        pass

    def draw(self):
        x, y, wid, hei, px, py = charcter_sheet.handgun_shot_body[(int)(self.frame_body)]
        sx, sy = self.x-server.background.window_left, self.y-server.background.window_bottom
        if self.dir == -1:
            self.image.clip_composite_draw(x, 2379 - y - hei, wid, hei, 0.0, 'h', sx + 2 * px * -1, sy + 2 * py,
                                           2 * wid, 2 * hei)
        else:
            self.image.clip_composite_draw(x, 2379 - y - hei, wid, hei, 0.0, '', sx + 2 * px, sy + 2 * py,
                                           2 * wid, 2 * hei)
        pass
leg_state = {
    leg_IDLE:  {RU: leg_IDLE,  LU: leg_IDLE,  RD:  leg_RUN,  LD: leg_RUN, Z: leg_JUMP, WAIT: leg_STOP},
    leg_RUN:   {RU: leg_STOP,  LU: leg_STOP, RD: leg_RUN, LD: leg_RUN, Z: leg_JUMP, WAIT: leg_STOP},
    leg_JUMP:   {RU: leg_JUMP,  LU: leg_JUMP, RD: leg_JUMP, LD: leg_JUMP, Z: leg_JUMP, WAIT: leg_STOP},
    leg_STOP:{RU: leg_IDLE,  LU: leg_IDLE, RD: leg_RUN, LD: leg_RUN, Z: leg_IDLE, WAIT: leg_IDLE}
}
body_state = {
    body_IDLE:  {RU: body_IDLE,  LU: body_IDLE,  RD:  body_RUN,  LD: body_RUN, X: body_ATTACK, ATK:body_IDLE},
    body_RUN:   {RU:  body_IDLE,  LU: body_IDLE, RD: body_IDLE, LD: body_IDLE, X:body_ATTACK, ATK:body_RUN},
    body_ATTACK:   {RU: body_ATTACK,  LU: body_ATTACK, RD: body_ATTACK, LD: body_ATTACK, X: body_ATTACK, ATK:body_RUN}
}

class Charcter:

    def __init__(self):
        self.x, self.y = 200, 400
        self.frame_leg = 0
        self.frame_body = 0
        self.speed_x, self.speed_y, self.dir = 0, 0,1
        self.temp_sp_x,self.temp_sp_y = 0,0
        self.image = load_image('sprites/player.png')

        self.event_que_leg = []
        self.event_que_body = []

        self.cur_state_leg = leg_IDLE
        self.cur_state_body = body_IDLE

        self.cur_state_leg.enter(self, None)
        self.cur_state_body.enter(self, None)

        self.legbox = game_world.box(self.x-15 ,self.y-21,self.x+15,self.y+21)

        self.jump = True
        game_world.add_collision_pairs(self.legbox, None, "character:box")
        game_world.add_collision_pairs(self.legbox, None, "character:enemy")
        game_world.add_collision_pairs(self.legbox, None, "character:boat")
        game_world.add_collision_pairs(self.legbox, None, "character:check_box")
    def update(self):
        self.collision()

        self.speed_y -= RUN_SPEED_PPS / 20

        self.cur_state_leg.do(self)
        self.cur_state_body.do(self)
        if self.event_que_leg:
            event = self.event_que_leg.pop()
            if self.cur_state_leg.exit(self,event):
                try:
                    self.cur_state_leg = leg_state[self.cur_state_leg][event]
                except KeyError:
                    print(self.cur_state_leg, event)
                self.cur_state_leg.enter(self, event)
        if self.event_que_body:
            event = self.event_que_body.pop()
            if self.cur_state_body.exit(self,event):
                try:
                    self.cur_state_body = body_state[self.cur_state_body][event]
                except KeyError:
                    print(self.cur_state_body, event)
                self.cur_state_body.enter(self, event)

        self.x += (self.speed_x +self.temp_sp_x) * game_framework.frame_time
        self.y += (self.speed_y) * game_framework.frame_time
        self.legbox.move_box((self.speed_x +self.temp_sp_x) * game_framework.frame_time,
                             (self.speed_y) * game_framework.frame_time)

        self.x = clamp(server.background.window_left+20,self.x,server.background.window_left+880)

    def draw(self):
        self.cur_state_leg.draw(self)
        self.cur_state_body.draw(self)
    def add_event(self, event,state):
        if state == 'leg':
            self.event_que_leg.insert(0, event)
        elif state == 'body':
            self.event_que_body.insert(0, event)
    def handle_event(self, event):
        if (event.type, event.key) in leg_key_event_table:
            key_event = leg_key_event_table[(event.type, event.key)]
            self.add_event(key_event, 'leg')
        if (event.type, event.key) in body_key_event_table:
            key_event = body_key_event_table[(event.type, event.key)]
            self.add_event(key_event, 'body')

        if event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
            self.dir = 1
            self.speed_x += RUN_SPEED_PPS
        elif event.type == SDL_KEYDOWN and event.key == SDLK_LEFT:
            self.dir = -1
            self.speed_x -= RUN_SPEED_PPS
        elif event.type == SDL_KEYUP and event.key == SDLK_RIGHT:
            self.speed_x -= RUN_SPEED_PPS
        elif event.type == SDL_KEYUP and event.key == SDLK_LEFT:
            self.speed_x += RUN_SPEED_PPS

    def collision(self):
        self.jump = True
        self.temp_sp_x = 0
        for other, group in self.legbox.all_collision():
            if group == 'character:box':
                if abs(other.bottom - self.legbox.top)<50 or abs(other.top - self.legbox.bottom)<50:
                    if self.legbox.bottom + self.legbox.top < other.top + other.bottom:
                        self.y += other.bottom - self.legbox.top
                        self.legbox.move_box(0, other.bottom - self.legbox.top)
                        self.speed_y = 0
                    else:
                        self.y += other.top - self.legbox.bottom
                        self.legbox.move_box(0, other.top - self.legbox.bottom)
                        self.speed_y = 0
                        self.jump = False

                else:
                    if self.legbox.left + self.legbox.right < other.left + other.right:
                        self.x += other.left - self.legbox.right
                        self.legbox.move_box(other.left - self.legbox.right,0)
                    else:
                        self.x += other.right - self.legbox.left
                        self.legbox.move_box(other.right - self.legbox.left,0)
            elif group == "character:boat":
                self.temp_sp_x += other.speed
            pass
