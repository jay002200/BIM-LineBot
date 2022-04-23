import requests
import json
from linebot import (
    LineBotApi, WebhookHandler
)

headers = {"Authorization":"Bearer H5ExUQxWHnJmOQlGUh0/SDmxb/8AZvKrOAqoGHARDfpMA1yrXJRnME0uL0NSzNxbGYkvPrk56VBs5D9gmwyh1rUoktZpeHcGfgHvp18mtX6pjF3zB4fH6/MUrWWB7CXankjsBfeXV2Gy143lbN74CQdB04t89/1O/w1cDnyilFU=","Content-Type":"application/json"}

body = {
    "size": {"width": 2500, "height": 1686},
    "selected": "true",
    "name": "menu",
    "chatBarText": "選單",
    "areas":[
        {
          "bounds": {"x": 0, "y": 0, "width": 1250, "height": 843},
          "action": {"type": "message", "text": "A2"}
        },
        {
          "bounds": {"x": 1251, "y": 0, "width": 1250, "height": 843},
          "action": {"type": "message", "text": "B2"}
        },
        {
          "bounds": {"x": 0, "y": 843, "width": 1250, "height": 843},
          "action": {"type": "message", "text": "C2"}
        },
        {
          "bounds": {"x": 1251, "y": 844, "width": 1250, "height": 843},
          "action": {"type": "postback", "label": "上一頁","data":"action=prev"}
        }
    ]
  }

req = requests.request('POST', 'https://api.line.me/v2/bot/richmenu', 
                       headers=headers,data=json.dumps(body).encode('utf-8'))

menuid = {}
menuid = json.loads(req.text)
richmenuid = menuid['richMenuId']
print(richmenuid)

line_bot_api = LineBotApi('H5ExUQxWHnJmOQlGUh0/SDmxb/8AZvKrOAqoGHARDfpMA1yrXJRnME0uL0NSzNxbGYkvPrk56VBs5D9gmwyh1rUoktZpeHcGfgHvp18mtX6pjF3zB4fH6/MUrWWB7CXankjsBfeXV2Gy143lbN74CQdB04t89/1O/w1cDnyilFU=')

with open("menu3.png", 'rb') as f:
    line_bot_api.set_rich_menu_image(richmenuid, "image/jpeg", f)