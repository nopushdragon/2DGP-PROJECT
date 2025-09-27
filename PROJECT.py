from pico2d import *

open_canvas(1200, 800)

class Character:
    def __init__(self, anime, x, y, frame=0,frameTimer = 0.0, state = "idle",flip = False):   #anime[0] = idle, anime[1] = walk, anime[2] = attack
        self.anime = anime
        self.x = x
        self.y = y
        self.frame = frame
        self.frameTimer = frameTimer
        self.state = state
        self.flip = flip

    def Update(self, dt):
        self.frameTimer += dt
        if self.state == "idle":
            frame_time = 0.5
            idx = 0
        elif self.state == "walk":
            frame_time = 0.2
            idx = 1
        elif self.state == "attack":
            frame_time = 0.2
            idx = 2
        else:
            frame_time = 0.5
            idx = 0

        if not (self.state == "attack" and self.frame == len(self.anime[2]) - 1):
            if self.frameTimer >= frame_time:
                self.frameTimer = 0.0
                self.frame = (self.frame + 1) % len(self.anime[idx])

        return idx  # 상태에 맞는 인덱스 반환

gunman = Character([[load_image('hope01_01.png'), load_image('hope01_02.png')],
                    [load_image('hope01_03.png'),load_image('hope01_04.png')],
                    [load_image('hope01_05.png'),load_image('hope01_06.png'),load_image('hope01_07.png')]],
                   600, 400)

prev_time = get_time()
def DeltaTime():
    global prev_time
    curr_time = get_time()
    dt = curr_time - prev_time
    prev_time = curr_time
    return dt

def GameUpdate():
    events = get_events()
    if gunman.state == "attack":
        return
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
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT and gunman.flip == True or event.key == SDLK_RIGHT and gunman.flip == False:
                gunman.state = "idle"


attack_end = False
attack_end_timer = 0.0
def Draw():
    global attack_end, attack_end_timer
    dt = DeltaTime()  # 프레임 간 시간 계산

    if gunman.state == "attack" and gunman.frame == len(gunman.anime[2]) - 1:
        attack_end = True

    clear_canvas()
    if gunman.flip == True:
        gunman.anime[gunman.Update(dt)][gunman.frame].clip_composite_draw(0, 0, 100, 100,0, 'h', gunman.x, gunman.y, 200, 200)
    else:
        gunman.anime[gunman.Update(dt)][gunman.frame].clip_draw(0, 0, 100, 100, gunman.x, gunman.y, 200, 200)
    update_canvas()

    if attack_end:
        attack_end_timer += dt
        if attack_end_timer >= 0.5:
            attack_end_timer = 0.0
            gunman.frame = 0
            gunman.state = "idle"
            attack_end = False

running = True
while running:
    GameUpdate()

    Draw()

close_canvas()