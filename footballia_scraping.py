# beautiful soup
import requests
from bs4 import BeautifulSoup
from csv import writer

# Selenium code
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd

base_url = 'https://footballia.net'

video_list = []

pageNumber = 20
url = f'{base_url}/teams/fc-barcelona?page={pageNumber}'
print('URL')
print(url)

response = requests.get(url)

print('Starting scraping footballia')

soup = BeautifulSoup(response.text, 'html.parser')
table_rows = soup.find(class_='table').tbody.select('tr')

options = webdriver.ChromeOptions()
# Path to your chrome profile
options.add_argument(
    "user-data-dir=C:\\Users\\Swapnesh\\AppData\\Local\\Google\\Chrome\\User Data")
driver = webdriver.Chrome(
    executable_path="D:/Study/Python/WebScraping TraversyMedia/chromedriver_win32/chromedriver.exe", chrome_options=options)


def checkIfSecondUrl():
    try:
        alert_element = driver.find_element_by_xpath(
            '/html/body/div/div/div/div/div[2]/div[2]/div/div[1]/span')
        alert_element_text = alert_element.get_attribute('innerHTML')
        print(alert_element_text)
        modified_url = ''
        if not 'New' in alert_element_text:
            print('alert element exists')
            driver.implicitly_wait(30)

            next_btn = driver.find_element_by_xpath(
                '//*[@id="jwplayer_controlbar"]/span[3]/span[3]')
            print(next_btn.get_attribute('innerHTML'))
            next_btn.click()
            new_element = driver.find_element_by_class_name('jwvideo')
            match_src = new_element.get_attribute('innerHTML')
            modified_url = (match_src.split('src', 1)[1]).split('"')[1]
            if modified_url.startswith('/'):
                modified_url = base_url + modified_url
            print(modified_url)
            return modified_url
    except:
        return ''


def openMatchUrl(matchurl):
    driver.get(matchurl)
    play_btn = driver.find_element_by_id('jwplayer_display_button_play')
    play_btn.click()
    element = driver.find_element_by_class_name('jwvideo')
    print('found element')
    match_src = element.get_attribute('innerHTML')
    modified_url = (match_src.split('src', 1)[1]).split('"')[1]
    if modified_url.startswith('/'):
        modified_url = base_url + modified_url
    print(modified_url)
    video_list.append(modified_url)
    secondUrl = checkIfSecondUrl()
    if secondUrl is None:
        secondUrl = ''
    else:
        video_list.append(secondUrl)    
    return modified_url + '\t' + secondUrl


with open(f'data/matches_{pageNumber}.csv', 'w') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['index', 'Playing Date', 'Link',
               'Competition', 'Season', 'Stage', 'Match Url']
    csv_writer.writerow(headers)

    for index, item in enumerate(table_rows):
        ind = index + 1
        playing_date = item.find(class_="playing_date").getText()
        competition = item.find(class_="competition").getText()
        season = item.find(class_="season").getText()
        stage = item.find(class_="stage").getText()
        match_el = item.find(class_="match")
        link = base_url + match_el.find('a')['href']
        match_url = openMatchUrl(link)
        csv_writer.writerow(
            [ind, playing_date, link, competition, season, stage, match_url])


driver.close()


print('Scraping done')
print('Video List')
print(video_list)

with open(f'data/matches_link_{pageNumber}.txt', 'w') as f:
    for item in video_list:
        f.write("%s\n" % item)