from pico2d import *
import game_world
import server
import game_framework

ex_bgm1 = None

def enter():
    global  ex_bgm1
    if ex_bgm1 == None:
        ex_bgm1 =load_wav("sound/effect/gen_10.wav")