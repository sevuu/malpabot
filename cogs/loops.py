import random, discord
from discord.ext import commands
from discord.ext import commands, tasks



prefix = '%'
intents = discord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix = prefix, intents=intents)
class Loops(commands.Cog):

    def __init__(self,client):
        self.client = client

    @client.command(brief = f'Wypisuje "siema" w nieskończoność ({prefix}siema stop aby zatrzymać)')
    async def siema(self,ctx, enabled="start",interval = 2):
        if enabled.lower() == "stop":
            self.siemaInterval.stop()
        elif enabled.lower() == "start":
            self.siemaInterval.change_interval(seconds = int(interval))
            self.siemaInterval.start(ctx)
    @tasks.loop(seconds=2, count=50)
    async def siemaInterval(self,ctx):
            await ctx.send("siema")

    @client.command(brief = f'Cumil Ślimak')
    async def slimak(self,ctx, enabled="start",interval = 3600):
        if enabled.lower() == "stop":
            self.cumilInterval.stop()
        elif enabled.lower() == "start":
            self.cumilInterval.change_interval(seconds = int(interval))
            self.cumilInterval.start(ctx)
    @tasks.loop(seconds=5)
    async def cumilInterval(self,ctx):
        f = open('./datafiles/slimak.txt',encoding='utf-8')
        slimakhuj = f.readlines()
        randomslimak = random.randint(0,len(slimakhuj)-1)
        await ctx.send(slimakhuj[randomslimak])


async def setup(client):
    await client.add_cog(Loops(client))
