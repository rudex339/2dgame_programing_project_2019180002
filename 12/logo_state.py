from pico2d import *
import game_framework
import play_state

running = False
image = None
logo_time = 0.0

def enter():
    global image
    image = load_image('sprites/Select Screen.png')
    pass

def exit():
    global image
    del image
    # fill here
    pass

def update():
    global logo_time
    global running
    if logo_time > 0.5:
        logo_time = 0
        game_framework.change_state(play_state)
    delay(0.01)
    if running:
        logo_time += 0.01
    # fill here
    pass

def draw():
    clear_canvas()
    image.clip_draw(3, 472 - 108 - 224, 304, 224,450, 300,
                        900, 600)
    update_canvas()
    # fill here
    pass

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN:
            running = True
