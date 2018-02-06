# -*- coding: utf-8 -*-
from telebot import types


def init_keyboard():
    markup = types.ReplyKeyboardMarkup(
        row_width=1, resize_keyboard=True
    )

    commands = ['/came', '/left', '/late',
                '/timeoff', '/location']

    markup.add(*commands)

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


def cancel_keyboard():
    markup = types.InlineKeyboardMarkup()
    cancel_button = types.InlineKeyboardButton(
        text="Отмена",
        callback_data='cancel'
    )

    markup.add(cancel_button)

    return markup


def yes_no_keyboard():
    markup = types.InlineKeyboardMarkup()
    yes_button = types.InlineKeyboardButton(
        text="Да",
        callback_data='Yes'
    )
    no_button = types.InlineKeyboardButton(
        text="Нет",
        callback_data='No'
    )

    markup.add(yes_button)
    markup.add(no_button)

    return markup
