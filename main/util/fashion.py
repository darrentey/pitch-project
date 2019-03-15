from urllib.request import urlopen,Request
from bs4 import BeautifulSoup
import bs4
import requests
import json

fashion_result=[]

def scrape_f1():
    soup = BeautifulSoup(urlopen('https://www.elle.com/fashion'),'html.parser')
    url = 'https://www.elle.com'
    for div in soup.find_all('div',class_='full-item'):
        for img in div.find_all('img',class_='lazyimage'):
            image = img.get('data-src')
        for div2 in div.find_all('div',class_='full-item-dek'):
            desc = div2.find('p').get_text()
            for a in div.find_all('a',class_='full-item-title'):
                title = a.get_text()
                link = url+div.find('a')['href']
                fashion_result.append(json.dumps({'title':title,'link':link,'image':image,'desc':desc}))

def scrape_f2():
    soup = BeautifulSoup(urlopen('https://www.whowhatwear.com/channel/trends'),'html.parser')
    url = 'https://www.whowhatwear.com'
    for div in soup.find_all('div',class_='card__item'):
        link = url+div.find('a')['href']
        image = div.find('img',class_='card__thumbnail')['src']
        title = (div.find('div',class_='card__title').text).strip()
        desc = (div.find('div',class_='card__description').text).strip()
        fashion_result.append(json.dumps({'title':title,'link':link,'image':image,'desc':desc}))

def scrape_f3():
    soup = BeautifulSoup(urlopen('https://fashionmagazine.com/category/fashion'),'html.parser')
    for article in soup.find_all('article',class_='post-preview--landscape'):
        for div in article.find_all('div',class_='post-preview--landscape__header-wrap'):
            for a in div.find_all('a'):
                link = a.get('href')
                image = a.find('img')['src']
                soup = BeautifulSoup(urlopen(link), 'html.parser')
                for meta in soup.find_all('meta',attrs={'name':'description'}):
                    desc = meta['content'] 
        for div in article.find_all('div',class_='post-preview--landscape__content-wrap'):
            for h2 in div.find_all('h2',class_='post-preview-title--landscape'):
                title = h2.get_text().strip()
        fashion_result.append(json.dumps({'title':title,'link':link,'image':image,'desc':desc}))

def scrape_f4():
    soup = BeautifulSoup(urlopen('https://www.gq-magazine.co.uk/topic/fashion'),'html.parser')
    url = 'https://www.gq-magazine.co.uk'
    for li in soup.find_all('li',class_='c-card-section__card-listitem'):
        for article in li.find_all('article',class_='c-card--tg-article'):
            link = url+article.find('a')['href']
            soup = BeautifulSoup(urlopen(link), 'html.parser')
            for meta in soup.find_all('meta',attrs={'property':"og:description"}):
                desc = meta['content'] 
        for div in li.find_all('div',class_='c-card__image--square'):
            for img in div.find_all('img'):
                if img.get('data-src'):
                    image = img.get('data-src')
        for div in li.find_all('div',class_='c-card__header'):
            for span in div.find('span'):
                title = span
        fashion_result.append(json.dumps({'title':title,'link':link,'image':image,'desc':desc}))

def scrape_f5():
    soup = BeautifulSoup(urlopen('https://www.wmagazine.com/fashion'),'html.parser')
    url = 'https://www.wmagazine.com'
    for li in soup.find_all('li',class_='component-river-item'):
        for div2 in li.find_all('div',class_='feature-item-content'):
            for a in div2.find_all('a',class_='feature-item-link'):
                link = url+a.get('href')
                title = a.get_text()
                soup = BeautifulSoup(urlopen(link), 'html.parser')
                for meta in soup.find_all('meta',attrs={'property':'og:description'}):
                    desc = meta['content'] 
                for meta in soup.find_all('meta',attrs={'property':'og:image'}):
                    image = meta['content'] 
        fashion_result.append(json.dumps({'title':title,'link':link,'image':image,'desc':desc}))

def scrape_f6():
    soup = BeautifulSoup(urlopen('https://www.yesstyle.com/blog/category/trend-and-style'),'html.parser')
    for article in soup.find_all('article',class_='box'):
        for div in article.find_all('div',class_='entry-thumbnail'):
            link = div.find('a')['href']
            title = div.find('a')['title']
            image = div.find('img')['src']
        for div2 in article.find_all('div',class_='entry-summary'):
            desc = div2.find('p').text
        fashion_result.append(json.dumps({'title':title,'link':link,'image':image,'desc':desc}))

def scrape_f7():
    req=Request("http://fashionbombdaily.com/category/trend",headers = {'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(urlopen(req),'html.parser')
    for article in soup.find_all('article',class_='post-featured'):
        for div in article.find_all('div',class_='overlay-media'):
            link = div.find('a')['href']
            image = div.find('img')['src']
        for div in article.find_all('div',class_='overlay-outer'):
            title = div.find('h2').get_text()
        fashion_result.append(json.dumps({'title':title,'link':link,'image':image,'desc':''}))

def scrape_f8():
    soup = BeautifulSoup(urlopen('https://www.nytimes.com/section/fashion'),'html.parser')
    url='https://www.nytimes.com'
    for article in soup.find_all('article'):
        for a in article.find_all('a'):
            for img in a.find_all('img'):
                link = url+a.get('href') 
                image = img.get('src')
        for div in article.find_all('div'):
            for a in div.find_all('a'):
                title = a.get_text()
            for p in div.find_all('p')[:1]:
                desc = p.text
        fashion_result.append(json.dumps({'title':title,'link':link,'image':image,'desc':desc}))

def scrape_f9():
    req=Request("https://blog.daraz.pk/category/fashion",headers = {'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(urlopen(req),'html.parser')
    for article in soup.find_all('article',class_='archive-layout'):
        link = article.find('a')['href']
        image = article.find('img')['src']
        for a in article.find_all('a',itemprop='mainEntityOfPage'):
            title = a.find('span').get_text()
        for div in article.find_all('div',class_='entry-summary'):
            desc = div.find('p').text
            fashion_result.append(json.dumps({'title':title,'link':link,'image':image,'desc':desc}))

def scrape_f10():
    soup = BeautifulSoup(urlopen('https://www.marieclaire.co.uk/fashion'),'html.parser')
    for li in soup.find_all('li',class_='listing-item'):
        for a in li.find_all('a',class_='entry'):
            link = a.get('href')
            title = a.get('title')
            for img in a.find_all('img',class_='image-sm'):
                image = img.get('data-src')
                soup = BeautifulSoup(urlopen(link), 'html.parser')
                for meta in soup.find_all('meta',attrs={'name':'description'}):
                    desc = meta['content']
                    fashion_result.append(json.dumps({'title':title,'link':link,'image':image,'desc':desc}))

def scrape_f11():
    soup = BeautifulSoup(urlopen('https://www.glamourmagazine.co.uk/topic/fashion-trends'),'html.parser')
    url = 'https://www.glamourmagazine.co.uk'
    for li in soup.find_all('li',class_='c-card-section__card-listitem'):
        for article in li.find_all('article',class_='c-card--tg-article'):
            link = url+article.find('a')['href']
            soup = BeautifulSoup(urlopen(link), 'html.parser')
            for meta in soup.find_all('meta',attrs={'name':'description'}):
                desc = meta['content']
        for div in li.find_all('div',class_='c-card__image--square'):
            for img in div.find_all('img'):
                if img.get('data-src'):
                    image = img.get('data-src')
        for div in li.find_all('div',class_='c-card__header'):
            for span in div.find('span'):
                title = span
        fashion_result.append(json.dumps({'title':title,'link':link,'image':image,'desc':desc}))

