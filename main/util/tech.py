from urllib.request import urlopen,Request
from bs4 import BeautifulSoup
import bs4
import requests
import json

tech_result=[]

def scrape_t1():
    soup = BeautifulSoup(urlopen('https://www.businessinsider.my/tech-insider/'),'html.parser')
    for div in soup.find_all('div',class_='td-module-thumb'):
        for a in div.find_all('a'):
                soup = BeautifulSoup(urlopen(a.get('href')), 'html.parser')
                for meta in soup.find_all('meta',attrs={'property':"og:description"}):
                    desc = meta['content']  
                for meta in soup.find_all('meta',attrs={'property':"og:image"}):
                    image = meta['content']  
                    tech_result.append(json.dumps({
                        'title' : (a.get('title')).strip(),
                        'link' : a.get('href'),
                        'image' : image,
                        'desc' : desc
                    }))

def scrape_t2():
    soup = BeautifulSoup(urlopen('https://www.cnet.com/news/'),'html.parser')
    url='https://www.cnet.com'
    for main in soup.find_all('div',class_='riverPost'):
        for div1 in main.find_all('div',class_='assetText'):
            for h3 in div1.find_all('h3'):
                title = (h3.get_text()).strip()
                link = url+h3.find('a')['href']
            for p in div1.find_all('p'): 
                desc = (p.get_text()).strip()
        for div2 in main.find_all('div',class_='assetThumb'):
            for a in div2.find_all('a'):
                for img in a.find_all('img'):
                    if img.get('src'):
                        image = img.get('src')
            tech_result.append(json.dumps({'title':title,'link':link,'image':image,'desc':desc}))

def scrape_t3():
    soup = BeautifulSoup(urlopen('https://techcrunch.com'),'html.parser')
    title=[]
    link=[]
    image=[]
    desc=[]
    for div in soup.find_all('div',class_='river--homepage'):
        for div2 in div.find_all('div',class_='post-block__content'):
            desc.append(div2.text)       
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
            'image':image[i],
            'desc':desc[i]
        }))
        i+=1

def scrape_t4():
    soup = BeautifulSoup(urlopen('https://www.techmeme.com'),'html.parser')
    url='https://www.techmeme.com'
    for div in soup.find_all('div',class_='clus'):
        title = div.find('strong').get_text()
        summary = div.find('div',class_='ii').get_text()
        if title in summary:
            desc = summary.replace(title,'')
            for a in div.find_all('a'):
                for img in a.find_all('img'):
                    link = a.get('href')
                    image = url+img.get('src')
            tech_result.append(json.dumps({'title':title,'link':link,'image':image,'desc':desc}))

def scrape_t5():
    soup = BeautifulSoup(urlopen('https://www.nytimes.com/section/technology'),'html.parser')
    url='https://www.nytimes.com'
    for ol in soup.find_all('ol'):
        for a in ol.find_all('a'):
            for img in a.find_all('img'):
                link = url+a.get('href')
                image = img.get('src')
            for h2 in a.find_all('h2'):            
                title = h2.text
            for p in a.find_all('p',class_='css-1echdzn'):            
                desc = p.text
                tech_result.append(json.dumps({'title':title,'link':link,'image':image,'desc':desc}))

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
            desc = header.find('p').get_text(strip=True)
        tech_result.append(json.dumps({'title':title,'link':link,'image':image,'desc':desc}))
         
        

def scrape_t7():
    soup = BeautifulSoup(urlopen('https://www.theverge.com'),'html.parser')
    for div in soup.find_all('div',class_='c-entry-box--compact'):
        for div2 in div.find_all('div',class_='c-entry-box--compact__body'):
            link = div2.find('a')['href']  
            title = (div2.find('a').get_text()).strip()
        if link != 'https://www.theverge.com/': 
            soup = BeautifulSoup(urlopen(link), 'html.parser')
            for meta in soup.find_all('meta',attrs={'name':'description'}):
                desc = meta['content'] 
            for meta in soup.find_all('meta',attrs={'property':"og:image"}):
                image = meta['content']    
            tech_result.append(json.dumps({'title':title,'link':link,'image':image,'desc':desc}))


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
            for div3 in div2.find_all('div',class_='entry-content'):
                desc = div3.find('p').text
        tech_result.append(json.dumps({'title':title,'link':link,'image':image,'desc':desc}))

def scrape_t9():
    soup = BeautifulSoup(urlopen('https://venturebeat.com'),'html.parser')
    for div in soup.find_all('div',class_='story-river'):
        for article in div.find_all('article'):
            for header in article.find_all('header',class_='article-header'):
                link = header.find('a')['href'] 
                title = header.find('a').get_text()
                soup = BeautifulSoup(urlopen(link), 'html.parser')
                for meta in soup.find_all('meta',attrs={'property':"og:description"}):
                    desc = meta['content']  
                for meta in soup.find_all('meta',attrs={'property':"og:image"}):
                    image = meta['content']  
                    tech_result.append(json.dumps({'title':title,'link':link,'image':image,'desc':desc}))

def scrape_t10():
    r = requests.get('http://feeds.bbci.co.uk/news/technology/rss.xml')
    data = r.text
    soup = BeautifulSoup(data,'html.parser')
    for item in soup.find_all('item'):
        desc = item.find('description')
        tech_result.append(json.dumps({
            'title':item.find(text=lambda tag: isinstance(tag, bs4.CData)).string.strip(),
            'link':item.find('guid').text,
            'image':item.find('media:thumbnail')['url'],
            'desc':desc.find(text=lambda tag: isinstance(tag, bs4.CData)).string.strip()
        }))