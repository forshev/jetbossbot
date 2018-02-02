# -*- coding: utf-8 -*-
from telebot import types


def init_keyboard():
    markup = types.ReplyKeyboardMarkup()

    markup.add('/came')
    markup.add('/left')

    return markup
