#架設伺服器 flask,django
from flask import Flask,request,abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,StickerSendMessage
)

app = Flask(__name__)

line_bot_api = LineBotApi('E68XVebCPS60dBwxcjZMHPcYqJqt1urcTW536V0hXvLYrF0jwzW+rl7wWDIjPCCUAit4WzvgUcMsX95flGdZJgYn2MouWogTxIUeWYzvY9GI1ONgNGx36Xt/09KMdog/U7egn3C9FMpjEokQggYzHAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('a35284b8765b0de831848672e14c2a62')


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
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    r = '我不太懂你在說甚麼，但是應該在誇獎曼很美吧^___^'

    if '生氣' in msg:
        sticker_message = StickerSendMessage(
            package_id='2',
            sticker_id='23'
        )
        line_bot_api.reply_message(
        event.reply_token,
        sticker_message)
        return

    if msg in ['hi','HI','Hi','你好'] :
        r = 'Hello!'
    elif msg =='你吃飯了嗎':
        r = '還沒>////<'
    elif msg == '我愛你':
        r = '我更愛你!!!'
    elif '什麼' in msg:
        r = '我在想你'
    elif '曼' in msg:
        r = '對阿曼很漂亮!'

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))


if __name__ == "__main__":
    app.run()