# ---------------------------------------------------
# File Name: init.py
# Author: NeonAnurag
# GitHub: https://github.com/MyselfNeon/
# Telegram: https://t.me/MyelfNeon
# Created: 2025-11-21
# Last Modified: 2025-11-22
# Version: Latest
# License: MIT License
# ---------------------------------------------------

from aiohttp import web
from .stream_routes import routes

def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(routes)
    return web_app


# MyselfNeon
# Don't Remove Credit 🥺
# Telegram Channel @NeonFiles