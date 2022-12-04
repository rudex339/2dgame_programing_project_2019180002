from pico2d import *
import game_world
import game_framework
import server

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 80.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8
class Bullet:
        image = None

        def __init__(self, x = 800, y = 300, dir = 1):
            if Bullet.image == None:
                        Bullet.image = load_image('sprites/bullet.png')
            self.x, self.y, self.dir = x,y, dir
            game_world.add_collision_pairs(self, None, "character:box")
            game_world.add_collision_pairs( None,self, "bullet:hitbox")
        def draw(self):
                sx, sy = self.x - server.background.window_left, self.y - server.background.window_bottom
                if self.dir == -1:
                        self.image.clip_composite_draw(0, 0, 27, 5, 0.0, 'h', sx, sy,
                                                       54, 10)
                else:
                        self.image.clip_composite_draw(0, 0, 27, 5, 0.0, '', sx, sy,
                                                       54, 10)

        def update(self):
                self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time


                if self.x - server.background.window_left < -10 or self.x - server.background.window_left > 910:
                        print("bullet delete")
                        game_world.remove_object(self)
                        game_world.remove_collision_object(self)

        def get_bb(self):
                return self.x - 27/2, self.y - 5/2, self.x+27/2, self.y+5/2

        def handle_collision(self, other, group):
                if group == 'character:box':
                        pass
                elif group == 'bullet:hitbox':
                    print("bullet hit")
                    pass
                game_world.remove_object(self)
                game_world.remove_collision_object(self)


                pass
