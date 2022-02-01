from discord import slash_command
from discord.ext import commands

from methods.wrappers import is_me
from settings import Settings


class admin(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.guild_only()
    @is_me()
    @commands.has_permissions(administrator=True)
    @slash_command(description="AHOY")
    async def test_mode(self, ctx):
        if Settings.TEST_MODE:
            Settings.TEST_MODE = False
        else:
            Settings.TEST_MODE = True
        await ctx.respond(f"Test Mode on {ctx.author}!")


def setup(bot):
    bot.add_cog(admin(bot))
