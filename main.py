import discord, random, os
from discord.ext import commands, tasks
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

@client.event
async def on_message(message):
    if message.content.startswith("hej"):
        await message.channel.send('cześć :)')

    if message.content.startswith("sobi"):
        await message.channel.send('łysol')
    await client.process_commands(message)

@client.command(brief = f'Wypisuje "siema" w nieskończoność ({prefix}siema stop aby zatrzymać)')
async def siema(ctx, enabled="start",interval = 2):
    if enabled.lower() == "stop":
        siemaInterval.stop()
    elif enabled.lower() == "start":
        siemaInterval.change_interval(seconds = int(interval))
        siemaInterval.start(ctx)
@tasks.loop(seconds=2, count=50)
async def siemaInterval(ctx):
        await ctx.send("siema")

@client.command(brief = f'Cumil Ślimak')
async def slimak(ctx, enabled="start",interval = 3599):
    if enabled.lower() == "stop":
        cumilInterval.stop()
    elif enabled.lower() == "start":
        cumilInterval.change_interval(seconds = int(interval))
        cumilInterval.start(ctx)
@tasks.loop(seconds=5)
async def cumilInterval(ctx):
    f = open('./datafiles/slimak.txt',encoding='utf-8')
    slimakhuj = f.readlines()
    # await asyncio.sleep(0.01)   #nie wiem po co to tu w sumie dałem ale dla pewności zostawie bo czemu nie
    randomslimak = random.randint(0,len(slimakhuj)-1)
    await ctx.send(slimakhuj[randomslimak])

@client.command()
async def load(ctx,extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx,extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(bottoken.token)
