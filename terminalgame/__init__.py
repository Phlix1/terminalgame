"""Terminalgame is a set of Python modules designed for writing games.
"""

import sys
import os
import terminalgame.display
import terminalgame.draw
import terminalgame.event
import terminalgame.key
import terminalgame.Rect
import terminalgame.sprite
import terminalgame.Surface
import terminalgame.time
import terminalgame.locals
from terminalgame.locals import *

def init():
    terminalgame.display.init()
    terminalgame.time.init()
    terminalgame.event.init()

def quit():
    terminalgame.display.quit()