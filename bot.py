# -*- coding: utf-8 -*-
import config
import telebot

from datetime import datetime
from messages import *
from utils import init_keyboard


bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=["start"])
def start_handler(message):
    markup = init_keyboard()
    reply = start_message

    bot.send_message(message.chat.id, reply, reply_markup=markup)


@bot.message_handler(commands=["came"])
def came_handler(message):
    full_name = '{} {}'.format(
        message.chat.first_name,
        message.chat.last_name
    )
    time = datetime.fromtimestamp(
        message.date
    ).strftime('%H:%M')
    reply = came_message.format(full_name, time)

    bot.send_message(message.chat.id, reply)


if __name__ == '__main__':
    print("Bot is running...")
    bot.polling(none_stop=True)
