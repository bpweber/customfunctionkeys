import keyboard

key_maps = {
    'pause': 'play/pause',
    'page up': 'volume up',
    'page down': 'volume down'
    }

fn_keys = ['caps lock']

def map_all_keys():
    for k, v in key_maps.items():
        keyboard.remap_key(k, v)

def map_fn_keys():
    for key in fn_keys:
        keyboard.on_press_key(key, lambda e: fn(True), suppress=True)
        keyboard.on_release_key(key, lambda e: fn(False), suppress=True)

def fn(pressed):
    if pressed:
        map_all_keys()
    else:
        keyboard.unhook_all()
        map_fn_keys()

map_fn_keys()

keyboard.wait()