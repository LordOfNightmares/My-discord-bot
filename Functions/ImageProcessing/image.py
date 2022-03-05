import discord
from discord.ext import commands

from Functions.ImageProcessing.libs.webp import image_convert
from Functions.ImageProcessing.libs.wrappers import image_process


class Image(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(2, 5, commands.BucketType.user)
    async def convert(self, ctx):
        try:
            if len(ctx.message.content.split(' ')) > 1:
                format_type = ctx.message.content.split(' ')[1]
            else:
                format_type = "webp"
            await image_process(self.bot, ctx, image_convert, format_type=format_type)
        except discord.errors:
            await ctx.send(":warning: **I do not have permission to send files!**")
        except Exception as e:
            await ctx.send(e)

def setup(bot):
    bot.add_cog(Image(bot))
