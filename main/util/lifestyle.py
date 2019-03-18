from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import json

lifestyle_result=[]

def scrape_l1():
    soup = BeautifulSoup(urlopen('https://www.health.com'), 'html.parser')
    url = 'https://www.health.com'
    for article in soup.find_all('article',class_='partial tile media image-top type-article'):
        for img in article.find_all('a',class_='media-img margin-16-bottom'):
            for a in article.find_all('h3'):
                link = url+article.find('a')['href']
                soup = BeautifulSoup(urlopen(link), 'html.parser')
                for meta in soup.find_all('meta',attrs={'property':'og:description'}):
                    desc = meta['content'] 
                    lifestyle_result.append(json.dumps({
                        'title':a.get_text(strip=True),
                        'link':link,
                        'image':img.find('div').get('data-src'),
                        'desc': desc
                    }))

def scrape_l2():
    soup = BeautifulSoup(urlopen('https://www.womenshealthmag.com'), 'html.parser')
    url='https://www.womenshealthmag.com'
    for div in soup.find_all('div',class_='simple-item grid-simple-item'):
        for img in div.find_all('img'):
            for a in div.find_all('a', class_='simple-item-title item-title'):
                link = url+div.find('a')['href']
                soup = BeautifulSoup(urlopen(link), 'html.parser')
                for meta in soup.find_all('meta',attrs={'property':'og:description'}):
                    desc = meta['content'] 
                    lifestyle_result.append(json.dumps({
                        'title':a.get_text(strip=True),
                        'link':link,
                        'image':img.get('data-src'),
                        'desc': desc
                    }))
    for div in soup.find_all('div',class_='simple-item grid-simple-item grid-simple-item-last-mobile'):
        for img in div.find_all('img'):
            for a in div.find_all('a', class_='simple-item-title item-title'):
                link = url+div.find('a')['href']
                soup = BeautifulSoup(urlopen(link), 'html.parser')
                for meta in soup.find_all('meta',attrs={'property':'og:description'}):
                    desc = meta['content'] 
                    lifestyle_result.append(json.dumps({
                        'title':a.get_text(strip=True),
                        'link':link,
                        'image':img.get('data-src'),
                        'desc': desc
                    }))
    for div in soup.find_all('div',class_='simple-item grid-simple-item grid-simple-item-last-tablet'):
        for img in div.find_all('img'):
            for a in div.find_all('a', class_='simple-item-title item-title'):
                link = url+div.find('a')['href']
                soup = BeautifulSoup(urlopen(link), 'html.parser')
                for meta in soup.find_all('meta',attrs={'property':'og:description'}):
                    desc = meta['content'] 
                    lifestyle_result.append(json.dumps({
                        'title':a.get_text(strip=True),
                        'link':link,
                        'image':img.get('data-src'),
                        'desc': desc
                    }))

# printing out json two times --solved
def scrape_l3():
    soup = BeautifulSoup(urlopen('https://www.cntraveller.com/topic/inspiration'), 'html.parser')
    url = 'https://www.cntraveller.com'
    for li in soup.find_all('li',class_='c-card-section__card-listitem js-c-card-section__card-listitem'):
        for a in li.find_all('h3', class_='c-card__title'):
            link = url+li.find('a')['href']
            soup = BeautifulSoup(urlopen(link), 'html.parser')
            for meta in soup.find_all('meta',attrs={'property':'og:description'}):
                desc = meta['content']
            for meta in soup.find_all('meta',attrs={'property':'og:image'}):
                image = meta['content']
            lifestyle_result.append(json.dumps({
                'title':a.get_text(strip=True),
                'link':link,
                'image':image,
                'desc': desc
            }))

def scrape_l4():
    soup = BeautifulSoup(urlopen('https://www.ricksteves.com/watch-read-listen/read/travel-news'), 'html.parser')
    url = 'https://www.ricksteves.com'
    for div in soup.find_all('div',class_='width40'):
        for img in div.find_all('img'):
            for a in div.find_all('h4'):
                link = url+div.find('a')['href']
                lifestyle_result.append(json.dumps({
                    'title':a.get_text(strip=True),
                    'link':link,
                    'image':img.get('src'),
                    'desc': ''
                }))

def scrape_l5():
    soup = BeautifulSoup(urlopen('https://www.medicalnewstoday.com'), 'html.parser')
    url = 'https://www.medicalnewstoday.com'
    for li in soup.find_all('li',class_='featured'):
        for img in li.find_all('img'):
            for a in li.find_all('a'):
                link = url+li.find('a')['href']
                soup = BeautifulSoup(urlopen(link), 'html.parser')
                for meta in soup.find_all('meta',attrs={'property':'og:description'}):
                    desc = meta['content']
                    lifestyle_result.append(json.dumps({
                        'title':a.get('title'),
                        'link':link,
                        'image':img.get('data-src'),
                        'desc': desc
                    }))
    for li in soup.find_all('li',class_='written'):
        for img in li.find_all('img'):
            for a in li.find_all('a'):
                link = url+li.find('a')['href']
                soup = BeautifulSoup(urlopen(link), 'html.parser')
                for meta in soup.find_all('meta',attrs={'property':'og:description'}):
                    desc = meta['content']
                    lifestyle_result.append(json.dumps({
                        'title':a.get('title'),
                        'link':link,
                        'image':img.get('data-src'),
                        'desc': desc
                    }))

def scrape_l6():
    soup = BeautifulSoup(urlopen('https://www.star2.com/travel'), 'html.parser')
    for div in soup.find_all('div',class_='col-sm-6 clearfix'):
        for img in div.find_all('img'):
            for a in div.find_all('h3'):
                link = div.find('a')['href']
                soup = BeautifulSoup(urlopen(link), 'html.parser')
                for meta in soup.find_all('meta',attrs={'property':'og:description'}):
                    desc = meta['content']
                    lifestyle_result.append(json.dumps({
                        'title':a.get_text(strip=True),
                        'link':link,
                        'image':img.get('src'),
                        'desc': desc
                    }))

def scrape_l7():
    soup = BeautifulSoup(urlopen('https://www.star2.com/food'), 'html.parser')
    for div in soup.find_all('div',class_='col-sm-4'):
        for img in div.find_all('img'):
            for a in div.find_all('h3'):
                link = div.find('a')['href']
                soup = BeautifulSoup(urlopen(link), 'html.parser')
                for meta in soup.find_all('meta',attrs={'property':'og:description'}):
                    desc = meta['content']
                    lifestyle_result.append(json.dumps({
                        'title':a.get_text(strip=True),
                        'link':link,
                        'image':img.get('src'),
                        'desc': desc
                    }))

def scrape_l8():
    soup = BeautifulSoup(urlopen('https://www.justaguything.com'), 'html.parser')
    for article in soup.find_all('article'):
        for img in article.find_all('img'):
            image = img.get('src')
        for a in article.find_all('h2',class_='entry-title'):
            link = article.find('a')['href']
        for div in article.find_all('div',class_='entry-summary'):
            desc = div.find('p').get_text()
        lifestyle_result.append(json.dumps({
            'title':a.get_text(strip=True),
            'link':link,
            'image': image,
            'desc': desc
        }))

def scrape_l9():
    soup = BeautifulSoup(urlopen('https://www.gq-magazine.co.uk/topic/lifestyle'),'html.parser')
    url = 'https://www.gq-magazine.co.uk'
    for li in soup.find_all('li',class_='c-card-section__card-listitem'):
        for article in li.find_all('article',class_='c-card--tg-article'):
            link = url+article.find('a')['href']
            soup = BeautifulSoup(urlopen(link), 'html.parser')
            for meta in soup.find_all('meta',attrs={'property':"og:description"}):
                desc = meta['content'] 
            for meta in soup.find_all('meta',attrs={'property':'og:image'}):
                image = meta['content']
        for div in li.find_all('div',class_='c-card__header'):
            for span in div.find('span'):
                title = span
        lifestyle_result.append(json.dumps({'title':title,'link':link,'image':image,'desc':desc}))

def scrape_l10():
    soup = BeautifulSoup(urlopen('https://www.telegraph.co.uk/travel/news/'), 'html.parser')
    url = 'https://www.telegraph.co.uk'
    for li in soup.find_all('li',class_='list-of-entities__item'):
        for img in li.find_all('img'):
            for a in li.find_all('h3'):
                link = url+li.find('a')['href']
                lifestyle_result.append(json.dumps({
                    'title':a.get_text(strip=True),
                    'link':link,
                    'image':url+img.get('src'),
                    'desc':''
                }))