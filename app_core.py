from datetime import date
from flask import Flask, request, abort
from gspread.models import Worksheet
from linebot import exceptions
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
from imgurpython import ImgurClient
import re
import random
import time
import os
import tempfile
import gspread
import configparser
from oauth2client.service_account import ServiceAccountCredentials as SAC
from requests.api import get

    
app = Flask(__name__)
now_time = time.strftime("%b %d %a %H:%M:%S %Y", time.localtime()) 
config = configparser.ConfigParser()
config.read('config.ini')
# The line bot access token and webhook id

line_bot_api = LineBotApi(config.get('linebot','channel_access_token'))
handler = WebhookHandler(config.get('line-bot', 'channel_secret'))

# The imgur client id, client secret, access token and refresh token
client_id = '-'
client_secret = '-'
access_token = '-'
refresh_token = '-'
client = ImgurClient(client_id, client_secret, access_token, refresh_token)

@app.route("/", methods=['POST'])
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


@handler.add(MessageEvent, message=(TextMessage, ImageMessage))
def handle_message(event):
    # receive key word -> send message or do something   
    if isinstance(event.message, TextMessage):
        now_time = time.strftime("%b %d %a %H:%M:%S %Y", time.localtime()) 
        a = 0
        b = 0     
        user_id = event.source.user_id
        replymessage = event.message.text
        
        profile = line_bot_api.get_profile(user_id)
        echeckcode = re.split(r'[\s]\s*', replymessage)
        inputnum = []
        isrepeat = False
        for num in echeckcode[0]:
            if num in inputnum:
                isrepeat = True
                break
            inputnum.append(num)   
            
        topic = gettopic()
        topic_list = list(str(topic))
        if user_id != "-":
            user_list = []
            user_list.append(profile.display_name)
            user_list.append(profile.picture_url)
            user_list.append(replymessage)
            user_list.append(now_time)
            user_list.append(user_id)
            googlesheet(user_list)
        
        mainimage = ImagemapSendMessage(
        base_url='https://imgur.com/-.jpg',
        alt_text='圖片',
        base_size=BaseSize(height=720, width=1280),     
        actions=[
            MessageImagemapAction(
                text='怡居A區',
                area=ImagemapArea(
                    x=223, y=160, width=80, height=80
                )
            ),
            MessageImagemapAction(
                text='怡居B區',
                area=ImagemapArea(
                    x=172, y=347, width=80, height=80
                )
            ),
            MessageImagemapAction(
                text='怡居C區',
                area=ImagemapArea(
                    x=415, y=346, width=80, height=80
                )
            ),
            MessageImagemapAction(
                text='怡居D區',
                area=ImagemapArea(
                    x=712, y=340, width=80, height=80
                )
            ),
            MessageImagemapAction(
                text='怡居E區',
                area=ImagemapArea(
                    x=962, y=346, width=80, height=80
                )
            ),
            MessageImagemapAction(
                text='怡居F區',
                area=ImagemapArea(
                    x=929, y=150, width=80, height=80
                )
            ),
            MessageImagemapAction(
                text='怡居G區',
                area=ImagemapArea(
                    x=734, y=143, width=80, height=80
                )
            ),
            MessageImagemapAction(
                text='怡居H區',
                area=ImagemapArea(
                    x=442, y=156, width=81, height=80
                )
            )         
        ]
    )

        sec_mainimage = ImagemapSendMessage(
        base_url='https://imgur.com/-.jpg',
        alt_text='圖片',
        base_size=BaseSize(height=720, width=1280),     
        actions=[
            URIImagemapAction(
                link_uri='https://photos.app.goo.gl/-',
                area=ImagemapArea(
                    x=263, y=316, width=80, height=80
                )
            ),
            URIImagemapAction(
                link_uri='https://photos.app.goo.gl/-',
                area=ImagemapArea(
                    x=396, y=310, width=80, height=80
                )
            )
                     
        ]
    )
        
        mainimagemenu = TemplateSendMessage(
                            alt_text='Buttons template',
                            template=ButtonsTemplate(
                                title='Menu',
                                text=' ',
                                actions=[
                                    MessageTemplateAction(
                                        label='看主圖',
                                        text='主圖'
                                    )
                                ]
                            )
                        )
        
        Aarea = ImagemapSendMessage(
        base_url='https://imgur.com/-.jpg',
        alt_text='圖片',
        base_size=BaseSize(height=720, width=1280),     
        actions=[
            URIImagemapAction(
                link_uri='https://photos.app.goo.gl/-',
                area=ImagemapArea(
                    x=365, y=87, width=80, height=80
                )
            ),
            URIImagemapAction(
                link_uri='https://photos.app.goo.gl/-',
                area=ImagemapArea(
                    x=593, y=267, width=80, height=80
                )
            ),
            URIImagemapAction(
                link_uri='https://photos.app.goo.gl/-',
                area=ImagemapArea(
                    x=712, y=356, width=80, height=80
                )
            ),
        ]
    )
               
        Barea = ImagemapSendMessage(
        base_url='https://imgur.com/-.jpg',
        alt_text='圖片',
        base_size=BaseSize(height=720, width=1280),     
        actions=[
            URIImagemapAction(
                link_uri='https://photos.app.goo.gl/-',
                area=ImagemapArea(
                    x=461, y=533, width=80, height=80
                )
            ),
            URIImagemapAction(
                link_uri='https://photos.app.goo.gl/-',
                area=ImagemapArea(
                    x=684, y=248, width=80, height=80
                )
            ),
            URIImagemapAction(
                link_uri='https://photos.app.goo.gl/-',
                area=ImagemapArea(
                    x=822, y=324, width=80, height=80
                )
            ),
        ]
    )
        
        Carea = ImagemapSendMessage(
        base_url='https://imgur.com/-.jpg',
        alt_text='圖片',
        base_size=BaseSize(height=720, width=1280),     
        actions=[
            URIImagemapAction(
                link_uri='https://photos.app.goo.gl/-',
                area=ImagemapArea(
                    x=834, y=464, width=80, height=80
                )
            ),
            URIImagemapAction(
                link_uri='https://photos.app.goo.gl/-',
                area=ImagemapArea(
                    x=569, y=117, width=80, height=80
                )
            ),
            URIImagemapAction(
                link_uri='https://photos.app.goo.gl/-',
                area=ImagemapArea(
                    x=397, y=307, width=80, height=80
                )
            ),
        ]
    )

        Darea = ImagemapSendMessage(
        base_url='https://imgur.com-.jpg',
        alt_text='圖片',
        base_size=BaseSize(height=720, width=1280),     
        actions=[
            URIImagemapAction(
                link_uri='https://photos.app.goo.gl/-',
                area=ImagemapArea(
                    x=383, y=436, width=80, height=80
                )
            ),
            URIImagemapAction(
                link_uri='https://photos.app.goo.gl/-',
                area=ImagemapArea(
                    x=654, y=154, width=80, height=80
                )
            ),
            URIImagemapAction(
                link_uri='https://photos.app.goo.gl/-',
                area=ImagemapArea(
                    x=818, y=295, width=80, height=80
                )
            ),
        ]
    )

        Earea = ImagemapSendMessage(
        base_url='https://imgur.com/-jpg',
        alt_text='圖片',
        base_size=BaseSize(height=720, width=1280),     
        actions=[
            URIImagemapAction(
                link_uri='https://photos.app.goo.gl/-',
                area=ImagemapArea(
                    x=786, y=505, width=80, height=80
                )
            ),
            URIImagemapAction(
                link_uri='https://photos.app.goo.gl/-',
                area=ImagemapArea(
                    x=635, y=54, width=80, height=80
                )
            ),
            URIImagemapAction(
                link_uri='https://photos.app.goo.gl/J-',
                area=ImagemapArea(
                    x=465, y=311, width=80, height=80
                )
            ),
        ]
    )

        Farea = ImagemapSendMessage(
        base_url='https://imgur.com/-.jpg',
        alt_text='圖片',
        base_size=BaseSize(height=720, width=1280),     
        actions=[
            URIImagemapAction(
                link_uri='https://photos.app.goo.gl/-',
                area=ImagemapArea(
                    x=779, y=82, width=80, height=80
                )
            ),
            URIImagemapAction(
                link_uri='https://photos.app.goo.gl/-',
                area=ImagemapArea(
                    x=576, y=296, width=80, height=80
                )
            ),
            URIImagemapAction(
                link_uri='https://photos.app.goo.gl/-',
                area=ImagemapArea(
                    x=449, y=236, width=80, height=80
                )
            ),
        ]
    )
  
        Garea = ImagemapSendMessage(
        base_url='https://imgur.com/-.jpg',
        alt_text='圖片',
        base_size=BaseSize(height=720, width=1280),     
        actions=[
            URIImagemapAction(
                link_uri='https://photos.app.goo.gl/-',
                area=ImagemapArea(
                    x=728, y=145, width=80, height=80
                )
            ),
            URIImagemapAction(
                link_uri='https://photos.app.goo.gl/-',
                area=ImagemapArea(
                    x=478, y=421, width=80, height=80
                )
            ),
            URIImagemapAction(
                link_uri='https://photos.app.goo.gl-',
                area=ImagemapArea(
                    x=328, y=264, width=80, height=80
                )
            ),
        ]
    )      

        Harea = ImagemapSendMessage(
        base_url='https://imgur.com/-.jpg',
        alt_text='圖片',
        base_size=BaseSize(height=720, width=1280),     
        actions=[
            URIImagemapAction(
                link_uri='https://photos.app.goo.gl/-',
                area=ImagemapArea(
                    x=471, y=152, width=80, height=80
                )
            ),
            URIImagemapAction(
                link_uri='https://photos.app.goo.gl-',
                area=ImagemapArea(
                    x=713, y=416, width=80, height=80
                )
            ),
            URIImagemapAction(
                link_uri='https://photos.app.goo.gl/-',
                area=ImagemapArea(
                    x=861, y=243, width=80, height=80
                )
            ),
        ]
    )     
        bouns_url = []
        bouns_url.append("-")
        bouns_url.append("-")
        bouns_random = random.randint(0,1)
           
        bouns = ImagemapSendMessage(
        base_url = 'https://imgur.com/-.jpg',
        alt_text='圖片',
        base_size=BaseSize(height=540, width=800),     
        actions=[
            URIImagemapAction(
                link_uri=bouns_url[bouns_random],
                area=ImagemapArea(
                    x=0, y=0, width=800, height=540
                )
            )
                     
        ]
    )

        if replymessage == "怡居標準層":
            line_bot_api.reply_message(
                event.reply_token,[
                    mainimage
            ])
        
        elif replymessage == "森山標準層":
            line_bot_api.reply_message(
                event.reply_token,[
                    sec_mainimage
            ])
        
        elif replymessage == "主圖":
            line_bot_api.reply_message(
                event.reply_token,[
                    mainimage
            ])
            
        elif replymessage == "怡居A區":
            line_bot_api.reply_message(
                event.reply_token,[
                    Aarea,
                    mainimagemenu
                ]
            )
        
        elif replymessage == "怡居B區":
            line_bot_api.reply_message(
                event.reply_token,[
                    Barea,
                    mainimagemenu
                ]
            )

        elif replymessage == "怡居C區":
            line_bot_api.reply_message(
                event.reply_token,[
                    Carea,
                    mainimagemenu
                ]
            )
            
        elif replymessage == "怡居D區":
            line_bot_api.reply_message(
                event.reply_token,[
                    Darea,
                    mainimagemenu
                ]
            )
            
        elif replymessage == "怡居E區":
            line_bot_api.reply_message(
                event.reply_token,[
                    Earea,
                    mainimagemenu
                ]
            )

        elif replymessage == "怡居F區":
            line_bot_api.reply_message(
                event.reply_token,[
                    Farea,
                    mainimagemenu
                ]
            )
            
        elif replymessage == "怡居G區":
            line_bot_api.reply_message(
                event.reply_token,[
                    Garea,
                    mainimagemenu
                ]
            )
            
        elif replymessage == "森山A區":
            line_bot_api.reply_message(
                event.reply_token,[
                    Aarea,
                    mainimagemenu
                ]
            )
    
        elif replymessage == "森山A區":
            line_bot_api.reply_message(
                event.reply_token,[
                    Aarea,
                    mainimagemenu
                ]
            )
            
        elif replymessage == "換選單":
            line_bot_api.link_rich_menu_to_user(user_id, "richmenu-02597e229bc07519300cea60aec3aec1")
        
        elif replymessage == "玩遊戲":     
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(
                    text="猜數字，範圍0-9，有四位數，沒有重複。")
                )

        elif replymessage == "內容更新": 
            if user_id == "U7a0c8d183579728cc7c1061b06db55e5" or user_id == "Uf0bc03258f4b309c5b7efa50fc8148ec" or user_id == "Ue49f885e71511044d7a1f622eb09da0f" or user_id == "U32463eb3450de04e9d95d0d2b67aa455" or profile.display_name == "Min":
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(
                        text=getupdate())
                    )
                    
            
        elif replymessage == "每日笑話":
            jokelist = []
            jokelist = getjoke()
            jokecount = len(jokelist)
            randomcount = random.randint(0,jokecount-1)
            if user_id == "U7a0c8d183579728cc7c1061b06db55e5" or user_id == "Uf0bc03258f4b309c5b7efa50fc8148ec" :
                line_bot_api.reply_message(
                    event.reply_token,[
                    TextSendMessage(
                        text=jokelist[randomcount]),
                    TextSendMessage(
                        text="傳笑話指令：a 笑話"),
                    ]
                    )
            else:
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(
                        text=jokelist[randomcount])                   
                    )
        
        
        elif str(replymessage).find("a") != -1:
            if user_id == "U7a0c8d183579728cc7c1061b06db55e5" or user_id == "Uf0bc03258f4b309c5b7efa50fc8148ec":
                try:
                    data_1, data_2 = str(replymessage).split('a ', 1)
                    check = str(data_2)
                except Exception as e:
                    pass

                try:
                    data_1, data_2 = str(replymessage).split('A ', 1)
                    check = str(data_2)
                except Exception as e:
                    pass
                print(check)
                try:
                    acheck=[]
                    acheck.append(check)
                    acheck.append(" ")
                    everydayjoke(acheck)
                    line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(
                            text="笑話網址：https://docs.google.com/-")
                    )
                except Exception as e:
                    print(e)
                    line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(
                            text="傳送失敗"
                    )
                    )
            else:
                line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(
                    text="選單",
                    quick_reply=QuickReply(
                        items=[
                            QuickReplyButton(action=MessageAction(
                                label="圖片", text="怡居標準層"))
                        ])))  
                
        elif replymessage == topic:
            randomtopic()
            line_bot_api.reply_message(
                event.reply_token,[
                    bouns
                ]
            )          

        else:            
            try:
                if int(echeckcode[0]) >= 100 and int(echeckcode[0]) <= 9999:
                    if isrepeat:
                        line_bot_api.reply_message(
                        event.reply_token,
                        TextSendMessage(
                                text="錯誤，有重複的數。")
                        )
                    else:
                        user_ans = list(str(echeckcode[0]))
                        print(topic_list[0:4])
                        for i in range(0,4):
                            if user_ans[i] == topic_list[i]:
                                a += 1
                                user_ans[i] = '-'
                        for i in range(0,4):
                            for j in range(0,4):
                                if topic_list[i] == user_ans[j]:
                                    b += 1       
                        reply = str(a) + "A" + str(b) + "B"
                        reply = reply + "\n" + "上次解出答案時間為：" + getdate()         
                        line_bot_api.reply_message(
                        event.reply_token,
                        TextSendMessage(
                                text=reply)
                        )
            except ValueError:
                line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(
                    text="選單",
                    quick_reply=QuickReply(
                        items=[
                            QuickReplyButton(action=MessageAction(
                                label="圖片", text="怡居標準層"))
                        ])))     
            

    
    static_tmp_path = "/app"
    reply_arr = []
    reply_arr.append(TextSendMessage('上傳成功'))
    reply_arr.append(TextSendMessage('相簿網址:https://imgur.com/a/-'))


        
    if isinstance(event.message, ImageMessage):
        ext = 'jpg'
        message_content = line_bot_api.get_message_content(event.message.id)
        with tempfile.NamedTemporaryFile(dir=static_tmp_path, prefix=ext + '-', delete=False) as tf:
            for chunk in message_content.iter_content():
                tf.write(chunk)
            tempfile_path = tf.name

        dist_path = tempfile_path + '.' + ext
        dist_name = os.path.basename(dist_path)
        os.rename(tempfile_path, dist_path)

        try:
            client = ImgurClient(client_id, client_secret,
                                 access_token, refresh_token)
            config = {
                'album': '5vg59Vz',
                'name': dist_name,
                'title': '',
                'description': ''
            }
            path = os.path.join(
                'static', '/app', dist_name)
            client.upload_from_path(path, config=config, anon=False)
            os.remove(path)
            print(path)
            line_bot_api.reply_message(
                event.reply_token,
                reply_arr)
        except Exception as e :
            print(e)
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage('上傳失敗'))
        return 0
    
def googlesheet(info):
    Json = 'googlesheet.json' # Json 的單引號內容請改成妳剛剛下載的那個金鑰
    Url = ['https://spreadsheets.google.com/feeds']
    Connect = SAC.from_json_keyfile_name(Json, Url)
    GoogleSheets = gspread.authorize(Connect)
    Sheet = GoogleSheets.open_by_key('-') # 這裡請輸入妳自己的試算表代號
    Sheets = Sheet.sheet1
    Sheets.append_row(info)

def everydayjoke(joke):
    Json = 'googlesheet.json' # Json 的單引號內容請改成妳剛剛下載的那個金鑰
    Url = ['https://spreadsheets.google.com/feeds']
    Connect = SAC.from_json_keyfile_name(Json, Url)
    GoogleSheets = gspread.authorize(Connect)
    Sheet = GoogleSheets.open_by_key('-') # 這裡請輸入妳自己的試算表代號
    Sheets = Sheet.sheet1
    Sheets.append_row(joke)
    
def gettopic():
    Json = 'googlesheet.json' # Json 的單引號內容請改成妳剛剛下載的那個金鑰
    Url = ['https://spreadsheets.google.com/feeds']
    Connect = SAC.from_json_keyfile_name(Json, Url)
    GoogleSheets = gspread.authorize(Connect)
    Sheet = GoogleSheets.open_by_key('-') # 這裡請輸入妳自己的試算表代號
    worksheet = Sheet.get_worksheet(0)
    topic = worksheet.acell('A1').value
    return topic

def getjoke():
    Json = 'googlesheet.json' # Json 的單引號內容請改成妳剛剛下載的那個金鑰
    Url = ['https://spreadsheets.google.com/feeds']
    Connect = SAC.from_json_keyfile_name(Json, Url)
    GoogleSheets = gspread.authorize(Connect)
    Sheet = GoogleSheets.open_by_key('-') # 這裡請輸入妳自己的試算表代號
    worksheet = Sheet.get_worksheet(0)
    joke = worksheet.col_values(1)
    return joke   

def getdate():
    Json = 'googlesheet.json' # Json 的單引號內容請改成妳剛剛下載的那個金鑰
    Url = ['https://spreadsheets.google.com/feeds']
    Connect = SAC.from_json_keyfile_name(Json, Url)
    GoogleSheets = gspread.authorize(Connect)
    Sheet = GoogleSheets.open_by_key('-') # 這裡請輸入妳自己的試算表代號
    worksheet = Sheet.get_worksheet(0)
    topic = worksheet.acell('B1').value
    return topic

def getupdate():
    Json = 'googlesheet.json' # Json 的單引號內容請改成妳剛剛下載的那個金鑰
    Url = ['https://spreadsheets.google.com/feeds']
    Connect = SAC.from_json_keyfile_name(Json, Url)
    GoogleSheets = gspread.authorize(Connect)
    Sheet = GoogleSheets.open_by_key('-') # 這裡請輸入妳自己的試算表代號
    worksheet = Sheet.get_worksheet(0)
    data = worksheet.acell('A1').value
    return data  
def randomtopic():
    the_time = time.strftime("%b %d %a %H:%M:%S %Y", time.localtime()) 
    Json = 'googlesheet.json' # Json 的單引號內容請改成妳剛剛下載的那個金鑰
    Url = ['https://spreadsheets.google.com/feeds']
    Connect = SAC.from_json_keyfile_name(Json, Url)
    GoogleSheets = gspread.authorize(Connect)
    Sheet = GoogleSheets.open_by_key('-') # 這裡請輸入妳自己的試算表代號
    worksheet = Sheet.get_worksheet(0)
    topic = random.sample(range(0,9),4)
    topic1 = ""
    for i in range(0,4):
        topic1 += str(topic[i])
    worksheet.update('A1',topic1)
    worksheet.update('B1',the_time)
    
@handler.add(PostbackEvent)
def handle_postback(event):
    # postback 資料
    data = event.postback.data
    # 使用者Id
    userId = event.source.user_id
    
    # 下一頁
    if data == "action=next":
        # 設定個別用戶選單
        line_bot_api.link_rich_menu_to_user(userId, "richmenu-8575b75c318836e256a903deb0b1528d")
    # 上一頁
    elif data == "action=prev":
        # 移除個別用戶選單
        line_bot_api.unlink_rich_menu_from_user(userId) 
    
if __name__ == "__main__":
    app.run()
