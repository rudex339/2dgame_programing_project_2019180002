import character
import object
import stage
from pico2d import*

class World:
    def __init__(self):
        stage.enter()
        self.player = character.Charcter()

    def draw(self):
        stage.draw_1()
        self.player.draw(stage.m_x*3,stage.m_y*3)
        stage.draw_2()
    def update(self):
        x, y = 0,0
        y -= 10
        mx, my = stage.check_object(self.player,x,y)
        if my < -10:
            self.player.input_jump(1)
        self.player.speed_change(mx,my)
        self.player.update(stage.m_x*3)
        stage.focus_player(self.player)
        stage.update()

        delay(0.05)
    def handle_events(self, type, key):
        self.player.handle_events(type, key)



