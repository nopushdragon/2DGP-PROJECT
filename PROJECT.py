from pico2d import *

open_canvas(1200,800)

running = True
prev_time = get_time()

while running:
    curr_time = get_time()
    dt = curr_time - prev_time
    prev_time = curr_time

    clear_canvas()

    update_canvas()

close_canvas()