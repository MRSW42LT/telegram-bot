from telebot import *
from dolar import cotar_dolar
from constants import API_KEY

app = telebot.TeleBot(API_KEY)

@app.inline_handler(lambda query: query.query == 'dolar')
def dolar_query(inline_query):
    r = types.InlineQueryResultArticle(
        # The id of our inline result
        id='1',
        title='dolar',
        input_message_content=types.InputTextMessageContent(
        cotar_dolar()
        )
    )
    app.answer_inline_query(inline_query.id, [r])

@app.inline_handler(lambda query: query.query == 'help')
def help_query(inline_query):
    r = types.InlineQueryResultArticle(
        # The id of our inline result
        id='2',
        title='help',
        input_message_content=types.InputTextMessageContent(
            'Por favor, leia as instruções em https://denis.software/'
        )
    )
    app.answer_inline_query(inline_query.id, [r])

app.polling(True)