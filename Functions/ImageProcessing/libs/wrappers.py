import os
import re
import shutil
import tempfile
from functools import partial

import discord
import requests


def get_url_images_in_text(text):
    '''finds image urls'''
    return re.findall(r'(https?:\/\/.*\.(?:png|jpg|webp|jiff|jpeg))', text)


async def get_im(ctx):
    get_images = None
    if len(ctx.message.attachments) > 0 and "image" in ctx.message.attachments[-1].content_type:
        get_images = [ctx.message.attachments[-1].url]
    if get_images is None:
        async for message in ctx.channel.history(limit=100):
            if len(url := get_url_images_in_text(message.content)) > 0 and url[-1]:
                get_images = url
                break
            elif len(message.attachments) > 0 and "image" in message.attachments[0].content_type:
                get_images = [message.attachments[-1].url]
                break
    return get_images


async def image_process(bot, ctx, function, *args, **kwargs):
    get_images = await get_im(ctx)
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
        fn = partial(function, *args, **kwargs,
                     read_image=read_image)
        final, fname = await bot.loop.run_in_executor(None, fn)
        file = discord.File(filename=fname, fp=final)
    await ctx.send(file=file)
    shutil.rmtree(tmp.name)
