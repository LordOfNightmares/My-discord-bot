# For Bot
from os import environ as env


class Settings:
    BOT_MODE="bot"
    TOKEN = {"bot": {"token": env['TOKEN1']},
             "selfbot": {"token": env['TOKEN2'],
                    "bot": False}}
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


class BotPresence:

    def __init__(self):
        pass
