import requests
import json
import configparser
from linebot import (
    LineBotApi, WebhookHandler
)

headers = {"Authorization":"Bearer <CHANNEL-ACCESS-TOKEN>","Content-Type":"application/json"}

body = {
    "size": {"width": 2500, "height": 1686},
    "selected": "true",
    "name": "menu",
    "chatBarText": "選單",
    "areas":[
        {
          "bounds": {"x": 0, "y": 0, "width": 1250, "height": 843},
          "action": {"type": "message", "text": "怡居標準層"}
        },
        {
          "bounds": {"x": 1251, "y": 0, "width": 1250, "height": 843},
          "action": {"type": "message", "text": "森山標準層"}
        },
        {
          "bounds": {"x": 0, "y": 843, "width": 1250, "height": 843},
          "action": {"type": "message", "text": "內容更新"}
        },
        {
          "bounds": {"x": 1251, "y": 844, "width": 1250, "height": 843},
          "action": {"type": "postback", "label": "下一頁","data":"action=next"}
        }
    ]
  }

req = requests.request('POST', 'https://api.line.me/v2/bot/richmenu', 
                       headers=headers,data=json.dumps(body).encode('utf-8'))

menuid = {}
menuid = json.loads(req.text)
richmenuid = menuid['richMenuId']
print(richmenuid)
config = configparser.ConfigParser()
config.read('config.ini')

line_bot_api = LineBotApi(config.get('linebot','channel_access_token'))

with open("menu.png", 'rb') as f:
    line_bot_api.set_rich_menu_image(richmenuid, "image/jpeg", f)
    
headers = {"Authorization":"Bearer <CHANNEL-ACCESS-TOKEN>","Content-Type":"application/json"}

uploadmenu = "https://api.line.me/v2/bot/user/all/richmenu/" + richmenuid

req = requests.request('POST', uploadmenu, 
                       headers=headers)

print(req.text)