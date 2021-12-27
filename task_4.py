import keyboard
from pyscreenshot import grab
import pyautogui
import PIL
from random import randint
from time import sleep


while True:
    try:
        if keyboard.read_key() == 'w':
            im = grab(childprocess=False)
            r, g, b = im.getpixel((953, 4))
            print(123)
            if r == 255 and g == 255 and b == 255:
                rnd = randint(0, 10) * 0.01
                print(rnd)
                sleep(rnd)
                print(14234512351435234523452345234523453245)
                pyautogui.click(x=1730, y=930)
            pass
        if keyboard.read_key() == "p":
            break
    except:
        print(0)
        continue
