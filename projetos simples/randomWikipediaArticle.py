import bs4
import requests
from openpyxl import Workbook

wb = Workbook()

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64;     x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "DNT":"1","Connection":"close",
    "Upgrade-Insecure-Requests":"1"
    }
url ='https://en.wikipedia.org/wiki/Special:Random'

while True:
    response = requests.get(url, headers=headers) #get url
    soup = bs4.BeautifulSoup(response.content, "lxml") #get page content

    wikiName = soup.find('h1', attrs={'class':'firstHeading'}).text.strip() #get page title
    print('-'*50)
    print('Title: ', wikiName)
    print('Link: ', response.url)
    userChoice = input('\nKeep randomizing wikipedias\'s pages? (Y/N)').lower()
    if userChoice in 'n':
        break
    else:
        userChoice = ''


