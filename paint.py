import gamemanager

def MapDraw(dt):
    pass

def ObjectDraw(dt):
    gamemanager.clear_canvas()
    gamemanager.hometown.draw()
    gamemanager.gunman.draw(dt)
    for b in gamemanager.gunman.projectile:
        b.draw()
    gamemanager.update_canvas()