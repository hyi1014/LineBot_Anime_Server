import os
import random
from dotenv import load_dotenv

from linebot import LineBotApi
from linebot.exceptions import InvalidSignatureError
from linebot.models import *

load_dotenv()
line_bot_api = LineBotApi(os.getenv('CHANNEL_ACCESS_TOKEN', default=''))

#from fsm import *

name_list = []
keyword_list = []

def get_id(event):
    if(event.source.type == 'user'):
        return event.source.user_id
    if(event.source.type == 'group'):
        return event.source.group_id

def show_help_msg(event):
    text= "-----Help-----\n"
    text+= "1. help / show fsm / show process\n"
    text+= "2. exit\n"
    
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
    text += "1. set name and search the anime updated-info\n"
    text += "2. list the anime updated-info of the week\n"


def clear_list():
    name_list.clear()
    keyword_list.clear()
    
def show_state_msg(event, state):
    text = state
    line_bot_api.reply_message(event.reply_token, 
                               TextSendMessage(text))
