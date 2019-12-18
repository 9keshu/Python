import pyautogui, time
time.sleep(5) # to wait until the program is  launched 
pyautogui.click() # click to put drawing program in focus
distance = 200
while distance > 0:
    pyautogui.dragRel(distance, 0, duration = 0.5) # move right
    distance = distance - 5
    pyautogui.dragRel(0,distance, duration = 0.5) #move down
    pyautogui.dragRel(-distance, 0, duration = 0.5) #move left
    distance = distance - 5
    pyautogui.dragRel(0, -distance, duration = 0.5) #move up
