# For Bot
from os import environ as env


class Settings:
    BOT_MODE = "bot"
    TOKEN = env['TOKEN1']
    TOKEN2 = env['TOKEN2']
    myID = env['MyID']
    BotStatus = "Bakuretsu Bakuretsu la la la"
    Prefix = "."
    cogs: list = [
        "Functions.Fun.games",
        # "Functions.Fun.gameinfos",
        # "Functions.Fun.otherfuncommands",
        # "Functions.Info.info",
        # "Functions.Misc.misc",
        # "Functions.NewMember.newmember",
        # "Functions.Admin.admin"
        "Functions.Test.test"
    ]
