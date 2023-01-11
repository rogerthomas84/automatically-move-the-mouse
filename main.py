import random
from time import sleep

import autopy


def random_move():
    width, height = autopy.screen.size()
    # We minus 2 to avoid locking hot corners
    w = int(width) - 2
    h = int(height) - 2

    x = random.randint(2, w)
    y = random.randint(2, h)
    autopy.mouse.move(x, y)


if __name__ == '__main__':
    try:
        while True:
            random_move()
            sleep(5)
    except KeyboardInterrupt:
        exit(0)
