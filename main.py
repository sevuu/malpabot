import discord, os, asyncio
from discord.ext import commands
from lib import bottoken

prefix = '%'
intents = discord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix = prefix, intents=intents)

@client.event
async def on_ready():
    print('dzialam kurwa {0.user}\nhttps://discord.com/oauth2/authorize?client_id=811696300285362207&scope=bot&permissions=8'.format(client))
    await client.change_presence(status=discord.Status.online, activity=discord.Game(f'piwko :)) | {prefix}help'))
    user = await client.fetch_user('252217902202093568')
    channel = await user.create_dm()
    
    await channel.send("Dziala")

@client.command()
async def load(ctx,extension):
    await client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx,extension):
    await client.unload_extension(f'cogs.{extension}')

@client.command()
async def reload(ctx,extension):
    await client.reload_extension(f'cogs.{extension}')

async def loadc():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await client.load_extension(f'cogs.{filename[:-3]}')

async def main():
    await loadc()
    await client.start(bottoken.token)

asyncio.run(main())
