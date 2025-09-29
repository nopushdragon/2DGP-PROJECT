WIDTH = 1200
HEIGHT = 800

from pico2d import *
open_canvas(WIDTH, HEIGHT)
from background import *
from projectile import *
from paint import *
from character import characters

gunman = characters[0]

hometown = BackGround(load_image('source\\background\\bg_tile_chapter_01_01.png'),WIDTH/2,HEIGHT/2,960,800)

prev_time = get_time()
def DeltaTime():
    global prev_time
    curr_time = get_time()
    dt = curr_time - prev_time
    prev_time = curr_time
    return dt

def GameUpdate(dt):
    InputKey()
    WaitForShoot(dt)
    for b in gunman.projectile[::-1]:
        b.update(dt)
        if not b.visible:
            gunman.projectile.remove(b)

    if gunman.flip == False and gunman.state == "walk":
        hometown.move(-200*dt)
    elif gunman.flip == True and gunman.state == "walk":
        hometown.move(200*dt)


def InputKey():
    events = get_events()
    if not gunman.state == "attack":
        for event in events:
            if event.type == SDL_KEYDOWN:
                if event.key == SDLK_LEFT or event.key == ord("a") or event.key == ord("A"):
                    gunman.state = "walk"
                    gunman.flip = True
                elif event.key == SDLK_RIGHT or event.key == ord("d") or event.key == ord("D"):
                    gunman.state = "walk"
                    gunman.flip = False
                elif event.key == SDLK_SPACE:
                    gunman.frameTimer = 0.0
                    gunman.frame = 0
                    gunman.state = "attack"
                elif event.key == SDLK_ESCAPE:
                    quit()
            elif event.type == SDL_KEYUP:
                if event.key == SDLK_LEFT and gunman.flip == True or event.key == SDLK_RIGHT and gunman.flip == False:
                    gunman.state = "idle"

shootMotionEnd = False
shootMotionEndTimer = 0.0
def WaitForShoot(dt):
    global shootMotionEnd, shootMotionEndTimer

    if gunman.state == "attack" and gunman.frame == len(gunman.anime[2]) - 1:
        shootMotionEnd = True

    if shootMotionEnd:
        shootMotionEndTimer += dt
        if shootMotionEndTimer >= 0.1:
            shootMotionEndTimer = 0.0
            gunman.frame = 0
            gunman.state = "idle"
            shootMotionEnd = False
            gunman.Shoot()

def main():
    while (True):
        dt = DeltaTime()
        GameUpdate(dt)

        MapDraw(dt)
        ObjectDraw(dt)

    close_canvas()