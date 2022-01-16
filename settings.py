# For Bot
from os import environ as env


class Settings:
    TOKEN = env['TOKEN2']
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

    def __init__(self):
        pass
