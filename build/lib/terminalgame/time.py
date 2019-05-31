import time
import terminalgame.event as event
import terminalgame
start_ts = 0
timer_events = []
def init(): # call when pychar-game init
    terminalgame.time.start_ts = int(time.time()*1000)

def get_ticks():
    return int(time.time()*1000)-terminalgame.time.start_ts

def set_timer(eventid, milliseconds):
    e = event.Event(eventid,{'key':None, 'char':None})
    terminalgame.time.timer_events.append((milliseconds, e))

def wait():
    pass

class Clock:
    fps = 1
    def __init__(self):
        self.fps = 1
    def tick(self, framerate=1):
        self.fps = framerate
        time.sleep(1/framerate)
        ct = terminalgame.time.get_ticks()
        del_event = []
        for ent in terminalgame.time.timer_events:
            if ent[0]<=ct:
                event.post(ent[1])
                del_event.append(ent)
        for de in del_event:
            terminalgame.time.timer_events.remove(de)
        
    def get_fps(self):
        return self.fps


