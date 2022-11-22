import pyautogui, time

while True:
    img = pyautogui.screenshot()
    img.save("SS.jpg")
    time.sleep(5)
