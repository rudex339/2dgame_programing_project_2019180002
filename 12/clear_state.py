from pico2d import *
import game_framework
import logo_state

running = True
Font = None
Font2 = None
logo_time = 0.0

def enter():
    global Font
    Font = load_font('ENCR10B.TTF',20)
    pass

def exit():
    global Font
    del Font
    # fill here
    pass

def update():
    pass

def draw():
    Font.draw(450,300,'congraturation',(255,255,255))
    Font.draw(450,  200, 'press any key', (0, 0, 0))
    update_canvas()
    # fill here
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN:
            game_framework.change_state(logo_state)