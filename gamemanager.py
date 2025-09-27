from pico2d import *
from object import *
from paint import *

attack_end = False
attack_end_timer = 0.0
gunman = Character([[load_image('hope01_01.png'), load_image('hope01_02.png')],
                        [load_image('hope01_03.png'), load_image('hope01_04.png')],
                        [load_image('hope01_05.png'), load_image('hope01_06.png'), load_image('hope01_07.png')]],
                       600, 400)


def GameUpdate(dt):
    global attack_end, attack_end_timer

    events = get_events()
    if not gunman.state == "attack":
        for event in events:
            if event.type == SDL_KEYDOWN:
                if event.key == SDLK_LEFT:
                    gunman.state = "walk"
                    gunman.flip = True
                elif event.key == SDLK_RIGHT:
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

    if gunman.state == "attack" and gunman.frame == len(gunman.anime[2]) - 1:
        attack_end = True

    if attack_end:
        attack_end_timer += dt
        if attack_end_timer >= 0.5:
            attack_end_timer = 0.0
            gunman.frame = 0
            gunman.state = "idle"
            attack_end = False

prev_time = get_time()
def DeltaTime():
    global prev_time
    curr_time = get_time()
    dt = curr_time - prev_time
    prev_time = curr_time
    return dt

def main():
    while (True):
        dt = DeltaTime()
        GameUpdate(dt)

        MapDraw(dt)
        ObjectDraw(dt)

    close_canvas()