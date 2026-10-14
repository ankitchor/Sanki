# © @MuskanBot

import os
import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()


# =========================================================
# TELEGRAM CONFIGURATION
# =========================================================

# Get these values from https://my.telegram.org/apps
API_ID = int(getenv("API_ID", "0"))
API_HASH = getenv("API_HASH")

# Get your bot token from @BotFather
BOT_TOKEN = getenv("BOT_TOKEN")


# =========================================================
# DATABASE
# =========================================================

# Get your MongoDB URL from MongoDB Atlas
MONGO_DB_URI = getenv("MONGO_DB_URI", None)


# =========================================================
# DURATION
# =========================================================

# Duration limit in minutes
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "900"))


# =========================================================
# LOGGER / OWNER
# =========================================================

# Telegram group/channel ID for logging
LOGGER_ID = int(getenv("LOGGER_ID", "0"))

# Telegram user ID of bot owner
OWNER_ID = int(getenv("OWNER_ID", "0"))


# =========================================================
# START VERIFICATION GROUP
# =========================================================

# जिस Group में नए Member को पहले Bot START करना होगा
#
# Railway/Heroku Variables में:
#
# REQUIRED_START_GROUP_ID = -1003961210499
#
# यहाँ अपने उस Chat Group की ID डालें।
# LOGGER_ID की ID यहाँ नहीं डालनी है।
# =========================================================

REQUIRED_START_GROUP_ID = int(
    getenv("REQUIRED_START_GROUP_ID", "-1003961210499")
)


# =========================================================
# HEROKU CONFIGURATION
# =========================================================

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)

HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)


# =========================================================
# UPSTREAM REPOSITORY
# =========================================================

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/ankitchor/Sanki",
)

UPSTREAM_BRANCH = getenv(
    "UPSTREAM_BRANCH",
    "jani",
)

GIT_TOKEN = getenv(
    "GIT_TOKEN",
    None,
)


# =========================================================
# SUPPORT
# =========================================================

SUPPORT_CHANNEL = getenv(
    "SUPPORT_CHANNEL",
    "https://t.me/KRISHNA_MUSIC_WORLDS",
)

SUPPORT_CHAT = getenv(
    "SUPPORT_CHAT",
    "https://t.me/+D-zpgKEMbes2ZWZl",
)


# =========================================================
# SHRUTI API
# =========================================================

# You can also set these from Heroku Config Vars:
# SHRUTI_API_URL
# SHRUTI_API_KEY

API_URL = getenv(
    "SHRUTI_API_URL",
    "https://api.shrutibots.site",
)

API_KEY = getenv(
    "SHRUTI_API_KEY",
    "ShrutiBotsBRZ3aFj841W6qHqPqGtS",
)


# =========================================================
# ASSISTANT SETTINGS
# =========================================================

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


# =========================================================
# SPOTIFY
# =========================================================

SPOTIFY_CLIENT_ID = getenv(
    "SPOTIFY_CLIENT_ID",
    None,
)

SPOTIFY_CLIENT_SECRET = getenv(
    "SPOTIFY_CLIENT_SECRET",
    None,
)


# =========================================================
# PLAYLIST
# =========================================================

PLAYLIST_FETCH_LIMIT = int(
    getenv(
        "PLAYLIST_FETCH_LIMIT",
        "25",
    )
)


# =========================================================
# TELEGRAM FILE SIZE LIMIT
# =========================================================

# Audio file size limit in bytes
TG_AUDIO_FILESIZE_LIMIT = int(
    getenv(
        "TG_AUDIO_FILESIZE_LIMIT",
        "104857600",
    )
)

# Video file size limit in bytes
TG_VIDEO_FILESIZE_LIMIT = int(
    getenv(
        "TG_VIDEO_FILESIZE_LIMIT",
        "1073741824",
    )
)


# =========================================================
# STRING SESSIONS
# =========================================================

STRING1 = getenv(
    "STRING_SESSION",
    None,
)

STRING2 = getenv(
    "STRING_SESSION2",
    None,
)

STRING3 = getenv(
    "STRING_SESSION3",
    None,
)

STRING4 = getenv(
    "STRING_SESSION4",
    None,
)

STRING5 = getenv(
    "STRING_SESSION5",
    None,
)


# =========================================================
# BANNED USERS
# =========================================================

BANNED_USERS = filters.user()


# =========================================================
# GLOBAL VARIABLES
# =========================================================

adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


# =========================================================
# IMAGE URLS
# =========================================================

START_IMG_URL = getenv(
"START_IMG_URL", "https://image-link.edgeone.app/1791892945910-j7696s.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://image-link.edgeone.app/1791892945910-j7696s.jpg"
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
)

# =========================================================
# TIME CONVERSION
# =========================================================

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


# =========================================================
# URL VALIDATION
# =========================================================

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
