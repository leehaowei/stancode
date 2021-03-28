"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
The programme used Object Oriented Programming to create the class BreakoutGraphics used to
set up a game in the main programme.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel, GPolygon
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

# CONSTANT
BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 4.0  # Initial vertical speed for the ball.
MAX_X_SPEED = 4      # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):

        # Set up the variables
        self.__ball_r = ball_radius
        self.__pw = paddle_width
        self.__ph = paddle_height
        self.__po = paddle_offset
        self.__br = brick_rows
        self.__bc = brick_cols
        self.__bs = brick_spacing
        self.__bw = brick_width
        self.__bh = brick_height
        self.__bo = brick_offset
        self.pdc = True  # A switch to avoid the ball sticking on the paddle when the paddle touches the ball rapidly.
        self.speed_up = False

        # Create a graphical window, with some extra space.
        self.__window_width = self.__bc * (self.__bw + self.__bs) - self.__bs
        self.__window_height = self.__bo + 3 * (self.__br * (self.__bh + self.__bs) - self.__bs)
        self.window = GWindow(self.__window_width, self.__window_height, title=title)
        self.back_c = GRect(self.__window_width, self.__window_height)
        self.back_c.filled = True
        self.window.add(self.back_c)

        # Create a paddle.
        self.paddle = GRect(self.__pw, self.__ph)
        self.paddle.filled = True
        self.paddle.fill_color = 'white'
        self.paddle.color = 'white'
        self.window.add(self.paddle, (self.__window_width - self.__pw) / 2, self.__window_height - self.__po)

        # Center a filled ball in the graphical window.
        self.ball = GOval(self.__ball_r * 2, self.__ball_r * 2)
        self.ball.filled = True
        self.ball.fill_color = 'white'
        self.ball.color = 'white'
        self.set_ball()

        # Default initial velocity for the ball.
        self.__dx = 0
        self.__dy = INITIAL_Y_SPEED
        self.set_ball_v()

        # Draw bricks.
        self.bx = 0
        self.by = brick_offset
        self.set_bricks()

        # label
        self.life1 = GOval(self.__ball_r, self.__ball_r)  # First life count.
        self.life1.filled = True
        self.life1.fill_color = 'white'
        self.life1.color = 'white'
        self.life2 = GOval(self.__ball_r, self.__ball_r)   # Second life count.
        self.life2.filled = True
        self.life2.fill_color = 'white'
        self.life2.color = 'white'
        self.life3 = GOval(self.__ball_r, self.__ball_r)   # Third life count.
        self.life3.filled = True
        self.life3.fill_color = 'white'
        self.life3.color = 'white'

        self.label1 = GLabel('Life: 3')  # The label of life counts.
        self.label1.filled = True
        self.label1.color = 'white'
        self.label2 = GLabel('score: 0')
        self.label2.filled = True
        self.label2.color = 'white'
        self.label3 = GLabel('GAME OVER') # The label showed when losing all life counts.
        self.label3.filled = True
        self.label3.color = 'white'
        self.label3.font = 'Courier-30'
        self.window.add(self.life1, self.__window_width - self.__pw, self.__window_height - self.__po)
        self.window.add(self.life2, self.__window_width - self.__pw + 2*self.__ball_r, self.__window_height - self.__po)
        self.window.add(self.life3, self.__window_width - self.__pw + 4*self.__ball_r, self.__window_height - self.__po)

        self.window.add(self.label1, self.window.width - 1.5 * self.label2.width,
                        self.window.height - self.label2.height)
        self.window.add(self.label2, 0, self.window.height - self.label1.height)
        # switch
        self.on = False

        # Initialize our mouse listeners.
        onmouseclicked(self.start)
        onmousemoved(self.sense)

        self.break_count = 0

    def start(self, m):
        """
        The function to tell whether the game is start.
        :param m: event
        :return: bool
        """
        if not self.on:
            self.on = True

    # functions of the ball
    def set_ball(self):
        """
        The function is used to set up the ball's initial position.
        """
        self.window.add(self.ball, self.__window_width / 2 - self.__ball_r, self.__window_height / 2 - self.__ball_r)

    def set_ball_v(self):
        """
        To set the position of the ball at each play.
        """
        self.__dx = 15
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx *= -1

    # Getter
    def get_dx(self):
        """
        :return: the horizontal velocity
        """
        return self.__dx

    def get_dy(self):
        """
        :return:  the vertical velocity
        """
        return self.__dy

    def get_br(self):
        """
        :return: the number of brick rows
        """
        return self.__br

    def get_bc(self):
        """
        :return: the number of brick columns
        """
        return self.__bc

    # function of the paddle
    def sense(self, m):
        """
        A function in onmousemoved, used to detect the position of the mouse and move the paddle accordingly.
        :param m: the mouse
        """
        px = m.x - self.paddle.width / 2
        py = self.__window_height - self.__po
        if m.x >= self.paddle.width / 2:
            if m.x + self.paddle.width / 2 <= self.window.width:
                self.window.add(self.paddle, px, py)

    def set_bricks(self):
        """
        A function to set up the bricks with different colors.
        """
        count = 1
        for i in range(self.__br):
            for j in range(self.__bc):
                if count <= 2:
                    b = self.red_b()
                elif count <= 4:
                    b = self.orange_b()
                elif count <= 6:
                    b = self.yellow_b()
                elif count <= 8:
                    b = self.green_b()
                else:
                    b = self.blue_b()
                self.window.add(b, self.bx, self.by)
                self.bx = self.bx + self.__bw + self.__bs
            count += 1
            self.bx = 0
            self.by = self.by + self.__bh + self.__bs

    # functions for the animation
    def to_break(self):
        """
        1. A function for the ball to detect if it touch a thing. The ball will bounce if touches either the paddle or
        a brick, and breaks the break when touching. While touching the paddle will turn the variable pdc to False
        to avoid multiple bouncing, avoiding the ball looks like sticking to the paddle.
        2. c1, c2, c3, and c4 are the four corners of the square circumscribed outside the ball.
        3. The 4 points will ignore the lable and GOval object used to count the life and score.
        :return: bool, when True, activating the animation of breaking the bricks.
        """
        c1 = self.window.get_object_at(self.ball.x, self.ball.y)
        c2 = self.window.get_object_at(self.ball.x + 2 * self.__ball_r, self.ball.y)
        c3 = self.window.get_object_at(self.ball.x, self.ball.y + 2 * self.__ball_r)
        c4 = self.window.get_object_at(self.ball.x + 2 * self.__ball_r, self.ball.y + 2 * self.__ball_r)
        if c1 is not None and c1 is not self.label1 and c1 is not self.label2 and c1 is not self.back_c and \
                c1 is not self.life1 and c1 is not self.life2 and c1 is not self.life3:
            if c1 is self.paddle:
                if self.pdc:
                    self.pdc = False
                    return True
                else:
                    return False
            else:
                self.window.remove(c1)
                self.break_count += 1
                self.speed_up = True
                self.pdc = True
                self.label2.text = 'Score: ' + str(self.break_count)
                return True
        elif c2 is not None and c2 is not self.label1 and c2 is not self.label2 and c2 is not self.back_c and \
                c2 is not self.life1 and c2 is not self.life2 and c2 is not self.life3:
            if c2 is self.paddle:
                if self.pdc:
                    self.pdc = False
                    return True
                else:
                    return False
            else:
                self.window.remove(c2)
                self.break_count += 1
                self.speed_up = True
                self.pdc = True
                self.label2.text = 'Score: ' + str(self.break_count)
                return True
        elif c3 is not None and c3 is not self.label1 and c3 is not self.label2 and c3 is not self.back_c and \
                c3 is not self.life1 and c3 is not self.life2 and c3 is not self.life3:
            if c3 is self.paddle:
                if self.pdc:
                    self.pdc = False
                    return True
                else:
                    return False
            else:
                self.window.remove(c3)
                self.break_count += 1
                self.speed_up = True
                self.pdc = True
                self.label2.text = 'Score: ' + str(self.break_count)
            return True
        elif c4 is not None and c4 is not self.label1 and c4 is not self.label2 and c4 is not self.back_c and \
                c4 is not self.life1 and c4 is not self.life2 and c4 is not self.life3:
            if c4 is self.paddle:
                if self.pdc:
                    self.pdc = False
                    return True
                else:
                    return False
            else:
                self.window.remove(c4)
                self.break_count += 1
                self.speed_up = True
                self.pdc = True
                self.label2.text = 'Score: ' + str(self.break_count)
            return True

    # To set the color of bricks
    def red_b(self):
        b = GRect(self.__bw, self.__bh)
        b.filled = True
        b.fill_color = 'darkgreen'
        b.color = 'darkgreen'
        return b

    def orange_b(self):
        b = GRect(self.__bw, self.__bh)
        b.filled = True
        b.fill_color = 'forestgreen'
        b.color = 'forestgreen'
        return b

    def yellow_b(self):
        b = GRect(self.__bw, self.__bh)
        b.filled = True
        b.fill_color = 'seagreen'
        b.color = 'seagreen'
        return b

    def green_b(self):
        b = GRect(self.__bw, self.__bh)
        b.filled = True
        b.fill_color = 'palegreen'
        b.color = 'palegreen'
        return b

    def blue_b(self):
        b = GRect(self.__bw, self.__bh)
        b.filled = True
        b.fill_color = 'lawngreen'
        b.color = 'lawngreen'
        return b

