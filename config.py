from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/2f7d46d6b87635fe01d93.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/2f7d46d6b87635fe01d93.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/E0_0_0")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/T_T_T_U")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5801201416").split()))


FAILED = "https://telegra.ph/file/2f7d46d6b87635fe01d93.jpg"
