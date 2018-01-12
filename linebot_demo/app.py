from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

#import pandas as pd

app = Flask(__name__)

line_bot_api = LineBotApi('IJlBFSC+WIrj3Ki+//TGjuz6buq0hW6AsfLzvWer0+LtcLXREgx73Kz/7MXnnADu2u5rpykWjYj/yMODFDsHINay+ZgiI6MRFHn+36cKMIfDn+dl4zlScsKM1bJ1QVun2lleXhkKgrgXtaT2d5d8FgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('acb6bb2d30f775a13dfc5b2a84f35ad0')

#url = "talk.csv"
#talk_csv = pd.read_csv(url)

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


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    #filter = talk_csv["message"] == event.message.text
    #new_df = talk_csv[filter]
    #get_messageBOT = new_df.ix[:,1]
    #reply_messageBOT = new_df.ix[:,2]

    if event.message.text == "台灣":
        content = "一個國家"
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content)
        )
        return 0
        
    if event.message.text == "俄羅斯":
        buttons_template = TemplateSendMessage(
            alt_text='俄羅斯 template',
            template=ButtonsTemplate(
                title='俄羅斯',
                text='請選擇',
                thumbnail_image_url='https://i.imgur.com/XdaNACs.jpg',
                actions=[
                    URITemplateAction(
                        label='伊爾庫茨克',
                        uri = 'https://www.flickr.com/photos/ycsung/albums/72157685740118473'
                    ),
                    URITemplateAction(
                        label='貝加爾湖',
                        uri='https://www.flickr.com/photos/ycsung/albums/72157688149531465'
                    ),
                    URITemplateAction(
                        label='斯柳江卡',
                        uri='https://www.flickr.com/photos/ycsung/albums/72157685739140593'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template)
        return 0

    if event.message.text == "蒙古":
        buttons_template = TemplateSendMessage(
            alt_text='蒙古 template',
            template=ButtonsTemplate(
                title='蒙古',
                text='請選擇',
                thumbnail_image_url='https://i.imgur.com/9sF0hkS.jpg',
                actions=[
                    URITemplateAction(
                        label='Day 1',
                        uri='https://www.flickr.com/photos/ycsung/albums/72157685528935100'
                    ),
                    URITemplateAction(
                        label='Day 2',
                        uri='https://www.flickr.com/photos/ycsung/albums/72157685704399403'
                    ),
                    URITemplateAction(
                        label ='Day 3',
                        uri = 'https://www.flickr.com/photos/ycsung/albums/72157685707045943'

                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template)
        return 0

    if event.message.text == "西伯利亞鐵路":
        buttons_template = TemplateSendMessage(
            alt_text='西伯利亞鐵路 template',
            template=ButtonsTemplate(
                title='西伯利亞鐵路',
                text='請選擇',
                thumbnail_image_url='https://i.imgur.com/fJbzG4N.jpg',
                actions=[
                    URITemplateAction(
                        label='Ulaanbaatar',
                        uri='https://www.flickr.com/photos/ycsung/albums/72157688118311475'
                    ),
                    URITemplateAction(
                        label='Sukhebator',
                        uri='https://www.flickr.com/photos/ycsung/albums/72157685546784960'
                    ),
                    URITemplateAction(
                        label ='Naushki',
                        uri = 'https://www.flickr.com/photos/ycsung/albums/72157685735316603'

                    ),
                    URITemplateAction(
                        label='Ulan-Ude',
                        uri='https://www.flickr.com/photos/ycsung/albums/72157685647987224'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template)
        return 0

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text+" （嗚嗚嗚 聽不懂～）"))


if __name__ == "__main__":
    app.run()




