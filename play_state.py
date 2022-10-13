import world
import game_framework
from pico2d import*


World = None # c로 따지믄 NULL
running = True

def handle_events():
    global running
    events = get_events()
    for event in events:
        World.handle_events(event.type, event.key)
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            quit()





# 초기화
def enter():
    global World, running
    World = world.World()
    running = True
# finalization code
def exit():
    global World,running
    del World
    running = False
def update():
    World.update()

def draw():
    clear_canvas()
    draw_world()
    update_canvas()


def draw_world():
    World.draw()


def pause():
    pass
def resume():
    pass