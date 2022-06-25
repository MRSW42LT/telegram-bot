from telebot import *
from dolar import cotar_dolar
from constants import API_KEY

app = TeleBot(__name__)

@app.inline_handler(lambda query: query.query == 'dolar')
def test(inline_query):
    r = types.InlineQueryResultArticle(
        # The id of our inline result
        id='1',
        title='dolar',
        input_message_content=types.InputTextMessageContent(
        cotar_dolar()
        )
    )
    app.answer_inline_query(inline_query.id, [r])


@app.inline_handler(lambda query: query.query == 'image')
def image(inline_query):
    r = types.InlineQueryResultPhoto(
        id='11',
        photo_url='https://images.assettype.com/swarajya/2020-08/a46bd36a-e65b-4b0b-91d9-c0fcac98c518/telegram.jpg?w=1200&h=800',
        thumb_url='https://images.assettype.com/swarajya/2020-08/a46bd36a-e65b-4b0b-91d9-c0fcac98c518/telegram.jpg?w=1200&h=800'
    )

    app.answer_inline_query(inline_query.id, [r])


if __name__ == '__main__':
    app = telebot.TeleBot(API_KEY)
    app.polling(True)