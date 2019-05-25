import time
import terminalgame
from terminalgame.Rect import Rect
import curses
from terminalgame.Surface import Surface
import terminalgame.draw as draw
from terminalgame.locals import *

def init():
    terminalgame.display.rootwin = curses.initscr()
    curses.cbreak()
    curses.curs_set(False)
    curses.noecho()
def quit():
    terminalgame.key.key_monitor_stop()
    curses.nocbreak()
    terminalgame.display.win.keypad(0)
    curses.echo()
    curses.endwin()
def set_mode(height, width, y=0, x=0, border=True):
    #try:
    #    terminalgame.display.win = curses.newwin(height, width, y, x)
    #except curses.error:
    #    height, width = rootwin.getmaxyx()
    #    terminalgame.display.win = curses.newwin(height, width, 0, 0)
    maxheight, maxwidth = rootwin.getmaxyx()
    if height>maxheight:
        height = maxheight
    if width>maxwidth:
        width = maxwidth
    terminalgame.display.win = curses.newwin(height, width, 0, 0)
    terminalgame.display.win.keypad(1)
    terminalgame.display.win.timeout(timeout)
    terminalgame.key.key_monitor_start()
    terminalgame.display.win.refresh()
    terminalgame.display.border = border
    if border:
        terminalgame.display.height = height-2
        terminalgame.display.width = width-2
        terminalgame.display.win.border(0)
        terminalgame.display.screen = Surface(height-2, width-2)
    else:
        terminalgame.display.height = height
        terminalgame.display.width = width
        terminalgame.display.screen = Surface(height, width)
    return terminalgame.display.screen
def flip():
    if border:
        for i in range(height):
            for j in range(width):
                if screen.image[i][j]!='':
                    win.addch(i+1,j+1,screen.image[i][j])
                else:
                    win.addch(i+1,j+1,' ')
    else:
        try:
            for i in range(height):
                for j in range(width):
                    if screen.image[i][j]!='':
                        win.addch(i,j,screen.image[i][j])
                    else:
                        win.addch(i+1,j+1,' ')
        except curses.error:
            pass
    win.refresh()
def update():
    pass

def get_surface():
    return screen

'''
#test
w = display()
w.init()
screen = w.set_mode(80,80,border=True)
#s1 = Surface(10,10)
#s1.fill()
#dest = Rect(0,0,0,0)
#re = screen.blit(s1, dest, area=Rect(0,0,5,10))
#print(re.left, re.top, re.width, re.height)
draw.rect(screen, Rect(30,30,100,100),width=0)
rect=draw.circle(screen, (30,30),15,width=1)
rect = draw.line(screen, (-10,-10),(100,100))
print(rect.left, rect.top, rect.height, rect.width)
start = time.clock()
i=0
while i<1000:
    w.flip()
    i += 1

end = time.clock()
fps = 1000/(end-start)

print(fps)
'''