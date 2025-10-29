# ------------- Imports -------------
from os import environ as env
from dotenv import load_dotenv

# ------------- Load Environment Variables -------------
load_dotenv()

# ------------- Telegram Configuration -------------
class Telegram:
    API_ID = int(env.get("API_ID"))
    API_HASH = str(env.get("API_HASH"))
    BOT_TOKEN = str(env.get("BOT_TOKEN"))
    OWNER_ID = int(env.get('OWNER_ID', '841851780'))
    WORKERS = int(env.get("WORKERS", "6"))  # 6 workers = 6 commands at once
    DATABASE_URL = str(env.get('DATABASE_URL'))
    UPDATES_CHANNEL = str(env.get('UPDATES_CHANNEL', "neonfiles"))
    SESSION_NAME = str(env.get('SESSION_NAME', 'MyselfNeon'))
    FORCE_SUB_ID = env.get('FORCE_SUB_ID', None)
    FORCE_SUB = env.get('FORCE_UPDATES_CHANNEL', False)
    FORCE_SUB = True if str(FORCE_SUB).lower() == "true" else False
    SLEEP_THRESHOLD = int(env.get("SLEEP_THRESHOLD", "60"))
    FILE_PIC = env.get('FILE_PIC', "https://graph.org/file/5bb9935be0229adf98b73.jpg")
    START_PIC = env.get('START_PIC', "https://graph.org/file/290af25276fa34fa8f0aa.jpg")
    VERIFY_PIC = env.get('VERIFY_PIC', "https://graph.org/file/736e21cc0efa4d8c2a0e4.jpg")
    MULTI_CLIENT = False
    FLOG_CHANNEL = int(env.get("FLOG_CHANNEL", None))   # Logs channel for file logs
    ULOG_CHANNEL = int(env.get("ULOG_CHANNEL", None))   # Logs channel for user logs
    MODE = env.get("MODE", "primary")
    SECONDARY = True if MODE.lower() == "secondary" else False
    AUTH_USERS = list(set(int(x) for x in str(env.get("AUTH_USERS", "")).split()))

# ------------- Server Configuration -------------
class Server:
    PORT = int(env.get("PORT", 8080))  # Render will auto-assign or override this
    BIND_ADDRESS = str(env.get("BIND_ADDRESS", "0.0.0.0"))  # <-- important fix
    PING_INTERVAL = int(env.get("PING_INTERVAL", "1200"))
    HAS_SSL = str(env.get("HAS_SSL", "1").lower()) in ("1", "true", "t", "yes", "y")
    NO_PORT = str(env.get("NO_PORT", "1").lower()) in ("1", "true", "t", "yes", "y")
    FQDN = str(env.get("FQDN", "filesyream.onrender.com"))  # <-- your Render domain (no https://)
    URL = "http{}://{}{}/".format(
        "s" if HAS_SSL else "", FQDN, "" if NO_PORT else ":" + str(PORT)
    )

# ------------- Keep-Alive URL -------------
KEEP_ALIVE_URL = env.get("KEEP_ALIVE_URL", "https://filesyream.onrender.com/")
