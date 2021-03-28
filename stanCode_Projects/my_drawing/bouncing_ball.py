"""
File: 
Name:
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE)
quota = 3       # A variable to check how many times left a user can activate the animation.
disturb = True  # A variable to determine if a mouse click can affect the ball.


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    set_up_ball()
    onmouseclicked(fall)


def fall(m):
    global quota
    global ball
    global disturb
    if disturb:
        disturb = False  # When the ball is moving, disturb will switch to False and a click cannot affect the ball.
        if quota > 0:
            quota -= 1
            vy = 0
            while True:
                if ball.x > window.width:
                    window.add(ball, START_X, START_Y)
                    break
                vy += GRAVITY
                ball.move(VX, vy)
                if ball.y + ball.height >= window.height:
                    vy *= -REDUCE
                    if vy > 0:        # To make sure vy will always be forced up evey time a ball hits the ground.
                        vy *= -1
                pause(DELAY)
        disturb = True


def set_up_ball():
    ball.filled = True
    window.add(ball, START_X, START_Y)


if __name__ == "__main__":
    main()
