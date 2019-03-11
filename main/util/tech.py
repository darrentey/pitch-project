from urllib.request import urlopen,Request
from bs4 import BeautifulSoup
import bs4
import requests
import json

    # top 50 popular hashtag in Instagram
    # req=Request("https://top-hashtags.com/instagram/",headers = {'User-Agent': 'Mozilla/5.0'})
    # soup = BeautifulSoup(urlopen(req), 'html.parser')
    # insta=[]
    # for rank in soup.find_all('div',class_='tht-tag'):
    #     insta.append(rank.text)
    # i=0
    # while i < 50:
    #     print(insta[i])
    #     i+=1

    # top 20 twitter trending hashtag
    # soup = BeautifulSoup(urlopen("http://tweeplers.com/hashtags/?cc=WORLD"), 'html.parser')
    # twitter=[]
    # for trend in soup.find_all('b'):
    #     if '#' in trend.text:
    #         twitter.append(trend.text)
    # print(twitter)

tech_result=[]

def scrape_t1():
    soup = BeautifulSoup(urlopen('https://www.businessinsider.my/tech-insider/'),'html.parser')
    for div in soup.find_all('div',class_='td-module-thumb'):
        for a in div.find_all('a'):
            for img in a.find_all('img'):
                x = (a.get('title')).strip()
                title = x.replace("\u2018","'")
                title = title.replace("\u2019","'")
                title = title.replace("\u2014","-")                
                tech_result.append(json.dumps({
                    'title' : title,
                    'link' : a.get('href'),
                    'image' : img.get('src')
                }))

def scrape_t2():
    soup = BeautifulSoup(urlopen('https://www.cnet.com/news/'),'html.parser')
    url='https://www.cnet.com'
    for main in soup.find_all('div',class_='riverPost'):
        for div1 in main.find_all('div',class_='assetText'):
            for h3 in div1.find_all('h3'):
                title = (h3.get_text()).strip()
                link = url+h3.find('a')['href'] 
        for div2 in main.find_all('div',class_='assetThumb'):
            for a in div2.find_all('a'):
                for img in a.find_all('img'):
                    if img.get('src'):
                        image = img.get('src')
            tech_result.append(json.dumps({'title':title,'link':link,'image':image}))

def scrape_t3():
    soup = BeautifulSoup(urlopen('https://techcrunch.com'),'html.parser')
    title=[]
    link=[]
    image=[]
    for div in soup.find_all('div',class_='river--homepage'):
        for h2 in div.find_all('h2',class_='post-block__title'):
            title.append((h2.find('a').get_text()).strip())
            link.append(h2.find('a')['href']) 
        for img in div.find_all('img'):
            image.append(img.get('src'))
    i=0
    while i < len(title):
        tech_result.append(json.dumps({
            'title':title[i],
            'link':link[i],
            'image':image[i]
        }))
        i+=1

def scrape_t4():
    soup = BeautifulSoup(urlopen('https://www.techmeme.com'),'html.parser')
    url='https://www.techmeme.com'
    for div in soup.find_all('div',class_='clus'):
        for a in div.find_all('a'):
            for img in a.find_all('img'):
                link = a.get('href')
                image = url+img.get('src')
        for a in div.find('a',class_='ourh'):
            title = a
        tech_result.append(json.dumps({'title':title,'link':link,'image':image}))

def scrape_t5():
    soup = BeautifulSoup(urlopen('https://www.nytimes.com/section/technology'),'html.parser')
    url='https://www.nytimes.com'
    for article in soup.find_all('article'):
        for a in article.find_all('a'):
            for img in a.find_all('img'):
                link = url+a.get('href')
                image = img.get('src')
        for div in article.find_all('div'):
            for a in div.find_all('a'):
                if a.get_text():
                    title = a.get_text()
        tech_result.append(json.dumps({'title':title,'link':link,'image':image}))

def scrape_t6():
    soup = BeautifulSoup(urlopen('https://arstechnica.com/gadgets'),'html.parser')
    for li in soup.find_all('li',class_='tease'):
        for figure in li.find_all('figure'):
            for div in figure.find_all('div'):
                img_url = div.get('style')
                t = img_url[img_url.find("https://"):]
                image = t[:t.find("'")]
        for header in li.find_all('header'):
            link = header.find('a')['href']
            title = header.find('a').get_text(strip=True)
        tech_result.append(json.dumps({'title':title,'link':link,'image':image}))

def scrape_t7():
    soup = BeautifulSoup(urlopen('https://www.theverge.com'),'html.parser')
    for div in soup.find_all('div',class_='c-entry-box--compact'):
        for a in div.find_all('a'):
            for img in a.find_all('img'):
                image = img.get('src')
        for div2 in div.find_all('div',class_='c-entry-box--compact__body'):
            link = div2.find('a')['href']  
            title = (div2.find('a').get_text()).strip()
        if image != None:
            if link != 'https://www.theverge.com/':    
                tech_result.append(json.dumps({'title':title,'link':link,'image':image}))

def scrape_t8():
    req=Request("https://readwrite.com",headers = {'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(urlopen(req),'html.parser')
    for article in soup.find_all('article'):
        for div in article.find_all('div',class_='post-thumb'):
            for img in div.find_all('img'):
                image = img.get('src')
        for div2 in article.find_all('div',class_='col-md-9'):
            for header in div2.find_all('header'):
                link = header.find('a')['href']  
                title = header.find('a').get_text()
        tech_result.append(json.dumps({'title':title,'link':link,'image':image}))

def scrape_t9():
    soup = BeautifulSoup(urlopen('https://venturebeat.com'),'html.parser')
    for div in soup.find_all('div',class_='story-river'):
        for article in div.find_all('article'):
            for div in article.find_all('div',class_='article-media-thumbnail'):
                for img in div.find_all('img'):
                    image = img.get('src')
            for header in article.find_all('header',class_='article-header'):
                link = header.find('a')['href'] 
                title = header.find('a').get_text()
            tech_result.append(json.dumps({'title':title,'link':link,'image':image}))

def scrape_t10():
    r = requests.get('http://feeds.bbci.co.uk/news/technology/rss.xml')
    data = r.text
    soup = BeautifulSoup(data,'html.parser')
    for item in soup.find_all('item'):
        tech_result.append(json.dumps({
            'title':item.find(text=lambda tag: isinstance(tag, bs4.CData)).string.strip(),
            'link':item.find('guid').text,
            'image':item.find('media:thumbnail')['url']
        }))
