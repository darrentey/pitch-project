from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import json

food_result=[]

def scrape_fb1():
    soup = BeautifulSoup(urlopen('https://www.star2.com/food'), 'html.parser')
    for div in soup.find_all('div',class_='col-sm-4'):
        for img in div.find_all('img'):
            for a in div.find_all('h3'):
                food_result.append(json.dumps({
                    'title':a.get_text(strip=True),
                    'link':div.find('a')['href'],
                    'image':img.get('src'),
                }))
    print(food_result)

def scrape_fb2():
    soup = BeautifulSoup(urlopen('https://www.thestar.com.my/metro/eat-and-drink'), 'html.parser')
    url = 'https://www.thestar.com.my'
    for div in soup.find_all('div', class_='row list-listing'):
        for img in div.find_all('img'):
            for p in div.find_all('p'):
                food_result.append(json.dumps({
                    'title':div.find('h2').get_text(),
                    'link':url+div.find('a')['href'],
                    'image':url+img.get('src'),
                    'desc':p.get_text(strip=True),
                }))
    print(food_result)

# multiple printed items
def scrape_fb3():
    soup = BeautifulSoup(urlopen('https://www.mariefranceasia.com/my/food-my'), 'html.parser')
    check=[]
    for div in soup.find_all('div', class_='col-xs-12 col-sm-6 col-md-6 item-post'):
        for img in div.find_all('img'):
            for a in div.find_all('a'):
                link = a['href']
                if link not in check:
                    food_result.append(json.dumps({
                        'title':div.find('div', class_='info_title').get_text(strip=True),
                        'link':link,
                        'image':img.get('data-src'),
                        'desc':a.get_text(strip=True),
                    }))
                else:
                    return
    print(food_result)

# repeated 2 times
def scrape_fb4():
    soup = BeautifulSoup(urlopen('https://www.freemalaysiatoday.com/category/leisure/food'), 'html.parser')
    for div in soup.find_all('div', class_='td-block-span6'):
        for img in div.find_all('img'):
            for a in div.find_all('a'):
                food_result.append(json.dumps({
                    'title':a['title'],
                    'link':a['href'],
                    'image':img.get('src'),
                    'desc':div.find('div', class_='td-excerpt').get_text(strip=True),
                }))
    print(food_result)