# -*- coding: utf-8 -*-
import config
import telebot
import time

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
    try:
        full_name = '{} {}'.format(
            message.chat.first_name,
            message.chat.last_name
        )
        time = datetime.fromtimestamp(
            message.date
        ).strftime('%H:%M')
    except Exception as e:
        print(e)

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
    try:
        lat = message.location.latitude
        lon = message.location.longitude

        print(lat, lon)
    except Exception as e:
        print(e)


@bot.message_handler(commands=['late'])
def late_handler(message):
    markup = cancel_keyboard()
    reply = late_message

    bot.send_message(message.chat.id, reply, reply_markup=markup)


@bot.message_handler(commands=['timeoff'])
def timeoff_handler(message):
    markup = cancel_keyboard()
    reply = timeoff_message

    bot.send_message(message.chat.id, reply, reply_markup=markup)


def main_loop():
    bot.polling(none_stop=True)
    while 1:
        time.sleep(3)


if __name__ == '__main__':
    try:
        print('Bot is running...')
        main_loop()
    except KeyboardInterrupt:
        print('\nExiting by user request.')
