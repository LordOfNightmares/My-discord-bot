import os
import shutil
import tempfile
from functools import partial

import discord
import requests
from discord.ext import commands

from Functions.ImageProcessing.webp import image_convert, get_url_images_in_text


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
            get_images = None
            async for message in ctx.channel.history(limit=100):
                if len(url := get_url_images_in_text(message.content)) > 0 and url[0]:
                    get_images = url
                    break

                elif len(message.attachments) > 0 and "image" in message.attachments[0].content_type:
                    get_images = [message.attachments[0].url]
                    break
            if not get_images:
                return
            url, fname = get_images[0].rsplit("/", 1)
            r = requests.get(get_images[0], allow_redirects=True)
            tmp = tempfile.TemporaryDirectory()
            t_path = None
            if r.status_code == 200:
                t_path = os.path.join(tmp.name, fname)
                with open(t_path, 'wb') as handler:
                    handler.write(r.content)
            with open(t_path, 'rb') as read_image:
                fn = partial(image_convert,
                             read_image,
                             format_type=format_type,
                             fname=fname.split(".")[0])
                final, fname = await self.bot.loop.run_in_executor(None, fn)
                file = discord.File(filename=fname, fp=final)
            await ctx.send(file=file)
            shutil.rmtree(tmp.name)
        except discord.errors:
            await ctx.send(":warning: **I do not have permission to send files!**")
        except Exception as e:
            await ctx.send(e)


def setup(bot):
    bot.add_cog(Image(bot))
