from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import json

beauty_result=[]

def scrape_b1():
    soup = BeautifulSoup(urlopen('https://www.elle.com/beauty'),'html.parser')
    url = 'https://www.elle.com'
    for div in soup.find_all('div',class_='full-item'):
        for img in div.find_all('img',class_='lazyimage'):
            for a in div.find_all('a',class_='full-item-title'):
                beauty_result.append(json.dumps({
                    'title':a.get_text(),
                    'link':url+div.find('a')['href'],
                    'image':img.get('data-src')
                }))

def scrape_b2():
    soup = BeautifulSoup(urlopen('https://www.instyle.com/beauty'), 'html.parser')
    url = 'https://www.instyle.com'
    for article in soup.find_all('article',class_='component tile media image-top type-article'):
        for img in article.find_all('div',class_='component lazy-image thumbnail'):
            h3 = article.find('h3')
            a_link = h3.find('a')
            beauty_result.append(json.dumps({
                'title': a_link.get_text(strip=True),
                'link': url + a_link.get('href'),
                'image': img.get('data-src')
                }))

def scrape_b3():
    soup = BeautifulSoup(urlopen('https://intothegloss.com/sections/skincare/'), 'html.parser')
    url = 'https://intothegloss.com'
    for div in soup.find_all('div', class_='l-row--full m-posts-item m-posts-item--'):
        for img in div.find_all('div', class_='m-img-lazy'):
            for a in div.find_all('h2'):
                article_link = a.find('a')['href']
                beauty_result.append(json.dumps({
                    'title':a.get_text(strip=True),
                    'link':url+article_link,
                    'image':img.find('img').get('data-src')
                }))

def scrape_b4():
    soup = BeautifulSoup(urlopen('https://fashionmagazine.com/beauty'),'html.parser')
    for article in soup.find_all('article',class_='post-preview--portrait'):
        for div in article.find_all('div',class_='post-preview--portrait__header-wrap'):
            for a in div.find_all('a'):
                link = a.get('href')
                image = a.find('img')['src']
        for div in article.find_all('div',class_='post-preview--portrait__content-wrap'):
            for h2 in div.find_all('h2',class_='post-preview-title--portrait'):
                title = h2.get_text().strip()
        beauty_result.append(json.dumps({'title':title,'link':link,'image':image}))

    for article in soup.find_all('article',class_='post-preview--landscape'):
        for div in article.find_all('div',class_='post-preview--landscape__header-wrap'):
            for a in div.find_all('a'):
                link = a.get('href')
                image = a.find('img')['src']
        for div in article.find_all('div',class_='post-preview--landscape__content-wrap'):
            for h2 in div.find_all('h2',class_='post-preview-title--landscape'):
                title = h2.get_text().strip()
        beauty_result.append(json.dumps({'title':title,'link':link,'image':image}))

def scrape_b5():
    soup = BeautifulSoup(urlopen('https://www.gq-magazine.co.uk/topic/grooming'),'html.parser')
    url = 'https://www.gq-magazine.co.uk'
    for li in soup.find_all('li',class_='c-card-section__card-listitem'):
        for article in li.find_all('article',class_='c-card--tg-article'):
            link = url+article.find('a')['href']
        for div in li.find_all('div',class_='c-card__image--square'):
            for img in div.find_all('img'):
                if img.get('data-src'):
                    image = img.get('data-src')
        for div in li.find_all('div',class_='c-card__header'):
            for span in div.find('span'):
                title = span
        beauty_result.append(json.dumps({'title':title,'link':link,'image':image}))

def scrape_b6():
    soup = BeautifulSoup(urlopen('https://www.vogue.co.uk/topic/beauty'),'html.parser')
    url = 'https://www.vogue.co.uk'
    for li in soup.find_all('li',class_='c-card-section__card-listitem'):
        for article in li.find_all('article',class_='c-card--tg-article'):
            link = url+article.find('a')['href']
        for div in li.find_all('div',class_='c-card__image--square'):
            for img in div.find_all('img'):
                if img.get('data-src'):
                    image = img.get('data-src')
        for div in li.find_all('div',class_='c-card__header'):
            for span in div.find('span'):
                title = span
        beauty_result.append(json.dumps({'title':title,'link':link,'image':image}))

def scrape_b7():
    soup = BeautifulSoup(urlopen('https://www.glamourmagazine.co.uk/topic/beauty-news'),'html.parser')
    url = 'https://www.glamourmagazine.co.uk'
    for li in soup.find_all('li',class_='c-card-section__card-listitem'):
        for article in li.find_all('article',class_='c-card--tg-article'):
            link = url+article.find('a')['href']
        for div in li.find_all('div',class_='c-card__image--square'):
            for img in div.find_all('img'):
                if img.get('data-src'):
                    image = img.get('data-src')
        for div in li.find_all('div',class_='c-card__header'):
            for span in div.find('span'):
                title = span
        beauty_result.append(json.dumps({'title':title,'link':link,'image':image}))

# need to fix image
def scrape_b8():
    soup = BeautifulSoup(urlopen('https://www.self.com/beauty'),'html.parser')
    url = 'https://www.self.com/'
    for li in soup.find_all('li',class_='component-river-item'):
        # for img in li.find_all('picture',class_='component-responsive-image'):
            for a in li.find_all('a',class_='component-link river-item-content-item river-item-content-hed'):
                beauty_result.append(json.dumps({
                    'title':a.get_text(),
                    'link':url+li.find('a')['href'],
                    # 'image':img.get('data-src')
                }))

def scrape_b9():
    soup = BeautifulSoup(urlopen('https://www.harpersbazaar.com/uk/beauty/'),'html.parser')
    url = 'https://www.harpersbazaar.com/uk/'
    for div in soup.find_all('div',class_='full-item'):
        for img in div.find_all('img',class_='lazyimage'):
            for a in div.find_all('a',class_='full-item-title'):
                beauty_result.append(json.dumps({
                    'title':a.get_text(),
                    'link':url+div.find('a')['href'],
                    'image':img.get('data-src')
                }))

def scrape_b10():
    soup = BeautifulSoup(urlopen('https://www.cosmopolitan.com/uk/beauty-hair'),'html.parser')
    url = 'https://www.cosmopolitan.com/uk'
    for div in soup.find_all('div',class_='full-item'):
        for img in div.find_all('img',class_='lazyimage'):
            for a in div.find_all('a',class_='full-item-title'):
                beauty_result.append(json.dumps({
                    'title':a.get_text(),
                    'link':url+div.find('a')['href'],
                    'image':img.get('data-src')
                }))


