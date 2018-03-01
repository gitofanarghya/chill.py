import pyautogui

while True:
	pyautogui.moveRel(100, 0, duration=0.25)
	pyautogui.moveRel(0, 100, duration=0.25)
	pyautogui.moveRel(-100, 0, duration=0.25)
	pyautogui.moveRel(0, -100, duration=0.25)
	pyautogui.click()
