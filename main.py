import random
from time import sleep

import autopy


def random_move():
    width, height = autopy.screen.size()
    w = int(width)
    h = int(height)

    x = random.randint(0, w)
    y = random.randint(0, h)
    autopy.mouse.move(x, y)


if __name__ == '__main__':
    try:
        while True:
            random_move()
            sleep(5)
    except KeyboardInterrupt:
        exit(0)
