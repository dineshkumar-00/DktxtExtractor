#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    API_ID = int(os.environ.get("API_ID", "22124800"))
    API_HASH = os.environ.get("API_HASH", "d8daf7c470e7bbe2d8481d0e20901e0f")
    AUTH_USERS = os.environ.get("AUTH_USERS", "")
