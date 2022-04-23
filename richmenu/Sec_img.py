import requests
import json
from linebot import (
    LineBotApi,
)

from linebot.models import (
    RichMenu,
    RichMenuArea,
    RichMenuSize,
    RichMenuBounds,
    URIAction
)
from linebot.models.actions import RichMenuSwitchAction
from linebot.models.rich_menu import RichMenuAlias
import configparser
import os
config = configparser.ConfigParser()
config.read('config.ini')
line_bot_api = config.get('line-bot', 'channel_access_token')
headers1 = "{\"Authorization\":\"Bearer " + line_bot_api + "\",\"Content-Type\":\"application/json\"}"
headers = json.loads(headers1)
menu_pic = input("輸入路徑:")

body = {
    "size": {"width": 800, "height": 360},
    "selected": "false",
    "name": "richmenu-b",
    "chatBarText": "選單",
    "areas":[
        {
          "bounds": {"x": 0, "y": 50, "width": 400, "height": 153},
          "action": {"type": "message", "text": "工程數量"}
        },
        # {
        #   "bounds": {"x": 400, "y": 50, "width": 400, "height": 153},
        #   "action": {"type": "message", "text": "模型網址"}
        # },
        # {
        #   "bounds": {"x": 0, "y": 203, "width": 400, "height": 153},
        #   "action": {"type": "message", "text": "模板模型"}
        # },
        # {
        #   "bounds": {"x": 400, "y": 203, "width": 400, "height": 153},
        #   "action": {"type": "message", "text": "圖資圖說"}
        # },
        {
          "bounds": {"x": 0, "y": 0, "width": 400, "height": 50},
          "action": {"type": "richmenuswitch",
                "richMenuAliasId": "richmenu-alias-a",
                "data": "richmenu-changed-to-a"}
        }
    ]
  }

req = requests.request('POST', 'https://api.line.me/v2/bot/richmenu', 
                       headers=headers,data=json.dumps(body).encode('utf-8'))

menuid = {}
menuid = json.loads(req.text)
richmenuid = menuid['richMenuId']
print(richmenuid)

line_bot_api = LineBotApi(config.get('line-bot', 'channel_access_token'))

with open(menu_pic, 'rb') as f:
    line_bot_api.set_rich_menu_image(richmenuid, "image/jpeg", f)
    
try:
  line_bot_api.delete_rich_menu_alias("richmenu-alias-b")
except:
  print('')
  
alias_b = RichMenuAlias(
        rich_menu_alias_id='richmenu-alias-b',
        rich_menu_id=richmenuid
    )
line_bot_api.create_rich_menu_alias(alias_b)
print('success')
os.system("pause")