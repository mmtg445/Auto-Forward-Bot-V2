from os import environ 

class Config:
    API_ID = environ.get("API_ID", "23774463")
    API_HASH = environ.get("API_HASH", "46460eb9fe6fc54c0adf2a795e61d724")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7946608549:AAGke6Uw3SvCd270wGHwunxx-HvlciTcTi8") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://rohanahamed75:gt4RXJZ1mUtOh4Xv@mmtg.0ong5.mongodb.net/?retryWrites=true&w=majority&appName=mmtg")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '8102446291').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
