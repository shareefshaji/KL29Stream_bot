import os

class temp(object):
    BOT = None

API_ID = int(os.getenv('27549502'))
API_HASH = os.getenv('35892287036e27af8e9298f03483fdd4')
BOT_TOKEN = os.getenv('7791848217:AAFQwEBFcp8IPVHx4hH1Cza1fCGYP2fz8nY')

PORT = int(os.getenv('PORT', 8080))
BIN_CHANNEL = int(os.getenv("-1002757225573"))
STREAM_URL = os.getenv("https://beestream.in")
