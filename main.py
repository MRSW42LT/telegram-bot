import logging
from html import escape
from uuid import uuid4
from telegram import InlineQueryResultArticle, InputTextMessageContent, Update
from telegram.constants import ParseMode
from telegram.ext import Application, CommandHandler, ContextTypes, InlineQueryHandler
from constants import API_KEY

from Functions.finance.dolar import cotar_dolar
#from Functions.finance.stocks import getStockClose
from Functions.finance.stocks import stock
from Functions.geography.climate import get_climate

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context.
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    await update.message.reply_text("Hi! Read the instructions on our website. https://denis.software/")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Help! Hi! Read the instructions on our website. https://denis.software/")

async def dolar_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /dolar is issued."""
    await update.message.reply_text(cotar_dolar())

async def tempo_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    city = " ".join(context.args)
    await update.message.reply_text(get_climate(city))

async def stock_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    company = " ".join(context.args)
    await update.message.reply_text(stock(company))
    if await update.message.reply_photo(photo=open('historyData.png', 'rb')):
        import os
        os.remove("historyData.png") 


async def inline_query(update: Update, context) -> None:
    """Handle the inline query. This is run when you type: @botusername <query>"""
    query = update.inline_query.query
    data = update.inline_query.query.replace('/tempo', '')

    if query == "":
        return

    if query == "/help":
        results = [
            InlineQueryResultArticle(
                id=str(uuid4()),
                title="help",
                input_message_content=InputTextMessageContent(
                    'Hi! Read the instructions on our website. https://denis.software/', parse_mode=ParseMode.HTML
                ),
            ),
        ]
        return await update.inline_query.answer(results)

    if query == "/dolar":
        results = [
            InlineQueryResultArticle(
                id=str(uuid4()),
                title="dolar",
                input_message_content=InputTextMessageContent(
                    cotar_dolar(), parse_mode=ParseMode.HTML
                ),
            ),
        ]
        return await update.inline_query.answer(results)

    if "/tempo" in query:
        results = [
            InlineQueryResultArticle(
                id=str(uuid4()),
                title="tempo agora",
                input_message_content=InputTextMessageContent(
                    f'<i>\n Used the command </i> {query} {get_climate(data)}' , parse_mode=ParseMode.HTML
                ),
            ),
        ]
        return await update.inline_query.answer(results)


def main() -> None:
    """Run the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(API_KEY).build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("dolar", dolar_command))
    application.add_handler(CommandHandler("tempo", tempo_command))
    application.add_handler(CommandHandler("stock", stock_command))

    # on non command i.e message - echo the message on Telegram
    application.add_handler(InlineQueryHandler(inline_query))

    # Run the bot until the user presses Ctrl-C
    application.run_polling()


if __name__ == "__main__":
    main()