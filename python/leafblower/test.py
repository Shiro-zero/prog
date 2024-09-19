import keyboard
import pyautogui
import time

pyautogui.FAILSAFE = True


def bot():
    pyautogui.moveTo(255, 220)
    print("start")
    while not (keyboard.is_pressed('q')):

        target = pyautogui.locateCenterOnScreen('borb.png')
        while target is None:
            # print("target:none")
            target = pyautogui.locateCenterOnScreen('borb.png')

        print(target)

        if pyautogui.pixelMatchesColor(target.x, 300, (151, 113, 74)):
            print("good")
    print("end")


def main():
    bot()
    print("Hello World!")


if __name__ == "__main__":
    main()
