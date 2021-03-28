"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao

YOUR DESCRIPTION HERE：
1. The programme sets up a game with 3 life-count with the life-count showed at the bottom right and
score at the bottom left.
2. The speed of the ball increases every time the ball breaks a brick.
"""

from campy.gui.events.timer import pause
from breakoutgraphics_ext import BreakoutGraphics

# CONSTANT
FRAME_RATE = 1000 / 120  # 120 frames per second.
NUM_LIVES = 3


def main():
    global NUM_LIVES
    graphics = BreakoutGraphics()
    dx, dy = graphics.get_dx(), graphics.get_dy()
    graphics.label1.text = 'Life: ' + str(NUM_LIVES)
    while True:
        br = graphics.get_br()
        bc = graphics.get_bc()
        pause(FRAME_RATE)
        graphics.label1.text = 'Life: ' + str(NUM_LIVES)
        if NUM_LIVES < 3:
            graphics.window.remove(graphics.life1)  # Remove first life count
        if NUM_LIVES < 2:
            graphics.window.remove(graphics.life2)  # Remove second life count
        if NUM_LIVES == 0:
            graphics.window.remove(graphics.life3)  # Remove the last life count
            break
        elif graphics.break_count == (br*bc):
            graphics.window.remove(graphics.ball)
            graphics.label3.text = 'YOU WIN'    # Changes the label when winning the game.
            break
        elif graphics.on:
            graphics.ball.move(dx, dy)
            if graphics.ball.y + graphics.ball.height > graphics.window.height:
                NUM_LIVES -= 1
                dx, dy = graphics.get_dx(), graphics.get_dy()
                graphics.on = False
                graphics.pdc = True
                graphics.set_ball()
            else:
                graphics.speed_up = False  # Set the speed up switch to False when using a new losing a life count.
                if graphics.to_break():
                    dy = -dy
                    if graphics.speed_up:  # Speed up the vertical velocity of the ball.
                        dy *= 1.05
                if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width > graphics.window.width:
                    dx = -dx
                    graphics.pdc = True
                if graphics.ball.y <= 0:
                    dy = -dy
                    graphics.pdc = True
    graphics.window.remove(graphics.ball)
    graphics.window.add(graphics.label3, graphics.window.width / 2 + 10, graphics.window.height / 2)


if __name__ == '__main__':
    main()
