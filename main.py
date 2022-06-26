#!/usr/bin/env python
# pylint: disable=unused-argument, wrong-import-position
# This program is dedicated to the public domain under the CC0 license.

"""
Don't forget to enable inline mode with @BotFather

First, a few handler functions are defined. Then, those functions are passed to
the Application and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic inline bot example. Applies different text transformations.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""
import logging
from html import escape
from uuid import uuid4
from telegram import InlineQueryResultArticle, InputTextMessageContent, Update
from telegram.constants import ParseMode
from telegram.ext import Application, CommandHandler, ContextTypes, InlineQueryHandler
from constants import API_KEY

from dolar import cotar_dolar
from climate import get_climate

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context.
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    await update.message.reply_text("Hi!")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Help!")

async def dolar_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /dolar is issued."""
    await update.message.reply_text(cotar_dolar())

async def tempo_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    city = " ".join(context.args)
    await update.message.reply_text(get_climate(city))


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
                    'ajuda', parse_mode=ParseMode.HTML
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
                    f'\n Used the command {query} \n\n{get_climate(data)}'
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

    # on non command i.e message - echo the message on Telegram
    application.add_handler(InlineQueryHandler(inline_query))

    # Run the bot until the user presses Ctrl-C
    application.run_polling()


if __name__ == "__main__":
    main()