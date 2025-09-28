from object import *
from pico2d import *
import gamemanager

def MapDraw(dt):
    pass

def ObjectDraw(dt):
    clear_canvas()
    gamemanager.hometown.draw()
    gamemanager.gunman.draw(dt)
    for b in gamemanager.bullet:
        b.draw()
    update_canvas()