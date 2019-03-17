from urllib.request import urlopen,Request
from bs4 import BeautifulSoup
import bs4
import requests
from models.general import General
import json

def insta_tag():
    req=Request("https://top-hashtags.com/instagram/",headers = {'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(urlopen(req), 'html.parser')
    insta=[]
    for rank in soup.find_all('div',class_='tht-tag'):
        insta.append(rank.text)
    General.update(contents=insta).where(General.name=="instagram").execute()


def twitter_tag():
    soup = BeautifulSoup(urlopen("http://tweeplers.com/hashtags/?cc=WORLD"), 'html.parser')
    twitter=[]
    for trend in soup.find_all('b'):
        if '#' in trend.text:
            twitter.append(trend.text)
    General.update(contents=twitter).where(General.name=="twitter").execute()


def calender():
    events = [{"date":"1","event":"Employee Appreciation Day"},{"date":"1","event":"Peanut Butter Lover’s Day"},{"date":"2","event":"National Read Across America Day (Dr. Seuss Day)"},{"date":"3","event":"Day of Unplugging"},{"date":"3","event":"World Wildlife Day"},{"date":"5","event":"Mardi Gras/Fat Tuesday"},{"date":"6","event":"Ash Wednesday"},{"date":"6","event":"Dentist’s Day"},{"date":"6","event":"Oreo Day"},{"date":"6","event":"Shaq’s Birthday"},{"date":"7","event":"Cereal Day"},{"date":"7-10","event":"Arnold Palmer Invitational PGA"},{"date":"8","event":"SXSW"},{"date":"8","event":"Popcorn Lover’s Day"},{"date":"8","event":"International Women’s Day"},{"date":"10" ,"event":"Daylight Savings"},{"date":"11" ,"event":"Napping Day"},{"date":"13" ,"event":"Jewel Day"},{"date":"14" ,"event":"Pi Day"},{"date":"14-17" ,"event":"The Players Championship PGA"},{"date":"15" ,"event":"The Ides of March"},{"date":"16" ,"event":"World Sleep Day"},{"date":"17" ,"event":"St. Patrick’s Day"},{"date":"18" ,"event":"Awkward Moments Day"},{"date":"20" ,"event":"First Day of Spring"},{"date":"20" ,"event":"Agriculture Day"},{"date":"20" ,"event":"World Down Syndrome Day"},{"date":"22" ,"event":"World Water Day"},{"date":"23" ,"event":"Puppy Day"},{"date":"25" ,"event":"Crossfit Open ends"},{"date":"26" ,"event":"Purple Day for Epilepsy Awareness"},{"date":"28" ,"event":"Baseball Opening Day"},{"date":"29" ,"event":"Mom & Pop Business Owner’s Day"},{"date":"30" ,"event":"National Doctor’s Day"},{"date":"31" ,"event":"Crayon Day"}]
    new_list = []
    for event in events:
        new_list.append(json.dumps(event))
    General.update(contents=new_list).where(General.name=="calendar").execute()

mar_result=[]

def scrape_m1():
    soup = BeautifulSoup(urlopen('http://www.curata.com/blog/category/creation/'),'html.parser')
    for div in soup.find_all('div',class_='post-grid'):
        for article in div.find_all('article'):        
            desc = article.find('p').text + '...'
            for img in article.find_all('img'):
                image = img.get('src')
                link = article.find('a')['href']
            for h2 in article.find_all('h2'):
                title = h2.find('a').get_text() 
            mar_result.append(json.dumps({'title':title,'link':link,'image':image,'desc':desc}))

def scrape_m2():
    soup = BeautifulSoup(urlopen('https://contentmarketinginstitute.com/blog/'),'html.parser')
    for div in soup.find_all('div',class_='post'):
        for h2 in div.find_all('h2',class_='entry-title'):
            desc = div.find('p').text
            link = h2.find('a')['href']
            title = h2.find('a').get_text() 
            mar_result.append(json.dumps({'title':title,'link':link,'image':'https://s3-ap-southeast-1.amazonaws.com/nextagram-backend/cover.png','desc':desc}))

def scrape_m3():
    req=Request("https://www.convinceandconvert.com/category/greatest-hits/",headers = {'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(urlopen(req),'html.parser')
    for article in soup.find_all('article',class_='post'):
        for div in article.find_all('div'):
            for img in div.find_all('img'):
                image = img.get('src')
        for h4 in article.find_all('h4',class_='heading'):
            for a in h4.find_all('a'):
                link = a.get('href')
                title = a.text
                req=Request(link,headers = {'User-Agent': 'Mozilla/5.0'})
                soup = BeautifulSoup(urlopen(req), 'html.parser')
                for meta in soup.find_all('meta',attrs={'name':"description"}):
                    desc = meta['content']  
            mar_result.append(json.dumps({'title':title,'link':link,'image':image,'desc':desc}))

def scrape_m4():
    soup = BeautifulSoup(urlopen('https://www.briansolis.com/category/articles/'),'html.parser')
    for article in soup.find_all('article',class_='post'):
        desc = article.find('p').text
        for a in article.find_all('a',class_='overlay'):
            link = a.get('href')
            title = a.get('title')
        for img in article.find_all('img'):
            image = img.get('src')
            mar_result.append(json.dumps({'title':title,'link':link,'image':image,'desc':desc}))

def scrape_m5():
    soup = BeautifulSoup(urlopen('http://www.postadvertising.com/'),'html.parser')
    url = 'http://www.postadvertising.com'
    for article in soup.find_all('article',class_='entry'):
        for div in article.find_all('div',class_='excerpt-thumb'):
            link = url + div.find('a')['href']
            for a in div.find_all('a',class_='content-fill'):
                for img in a.find_all('img'):
                    image = img.get('data-image')
                    title = img.get('alt')
        for div2 in article.find_all('div',class_='entry-content'):
            for p in div2.find_all('p'):
                desc = p.text
                mar_result.append(json.dumps({'title':title,'link':link,'image':image,'desc':desc}))

def scrape_m6():
    soup = BeautifulSoup(urlopen('https://blog.hubspot.com/marketing'),'html.parser')
    for article in soup.find_all('article'):
        for figure in article.find_all('figure'):
            for img in figure.find_all('img'):
                image = img.get('src')
        for div in article.find_all('div',class_='blog-card__content'):
            for h3 in div.find_all('h3'):
                for a in h3.find_all('a'):
                    link = a.get('href')
                    title = a.text.strip()
                    soup = BeautifulSoup(urlopen(link), 'html.parser')
                    for meta in soup.find_all('meta',attrs={'name':"description"}):
                        desc = meta['content']  
                        mar_result.append(json.dumps({'title':title,'link':link,'image':image,'desc':desc}))