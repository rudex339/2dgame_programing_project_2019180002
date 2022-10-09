import charcter_sheet
from pico2d import *

class Charcter:
     def __init__(self):
        self.leg_frame = 0
        self.body_frame = 0
        self.image_1 = load_image('sprites/player.png')
        self.image_m1 = load_image('sprites/player_r.png')
        self.up_body_list = charcter_sheet.handgun_waiting_body
        self.leg_list = charcter_sheet.waiting_leg
        self.leg_frame_m = len(self.leg_list)
        self.body_frame_m = len(self.up_body_list)
        self.direct = 1
        self.speed = 0
     def animation(self):
         # leg
         x, y, wid, hei, px, py = self.leg_list[self.leg_frame]
         if self.direct == 1 :
            self.image_1.clip_draw(x, 2379 - y - hei, wid, hei, 400 + px, 50 + py)
         elif self.direct == -1:
             self.image_m1.clip_draw(1278-x-wid, 2379 - y - hei, wid, hei, 400 - px, 50 + py)
             pass
         self.leg_frame = (self.leg_frame + 1) % self.leg_frame_m
         # up_body
         x, y, wid, hei, px, py = self.up_body_list[self.body_frame]
         if self.direct == 1:
            self.image_1.clip_draw(x, 2379 - y - hei, wid, hei, 400+px, 50+py)
         elif self.direct == -1:
             self.image_m1.clip_draw(1278-x-wid, 2379 - y - hei, wid, hei, 400 - px, 50 + py)
             pass
         self.body_frame = (self.body_frame + 1) % self.body_frame_m
     def update(self):
        if self.speed == 1:
             if self.up_body_list != charcter_sheet.handgun_walking_body:
                 self.up_body_list = charcter_sheet.handgun_walking_body
                 self.body_frame_m = len(charcter_sheet.handgun_walking_body)
                 self.body_frame = 0
             if self.leg_list != charcter_sheet.walking_leg:
                 self.leg_list = charcter_sheet.walking_leg
                 self.leg_frame_m = len(charcter_sheet.walking_leg)
                 self.leg_frame = 0
        elif self.speed == -1:
            if self.up_body_list != charcter_sheet.handgun_walking_body:
                self.up_body_list = charcter_sheet.handgun_walking_body
                self.body_frame_m = len(charcter_sheet.handgun_walking_body)
                self.body_frame = 0
            if self.leg_list != charcter_sheet.walking_leg:
                self.leg_list = charcter_sheet.walking_leg
                self.leg_frame_m = len(charcter_sheet.walking_leg)
                self.leg_frame = 0
        elif self.speed == 0:
            if self.up_body_list != charcter_sheet.handgun_waiting_body:
                self.up_body_list = charcter_sheet.handgun_waiting_body
                self.body_frame_m = len(charcter_sheet.handgun_waiting_body)
                self.body_frame = 0
            if self.leg_list != charcter_sheet.waiting_leg:
                self.leg_list = charcter_sheet.waiting_leg
                self.leg_frame_m = len(charcter_sheet.waiting_leg)
                self.leg_frame = 0

     def downput(self, type):
         if type == SDLK_RIGHT:
             self.speed += 1
             self.direct = 1
             pass
         elif type == SDLK_LEFT:
             self.speed += -1
             self.direct = -1
             pass
         elif type == SDLK_UP:

             pass
         elif type == SDLK_DOWN:

             pass
         pass
     def upput(self, type):
         if type == SDLK_RIGHT:
             self.speed -= 1
             pass
         elif type == SDLK_LEFT:
             self.speed += 1
             pass
         elif type == SDLK_UP:

             pass
         elif type == SDLK_DOWN:

             pass
         pass


