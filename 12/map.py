from pico2d import *

class Grass:
    image = None
    def __init__(self, ID):
        if Grass.image == None:
            Grass.image = load_image('grass.png')
        self.ID = ID
    def draw(self):
        if self.ID == 0:
            Grass.image.draw(400, 45)
        elif self.ID == 1:
            Grass.image.draw(400, 30)
    def update(self):
        pass

