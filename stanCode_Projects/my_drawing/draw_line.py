"""
File: 
Name:
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

# This constant controls the size of the hole
SIZE = 10
window = GWindow()
odd_x = 0
odd_y = 0
count = 0
start = GOval(SIZE, SIZE)


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(click)


def click(m):
    global odd_x
    global odd_y
    global count
    start.filled = True
    start.fill_color = 'white'
    start.color = 'black'
    window.add(start, x=m.x - SIZE / 2, y=m.y - SIZE / 2)
    count += 1
    if count % 2 == 0:
        window.remove(start)
        my_line = GLine(odd_x, odd_y, m.x, m.y)
        my_line.filled = True
        my_line.color = 'black'
        window.add(my_line)
    odd_x = m.x
    odd_y = m.y


if __name__ == "__main__":
    main()
