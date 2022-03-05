import discord
from discord.ext import commands

from methods.errors import error_not_owner, error_permission
from settings import Settings


class admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

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

    # @commands.command(help="Blah")
    @commands.slash_command(guild_ids=Settings.Guilds, description="Current commands")
    async def current(self, ctx):
        embed = discord.Embed(title="Commands", color=0xff0000)
        embed.add_field(name="Prefix commands",
                        value=f"```{[c.name for c in self.bot.commands]}```",
                        inline=False)
        embed.add_field(name="Pending slash(application) commands",
                        value=f"```{[c.name for c in self.bot.pending_application_commands]}```",
                        inline=False)
        await ctx.respond(embed=embed)

    @commands.is_owner()
    @commands.slash_command(guild_ids=Settings.Guilds, description="Owner Testing mode")
    async def test(self, ctx):
        if Settings.TEST_MODE:
            Settings.TEST_MODE = False
        else:
            Settings.TEST_MODE = True
        await ctx.respond(f"Test Mode on {Settings.TEST_MODE}!", ephemeral=True)

    @test.error
    async def backup_error(self, ctx, error):
        '''Handle a lack of permissions'''
        if isinstance(error, commands.BotMissingPermissions):
            await error_permission(ctx, attach=True)
        elif isinstance(error, commands.NotOwner):
            await error_not_owner(ctx)
        else:
            raise (type(error), error)


def setup(bot):
    bot.add_cog(admin(bot))
