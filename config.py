import os




class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

    APP_ID = int(os.environ.get("APP_ID", 34563456))

    API_HASH = os.environ.get("API_HASH", "sdrfgsrdgdsfg")
