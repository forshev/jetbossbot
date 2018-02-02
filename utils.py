# -*- coding: utf-8 -*-
from telebot import types


def init_keyboard():
    markup = types.ReplyKeyboardMarkup(
        row_width=1, resize_keyboard=True
    )

    markup.add('/came')
    markup.add('/left')
    markup.add('/location')

    return markup


def location_keyboard():
    markup = types.ReplyKeyboardMarkup(
        row_width=1, resize_keyboard=True
    )
    location_button = types.KeyboardButton(
        text="Отправить местоположение",
        request_location=True
    )

    markup.add(location_button)

    return markup
