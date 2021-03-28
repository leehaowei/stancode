"""
File: 
Name:
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect, GPolygon, GArc, GLine, GLabel
from campy.graphics.gwindow import GWindow

w = GWindow(640, 760, title='eiffel tower')


def main():
    """
    TODO:
    """
    sky()
    clouds()
    grass()
    tree()
    tower_base()
    neck()
    middle()
    top()
    head()
    bike()


def tree():
    b1 = GRect(4, 32, x=40, y=688)
    b1.filled = True
    b1.fill_color = 'chocolate'
    w.add(b1)

    t1 = GRect(32, 37.6, x=26.4, y=656)
    t1.filled = True
    t1.fill_color = 'seagreen'
    w.add(t1)


def sky():
    s = GRect(640, 760)
    s.filled = True
    s.fill_color = 'skyblue'
    s.color = 'skyblue'
    w.add(s)


def grass():
    g = GRect(640, 80)
    g.filled = True
    g.fill_color = 'seagreen'
    g.color = 'seagreen'
    w.add(g, 0, 720)


def tower_base():
    base = GPolygon()
    base.add_vertex((224, 600))
    base.add_vertex((424, 600))
    base.add_vertex((480, 720))
    base.add_vertex((160, 720))
    base.filled = True
    base.fill_color = 'silver'
    w.add(base)

    arc1 = GArc(200, 360, 0, 180)
    arc1.filled = True
    arc1.fill_color = 'skyblue'
    arc1.color = 'skyblue'
    w.add(arc1, 224, 630.4)

    arc2 = GArc(200, 360, 0, 180)
    w.add(arc2, 224, 630.4)

    base2 = GPolygon()
    base2.add_vertex((224, 584))
    base2.add_vertex((424, 584))
    base2.add_vertex((424, 600))
    base2.add_vertex((224, 600))
    base2.filled = True
    base2.fill_color = 'silver'
    w.add(base2)

    base3 = GPolygon()
    base3.add_vertex((224, 568))
    base3.add_vertex((424, 568))
    base3.add_vertex((424, 584))
    base3.add_vertex((224, 584))
    base3.filled = True
    base3.fill_color = 'silver'
    w.add(base3)


def middle():
    md = GPolygon()
    md.add_vertex((264, 464))
    md.add_vertex((384, 464))
    md.add_vertex((408, 568))
    md.add_vertex((240, 568))
    md.filled = True
    md.fill_color = 'silver'
    w.add(md)

    md2 = GPolygon()
    md2.add_vertex((300, 488))
    md2.add_vertex((348, 488))
    md2.add_vertex((356, 568))
    md2.add_vertex((292, 568))
    md2.filled = True
    md2.fill_color = 'skyblue'
    w.add(md2)

    md3 = GPolygon()
    md3.add_vertex((260, 452))
    md3.add_vertex((388, 452))
    md3.add_vertex((388, 464))
    md3.add_vertex((260, 464))
    md3.filled = True
    md3.fill_color = 'silver'
    w.add(md3)


def neck():
    nk = GPolygon()
    nk.add_vertex((304, 112))
    nk.add_vertex((344, 112))
    nk.add_vertex((372, 452))
    nk.add_vertex((276, 452))
    nk.filled = True
    nk.fill_color = 'silver'
    w.add(nk)

    nk = GPolygon()
    nk.add_vertex((324, 280))
    nk.add_vertex((340, 452))
    nk.add_vertex((308, 452))
    nk.filled = True
    nk.fill_color = 'silver'
    nk.color = 'grey'
    w.add(nk)

    sln = GLine(324, 112, 324, 280)
    sln.color = 'grey'
    w.add(sln)


def head():
    hd1 = GPolygon()
    hd1.add_vertex((300, 96))
    hd1.add_vertex((348, 96))
    hd1.add_vertex((348, 112))
    hd1.add_vertex((300, 112))
    hd1.filled = True
    hd1.fill_color = 'silver'
    w.add(hd1)

    tp1 = GOval(11, 32, x=318, y=36)
    tp1.filled = True
    tp1.fill_color = 'silver'
    w.add(tp1)

    hd2 = GOval(32, 32, x=308, y=64)
    hd2.filled = True
    hd2.fill_color = 'silver'
    w.add(hd2)

    hd3 = GPolygon()
    hd3.add_vertex((308, 80))
    hd3.add_vertex((340, 80))
    hd3.add_vertex((340, 96))
    hd3.add_vertex((308, 96))
    hd3.filled = True
    hd3.fill_color = 'silver'
    w.add(hd3)

    tp2 = GPolygon()
    tp2.add_vertex((312, 56))
    tp2.add_vertex((336, 56))
    tp2.add_vertex((336, 64))
    tp2.add_vertex((312, 64))
    tp2.filled = True
    tp2.fill_color = 'silver'
    w.add(tp2)


def top():
    t = GPolygon()
    t.add_vertex((322.4, 8))
    t.add_vertex((326.4, 8))
    t.add_vertex((326.4, 40))
    t.add_vertex((322.4, 40))
    t.filled = True
    t.fill_color = 'silver'
    w.add(t)


def clouds():
    c1 = GOval(88, 24)
    c1.filled = True
    c1.fill_color = 'snow'
    c1.color = 'snow'

    c2 = GOval(40, 40)
    c2.filled = True
    c2.fill_color = 'snow'
    c2.color = 'snow'

    c3 = GOval(88, 24)
    c3.filled = True
    c3.fill_color = 'snow'
    c3.color = 'snow'

    c4 = GOval(40, 40)
    c4.filled = True
    c4.fill_color = 'snow'
    c4.color = 'snow'

    c5 = GOval(88, 24)
    c5.filled = True
    c5.fill_color = 'snow'
    c5.color = 'snow'

    c6 = GOval(40, 40)
    c6.filled = True
    c6.fill_color = 'snow'
    c6.color = 'snow'

    w.add(c1, 80, 80)
    w.add(c2, 96, 64)
    w.add(c3, 80, 400)
    w.add(c4, 96, 384)
    w.add(c5, 520, 240)
    w.add(c6, 536, 224)


def bike():
    ov1 = GOval(48, 48)
    w.add(ov1, 480, 672)

    ov2 = GOval(48, 48)
    w.add(ov2, 560, 672)

    ln1 = GLine(515, 674, 560, 695)
    w.add(ln1)

    ln2 = GLine(504, 692, 528, 656)
    w.add(ln2)

    ln3 = GLine(504, 656, 528, 656)
    w.add(ln3)

    ln4 = GLine(521.6, 664, 568, 664)
    w.add(ln4)

    ln5 = GLine(568, 664, 583, 692)
    w.add(ln5)

    ln6 = GLine(568, 664, 568, 652)
    w.add(ln6)

    ln7 = GLine(560, 652, 576, 652)
    w.add(ln7)

    ln8 = GLine(560, 695, 580, 695)
    w.add(ln8)

    hd = GArc(8, 8, 72, 144)
    w.add(hd, 502.4, 656)

    ov3 = GOval(8,8)
    w.add(ov3, 500, 692)

    ov4 = GOval(8, 8)
    w.add(ov4, 580, 692)


if __name__ == '__main__':
    main()
