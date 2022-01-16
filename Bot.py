import logging

import discord
from discord.ext import commands

from settings import Settings

intents = discord.Intents.default()
pre_settings = {"bot": {"help_command": None, "intents": intents},
                "selfbot": {"help_command": None, "self_bot": True}}
client = commands.Bot(command_prefix=Settings.Prefix, **pre_settings[Settings.BOT_MODE])


def load_cogs(client):
    for cog in Settings.cogs:
        try:
            logging.info(f"Loading cog {cog}")
            client.load_extension(cog)
            logging.info(f"Loaded cog {cog}")
        except Exception as e:
            exc = f"{type(e).__name__}: {e}"
            logging.exception(f"Failed to load cog {cog}\n{exc}")


@client.event
async def on_ready():
    print("Bot is ready!")
    await client.change_presence(status=discord.Status.online,
                                 activity=discord.Game(Settings.BotStatus))
    logging.basicConfig(format='%(asctime)s| %(threadName)s | %(levelname)-5s| %(message)s',
                        level=logging.INFO,
                        datefmt="%H:%M:%S")
    load_cogs(client)


if __name__ == '__main__':
    if Settings.BOT_MODE == 'bot':
        client.run(Settings.TOKEN)
    else:
        client.run(Settings.TOKEN, bot=False)
