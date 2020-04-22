import pyautogui
import pyperclip
import keyboard
keyboard.add_hotkey('f2', lambda: pyautogui.write(pyperclip.paste()))
