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
    events = [{"date":"March 1","event":"National Read Across America Day (Dr. Seuss Day)"},{"date":"March 1","event":"Employee Appreciation Day"},{"date":"March 1","event":"Peanut Butter Lover’s Day"},{"date":"March 3","event":"Day of Unplugging"},{"date":"March 3","event":"World Wildlife Day"},{"date":"March 5","event":"Mardi Gras/Fat Tuesday"},{"date":"March 6","event":"Ash Wednesday"},{"date":"March 6","event":"Dentist’s Day"},{"date":"March 6","event":"Oreo Day"},{"date":"March 6","event":"Shaq’s Birthday"},{"date":"March 7","event":"Cereal Day"},{"date":"March 7-10","event":"Arnold Palmer Invitational PGA"},{"date":"March 8","event":"SXSW"},{"date":"March 8","event":"Popcorn Lover’s Day"},{"date":"March 8","event":"International Women’s Day"},{"date":"March 10" ,"event":"Daylight Savings"},{"date":"March 11" ,"event":"Napping Day"},{"date":"March 13" ,"event":"Jewel Day"},{"date":"March 14" ,"event":"Pi Day"},{"date":"March 14-17" ,"event":"The Players Championship PGA"},{"date":"March 15" ,"event":"The Ides of March"},{"date":"March 16" ,"event":"World Sleep Day"},{"date":"March 17" ,"event":"St. Patrick’s Day"},{"date":"March 18" ,"event":"Awkward Moments Day"},{"date":"March 20" ,"event":"First Day of Spring"},{"date":"March 20" ,"event":"Agriculture Day"},{"date":"March 20" ,"event":"World Down Syndrome Day"},{"date":"March 22" ,"event":"World Water Day"},{"date":"March 23" ,"event":"Puppy Day"},{"date":"March 25" ,"event":"Crossfit Open ends"},{"date":"March 26" ,"event":"Purple Day for Epilepsy Awareness"},{"date":"March 28" ,"event":"Baseball Opening Day"},{"date":"March 29" ,"event":"Mom & Pop Business Owner’s Day"},{"date":"March 30" ,"event":"National Doctor’s Day"},{"date":"March 31" ,"event":"Crayon Day"}]
    new_list = []
    for event in events:
        new_list.append(json.dumps(event))
    General.update(contents=new_list).where(General.name=="calendar").execute()
