# For Bot
from os import environ as env

from methods.zalgo import convert_zalgo


class Settings:
    BOT_START_MODE = "bot"
    TEST_MODE = False
    TOKEN = 'TOKEN1' in env and env['TOKEN1']
    TOKEN2 = 'TOKEN2' in env and env['TOKEN2']
    myID = 'MyID' in env and env['MyID']
    BotStatus = convert_zalgo("Pain")
    Prefix = "."
    cogs: list = [
        # "Functions.Fun.games",
        # "Functions.Fun.gameinfos",
        # "Functions.Fun.otherfuncommands",
        # "Functions.Info.info",
        # "Functions.Misc.misc",
        # "Functions.NewMember.newmember",
        "Functions.Admin.admin",
        "Functions.Test.test"
    ]
