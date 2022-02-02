# For Bot
from os import environ as env

from methods.other.zalgo import convert_zalgo


class Settings:
    BOT_START_MODE = "bot"
    TEST_MODE = False

    if 'TOKEN1' in env:
        TOKEN = env['TOKEN1']
    if 'TOKEN2' in env:
        TOKEN2 = env['TOKEN2']
    if 'MyID' in env:
        myID = env['MyID']
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
    Guilds = []
