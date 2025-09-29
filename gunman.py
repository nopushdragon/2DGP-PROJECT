from pico2d import load_image
from character_base import *
from projectile import Projectile

gunman = Character([
    [load_image(f'source\\character\\hope01_0{i}.png') for i in range(1, 3)],
    [load_image(f'source\\character\\hope01_0{i}.png') for i in range(3, 5)],
    [load_image(f'source\\character\\hope01_0{i}.png') for i in range(5, 8)]
], 600, 400, [])

def shoot_override(self):
    self.projectile.append(
        Projectile(
            [load_image(f'source\\projectile\\40241_s2_0{i}.png') for i in range(1, 5)],
            self.x + 100 - (200 * int(self.flip)), self.y - 30, 122, 66,
            500, 0, 0.0, 0.1, self.flip, True
        )
    )

gunman.Shoot = shoot_override.__get__(gunman, Character)