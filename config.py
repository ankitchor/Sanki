# © @MuskanBot

import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# ==================== BASIC SETTINGS ====================

API_ID = int(getenv("API_ID", "0"))
API_HASH = getenv("API_HASH", "")
BOT_TOKEN = getenv("BOT_TOKEN", "")

OWNER_ID = int(getenv("OWNER_ID", "8986466577"))
OWNER_USERNAME = getenv("OWNER_USERNAME", "vip_ankit_121")

BOT_USERNAME = getenv("BOT_USERNAME", "shremusicbot")
BOT_NAME = getenv("BOT_NAME", "shremusicbot")

# ==================== LOGGING ====================

_logger_id_raw = getenv("LOGGER_ID", "").strip()
LOGGER_ID = int(_logger_id_raw) if _logger_id_raw else 0

# ==================== SUPPORT ====================

SUPPORT_CHANNEL = getenv(
    "SUPPORT_CHANNEL",
    "https://t.me/ytnaisha"
)

SUPPORT_CHAT = getenv(
    "SUPPORT_CHAT",
    "https://t.me/+T_5EDypRXsU3YTU1"
)

# ==================== API SETTINGS ====================

BASE_URL = ""
API_KEY = ""

# ==================== DATABASE ====================

MONGO_DB_URI = getenv("MONGO_DB_URI", "")

# ==================== HEROKU / GITHUB ====================

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", "")
HEROKU_API_KEY = getenv("HEROKU_API_KEY", "")

UPSTREAM_REPO = ""
UPSTREAM_BRANCH = "main"
GIT_TOKEN = ""

# ==================== ASSISTANT SESSIONS ====================

ASSUSERNAME = ""

STRING1 = getenv("STRING_SESSION", "")
STRING2 = getenv("STRING_SESSION2", "")
STRING3 = getenv("STRING_SESSION3", "")
STRING4 = getenv("STRING_SESSION4", "")
STRING5 = getenv("STRING_SESSION5", "")

# ==================== PLAYBACK SETTINGS ====================

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "900"))

def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60**i
        for i, x in enumerate(reversed(stringt.split(":")))
    )

DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

AUTO_LEAVING_ASSISTANT = "False"
AUTO_LEAVE_ASSISTANT_TIME = 900

SONG_DOWNLOAD_DURATION = 0
SONG_DOWNLOAD_DURATION_LIMIT = 0

PLAYLIST_FETCH_LIMIT = 25
TG_AUDIO_FILESIZE_LIMIT = 2097152000
TG_VIDEO_FILESIZE_LIMIT = 2097152000

# ==================== OPTIONAL SERVICES ====================

SPOTIFY_CLIENT_ID = ""
SPOTIFY_CLIENT_SECRET = ""

CHAT = ""

# ==================== BOT DATA ====================

BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

# ==================== IMAGE URLS ====================

# © @MuskanBot

import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# ==================== BASIC SETTINGS ====================

API_ID = int(getenv("API_ID", "0"))
API_HASH = getenv("API_HASH", "")
BOT_TOKEN = getenv("BOT_TOKEN", "")

OWNER_ID = int(getenv("OWNER_ID", "8986466577"))
OWNER_USERNAME = getenv("OWNER_USERNAME", "vip_ankit_121")

BOT_USERNAME = getenv("BOT_USERNAME", "shremusicbot")
BOT_NAME = getenv("BOT_NAME", "shremusicbot")

# ==================== LOGGING ====================

_logger_id_raw = getenv("LOGGER_ID", "").strip()
LOGGER_ID = int(_logger_id_raw) if _logger_id_raw else 0

# ==================== SUPPORT ====================

SUPPORT_CHANNEL = getenv(
    "SUPPORT_CHANNEL",
    "https://t.me/ytnaisha"
)

SUPPORT_CHAT = getenv(
    "SUPPORT_CHAT",
    "https://t.me/+T_5EDypRXsU3YTU1"
)

# ==================== API SETTINGS ====================

BASE_URL = ""
API_KEY = ""

# ==================== DATABASE ====================

MONGO_DB_URI = getenv("MONGO_DB_URI", "")

# ==================== HEROKU / GITHUB ====================

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", "")
HEROKU_API_KEY = getenv("HEROKU_API_KEY", "")

UPSTREAM_REPO = ""
UPSTREAM_BRANCH = "main"
GIT_TOKEN = ""

# ==================== ASSISTANT SESSIONS ====================

ASSUSERNAME = ""

STRING1 = getenv("STRING_SESSION", "")
STRING2 = getenv("STRING_SESSION2", "")
STRING3 = getenv("STRING_SESSION3", "")
STRING4 = getenv("STRING_SESSION4", "")
STRING5 = getenv("STRING_SESSION5", "")

# ==================== PLAYBACK SETTINGS ====================

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "900"))

def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60**i
        for i, x in enumerate(reversed(stringt.split(":")))
    )

DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

AUTO_LEAVING_ASSISTANT = "False"
AUTO_LEAVE_ASSISTANT_TIME = 900

SONG_DOWNLOAD_DURATION = 0
SONG_DOWNLOAD_DURATION_LIMIT = 0

PLAYLIST_FETCH_LIMIT = 25
TG_AUDIO_FILESIZE_LIMIT = 2097152000
TG_VIDEO_FILESIZE_LIMIT = 2097152000

# ==================== OPTIONAL SERVICES ====================

SPOTIFY_CLIENT_ID = ""
SPOTIFY_CLIENT_SECRET = ""

CHAT = ""

# ==================== BOT DATA ====================

BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

# ==================== IMAGE URLS ====================

# © @MuskanBot

import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# ==================== BASIC SETTINGS ====================

API_ID = int(getenv("API_ID", "0"))
API_HASH = getenv("API_HASH", "")
BOT_TOKEN = getenv("BOT_TOKEN", "")

OWNER_ID = int(getenv("OWNER_ID", "8986466577"))
OWNER_USERNAME = getenv("OWNER_USERNAME", "vip_ankit_121")

BOT_USERNAME = getenv("BOT_USERNAME", "shremusicbot")
BOT_NAME = getenv("BOT_NAME", "shremusicbot")

# ==================== LOGGING ====================

_logger_id_raw = getenv("LOGGER_ID", "").strip()
LOGGER_ID = int(_logger_id_raw) if _logger_id_raw else 0

# ==================== SUPPORT ====================

SUPPORT_CHANNEL = getenv(
    "SUPPORT_CHANNEL",
    "https://t.me/ytnaisha"
)

SUPPORT_CHAT = getenv(
    "SUPPORT_CHAT",
    "https://t.me/+T_5EDypRXsU3YTU1"
)

# ==================== API SETTINGS ====================

BASE_URL = getenv("BASE_URL", "https://api.shrutibots.site")
API_KEY = getenv("API_KEY", "ShrutiBotsmz4lGsT87UWrai3SBsPK")

# ==================== DATABASE ====================

MONGO_DB_URI = getenv("MONGO_DB_URI", "")

# ==================== HEROKU / GITHUB ====================

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", "")
HEROKU_API_KEY = getenv("HEROKU_API_KEY", "")

UPSTREAM_REPO = ""
UPSTREAM_BRANCH = "main"
GIT_TOKEN = ""

# ==================== ASSISTANT SESSIONS ====================

ASSUSERNAME = ""

STRING1 = getenv("STRING_SESSION", "")
STRING2 = getenv("STRING_SESSION2", "")
STRING3 = getenv("STRING_SESSION3", "")
STRING4 = getenv("STRING_SESSION4", "")
STRING5 = getenv("STRING_SESSION5", "")

# ==================== PLAYBACK SETTINGS ====================

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "900"))

def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60**i
        for i, x in enumerate(reversed(stringt.split(":")))
    )

DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

AUTO_LEAVING_ASSISTANT = "False"
AUTO_LEAVE_ASSISTANT_TIME = 900

SONG_DOWNLOAD_DURATION = 0
SONG_DOWNLOAD_DURATION_LIMIT = 0

PLAYLIST_FETCH_LIMIT = 25
TG_AUDIO_FILESIZE_LIMIT = 2097152000
TG_VIDEO_FILESIZE_LIMIT = 2097152000

# ==================== OPTIONAL SERVICES ====================

SPOTIFY_CLIENT_ID = ""
SPOTIFY_CLIENT_SECRET = ""

CHAT = ""

# ==================== BOT DATA ====================

BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

# ==================== IMAGE URLS ====================
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

# ==================== URL VALIDATION ====================

if SUPPORT_CHANNEL and not re.match(
    r"^https?://", SUPPORT_CHANNEL
):
    raise SystemExit(
        "[ERROR] SUPPORT_CHANNEL must start with https://"
    )

if SUPPORT_CHAT and not re.match(
    r"^https?://", SUPPORT_CHAT
):
    raise SystemExit(
        "[ERROR] SUPPORT_CHAT must start with https://"
    )

# ==================== EXPORTS ====================

__all__ = [
    "IQ_Proxy",
]

# ==================== URL VALIDATION ====================

if SUPPORT_CHANNEL and not re.match(
    r"^https?://", SUPPORT_CHANNEL
):
    raise SystemExit(
        "[ERROR] SUPPORT_CHANNEL must start with https://"
    )

if SUPPORT_CHAT and not re.match(
    r"^https?://", SUPPORT_CHAT
):
    raise SystemExit(
        "[ERROR] SUPPORT_CHAT must start with https://"
    )

# ==================== EXPORTS ====================

__all__ = [
    "IQ_Proxy",
]
# ==================== URL VALIDATION ====================

if SUPPORT_CHANNEL and not re.match(
    r"^https?://", SUPPORT_CHANNEL
):
    raise SystemExit(
        "[ERROR] SUPPORT_CHANNEL must start with https://"
    )

if SUPPORT_CHAT and not re.match(
    r"^https?://", SUPPORT_CHAT
):
    raise SystemExit(
        "[ERROR] SUPPORT_CHAT must start with https://"
    )

# ==================== EXPORTS ====================

__all__ = [
    "IQ_Proxy",
]
