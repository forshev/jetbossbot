# -*- coding: utf-8 -*-
from enum import Enum


class Statuses(Enum):
    START = "start"
    CAME = "came"
    LEFT = "left"
    LATE = "late"
    CONFIRM_LATE = "confirm_late"
