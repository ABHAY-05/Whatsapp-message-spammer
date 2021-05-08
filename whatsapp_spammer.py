import pyautogui, time
import webbrowser

Name_spam=input(f'Enter The name of person you want to Spam:')

time.sleep(5)


webbrowser.open("https://web.whatsapp.com/")
time.sleep(10)

position = pyautogui.locateOnScreen("search.png")
pyautogui.moveTo(position)
pyautogui.click()
time.sleep(5)

pyautogui.typewrite(Name_spam)
time.sleep(3)

pyautogui.press("enter")
time.sleep(5)
mes=open("spam.txt","r")

for word in mes: 
    pyautogui.typewrite(word)
    time.sleep(0)
    pyautogui.press("enter")
    time.sleep(0)