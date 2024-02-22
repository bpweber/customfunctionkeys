import keyboard
import pyautogui

pyautogui.PAUSE = 0.0

DOWN = 1
UP = 0

key_maps = {
    'pause': 'playpause',
    'page up': 'volumeup',
    'page down': 'volumedown'
    }

fn_keys = [
    'caps lock'
    ]

def fn(keypos):
    if keypos is DOWN:
        map_all_keys()
    else:
        keyboard.unhook_all()
        map_fn_keys()

def map_all_keys():
    for key, val in key_maps.items():
        map_key(key, DOWN, pyautogui.keyDown, val)
        map_key(key, UP, pyautogui.keyUp, val)

def map_fn_keys():
    for key in fn_keys:
        map_key(key, DOWN, fn, DOWN)
        map_key(key, UP, fn, UP)

def map_key(key, keypos, func, arg):
    if keypos is DOWN:
        keyboard.on_press_key(key, lambda e: func(arg), suppress=True)
    else:
        keyboard.on_release_key(key, lambda e: func(arg), suppress=True)

map_fn_keys()

keyboard.wait()
