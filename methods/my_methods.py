
from discord.ext import commands

from settings import Settings


def is_me(func=None, *args, **kwargs):
    def predicate(ctx):
        if ctx.message.author.id == Settings.myID or ctx.message.author.id in args:
            return True
        else:
            return False
    return commands.check(predicate)
