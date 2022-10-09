import character
from pico2d import*

open_canvas()
Player = character.Charcter()

def handle_events():
    global running
    global dir_x
    global dir_y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            Player.downput(event.key)
        elif event.type == SDL_KEYUP:
            Player.upput(event.key)



while (1):
    clear_canvas()
    Player.update()
    Player.animation()
    update_canvas()
    handle_events()
    delay(0.1)

