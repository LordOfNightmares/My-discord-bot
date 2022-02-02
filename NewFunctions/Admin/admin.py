from discord import slash_command
from discord.ext import commands

from bot import client
from settings import Settings


# @commands.guild_only()
# @is_me()
@client.event
@commands.has_permissions(administrator=True)
@slash_command(guild_ids=Settings.Guilds)
async def test_mode(self, ctx):
    if Settings.TEST_MODE:
        Settings.TEST_MODE = False
    else:
        Settings.TEST_MODE = True
    await ctx.respond(f"Test Mode on {Settings.TEST_MODE}!", ephemeral=True)
