WIDTH = 1200
HEIGHT = 800

from pico2d import *
open_canvas(WIDTH, HEIGHT)
from background import *
from projectile import *
from paint import *
from character import characters
import time

gunman = characters[0]
gunman.status = {"hp": 100, "atk": 50, "speed": 100}  # hp, attack, speed

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
    gunman.Update(dt)
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

def main():
    while True:
        start = time.time()
        dt = DeltaTime()

        GameUpdate(dt)

        MapDraw(dt)
        ObjectDraw(dt)
        print(gunman.status)
        elapsed = time.time() - start
        time.sleep(max(0, 1 / 60 - elapsed))  # 60프레임 고정
    close_canvas()