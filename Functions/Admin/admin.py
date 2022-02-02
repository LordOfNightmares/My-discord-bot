import discord
from discord.ext import commands

from bot import client
from settings import Settings


class admin(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        print(Settings.Guilds)

    # @commands.guild_only()
    # @is_me()
    # @commands.has_permissions(administrator=True)
    # @slash_command(guild_ids=Settings.Guilds)
    # async def test_mode(self, ctx):
    #     if Settings.TEST_MODE:
    #         Settings.TEST_MODE = False
    #     else:
    #         Settings.TEST_MODE = True
    #     await ctx.respond(f"Test Mode on {Settings.TEST_MODE}!", ephemeral=True)

    @commands.command(help="Blah")
    async def current(self, ctx):
        coms = [c.name for c in client.commands]
        app_coms = [c.name for c in client.pending_application_commands]
        embed = discord.Embed(title="Commands", color=0xff0000)
        embed.add_field(name="Prefix commands",
                        value=f"```{coms}```",
                        inline=False)
        embed.add_field(name="Pending slash(application) commands",
                        value=f"```{app_coms}```",
                        inline=False)
        await ctx.respond(embed=embed)

    @commands.has_permissions(administrator=True)
    @commands.slash_command(guild_ids=Settings.Guilds)
    async def test_mode(self, ctx):
        if Settings.TEST_MODE:
            Settings.TEST_MODE = False
        else:
            Settings.TEST_MODE = True
        await ctx.respond(f"Test Mode on {Settings.TEST_MODE}!", ephemeral=True)


def setup(bot):
    bot.add_cog(admin(bot))
