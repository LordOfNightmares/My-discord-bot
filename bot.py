import logging

import discord
from discord.ext import commands

from methods.default import get_guilds
from settings import Settings

intents = discord.Intents.default()
pre_settings = {"bot": {"help_command": None, "intents": intents},
                "self": {"help_command": None, "self_bot": True}}
client = commands.Bot(command_prefix=Settings.Prefix, **pre_settings[Settings.BOT_START_MODE])


def load_cogs(client, reload=False):
    for cog in Settings.cogs:
        try:
            logging.info(f"Loading cog {cog}")
            if reload:
                client.reload_extension(cog)
            else:
                client.load_extension(cog)
            logging.info(f"Loaded cog {cog}")
        except Exception as e:
            exc = f"{type(e).__name__}: {e}"
            logging.exception(f"Failed to load cog {cog}\n{exc}")


@client.event
async def on_message(message):
    """
    Temporary implementation for reloading cogs
    Future:
    •implement testing Function command Cog
    """
    if Settings.TEST_MODE:
        load_cogs(client, True)
        Settings.Guilds = get_guilds(client)
    await client.process_commands(message)


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online,
                                 activity=discord.Game(Settings.BotStatus))
    logging.basicConfig(format='%(asctime)s| %(threadName)s | %(levelname)-5s| %(message)s',
                        level=logging.INFO,
                        datefmt="%H:%M:%S")
    print("Bot is ready!")
    # pprint([c for c in vars(client).items()])
    Settings.Guilds = get_guilds(client)
    load_cogs(client)
    print(f"Prefix commands:\n{[c.name for c in client.commands]}")
    print(f"Pending slash(application) commands:\n```{[c.name for c in client.pending_application_commands]}")





def start():
    if Settings.BOT_START_MODE == 'bot':
        client.run(Settings.TOKEN)
    else:
        client.run(Settings.TOKEN, bot=False)


if __name__ == '__main__':
    try:
        start()
    except Exception:
        raise
