import keyboard
from pyscreenshot import grab
import pyautogui
import PIL

# wait for press key
while True:
    try:
        if keyboard.read_key() == "ц":
            print(123)
            im = grab(childprocess=False)
            r, g, b = im.getpixel((953, 4))
            if r == 255 and g == 255 and b == 255:
                print(14234512351435234523452345234523453245)
                pyautogui.click(x=1730, y=930)
            pass
        if keyboard.read_key() == "p":
            break
    except:
        print(0)
        continue
