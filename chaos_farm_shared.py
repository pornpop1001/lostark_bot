import pyautogui
import time

def lclick():
    time.sleep(0.1)
    pyautogui.click(button='left')
    time.sleep(0.2)
def rclick():
    time.sleep(0.2)
    pyautogui.click(button='right')
    time.sleep(0.2)
def double_lclick():
    time.sleep(0.2)
    pyautogui.doubleClick(button='left')
    time.sleep(0.2)
def double_rclick():
    time.sleep(0.2)
    pyautogui.doubleClick(button='right')
    time.sleep(0.2)
def b():
    pyautogui.write('b')
    time.sleep(0.2)
def g():
    pyautogui.write('g')
    time.sleep(0.5)
def i():
    pyautogui.write('i')
    time.sleep(0.2)
def alt_e():
    pyautogui.keyDown('alt')
    time.sleep(0.1)
    pyautogui.write('e')
    time.sleep(0.2)
    pyautogui.keyUp('alt')
def chaos_entrace_fast():
    ################################### chaos_entrance
    g()
    time.sleep(0.2)
    pyautogui.moveTo(x=1540, y=858) 
    lclick()
    time.sleep(0.2)
    pyautogui.moveTo(x=906, y=605) 
    lclick()
    time.sleep(6)   
def chaos_combo_fast():
    ##################################### chaos_combo
    pyautogui.moveTo(x=960, y=530)
    rclick() 
    time.sleep(0.3)
    pyautogui.write('q')
    time.sleep(0.13)
    pyautogui.write('q')
    
    time.sleep(0.8) 
    pyautogui.write('a')
    time.sleep(1.6)
    pyautogui.write('w')
    time.sleep(0.15)
    pyautogui.write('w')
    time.sleep(2.35)
    pyautogui.write('f')
    time.sleep(1.6)
    pyautogui.write('s')
    time.sleep(3)
    time.sleep(0.8)
    pyautogui.write('r')
    time.sleep(0.15)
    pyautogui.write('r')
    time.sleep(3.6)
    pyautogui.write('d')
    time.sleep(1)
    pyautogui.write('a')
    time.sleep(1.6)
    pyautogui.write('w')
    time.sleep(0.12)
    pyautogui.write('w')
    time.sleep(2.3)
    pyautogui.write('e')
    time.sleep(3.8)

    pyautogui.write('s')
    time.sleep(3)
    time.sleep(0.8)
    pyautogui.write('a')
    time.sleep(1.7)
    pyautogui.write('f') 
    time.sleep(1.7)
    pyautogui.write('w')
    time.sleep(0.12)
    pyautogui.write('w')
    time.sleep(2.4)
    pyautogui.write('d')
    time.sleep(1.2)
    pyautogui.write('r')
    time.sleep(0.15)
    pyautogui.write('r')
    time.sleep(3.55)
    pyautogui.write('s')
    time.sleep(2.8)
    pyautogui.write('e')
    time.sleep(0.4)
    pyautogui.write('a')
    time.sleep(1.3)
def chaos_exit():
    #################################### chaos_exit
    time.sleep(0.2)
    pyautogui.moveTo(x=131, y=281) 
    lclick()
    pyautogui.moveTo(x=903, y=590) 
    lclick()
    # time.sleep(15)
    time.sleep(10.1) # Standard
def repair_weapon():    
    # moveto_npc
    pyautogui.moveTo(x=1480, y=551)
    # pyautogui.moveTo(x=1725, y=489) 
    rclick()
    time.sleep(2)
    g()
    time.sleep(0.3)
    # repair
    pyautogui.moveTo(x=1090, y=677) 
    lclick()
    time.sleep(0.6)
    pyautogui.moveTo(x=1825, y=1028) 
    lclick()
    time.sleep(0.6)

    # # move back to chaos
    pyautogui.moveTo(x=7, y=364)
    # pyautogui.moveTo(x=137, y=553)
    rclick()
    time.sleep(2)



for i in range(3):
    for i in range(440):
        chaos_entrace_fast()
        chaos_combo_fast()
        chaos_exit()

