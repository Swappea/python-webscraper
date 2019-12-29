from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import pandas as pd

options = webdriver.ChromeOptions()
# Path to your chrome profile
options.add_argument(
    "user-data-dir=C:\\Users\\Swapnesh\\AppData\\Local\\Google\\Chrome\\User Data")
driver = webdriver.Chrome(
    executable_path="D:/Study/Python/WebScraping TraversyMedia/chromedriver_win32/chromedriver.exe", chrome_options=options)

url = "https://footballia.net/matches/atletico-de-madrid-fc-barcelona-liga-1-division-2008-2009"
# url = "https://footballia.net/matches/fc-barcelona-olympique-lyonnais-champions-league"

driver.get(url)
driver.implicitly_wait(30)
play_btn = driver.find_element_by_id('jwplayer_display_button_play')
play_btn.click()


element = driver.find_element_by_class_name('jwvideo')
print('found element')
match_src = element.get_attribute('innerHTML')
print(match_src)
print((match_src.split('src', 1)[1]).split('"')[1])

alert_element = driver.find_element_by_xpath(
    '/html/body/div/div/div/div/div[2]/div[2]/div/div[1]/span')
alert_element_text = alert_element.get_attribute('innerHTML')
print(alert_element_text)

if not 'New' in alert_element_text:
    print('alert element exists')
    driver.implicitly_wait(30)

    next_btn = driver.find_element_by_xpath(
        '//*[@id="jwplayer_controlbar"]/span[3]/span[3]')
    print(next_btn.get_attribute('innerHTML'))
    next_btn.click()
    new_element = driver.find_element_by_class_name('jwvideo')
    match_src_1 = element.get_attribute('innerHTML')
    print((match_src_1.split('src', 1)[1]).split('"')[1])


# match_src = element.get_attribute('src')

# driver.close()
