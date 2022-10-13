import charcter_sheet
from pico2d import *

class Charcter:
     def __init__(self):
         self.leg_frame = -1
         self.body_frame = -1

         self.image_1 = load_image('sprites/player.png')
         self.image_m1 = load_image('sprites/player_r.png')

         self.up_body_list = charcter_sheet.handgun_waiting_body
         self.leg_list = charcter_sheet.waiting_leg
         self.leg_frame_m = len(self.leg_list)
         self.body_frame_m = len(self.up_body_list)

         self.direct_x = 1
         self.direct_y = 0
         self.speed_x = 0
         self.speed_y = 0
         self.player_x = 40
         self.player_y = 50

         self.life = 1
         self.respon = 6
         self.situation = 0 # 0= 평소 상태 1=  공격 상태 2= 근접공격시작 3= 근접 공격  3= 투척상태 주로 상체의 상태
         self.Old_situation = 0# 0= 평소 상태 1=  공격 상태 2= 근접공격시작 3= 근접 공격  3= 투척상태 주로 상체의 상태
     def draw(self):
         if self.respon>0:
             x, y, wid, hei, px, py = charcter_sheet.responing[6-self.respon]
             self.image_1.clip_draw(x, 2379 - y - hei, wid, hei, self.player_x + 2*px, self.player_y + 2*py, 2*wid, 2*hei)
             self.respon -= 1
             return

         # leg
         self.leg_frame = (self.leg_frame + 1) % self.leg_frame_m
         x, y, wid, hei, px, py = self.leg_list[self.leg_frame]
         if self.direct_x == 1 :
            self.image_1.clip_draw(x, 2379 - y - hei, wid, hei, self.player_x + px, self.player_y + py, 2*wid, 2*hei)
         elif self.direct_x == -1:
             self.image_m1.clip_draw(1278-x-wid, 2379 - y - hei, wid, hei, self.player_x - 2*px, self.player_y + 2*py, 2*wid, 2*hei)
             pass

         # up_body
         self.body_frame = (self.body_frame + 1) % self.body_frame_m
         x, y, wid, hei, px, py = self.up_body_list[self.body_frame]
         if self.direct_x == 1:
            self.image_1.clip_draw(x, 2379 - y - hei, wid, hei, self.player_x+px, self.player_y+py)
         elif self.direct_x == -1:
             self.image_m1.clip_draw(1278-x-wid, 2379 - y - hei, wid, hei, self.player_x - 2*px, self.player_y + 2*py, 2*wid, 2*hei)

         return
     def key_update(self, type, key):
         if self.respon <= 0:
             if type == SDL_KEYDOWN:
                if key == SDLK_RIGHT:
                    self.speed_x += 1
                    self.direct_x = 1
                elif key == SDLK_LEFT:
                    self.speed_x += -1
                    self.direct_x = -1
                    pass
                elif key == SDLK_UP:
                    self.direct_y = 1
                    pass
                elif key == SDLK_DOWN:
                    pass
                elif key == SDLK_x:
                    self.Old_situation = self.situation
                    self.situation = 1
                    pass
             elif type == SDL_KEYUP:
                 if key == SDLK_RIGHT:
                     self.speed_x -= 1
                     pass
                 elif key == SDLK_LEFT:
                     self.speed_x += 1
                     pass
                 elif key == SDLK_UP:
                     if self.direct_y == 1:
                        self.direct_y = 0
                     pass
                 elif key == SDLK_DOWN:

                     pass
         pass
     def animation(self):
        #leg
         if self.speed_x != 0:
             if self.leg_list != charcter_sheet.walking_leg:
                 self.leg_list = charcter_sheet.walking_leg
                 self.leg_frame_m = len(charcter_sheet.walking_leg)
                 self.leg_frame = -1
         else :
             if self.leg_list != charcter_sheet.walking_stop_leg and self.leg_list != charcter_sheet.waiting_leg:
                 self.leg_list = charcter_sheet.walking_stop_leg
                 self.leg_frame_m = len(self.leg_list)
                 self.leg_frame = -1
             elif self.leg_list == charcter_sheet.walking_stop_leg and self.leg_frame == len(charcter_sheet.walking_stop_leg) - 2:
                 self.leg_list = charcter_sheet.waiting_leg
                 self.leg_frame_m = len(charcter_sheet.waiting_leg)
                 self.leg_frame = -1
        #body
         if self.situation == 1:
            if self.Old_situation == 0 or (self.body_frame > 4):
                self.up_body_list = charcter_sheet.handgun_shot_body
                self.body_frame_m = len(charcter_sheet.handgun_shot_body)
                self.body_frame = -1
                self.Old_situation = 1
                self.situation = 0

         elif self.Old_situation == 0:
             if self.direct_y !=0:
                 if self.direct_y == 1:
                     if self.up_body_list != charcter_sheet.handgun_aim_up_wait_body and self.up_body_list != charcter_sheet.handgun_aim_up_body:
                         self.up_body_list = charcter_sheet.handgun_aim_up_wait_body
                         self.body_frame_m = len(charcter_sheet.handgun_aim_up_wait_body)
                         self.body_frame = -1
                 pass
             elif self.speed_x == 0:
                 if self.up_body_list != charcter_sheet.handgun_waiting_body:
                     self.up_body_list = charcter_sheet.handgun_waiting_body
                     self.body_frame_m = len(charcter_sheet.handgun_waiting_body)
                     self.body_frame = -1
             else :
                 if self.up_body_list != charcter_sheet.handgun_walking_body:
                     self.up_body_list = charcter_sheet.handgun_walking_body
                     self.body_frame_m = len(charcter_sheet.handgun_walking_body)
                     self.body_frame = -1
             pass

         if self.up_body_list == charcter_sheet.handgun_shot_body and self.body_frame == self.body_frame_m - 2:
            self.Old_situation = 0
         elif self.up_body_list == charcter_sheet.handgun_aim_up_wait_body and self.body_frame == self.body_frame_m - 2:
            self.up_body_list = charcter_sheet.handgun_aim_up_body
            self.body_frame_m = len(charcter_sheet.handgun_aim_up_body)
            self.body_frame = -1
     def update(self):
        self.player_x += self.speed_x
        self.player_y += self.speed_y
        self.animation()
        pass           