import pico2d
import play_state
import game_framework

start_state = play_state # 모듈을 변수로 저장

pico2d.open_canvas(900,600)
game_framework.run(play_state)

pico2d.close_canvas()