import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "100"))

DEVS = list(map(int, os.getenv("DEVS", "8034783687").split()))

API_ID = int(os.getenv("API_ID", "35067623"))

API_HASH = os.getenv("API_HASH", "5a7ffaa7cb963f15c7641797b7814a86")

BOT_TOKEN = os.getenv("BOT_TOKEN", "8244608499:AAG4fScIRraSPLs9lFK1QPm0jmptImSOT_s")

OWNER_ID = int(os.getenv("OWNER_ID", "8034783687"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-5275361115").split()))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://fizzpamell:fizzpamell@cluster0.9nmhi5m.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-4628173231"))
