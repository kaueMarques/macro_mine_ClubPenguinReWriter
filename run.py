import pyautogui
import random
import time


# started
while(True):

    mine_place_x = random.randrange(365, 405)
    mine_place_y = random.randrange(518, 631)
    random_timer = random.randrange(3, 5)


    #mining
    pyautogui.click(556, 276)
    pyautogui.click(mine_place_x, mine_place_y)
    pyautogui.click(mine_place_x, mine_place_y)
    time.sleep(random_timer)
    pyautogui.press("d")
    pyautogui.press("d")
    time.sleep(random.randrange(5, 14))

    for i in range(0, 5):
        pyautogui.press("t")
        time.sleep(1)
        pyautogui.click(741, 183)

    pyautogui.press("d")
