import discord, os
from discord.ext import commands
from lib import bottoken


prefix = '%'
client = commands.Bot(command_prefix = prefix)

@client.event
async def on_ready():
    print('dzialam kurwa {0.user}\nhttps://discord.com/oauth2/authorize?client_id=811696300285362207&scope=bot&permissions=8'.format(client))
    await client.change_presence(status=discord.Status.online, activity=discord.Game(f'piwko :)) | {prefix}help'))
    user = await client.fetch_user('252217902202093568')
    channel = await user.create_dm()
    await channel.send("Dziala")

@client.command()
async def load(ctx,extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx,extension):
    client.unload_extension(f'cogs.{extension}')

@client.command()
async def reload(ctx,extension):
    client.reload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(bottoken.token)
