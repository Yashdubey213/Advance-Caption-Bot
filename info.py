from os import environ, getenv
import re

id_pattern = re.compile(r"^.\d+$")


def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


ADMIN = int(getenv("ADMIN", "5346278816"))
API_ID = int(getenv("API_ID", "22384370"))
API_HASH = str(getenv("API_HASH", "05e2be75292ecbec3f7a29bf13b1e29e"))
BOT_TOKEN = str(getenv("BOT_TOKEN", "6647184416:AAE362zR1uH0qm7KWXbar647r2YVgyxDk7I"))
MONGO_DB = str(
    getenv(
        "MONGO_DB",
        "mongodb+srv://replacewithyourmongodb:replacewithyourmongodb@cluster0.zi78j51.mongodb.net/?retryWrites=true&w=majority",
    )
)
DEF_CAP = str(
    getenv(
        "DEF_CAP",
        "<b>File Name:- `{file_name}`\n\n{file_size}</b>",
    )
)
