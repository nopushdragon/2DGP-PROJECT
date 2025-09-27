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