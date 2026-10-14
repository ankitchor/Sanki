© @MuskanBot

import os
import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

=========================================================

TELEGRAM CONFIGURATION

=========================================================

API_ID = int(getenv("API_ID", "0"))
API_HASH = getenv("API_HASH", "")
BOT_TOKEN = getenv("BOT_TOKEN", "")

=========================================================

DATABASE

=========================================================

MONGO_DB_URI = getenv("MONGO_DB_URI", None)

=========================================================

DURATION

=========================================================

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "900"))

=========================================================

LOGGER / OWNER

=========================================================

_logger_id_raw = getenv("LOGGER_ID", "0").strip()
LOGGER_ID = (
int(_logger_id_raw)
if _logger_id_raw.lstrip("-").isdigit()
else 0
)

OWNER_ID = int(getenv("OWNER_ID", "0"))

=========================================================

START VERIFICATION GROUP

=========================================================

REQUIRED_START_GROUP_ID = int(
getenv("REQUIRED_START_GROUP_ID", "-1003961210499")
)

=========================================================

HEROKU CONFIGURATION

=========================================================

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)

=========================================================

UPSTREAM REPOSITORY

=========================================================

UPSTREAM_REPO = getenv(
"UPSTREAM_REPO",
"https://github.com/ankitchor/Sanki",
)

UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "jani")

GIT_TOKEN = getenv("GIT_TOKEN", None)

=========================================================

SUPPORT

=========================================================

SUPPORT_CHANNEL = getenv(
"SUPPORT_CHANNEL",
"https://t.me/ytnaisha",
)

SUPPORT_CHAT = getenv(
"SUPPORT_CHAT",
"https://t.me/+T_5EDypRXsU3YTU1",
)

=========================================================

SHRUTI API

=========================================================

API_URL = getenv(
"SHRUTI_API_URL",
"https://api.shrutibots.site",
)

API_KEY = getenv(
"SHRUTI_API_KEY",
"ShrutiBotsBRZ3aFj841W6qHqPqGtS",
)

=========================================================

ASSISTANT SETTINGS

=========================================================

def get_bool_env(name, default=False):
value = getenv(name)

if value is None:
    return default

return value.lower() in (
    "true",
    "1",
    "yes",
    "on",
)

AUTO_LEAVING_ASSISTANT = get_bool_env(
"AUTO_LEAVING_ASSISTANT",
False,
)

=========================================================

SPOTIFY

=========================================================

SPOTIFY_CLIENT_ID = getenv(
"SPOTIFY_CLIENT_ID",
None,
)

SPOTIFY_CLIENT_SECRET = getenv(
"SPOTIFY_CLIENT_SECRET",
None,
)

=========================================================

PLAYLIST

=========================================================

PLAYLIST_FETCH_LIMIT = int(
getenv(
"PLAYLIST_FETCH_LIMIT",
"25",
)
)

=========================================================

TELEGRAM FILE SIZE LIMIT

=========================================================

TG_AUDIO_FILESIZE_LIMIT = int(
getenv(
"TG_AUDIO_FILESIZE_LIMIT",
"104857600",
)
)

TG_VIDEO_FILESIZE_LIMIT = int(
getenv(
"TG_VIDEO_FILESIZE_LIMIT",
"1073741824",
)
)

=========================================================

STRING SESSIONS

Assistant sessions disabled in this config

=========================================================

STRING1 = ""
STRING2 = ""
STRING3 = ""
STRING4 = ""
STRING5 = ""

=========================================================

BANNED USERS

=========================================================

BANNED_USERS = filters.user()

=========================================================

GLOBAL VARIABLES

=========================================================

adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

=========================================================

IMAGE URLS

=========================================================

START_IMG_URL = getenv(
"START_IMG_URL",
"https://image-link.edgeone.app/1791892945910-j7696s.jpg",
)

PING_IMG_URL = getenv(
"PING_IMG_URL",
"https://image-link.edgeone.app/1791892945910-j7696s.jpg",
)

PLAYLIST_IMG_URL = "https://litter.catbox.moe/a9oxfp.jpg"
STATS_IMG_URL = "https://telegra.ph/file/d30d11c4365c025c25e3e.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/c832e84cd991c865c7e4f.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/e575ae40d6635250974e1.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/03efec694e41e891b29dc.jpg"
IQ_Proxy = "https://i.ytimg.com/vi"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/d723f4c80da157fca1678.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/4dc854f961cd3ce46899b.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/d723f4c80da157fca1678.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/6c741a6bc1e1663ac96fc.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/6c741a6bc1e1663ac96fc.jpg"

=========================================================

TIME CONVERSION

=========================================================

def time_to_seconds(time):
stringt = str(time)

return sum(
    int(x) * 60 ** i
    for i, x in enumerate(
        reversed(stringt.split(":"))
    )
)

DURATION_LIMIT = int(
time_to_seconds(
f"{DURATION_LIMIT_MIN}:00"
)
)

=========================================================

URL VALIDATION

=========================================================

if SUPPORT_CHANNEL:
if not re.match(
r"^(?:http|https)://",
SUPPORT_CHANNEL,
):
raise SystemExit(
"[ERROR] - Your SUPPORT_CHANNEL URL is wrong. "
"Please ensure that it starts with https://"
)

if SUPPORT_CHAT:
if not re.match(
r"^(?:http|https)://",
SUPPORT_CHAT,
):
raise SystemExit(
"[ERROR] - Your SUPPORT_CHAT URL is wrong. "
"Please ensure that it starts with https://"
)

all = ["IQ_Proxy"]
