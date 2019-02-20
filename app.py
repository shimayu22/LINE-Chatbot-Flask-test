from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, 
    ImageMessage,ImageSendMessage,BaseSize,ImagemapArea,
    MessageImagemapAction,TemplateSendMessage,ButtonsTemplate,
    URIAction,ImagemapSendMessage,URIImagemapAction
)
import os

app = Flask(__name__)

#環境変数取得
YOUR_CHANNEL_ACCESS_TOKEN = os.environ["YOUR_CHANNEL_ACCESS_TOKEN"]
YOUR_CHANNEL_SECRET = os.environ["YOUR_CHANNEL_SECRET"]

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)

def make_image_message():
    messages = ImageSendMessage(
        original_content_url="https://www.shimay.uno/nekoguruma/wp-content/uploads/sites/2/2018/03/20171124_194201-508x339.jpg",
        preview_image_url="https://www.shimay.uno/nekoguruma/wp-content/uploads/sites/2/2018/03/20171124_194201-508x339.jpg"
    )
    return messages

def make_imagemap_message():
    messages = ImagemapSendMessage(
        base_url='https://www.shimay.uno/nekoguruma/wp-content/uploads/',
        alt_text='ブログも見てね！',
        base_size=BaseSize(width=508,height=339),
        actions=[
            URIImagemapAction(
                link_uri='https://www.shimay.uno/nekoguruma/archives/620',
                area=ImagemapArea(
                    x=0,y=0,width=508,height=339
                )
            )
        ]
    )
    return messages

def make_button_template():
    message_template = ButtonsTemplate(
        text="どこに表示されるかな？",
        title="タイトルですよ",
        thumbnail_image_url="https://www.shimay.uno/nekoguruma/wp-content/uploads/sites/2/2018/03/20171124_194201-508x339.jpg",
        actions=[
            URIAction(
                link_uri='https://www.shimay.uno/nekoguruma/archives/620',
                label='LABEL'
            )
        ]
    )
    return message_template


@app.route("/")
def hello_world():
    return "hello world!"


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


@handler.add(MessageEvent, message=(TextMessage))
def handle_image_message(event):
    messages = make_button_template()
    line_bot_api.reply_message(
        event.reply_token,
        [
            messages,
            TextSendMessage(text="https://www.shimay.uno/nekoguruma/archives/620")
        ]
    )


if __name__ == "__main__":
#    app.run()
    port = int(os.getenv("PORT",5000))
    app.run(host="0.0.0.0", port=port)