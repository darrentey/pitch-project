from urllib.request import urlopen,Request
from bs4 import BeautifulSoup
import bs4
import requests
import json

sport_result=[]

def scrape_s1():
    soup = BeautifulSoup(urlopen('https://sportsflashes.com/en/trending'),'html.parser')
    for div in soup.find_all('div',class_='card-container'):
        image = div.find('img')['src']
        title = div.find('p').get_text() 
        desc = (div.find('span').text).strip()
        url = div.get('onclick')
        t = str(url)[str(url).find("https://"):]
        link = str(t)[:str(t).find("')")]
        sport_result.append(json.dumps({'title':title,'link':link,'image':image,'desc':desc}))

def scrape_s2():
    soup = BeautifulSoup(urlopen('http://www.sportingnews.com/'),'html.parser')
    url = 'http://www.sportingnews.com'
    for li in soup.find_all('li',class_='media'):
        for figure in li.find_all('figure'):
            link = url + figure.find('a')['href']
            image = figure.find('img')['src']
            soup = BeautifulSoup(urlopen(link), 'html.parser')
            for meta in soup.find_all('meta',attrs={'property':"og:description"}):
                desc = meta['content'] 
            for meta in soup.find_all('meta',attrs={'property':"og:title"}):
                title = meta['content']
            sport_result.append(json.dumps({'title':title,'link':link,'image':image,'desc':desc}))

def scrape_s3():
    soup = BeautifulSoup(urlopen('http://www.espn.co.uk/fantasy/'),'html.parser')
    url = 'http://www.espn.co.uk'
    for article in soup.find_all('article',class_='contentItem'):
        for a in article.find_all('a',class_='contentItem__padding'):
            link = url + a.get('href')
            soup = BeautifulSoup(urlopen(link), 'html.parser')
            for meta in soup.find_all('meta',attrs={'property':"og:description"}):
                desc = meta['content'] 
            for meta in soup.find_all('meta',attrs={'property':"og:image"}):
                image = meta['content'] 
            for meta in soup.find_all('meta',attrs={'property':"og:title"}):
                title = meta['content'] 
            sport_result.append(json.dumps({'title':title,'link':link,'image':image,'desc':desc}))

def scrape_s4():
    req=Request('https://sport360.com/all-stories',headers = {'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(urlopen(req),'html.parser')
    for li in soup.find_all('li',class_='story'):
        link = li.find('a')['href']
        req=Request(link,headers = {'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(urlopen(req), 'html.parser')
        for meta in soup.find_all('meta',attrs={'property':"og:description"}):
            desc = meta['content'] 
        for meta in soup.find_all('meta',attrs={'property':"og:image"}):
            image = meta['content'] 
        for meta in soup.find_all('meta',attrs={'property':"og:title"}):
            title = meta['content'] 
        sport_result.append(json.dumps({'title':title,'link':link,'image':image,'desc':desc}))

def scrape_s5():
    soup = BeautifulSoup(urlopen('https://www.yardbarker.com/newsletter/edition/10262?latest=true'),'html.parser')
    for table in soup.find_all('table',class_='mb_story'):
        for div in table.find_all('div',class_='mb_head'):
            link = div.find('a')['href']
            title = div.find('a').get_text()
            soup = BeautifulSoup(urlopen(link), 'html.parser')
            for meta in soup.find_all('meta',attrs={'property':"og:description"}):
                desc = meta['content'] 
            for meta in soup.find_all('meta',attrs={'property':"og:image"}):
                image = meta['content'] 
            sport_result.append(json.dumps({'title':title,'link':link,'image':image,'desc':desc}))

def scrape_s6():
    soup = BeautifulSoup(urlopen('https://www.usatoday.com/sports'),'html.parser')
    url = 'https://www.usatoday.com'
    for ul in soup.find_all('ul',class_='contents'):
        for li in ul.find_all('li'):
            link = url + li.find('a')['href']
            title = li.find('span').get_text()
            soup = BeautifulSoup(urlopen(link), 'html.parser')
            for meta in soup.find_all('meta',attrs={'property':"og:description"}):
                desc = meta['content'] 
            for meta in soup.find_all('meta',attrs={'property':"og:image"}):
                image = meta['content'] 
            sport_result.append(json.dumps({'title':title,'link':link,'image':image,'desc':desc}))

def scrape_s7():
    soup = BeautifulSoup(urlopen('https://unafraidshow.com/category/sports/'),'html.parser')
    for article in soup.find_all('article',class_='blog-entry'):
        for header in article.find_all('header'):
            link = header.find('a')['href']
            title = header.find('a').get_text()
            soup = BeautifulSoup(urlopen(link), 'html.parser')
            for meta in soup.find_all('meta',attrs={'property':"og:description"}):
                desc = meta['content'] 
            for meta in soup.find_all('meta',attrs={'property':"og:image"}):
                image = meta['content'] 
            sport_result.append(json.dumps({'title':title,'link':link,'image':image,'desc':desc}))

def scrape_s8():
    soup = BeautifulSoup(urlopen('https://www.insidesport.co/category/latest-news/'),'html.parser')
    check = []
    for div in soup.find_all('div',class_='td-module-thumb'):
        link = div.find('a')['href']
        if link not in check:
            soup = BeautifulSoup(urlopen(link), 'html.parser')
            for meta in soup.find_all('meta',attrs={'property':"og:description"}):
                desc = meta['content'] 
            for meta in soup.find_all('meta',attrs={'property':"og:image"}):
                image = meta['content'] 
            for meta in soup.find_all('meta',attrs={'property':"og:title"}):
                title = meta['content'] 
            check.append(link)
            sport_result.append(json.dumps({'title':title,'link':link,'image':image,'desc':desc}))

def scrape_s9():
    soup = BeautifulSoup(urlopen('https://onlinesportsblog.com/category/all-sports/'),'html.parser')
    check = []
    for div in soup.find_all('div',class_='td-main-content-wrap'):
        for h3 in div.find_all('h3',class_='entry-title'):
            link = h3.find('a')['href']
            if link not in check:
                soup = BeautifulSoup(urlopen(link), 'html.parser')
                for meta in soup.find_all('meta',attrs={'property':"og:description"}):
                    desc = meta['content'] 
                for meta in soup.find_all('meta',attrs={'property':"og:image"}):
                    image = meta['content'] 
                for meta in soup.find_all('meta',attrs={'property':"og:title"}):
                    title = meta['content'] 
                check.append(link)
                sport_result.append(json.dumps({'title':title,'link':link,'image':image,'desc':desc}))

def scrape_s10():
    r = requests.get('http://franchisesports.co.uk/feed/')
    check = []
    data = r.text
    soup = BeautifulSoup(data,'html.parser')
    for item in soup.find_all('item'):
        link = item.find('guid').text
        if link not in check:
            soup = BeautifulSoup(urlopen(link), 'html.parser')
            for meta in soup.find_all('meta',attrs={'property':"og:description"}):
                desc = meta['content'] 
            for meta in soup.find_all('meta',attrs={'property':"og:image"}):
                image = meta['content'] 
            for meta in soup.find_all('meta',attrs={'property':"og:title"}):
                title = meta['content'] 
            check.append(link)
            sport_result.append(json.dumps({'title':title,'link':link,'image':image,'desc':desc}))

def scrape_s11():
    soup = BeautifulSoup(urlopen('https://esportsobserver.com/category/features/'),'html.parser')
    check = []
    for h3 in soup.find_all('h3',class_='entry-title'):
        link = h3.find('a')['href']
        if link not in check:
            soup = BeautifulSoup(urlopen(link), 'html.parser')
            for meta in soup.find_all('meta',attrs={'property':"og:description"}):
                desc = meta['content'] 
            for meta in soup.find_all('meta',attrs={'property':"og:image"}):
                image = meta['content'] 
            for meta in soup.find_all('meta',attrs={'property':"og:title"}):
                title = meta['content'] 
            check.append(link)
            sport_result.append(json.dumps({'title':title,'link':link,'image':image,'desc':desc}))

def scrape_s12():
    soup = BeautifulSoup(urlopen('https://esportsinsider.com/category/news-by-region/'),'html.parser')
    check = []
    for div in soup.find_all('div',class_='td-module-thumb'):
        link = div.find('a')['href']
        if link not in check:
            soup = BeautifulSoup(urlopen(link), 'html.parser')
            for meta in soup.find_all('meta',attrs={'property':"og:description"}):
                desc = meta['content'] + '...'
            for meta in soup.find_all('meta',attrs={'property':"og:image"}):
                image = meta['content'] 
            for meta in soup.find_all('meta',attrs={'property':"og:title"}):
                title = meta['content'] 
            check.append(link)
            sport_result.append(json.dumps({'title':title,'link':link,'image':image,'desc':desc}))