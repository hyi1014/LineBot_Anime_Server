# -*- coding: utf-8 -*-

#載入LineBot所需要的套件
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

import re
import os

app = Flask(__name__)

channel_acc_token = os.environ.get('CHANNEL_ACCESS_TOKEN')
channel_sct = os.environ.get('CHANNEL_SECRET')
user_id = os.environ.get('USER_ID')

# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi(channel_acc_token)
# 必須放上自己的Channel Secret
handler = WebhookHandler(channel_sct)

line_bot_api.push_message(user_id, TextSendMessage(text='AnimeBot Online'))


# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

 
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

 
#訊息傳遞區塊
##### 基本上程式編輯都在這個function #####
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = text=event.message.text
    if re.match('commands',message):
        line_bot_api.reply_message(event.reply_token,TextSendMessage('This is commands'))
    else:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(message))

#主程式
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
