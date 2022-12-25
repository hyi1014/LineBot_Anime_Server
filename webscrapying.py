import requests
import datetime
import numpy as np
from bs4 import BeautifulSoup

def get_anime1_url():
    url_anime1 = "https://anime1.me/"
    return url_anime1

def get_acg_url(date):
    url_ACG_HK = "https://acgsecrets.hk/bangumi/"+date+"/"
    return url_ACG_HK

def get_time(year, month):
    now_time = datetime.datetime.now()
    ret_year = year
    ret_month = month  
    if(year == None):
        ret_year = now_time.year
    if(month == None):
        month = now_time.month

    month_list = [1, 4, 7, 10]
    for m in month_list:
        if month > m:
            ret_month = m
        if m == month:
            return 0 # wrong month
    return [ret_year, ret_month]

def web_scrapying_ani1(ani1_url):
    response = requests.get(ani1_url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, "html.parser")
    for stream_site in soup.find_all("a"):
        print("> " + stream_site.text + " : ", end="")
        print(stream_site.get("href"))

def web_scrapying_acg(acg_url ,names):
    ret = ""
    response = requests.get(acg_url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, "html.parser")
    
    #search
    if(len(names)!=0):
        for anime in soup.find_all("div", {"class": {"anime_content"}}):
            for name in names:
                if anime.find("h3").text.find(name) >= 0:
                    ret += "Name: " + anime.find("h3").text + "\n"
                    for stream in anime.find_all("div", {"class": {"anime_streams"}}):
                        ret += "Loc: " + stream.find("span", {"class": "stream-area"}).text + '\n'
                        for stream_site in stream.find_all("span", {"class": "stream-sites"}):
                            ret += "> " + stream_site.find("a").text + " :"
                            link = stream_site.find("a").get("href")
                            if(type(link) == type(None)):
                                ret+= "None\n"
                            else:
                                ret+= link +"\n"        
    #list all
    else:
        for anime in soup.find_all("div", {"class": {"anime_content"}}):
            ret += "Name: " + (anime.find("h3").text) + '\n'
            #for stream in anime.find_all("div", {"class": {"anime_streams"}}):
            #   print("Loc: " + stream.find("span", {"class": "stream-area"}).text)
            #    for stream_site in stream.find_all("span", {"class": "stream-sites"}):
            #        print("> " + stream_site.find("a").text + " : ", end="")
            #        print(stream_site.find("a").get("href"))
    return ret
  
'''
if __name__ == "__main__":
    names = ["鏈鋸人"]
    #time = get_time(2022, 4)
    #print(time)
    acg_url = get_acg_url([2022, 10])
    #ani1_url = get_anime1_url()
    #web_scrapying_ani1(ani1_url)
    text = web_scrapying_acg(acg_url ,names)
    print(text)
'''   
    