from object import *
from pico2d import *
import gamemanager

open_canvas(1200, 800)

def MapDraw(dt):
    pass

def ObjectDraw(dt):
    clear_canvas()
    if gamemanager.gunman.flip == True:
        gamemanager.gunman.anime[gamemanager.gunman.Update(dt)][gamemanager.gunman.frame].clip_composite_draw(0, 0, 100, 100,0, 'h', gamemanager.gunman.x, gamemanager.gunman.y, 200, 200)
    else:
        gamemanager.gunman.anime[gamemanager.gunman.Update(dt)][gamemanager.gunman.frame].clip_draw(0, 0, 100, 100, gamemanager.gunman.x, gamemanager.gunman.y, 200, 200)
    update_canvas()