import terminalgame.locals

def post(e):
    terminalgame.locals.eventlist.append(e)

def init():
    terminalgame.locals.eventlist.clear()

def get():
    Eventlist = []
    while terminalgame.locals.eventlist!=[]:
        Eventlist.append(terminalgame.locals.eventlist.pop(0))
    return Eventlist
   
def poll():
    return terminalgame.locals.eventlist.pop(0)

class Event:
    def __init__(self, type, dict):
        self.type = type
        self.dict = dict

class EventType:
    QUIT = terminalgame.locals.QUIT
    KEYDOWN = terminalgame.locals.KEYDOWN
    KEYUP = terminalgame.locals.KEYUP
    USEREVENT = terminalgame.locals.USEREVENT