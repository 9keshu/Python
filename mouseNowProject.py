#! /usr/bin/python3
# mouseNowProject.py - Display the mouse cursor's current position.
import pyautogui
print('Press Ctrl-C to quit.')
#TODO: Get and print the coordinates.
try:
    while True:
        #TODO : Get and print the mouse coordinates.
        x,y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + 'Y: ' + str(y).rjust(4) + ' .'
        print(positionStr,end='')
        print('\b' * len(positionStr), end='', flush=True)


except KeyboardInterrupt:
    print('\nDone.')
