import os
import re
import datetime
import random
from dotenv import load_dotenv

from linebot import LineBotApi
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
from webscrapying import *

load_dotenv()
line_bot_api = LineBotApi(os.getenv('CHANNEL_ACCESS_TOKEN', default=''))

#from fsm import *

date = None
web = None
name_list = []
keyword_list = []

def get_id(event):
    if(event.source.type == 'user'):
        return event.source.user_id
    if(event.source.type == 'group'):
        return event.source.group_id

def show_help_msg(event):
    text= "-----Help-----\n"
    text+= "1. help / show fsm\n"
    text+= "3. exit\n"
    
    text += "-----Update-----\n"
    text += "1. update\n"
    text += "2. set name / show\n"
    text += "3. search\n"
    
    text += "-----Search Anime in ACG-----\n"
    text += "1. set web\n"
    text += "2. acg\n"
    text += "3. set date\n"
    text += "4. set names / set keywords\n"
    text += "5. search\n"
    
    text += "-----Search Anime in Anime1-----\n"
    text += "1. set web\n"
    text += "2. anime1\n"
    text += "3. set names\n"
    text += "4. search\n"
    line_bot_api.reply_message(event.reply_token, 
                                TextSendMessage(text))

def show_update_msg(event):
    text = "-----Options-----\n"
    text += "1. set name and search info\n"
    text += "2. list this week info\n"

    line_bot_api.reply_message(event.reply_token, 
                               TextSendMessage(text))


def add_name(event):
    global name_list
    msg = event.message.text
    name_list+=get_anime_list(msg, "add", event=event)
        
def del_name(event):
    global name_list
    msg = event.message.text
    del_list=get_anime_list(msg, "del", event=event)
    for i in range(len(del_list)):
        name_list.remove(del_list[i])
    
def add_keyword(event):
    global keyword_list
    msg = event.message.text
    keyword_list+=get_anime_list(msg, op="add", event=event)
    
def del_keyword(event):
    global keyword_list
    msg = event.message.text
    del_list=get_anime_list(msg, op="del", event=event)
    for i in range(len(del_list)):
        keyword_list.remove(del_list[i])

def show_name_list(event):
    text = "-----Name List-----\n"
    for i in range(len(name_list)):
        text += str(i+1) + ". " + name_list[i] + "\n"
    line_bot_api.reply_message(event.reply_token, 
                               TextSendMessage(text))
def show_keyword_list(event):
    text = "-----Keyword List-----\n"
    for i in range(len(keyword_list)):
        text += str(i+1) + ". " + keyword_list[i] + "\n"
    line_bot_api.reply_message(event.reply_token, 
                               TextSendMessage(text))

def show_set_web_msg(event):
    text = "-----Options-----\n"
    text += "1. acg\n"
    text += "2. anime1\n"
    line_bot_api.reply_message(event.reply_token,
                               TextSendMessage(text))

def show_web_acg_msg(event):
    global web
    web = "acg"
    text = "-----Options-----\n"
    text += "1. set date, search\n"
    text += "2. set date and name, search\n"
    text += "3. set date and keyword, search\n"
    line_bot_api.reply_message(event.reply_token,
                               TextSendMessage(text))
    
def show_web_anime1_msg(event):
    global web
    web = "anime1"
    text = "-----Options-----\n"
    text += "1. set name, search\n"
    line_bot_api.reply_message(event.reply_token,
                               TextSendMessage(text))
    
def set_date(event):
    global date
    date_list = re.split(r'[ ]', event.message.text)
    year = int(date_list[2])
    month = int(date_list[3])
    if(len(date_list) != 4 or
       not date_list[2].isdigit() or
       not date_list[3].isdigit() or
       year < 2017 or year > 2022 or
       month not in [1, 4, 7, 10]):
        line_bot_api.reply_message(event.reply_token,
                                    TextSendMessage("Wrong format"))
        return
    date = "{:4d}{:02d}".format(year, month)
    print(date)
    text = "Set date: " + date
    line_bot_api.reply_message(event.reply_token,
                                TextSendMessage(text))    

def show_set_date_msg(event):
    text = "-----Options-----\n"
    text += "set year and month\n"
    text += "year: 2017-2022\n"
    text += "month: 1, 4, 7, 10\n"
    text += "ex:set date 2020 10\n"
    line_bot_api.reply_message(event.reply_token, 
                               TextSendMessage(text))
def show_set_name_msg(event):
    text = "-----Options-----\n"
    text += "1. add name /...\n"
    text += "2. del name /...\n"
    text += "3. show name list\n"
    text += "4. search\n"
    text += "ex: add/del name 海賊王 火影忍者\n"
    text += "    show\n"
    text += "    search\n"
    line_bot_api.reply_message(event.reply_token, 
                               TextSendMessage(text))
    
def show_set_keyword_msg(event):
    text = "-----Options-----\n"
    text += "1. add keyword/...\n"
    text += "2. del keyword/...\n"
    text += "3. show keyword list\n"
    text += "4. search\n"
    text += "ex: add/del keyword 小說改編 喜劇\n"
    text += "    show\n"
    text += "    search\n"
    line_bot_api.reply_message(event.reply_token, 
                               TextSendMessage(text))

def clear_list():
    name_list.clear()
    keyword_list.clear()
    
def show_state_msg(event, state):
    text = state
    line_bot_api.reply_message(event.reply_token, 
                               TextSendMessage(text))

def get_anime_list(msg, op, event):
    op = op+" "
    msg = msg.replace(op, "")
    ret_list = re.split(r'[ ]', msg)
    text = "operation: " + op + " success\n"
    line_bot_api.reply_message(event.reply_token, 
                               TextSendMessage(text))
    return ret_list

def search_name(event):
    url = ""
    text = ""
    print(date)
    
    if(web == "acg"):
        url = get_acg_url(date)
        text = web_scrapying_acg_name(url, name_list)
    if(web == "anime1"):
        url = get_anime1_url()
        text = web_scrapying_anime1(url, name_list)
    line_bot_api.reply_message(event.reply_token,
                               TextSendMessage(text))
    clear_list()

def search_keyword(event):
    url = ""
    text = ""
    
    if(web == "acg"):
        url = get_acg_url(date)
        text = web_scrapying_acg_keywords(url, keyword_list)
    line_bot_api.reply_message(event.reply_token,
                               TextSendMessage(text))
    clear_list()   

def search_update(event):
    url = ""
    text = ""
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    for i in [10, 7, 4, 1]:
        if month > i:
            month = i
            break
    
    date = "{:4d}{:02d}".format(year, month)
    #print(date)
    url = get_acg_url(date)
    #print(url)
    text = web_scrapying_acg_update(url, name_list)
    #print(name_list)
    #print(text)
    line_bot_api.reply_message(event.reply_token,
                               TextSendMessage(text))
    clear_list()
