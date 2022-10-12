import map
from pico2d import*

open_canvas(900,600)
world = map.World()
program_on = True
def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            program_on = False
        else:
            world.key_update(event.type, event.key)



while (program_on):
    clear_canvas()
    world.draw()
    world.update()
    update_canvas()
    handle_events()
    delay(0.1)

