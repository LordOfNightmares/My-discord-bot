def get_guilds(client):
    return [guild.id for guild in client.guilds]