import gamemanager

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
            waitTime = 0.5
            idx = 0
        elif self.state == "walk":
            waitTime = 0.2
            idx = 1
        elif self.state == "attack":
            waitTime = 0.2
            idx = 2
        else:
            waitTime = 0.5
            idx = 0

        if not (self.state == "attack" and self.frame == len(self.anime[2]) - 1):
            if self.frameTimer >= waitTime:
                self.frameTimer = 0.0
                self.frame = (self.frame + 1) % len(self.anime[idx])

        return idx  # 상태에 맞는 인덱스 반환

    def draw(self,dt):
        if self.flip:
            self.anime[self.Update(dt)][self.frame].clip_composite_draw(0, 0, 100, 100,0, 'h', self.x, self.y, 200, 200)
        else:
            self.anime[self.Update(dt)][self.frame].clip_draw(0, 0, 100, 100, self.x, self.y, 200, 200)

class Projectile:
    def __init__(self, anime, x, y, width, height, speed,frame, frameTimer, waitTime, flip = False, visible = False):
        self.anime = anime
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.frame = frame
        self.frameTimer = frameTimer
        self.waitTime = waitTime
        self.flip = flip
        self.visible = visible

    def update(self, dt):
        if self.visible:
            self.frameTimer += dt

            if self.flip == False:
                self.x += self.speed * dt
                if self.x > gamemanager.WIDTH:
                    self.visible = False
            elif self.flip == True:
                self.x -= self.speed * dt
                if self.x < 0:
                    self.visible = False

            if self.frameTimer >= self.waitTime:
                self.frameTimer = 0.0
                '''if self.frame < len(self.anime) - 1:
                    self.frame += 1'''
                self.frame = (self.frame + 1) % len(self.anime)

    def draw(self):
        if self.visible:
            if self.flip == False:
                self.anime[self.frame].clip_draw(0, 0, self.width, self.height, self.x, self.y, 100, 30)
            elif self.flip == True:
                self.anime[self.frame].clip_composite_draw(0, 0, self.width, self.height, 0, 'h', self.x, self.y, 100, 30)

class BackGround:
    def __init__(self, image, x, y,width, height):
        self.image = image
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self):
        self.image.clip_draw(0, 0, self.width, self.height, self.x, self.y)
        self.image.clip_draw(0, 0, self.width, self.height, self.x - self.width, self.y)
        self.image.clip_draw(0, 0, self.width, self.height, self.x + self.width, self.y)

    def move(self, mx):
        self.x += mx
        if self.x > gamemanager.WIDTH:
            self.x += -self.width
        elif self.x < 0:
            self.x += self.width