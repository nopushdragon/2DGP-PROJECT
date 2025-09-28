
class Character:
    def __init__(self, anime, x, y, projectile , frame=0, frameTimer = 0.0, state = "idle",flip = False):   #anime[0] = idle, anime[1] = walk, anime[2] = attack
        self.anime = anime
        self.x = x
        self.y = y
        self.frame = frame
        self.frameTimer = frameTimer
        self.state = state
        self.flip = flip
        self.projectile = projectile

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