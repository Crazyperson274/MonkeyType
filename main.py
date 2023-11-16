import random
import time
import pyautogui
import keyboard
from selenium import webdriver
from bs4 import BeautifulSoup
import html5lib
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

noBot = False
repeat = False
browser = webdriver.Chrome()
#
def wordsToChars(wpm):
    if wpm <201:
        cpm = 1/((wpm*5)/60)
    elif wpm >200:
        cpm = 1/((wpm*5.4)/60)
    return cpm


URL = "https://monkeytype.com/account"
browser.get(URL)
time.sleep(1)

elem = browser.find_element(By.CLASS_NAME, "rejectAll")
elem.click()

time.sleep(.5)

elem = browser.find_element(By.NAME, "current-email")
elem.clear()
elem.send_keys("tylertalkstoomuch275@gmail.com")

elem = browser.find_element(By.NAME, "current-password")
elem.clear()
elem.send_keys("2mvpF@N1@Nwrx&fk")
elem.send_keys(Keys.RETURN)

time.sleep(3)
elem = browser.find_element(By.ID, "startTestButton")
elem.click()

while repeat:
    pass
time.sleep(2)
page_source = browser.page_source

soup = BeautifulSoup(page_source, 'html.parser')
spans = soup.find_all('div', class_='word')
words = ' '.join([span.get_text() for span in spans])
for c in words:
    if noBot:
        if c == 'u' or c == 't':
            time.sleep(wordsToChars(53))
        elif c == 'm' or c == 'a':
            time.sleep(wordsToChars(26))
        elif c == 'n':
            time.sleep(wordsToChars(65))
        else:
            time.sleep(wordsToChars(40))
    else:
        time.sleep(wordsToChars(700))
    pyautogui.press(c, _pause=False)

# pyautogui.typewrite(words)
time.sleep(3)

# elem = browser.find_element(By.ID, 'nextTestButton')
# elem.click()

time.sleep(900)
