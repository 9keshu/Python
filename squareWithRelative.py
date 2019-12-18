import pyautogui
for i in range(1,10):
    pyautogui.moveRel(100,0,duration=1)
    pyautogui.moveRel(0,100,duration=1)
    pyautogui.moveRel(-100,0,duration=1)
    pyautogui.moveRel(0,-100,duration=1)
