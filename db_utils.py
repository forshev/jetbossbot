# -*- coding: utf-8 -*-
from vedis import Vedis
import config


def get_state(user_id):
    with Vedis(config.db_file) as db:
        try:
            return db[user_id]
        except KeyError:
            return config.Statuses.S_START.value


def set_state(user_id, value):
    with Vedis(config.db_file) as db:
        try:
            db[user_id] = value
            return True
        except:
            return False
