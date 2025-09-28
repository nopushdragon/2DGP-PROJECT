from gamemanager import WIDTH

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
        if self.x > WIDTH:
            self.x -= self.width
        elif self.x < 0:
            self.x += self.width