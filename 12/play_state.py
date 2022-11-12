from pico2d import *
import game_framework
import game_world
import map

import map
from charcter import Charcter


charcter = None
grass = None

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        else:
            charcter.handle_event(event)


# 초기화
def enter():
    global charcter, grass
    charcter = Charcter()
    map.enter()
    game_world.add_object(charcter,1)
    #game_world.add_object( Map(1), 2)
# 종료
def exit():
    game_world.clear()

def update():
    for game_object in game_world.all_object():
        game_object.update()

def draw_world():
    for game_object in game_world.all_object():
        game_object.draw()

def draw():
    clear_canvas()
    draw_world()
    update_canvas()

def pause():
    pass

def resume():
    pass




def test_self():
    import play_state

    pico2d.open_canvas()
    game_framework.run(play_state)
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()
