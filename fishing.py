import pyautogui
import time
# from functions import *
import autopy


# minimize_visual_studio_code()

time.sleep(1.5)
# pyautogui.moveTo(x=1302, y=514)
# time.sleep(0.2)

for i in range(95):
    
    pyautogui.write('e')
    time.sleep(4)
    while True:
        screen_cap = autopy.bitmap.capture_screen(((956,430), (9,50)))
        find_fish = screen_cap.find_color(autopy.color.rgb_to_hex(252,212,141),0.03)
        # print(find_fish)  
        if find_fish:
            pyautogui.write('e')
            # print("Found fish: %s" % str(pos))
            break

    time.sleep(6.1)
            
# for i in range(100):
#     screen = autopy.bitmap.capture_screen(((927,449), (53,97)))
#     pos = screen.find_color((r, g, b),0.03, )
#     print(pos)

