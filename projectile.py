from gamemanager import WIDTH

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
                if self.x > WIDTH:
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
