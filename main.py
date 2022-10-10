import character
from pico2d import*

open_canvas()
Player = character.Charcter()
program_on = True
def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            program_on = False
        else:
            Player.key_update(event.type, event.key)



while (program_on):
    clear_canvas()
    Player.animation()
    Player.update()
    update_canvas()
    handle_events()
    delay(0.1)

