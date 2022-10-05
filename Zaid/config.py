##Config
import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


load_dotenv()
SESSION_NAME = getenv('SESSION_NAME', 'session')
BOT_TOKEN = getenv('BOT_TOKEN')
API_ID = int(getenv("API_ID", "6435225"))
API_HASH = getenv('API_HASH')
DURATION_LIMIT = int(getenv('DURATION_LIMIT', '540000'))
COMMAND_PREFIXES = list(getenv('COMMAND_PREFIXES', '/ !').split())
MONGO_DB_URI = getenv("MONGO_DB_URI")
SUDO_USERS = list(map(int, getenv('SUDO_USERS', '').split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", '-1001688479760'))
ASS_ID = int(getenv("ASS_ID", '1906953793'))
OWNER_ID = list(map(int, getenv('OWNER_ID', '').split()))
RESULT_PIC = getenv('RESULT_PIC', "https://telegra.ph/file/b35352e7a52281cbf37c7.jpg")
PLAYLIST_PIC = getenv('PLAYLIST_PIC', "https://telegra.ph/file/b35352e7a52281cbf37c7.jpg")
PING_IMG = getenv('PING_IMG', "https://telegra.ph/file/0ec6b20ad4d2ea8da601d.jpg")
