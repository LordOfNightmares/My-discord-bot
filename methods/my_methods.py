
from discord.ext import commands


def is_me(func=None, *args, **kwargs):
    def predicate(ctx):
        # print(ctx.message.author.id, ctx.message.author.id == 201107682516664330, ctx.message.author.id in args)
        if ctx.message.author.id == 201107682516664330 or ctx.message.author.id in args:
            return True
        else:
            return False
    return commands.check(predicate)
