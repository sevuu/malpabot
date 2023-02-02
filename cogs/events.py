import discord
from discord.ext import commands

prefix = '%'
intents = discord.Intents.all()
client = commands.Bot(command_prefix = prefix, intents=intents)

class events(commands.Cog):
    def __init__(self,client):
        self.client = client



    @commands.Cog.listener("on_message")
    async def greet(self,message):
        if message.content.startswith("huj"):
            await message.channel.send('witam')
        if message.content.startswith("hej"):
            await message.channel.send('cześć :)')
        if message.content.startswith("sobi"):
            await message.channel.send('łysol')


        blacklist = ['kizo','kiz0','k1z0','kizzo','kiizo','kizzzo','k|z0','k1zo','kizi0','kiz1o','kiiz0','kizmo',
            'kizko','kizk0','kiz0o','kizerro','kizzers','kizownik','kizers','kizbo','kizia','kimzo',
            'kibzo','kiwzo','kirzo','kiizo','kiiiizo','kiiizo','kizmio','kizbio','kiźo','kiżo','kimdzio',
            'kimziom','kizjom','kimdizom','kizzzers','kijzom','kiijzom','kijzzom',
            'nie mam zamiaru sie smucic tylko zatracic w tym co najlepsze','nie trwa wiecznie hotelowa doba w apartamencie',
            'mytosukces','disney prod sergiusz lesny','enzu disney','izo disney','chmielecka disney']

        if any(word in message.content.lower() for word in blacklist) or message.content.lower().startswith('!play k') and 'disney' in message.content.lower() or message.content.lower().startswith('!p k') and 'disney' in message.content.lower():
            await message.channel.send("spierdalaj")
            channel = self.bot.get_channel(965343277807173642)

            await channel.send(f"{message.author.mention} jest debilem")
            await message.author.kick()
            await self.process_commands(message)

async def setup(bot):
    await bot.add_cog(events(bot))
