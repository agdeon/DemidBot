import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import os
import time

from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_message_id = message.message_id
    bot.send_message(chat_id=message.chat.id,
                     text="Привет! Я тестовый бот. Вы только что ввели команду /start",
                     reply_to_message_id=user_message_id)


bot.infinity_polling()