https://t.me/P_E_Yfrom os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/0a9d70733b51b40e2d7f1.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/0a9d70733b51b40e2d7f1.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://https://t.me/Tm_S_TNT")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/P_E_Y")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1840881497").split()))


FAILED = "https://telegra.ph/file/0a9d70733b51b40e2d7f1.jpg"
