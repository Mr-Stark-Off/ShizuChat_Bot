from os import getenv

from pyrogram import filters
from dotenv import load_dotenv

load_dotenv()

API_ID = "27402174"
# -------------------------------------------------------------
API_HASH = "53cdb3d648bf50e7625386b3e6879c23"
# --------------------------------------------------------------
BOT_TOKEN = getenv("BOT_TOKEN", None)
STRING1 = getenv("STRING_SESSION", None)
DB_NAME = "shizuDB"
MONGO_URL = getenv("MONGO_URL", None)
OWNER_ID = int(getenv("OWNER_ID", "7829147196"))
BOT_ID = int(getenv("BOT_ID", "8184181775"))
SUPPORT_GRP = "btw_stark_officials"
UPDATE_CHNL = "btw_stark_officials"
OWNER_USERNAME = "Mr_stark_offf"
TIME_ZONE = "Asia/Kolkata"
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1002455679060"))
# --------------------------------------------------------------
SUDOERS = list(map(int, getenv("SUDOERS", "7009601543").split()))
# --------------------------------------------------------------

### DONT TOUCH or EDIT codes after this line
BANNED_USERS = filters.user()

# For customized or modified Repository
UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/BadshahAk/ShizuChat_Bot",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
