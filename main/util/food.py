from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import json

food_result=[]

# missing desc
def scrape_fb1():
    soup = BeautifulSoup(urlopen('https://www.star2.com/food'), 'html.parser')
    for div in soup.find_all('div',class_='col-sm-4'):
        for img in div.find_all('img'):
            for a in div.find_all('h3'):
                link = div.find('a')['href']
                # soup = BeautifulSoup(urlopen(link), 'html.parser')
                # for meta in soup.find_all('meta', attrs={'name':'description'}):
                #     desc = meta['content'],
                food_result.append(json.dumps({
                    'title':a.get_text(strip=True),
                    'link':link,
                    'image':img.get('src'),
                }))

def scrape_fb2():
    soup = BeautifulSoup(urlopen('https://www.thestar.com.my/metro/eat-and-drink'), 'html.parser')
    url = 'https://www.thestar.com.my'
    for div in soup.find_all('div', class_='row list-listing'):
        for p in div.find_all('p'):
            link = url+div.find('a')['href']
            soup = BeautifulSoup(urlopen(link), 'html.parser')
            for meta in soup.find_all('meta', attrs={'property':'og:image'}):
                img = meta['content']
                food_result.append(json.dumps({
                        'title':div.find('h2').get_text(),
                        'link':link,
                        'image':img,
                        'desc':p.get_text(strip=True),
                    }))

# delete [1]
def scrape_fb3():
    soup = BeautifulSoup(urlopen('https://www.mariefranceasia.com/my/food-my'), 'html.parser')
    check=[]
    for div in soup.find_all('div', class_='col-xs-12 col-sm-6 col-md-6 item-post'):
        for img in div.find_all('img'):
            for a in div.find_all('a'):
                link = a['href']
                title = div.find('div', class_='info_title').get_text(strip=True)
                if link not in check:
                    check.append(link)
                    food_result.append(json.dumps({
                        'title':title,
                        'link':link,
                        'image':img.get('data-src'),
                        'desc':a.get_text(strip=True)
                    }))

def scrape_fb4():
    soup = BeautifulSoup(urlopen('https://www.freemalaysiatoday.com/category/leisure/food'), 'html.parser')
    check=[]
    for div in soup.find_all('div', class_='td-block-span6'):
        for img in div.find_all('img'):
            for a in div.find_all('a'):
                link = a['href']
                if link not in check:
                    check.append(link)
                    food_result.append(json.dumps({
                        'title':a['title'],
                        'link':link,
                        'image':img.get('src'),
                        'desc':div.find('div', class_='td-excerpt').get_text(strip=True)
                    }))
    print(food_result)