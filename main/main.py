import logging
from utils.config import TOKEN
from utils.swap_language import swp_lng
from utils.youtube_downloader import yt_download
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hello, its my simple bot for translate english letters '
                              'into russian, for example ghbdtn in привет')


def help_command(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Just enter your wrong message and bot will fix everything')


def swap(update, context):
    """translate english letters into russian or russian into english"""
    update.message.reply_text(swp_lng(update.message.text))


def yt(update, context):
    url = update.message.text[4:].rstrip()
    yt_download(url)
    video = open('video.mp4', 'rb')
    update.message.reply_video(video)


def main():
    """Start the bot."""
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("yt", yt))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, swap))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
