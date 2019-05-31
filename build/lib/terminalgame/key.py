from pynput import keyboard
import terminalgame.event as event
from terminalgame.locals import *
import terminalgame
import time
def Key2KeyASCII(key):
    keytable = {
        keyboard.Key.alt : K_ALT,
        keyboard.Key.alt_l : K_LALT,
        keyboard.Key.alt_r : K_RALT,
        keyboard.Key.backspace : K_BACKSPACE,
        keyboard.Key.caps_lock : K_CAPSLOCK,
        keyboard.Key.cmd : K_CMD,
        keyboard.Key.cmd_r : K_RCMD,
        keyboard.Key.ctrl : K_CTRL,
        keyboard.Key.ctrl_l : K_LCTRL,
        keyboard.Key.ctrl_r : K_RCTRL,
        keyboard.Key.delete : K_DELETE,
        keyboard.Key.down : K_DOWN,
        keyboard.Key.end : K_END,
        keyboard.Key.enter : K_ENTER,
        keyboard.Key.esc : K_ESC,
        keyboard.Key.f1 : K_F1,
        keyboard.Key.f2 : K_F2,
        keyboard.Key.f3 : K_F3,
        keyboard.Key.f4 : K_F4,
        keyboard.Key.f5 : K_F5,
        keyboard.Key.f6 : K_F6,
        keyboard.Key.f7 : K_F7,
        keyboard.Key.f8 : K_F8,
        keyboard.Key.f9 : K_F9,
        keyboard.Key.f10 : K_F10,
        keyboard.Key.f11 : K_F11,
        keyboard.Key.f12 : K_F12,
        #keyboard.Key.f13 : K_F13,
        #keyboard.Key.f14 : K_F14,
        #keyboard.Key.f15 : K_F15,
        #keyboard.Key.f16 : K_F16,
        #keyboard.Key.f17 : K_F17,
        #keyboard.Key.f18 : K_F18,
        #keyboard.Key.f19 : K_F19,
        #keyboard.Key.f20 : K_F20,
        keyboard.Key.home : K_HOME,
        keyboard.Key.left : K_LEFT,
        keyboard.Key.page_down : K_PAGEDOWM,
        keyboard.Key.page_up : K_PAGEUP,
        keyboard.Key.right : K_RIGHT,
        keyboard.Key.shift : K_SHIFT,
        keyboard.Key.shift_r : K_RSHIFT,
        keyboard.Key.space : K_SPACE,
        keyboard.Key.tab : K_TAB,
        keyboard.Key.up : K_UP,
        keyboard.Key.insert : K_INSERT,
        keyboard.Key.menu : K_MENU,
        keyboard.Key.num_lock : K_NUMLOCK,
        keyboard.Key.pause : K_PAUSE,
        keyboard.Key.print_screen : K_PRINTSCREEN,
        keyboard.Key.scroll_lock : K_SCROLLLOCK,
        'a' : K_a,
        'b' : K_b,
        'c' : K_c,
        'd' : K_d,
        'e' : K_e,
        'f' : K_f,
        'g' : K_g,
        'h' : K_h,
        'i' : K_i,
        'j' : K_j,
        'k' : K_k,
        'l' : K_l,
        'm' : K_m,
        'n' : K_n,
        'o' : K_o,
        'p' : K_p,
        'q' : K_q,
        'r' : K_r,
        's' : K_s,
        't' : K_t,
        'u' : K_u,
        'v' : K_v,
        'w' : K_w,
        'x' : K_x,
        'y' : K_y,
        'z' : K_z,
        '0' : K_0,
        '1' : K_1,
        '2' : K_2,
        '3' : K_3,
        '4' : K_4,
        '5' : K_5,
        '6' : K_6,
        '7' : K_7,
        '8' : K_8,
        '9' : K_9,
        '/' : K_SLASH,       		
        '.' : K_PERIOD,      
        '-' : K_MINUS,     
        ',' : K_COMMA,    
        ';' : K_SEMICOLON,   
        '`' : K_BACKQUOTE,  
        '\\' : K_BACKSLASH,   
        '[' : K_LEFTBRACKET, 
        ']' : K_RIGHTBRACKET,
        "'" : K_QUOTEDBL  
    }
    try:
        return keytable[key.char], key.char
    except AttributeError:
        return keytable[key], None

def on_press(mykey):
    type = KEYDOWN
    dict={} #unicode, key
    dict['key'], dict['char']= Key2KeyASCII(mykey)
    event.post(event.Event(type,dict))
def on_release(mykey):
    type = KEYUP
    dict={} #key
    dict['key'], dict['char'] = Key2KeyASCII(mykey)
    event.post(event.Event(type,dict))
listener = keyboard.Listener(on_press = on_press,on_release = on_release, suppress=True)

def key_monitor_start():
    terminalgame.key.listener.start()

def key_monitor_stop():
    terminalgame.key.listener.stop()

def name(key):
    pass

def get_pressed():
    pass


