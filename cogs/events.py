import discord, re
from discord.ext import commands

class events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None



    @commands.Cog.listener("on_message")
    async def greet(self,message):
        if message.content.startswith("huj"):
            await message.channel.send('witam')
        if message.content.startswith("hej"):
            await message.channel.send('cześć :)')
        if message.content.startswith("sobi"):
            await message.channel.send('łysol')


        blacklist = ['kizo','_29dLT6OMTU','6E-gg25T84g','BjMcH1BF2hw',
            'kDLbsNlNll8','DOs8S3Iwcvw','peQJOeAICWo','38pLR7eKA6k','rAiIrtEmsxg',
            'Z-pmsb8UHuM','xN09Nwb1hzs','Rq1FPoGCTDg','N3XIi2zCNWQ','2MZrhk6slck','aEuk9FFqmsE',
            'Qtp1Qb0pYGU','e-c0U6uQORw','pDg6mV79AC4','pF9Vn7VZhq0','k0QHxjnrpwU','EvSnWjbxu2o',
            '7Uj1YnKCo6w','yK3RPK3YnsI','lDV6UZL8DfQ','YvtvAhN2m8M','3n1wae0RJZ8','mPzUYmHsb4Y',
            'MbwElOfRMWM','b-Hy7QxaCC0','AEM2EBs7TFQ','EYhCF2qeBA0','me5ge27XlL8','7YphHO9T9As',
            '1YwYCdH8u3c','7YphHO9T9As','ZqAAjoeu0m4','0TOvjoxPPxI','aJ1VQhU6Dlc','p-wBjqUjziA',
            'MbwElOfRMWM','AEM2EBs7TFQ','EYhCF2qeBA0','me5ge27XlL8','1YwYCdH8u3c','JZ9WJsT83WQ',
            'jBwgowp2g8Y','q-_KpAbdA2k','ZYcMAz4-hU8','9xqvyno21RQ','AzAIimi-_3I','8r0UCRxU1_M',
            'Vs0c7Di3c94','rpG90ARD3fE','KGw1Np5Q9AY','lb0VZgWrkNY','4yN0RcYhG-A','iiWE2XkCInI',
            '6V8MYDMwknY','m3tLCwv1MNI','hUDFz7Jw-ag','t2a-RpJuqFE','XE5G004diWE','bvtzcGhd8FY',
            'mRTYVIH6h0o','CSThbl1q0Gg','T_RAx6A5NCg','e0-eFD7i-vg','vqBxHt33q98','oc8pb9xv-WM',
            'kiz0','k1z0','kizzo','kiizo','kizzzo','k|z0','k1zo','kizi0','kiz1o','kiiz0','kizmo',
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
        

        # if message.content.lower().startswith('!play k') and 'disney' in message.content.lower():
        #     await message.channel.send("spierdalaj")
        #     channel = self.bot.get_channel(965343277807173642)

        #     await channel.send(f"{message.author.mention} jest debilem")
        #     await message.author.kick()
        #     await self.process_commands(message)
        



def setup(bot):
    bot.add_cog(events(bot))
