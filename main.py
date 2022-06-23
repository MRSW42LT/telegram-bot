from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import Constants as keys
import Responses as R

print ('bot started')

def start_command(update):
    update.message.reply_text('digite algo para iniciar')

def help_command(update):
    update.message.reply_text('just read the instructions https://denis.software/')

def handle_message(update):
    text = str(update.message.text).lower()
    response = R.sample_responses(text)
    update.message.reply_text(response)

def error(update):
    print(f"Update {update} caused error {error}")

def main():

    updater = Updater(keys.API_KEY)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start_command))
    dispatcher.add_handler(CommandHandler("start", help_command))

    dispatcher.add_handler(MessageHandler(Filters.text, handle_message))

    dispatcher.add_error_handler(error)

    updater.start_polling(1) # refresh a cada 1 segundo, 0 = instantâneo

main()
