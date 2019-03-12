from urllib.request import urlopen,Request
from bs4 import BeautifulSoup
import bs4
import requests
from models.general import General

def insta_tag():
    req=Request("https://top-hashtags.com/instagram/",headers = {'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(urlopen(req), 'html.parser')
    insta=[]
    for rank in soup.find_all('div',class_='tht-tag'):
        insta.append(rank.text)
    General(name="instagram",contents=insta).save()


def twitter_tag():
    soup = BeautifulSoup(urlopen("http://tweeplers.com/hashtags/?cc=WORLD"), 'html.parser')
    twitter=[]
    for trend in soup.find_all('b'):
        if '#' in trend.text:
            twitter.append(trend.text)
    General(name="twitter",contents=twitter).save()


