# -*- coding: utf-8 -*-
import config
import telebot

from datetime import datetime
from messages import *
from utils import *


bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start'])
def start_handler(message):
    markup = init_keyboard()
    reply = start_message

    bot.send_message(message.chat.id, reply, reply_markup=markup)


@bot.message_handler(commands=['help'])
def help_handler(message):
    bot.send_message(message.chat.id, help_message)


@bot.message_handler(commands=['came', 'left'])
def came_left_handler(message):
    full_name = '{} {}'.format(
        message.chat.first_name,
        message.chat.last_name
    )
    time = datetime.fromtimestamp(
        message.date
    ).strftime('%H:%M')

    if message.text == '/came':
        reply = came_message.format(full_name, time)
    elif message.text == '/left':
        reply = left_message.format(full_name, time)

    bot.send_message(message.chat.id, reply)


@bot.message_handler(commands=['location'])
def request_location(message):
    markup = location_keyboard()

    bot.send_message(
        message.chat.id,
        "Поделись местоположением",
        reply_markup=markup)

    bot.register_next_step_handler(message, location_handler)


@bot.message_handler(content_types=['location'])
def location_handler(message):
    lat = message.location.latitude
    lon = message.location.longitude

    print(lat, lon)


if __name__ == '__main__':
    print('Bot is running...')
    bot.polling(none_stop=True)
