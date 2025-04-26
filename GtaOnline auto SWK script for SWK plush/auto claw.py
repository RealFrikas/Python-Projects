import keyboard
import time
import threading

# Global flag to stop the script
running = True

def listen_for_escape():
    global running
    keyboard.wait('esc')  # waits until ESC is pressed
    print("ESC pressed. Exiting...")
    running = False

# Start listener thread
listener = threading.Thread(target=listen_for_escape)
listener.start()

print("Script started. Press ESC to stop.")

while running:
    # Press E
    keyboard.press_and_release('e')
    print("Pressed E")
    time.sleep(3)

    # Hold W
    keyboard.press('w')
    print("Holding W")
    time.sleep(4)
    keyboard.release('w')

    # Hold D
    keyboard.press('d')
    print("Holding D")
    time.sleep(4)
    keyboard.release('d')

    # Press Enter
    keyboard.press_and_release('enter')
    print("Pressed Enter")
    time.sleep(14)

print("Script exited.")