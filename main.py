"""Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

from distutils.log import debug
import logging
import string
from turtle import update
from telegram import Update
import cv2 , numpy as np
from src.core.init import Effects

Vfx = Effects()

def visualEffects (img_src : str , img_dst : str , effects : str) -> None :

    img = cv2.imread(img_src,1)
    arr = np.asarray(img)
    img = Vfx.Make(arr,effects)
    #cv2.imshow("Cute Kitens", img)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    return img 


from telegram.ext import Updater, CommandHandler, MessageHandler, Filters , CallbackContext

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Bienvenue sur NotAboT ! pour vous montrez les effets de NotAboT , envoyer une photo de vous-même')


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(update: Update, context: CallbackContext) -> None : 
    """Echo the user message."""
    update.message.reply_text(update.message.text)
    print(update.message)


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def photo(update : Update, context  : CallbackContext) -> None :
    fileDir : string = getFileDir(update.message.photo[-1].file_id , 'jpg')
    rended_ext  = "bitx"
    update.message.reply_text('calcule en cours ! veillez patientez ...')
    print(update.message)

    #dowload image with telegram id
    update.message.photo[-1].get_file().download(fileDir)
    img = visualEffects(fileDir,fileDir,'anime')
    cv2.imwrite(fileDir,img)
    update.message.reply_photo(photo=open(fileDir, 'rb'))

def getFileDir( fileName : str , extention : str  = 'jpg') -> None :
    filesRootFolder : str = "./files/"
    fileDir= filesRootFolder + fileName + '.' + extention
    debug(fileDir)
    return fileDir

def main():
    """Start the bot."""
    Token  : str  = "5199877367:AAHWzYIp00nXufPZa_hfell1U6iT29OV6yw"
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(Token, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram
    #dp.add_handler(MessageHandler(Filters.text, echo))

    #dp use photo
    dp.add_handler(MessageHandler(Filters.photo, photo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()