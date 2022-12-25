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
    #print(soup.prettify())
    for anime in soup.find_all("td"):
        for name in anime.find_all("a"):
            print(name.text + " : " + name.get("href"))
    #    for name in anime.find("td"):
    #        print(name.text)

def web_scrapying_acg_name(acg_url ,names):
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

def web_scrapying_acg_keywords(acg_url ,keywords):
    ret = ""
    response = requests.get(acg_url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, "html.parser")
    print(keywords)
    if(len(keywords)==0):
        return
    for anime in soup.find_all("div", {"class": {"anime_content"}}):
            match = 0
            for tag in anime.find_all("tags"):
                for keyword in keywords:
                    if(tag.text.find(keyword) >= 0):
                        match += 1
                        if(match == len(keywords)):
                            ret += ("Name: " + anime.find("h3").text) + "\n"
    return ret    

def web_scrapying_acg_update(acg_url, names):
    week = ["Mon:\n", "Tue:\n", "Wed:\n", "Thu:\n", "Fri:\n", "Sat:\n", "Sun:\n"]
    ret = ""
    response = requests.get(acg_url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, "html.parser")
    
    if(len(names)==0):
        for anime in soup.find_all("div", {"class": {"anime_content"}}):
            time = anime.find("div", {"class": "anime_onair time_today"}).text
            if time.find("一")>=0:
                week[0] += (anime.find("h3").text) + '\n'
            if time.find("二")>=0:
                week[1] += (anime.find("h3").text) + '\n'
            if time.find("三")>=0:
                week[2] += (anime.find("h3").text) + '\n'
            if time.find("四")>=0:
                week[3] += (anime.find("h3").text) + '\n' 
            if time.find("五")>=0:
                week[4] += (anime.find("h3").text) + '\n'
            if time.find("六")>=0:
                week[5] += (anime.find("h3").text) + '\n'
            if time.find("日")>=0:
                week[6] += (anime.find("h3").text) + '\n'
        for i in range(7):
            ret += week[i]
        return ret
      
    for anime in soup.find_all("div", {"class": {"anime_content"}}):
        time = anime.find("div", {"class": "anime_onair time_today"}).text
        for name in names:
            if anime.find("h3").text.find(name) >= 0:
                ret += ("Name: " + (anime.find("h3").text) + '\n')
                ret += (time + '\n')      
    return ret


   
'''
if __name__ == "__main__":
    names = ["鏈鋸人", "忍者"]
    keywords = ["喜劇"]
    do = []
    #time = get_time(2022, 4)
    #print(time)
    #acg_url = get_acg_url("202210")
    ani1_url = get_anime1_url()
    web_scrapying_ani1(ani1_url)
    #text = web_scrapying_acg_update(acg_url, names)
    #print(text)
''' 
    