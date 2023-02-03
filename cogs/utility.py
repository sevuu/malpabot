import discord, random, asyncio,os
from discord import message
from discord.ext import commands
from discord.ext.commands import has_permissions
from translate import Translator



prefix = '%'


class Utility(commands.Cog):

    def __init__(self,client):
        self.client = client


    @commands.command(brief = "Pong")
    async def ping(self,ctx):
        await ctx.channel.send(f'Pong! ({round(self.client.latency*1000)}ms)')


    @commands.command(brief="Pokazuje informacje o Tobie albo o oznaczonej osobie")
    async def id(self,ctx):
        if len(ctx.message.mentions)>0:
            embed=discord.Embed(title=str(ctx.message.mentions[0]), color=0xFF5733)
            embed.set_image(url = ctx.message.mentions[0].avatar_url)
            embed.add_field(name="Utworzono konto w dniu:", value=str(ctx.message.mentions[0].created_at.strftime("%A, %B %d %Y @ %H:%M:%S %p")), inline=False)
            embed.add_field(name="Dołączył na serwer w dniu:", value=str(ctx.message.mentions[0].joined_at.strftime("%A, %B %d %Y @ %H:%M:%S %p")), inline=False)
            if ctx.message.mentions[0].premium_since != None:
                embed.add_field(name="Zboostował serwer w dniu:", value=str(ctx.message.mentions[0].premium_since.strftime("%A, %B %d %Y @ %H:%M:%S %p")), inline=False)
            role = []
            for ranga in ctx.message.mentions[0].roles:
                role.append(f"<@&{str(ranga.id)}>")
            del role[0]
            embed.add_field(name="Role:", value=str(", ".join(role)), inline=False)
            embed.set_footer(text="ID: "+str(ctx.message.mentions[0].id))
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(title="Twój profil", color=0xFF5733)
            embed.set_image(url = ctx.message.author.avatar_url)
            embed.add_field(name="Utworzono konto w dniu:", value=str(ctx.message.author.created_at.strftime("%A, %B %d %Y @ %H:%M:%S %p")), inline=False)
            embed.add_field(name="Dołączyłeś na serwer w dniu:", value=str(ctx.message.author.joined_at.strftime("%A, %B %d %Y @ %H:%M:%S %p")), inline=False)
            if ctx.message.author.premium_since != None:
                embed.add_field(name="Zboostowałeś serwer w dniu:", value=str(ctx.message.author.premium_since.strftime("%A, %B %d %Y @ %H:%M:%S %p")), inline=False)
            role = []
            for ranga in ctx.message.author.roles:
                role.append(f"<@&{str(ranga.id)}>")
            del role[0]
            embed.add_field(name="Role:", value=str(", ".join(role)), inline=False)
            embed.set_footer(text="ID: "+str(ctx.message.author.id))
            await ctx.send(embed=embed)


    @commands.command(brief = f"Twój avatar (bezużyteczne bo {prefix}id istnieje)")
    async def avatar(self,ctx):
        if len(ctx.message.mentions)>0:
            embed=discord.Embed(title="avatar "+str(ctx.message.mentions[0]), color=0xFF5733)
            embed.set_image(url = ctx.message.mentions[0].avatar_url)
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(title=ctx.author.display_name, description="twój avatar", color=0xff0000)
            embed.set_image(url = ctx.author.avatar_url)
            await ctx.send(embed=embed)


    @commands.command(brief="dm po id")
    async def dm(self,ctx,user:discord.Member,*,msg=':)'):
        await user.send(msg)


    @commands.command(brief = f"Ankieta")
    async def poll(self,ctx, a, b=None, c=None, d=None, e=None, f=None):
        emojis = ['\U0001F1E6']
        if b == None:
            await ctx.send("podaj przynajmniej dwa argumenty")
        if b != None:
            mytitle = f'{a} czy {b}'
        if c != None:
            mytitle = mytitle + f' czy {c}'
        if d != None:
            mytitle = mytitle + f' czy {d}'
        if e != None:
            mytitle = mytitle + f' czy {e}'
        if f != None:
            mytitle = mytitle + f' czy {f}'
        embed=discord.Embed(title="Ankieta", description=mytitle)
        embed.add_field(name=f"{a}", value=":regional_indicator_a:  ", inline=True)
        if b != None:
            embed.add_field(name=f"{b}", value=":regional_indicator_b:  ", inline=True)
            emojis.append('\U0001F1E7')
        if c != None:
            embed.add_field(name=f"{c}", value=":regional_indicator_c:  ", inline=True)
            emojis.append('\U0001F1E8')
        if d != None:
            embed.add_field(name=f"{d}", value=":regional_indicator_d:  ", inline=True)
            emojis.append('\U0001F1E9')
            mytitle = mytitle + f' czy {d}'
        if e != None:
            embed.add_field(name=f"{e}", value=":regional_indicator_e:  ", inline=True)
            emojis.append('🇪')
            mytitle = mytitle + f' czy {e}'
        if f != None:
            embed.add_field(name=f"{f}", value=":regional_indicator_f:  ", inline=True)
            emojis.append('🇫')
            mytitle = mytitle + f' czy {f}'
        embed.set_footer(text=f"pool by: {ctx.author}")
        msg = await ctx.send(embed=embed)
        for emoji in emojis:
            await message.Message.add_reaction(msg, emoji)
            await asyncio.sleep(0.5)


    @commands.command(brief="Losuje randomową liczbę w wybranym zakresie")
    async def roll(self,ctx,a,b):
        await ctx.send(str(random.randint(int(a),int(b))))


    @commands.command(brief="")
    async def randlist(self,ctx,a,b,c):
        list = []
        for i in range(int(c)):
            list.append(random.randint(int(a),int(b)))
            i += 1
        liststr = str(list)
        if len(liststr) > 1999:
            await ctx.send('za długie')
        else:
            await ctx.send(f"{liststr}")


    @commands.command(brief="")
    async def randomrandlist(self,ctx):
        list = []
        Check = True
        while Check:
            a = random.randint(-9999999999999,9999999999999)
            b = random.randint(a,a+99999999999999)
            c = random.randint(0,99)
            for i in range(int(c)):
                list.append(random.randint(int(a),int(b)))
                i += 1
            liststr = str(list)
            if len(liststr) < 1999:
                Check = False
                await ctx.send(f"{liststr}")
            else:
                continue


    @commands.command(brief="Usuwa x wiadomości")
    @has_permissions(manage_messages=True)
    async def clear(self,ctx,amount=1):
        if ctx.message.author.id == 328989571947823104 or ctx.message.author.id == 252217902202093568:
            if amount <= 20:
                await ctx.channel.purge(limit=amount+1)
            else:
                await ctx.channel.send('pojebalo cie chyba')
        else:
            ctx.channel.send("nie jestes dababy pierdol sei")


    @commands.command(brief="wolny ram")
    async def freem(self,ctx):
        myCmd = os.popen(f'free -h -m').read()
        await ctx.send(f'```{myCmd}```')


    @commands.command(brief="host info")
    async def hostinfo(self,ctx):
        myCmd = int(os.popen('cat /sys/class/thermal/thermal_zone0/temp').read())
        await ctx.send(f'CPU temp: {myCmd/1000} °C')


    @commands.command(brief="link do bota")
    async def invite(self,ctx):
        await ctx.send('https://discord.com/oauth2/authorize?client_id=811696300285362207&scope=bot&permissions=8')


    @commands.command(brief="Status komend używających plików")
    async def filestatus(self,ctx):
        f = open("./datafiles/iq.txt","r")
        f2 = open("./datafiles/starzy.txt","r")
        content = f.read()
        content2 = f2.read()
        f.close()
        f2.close()
        await ctx.channel.send(f'iq: {content}; starzy: {content2}')


    @commands.command(brief=f"Translator (Lista kodów: https://is.gd/VwiXUH)")
    async def translate(self,ctx,fromlang,tolang,*,text):
        translator= Translator(to_lang=tolang, from_lang=fromlang)
        translation = translator.translate(text)
        # await ctx.send(translation)
        embed=discord.Embed(title="Translator")
        embed.add_field(name=f"{fromlang}".upper(), value=f"{text}", inline=True)
        embed.add_field(name=f"{tolang}".upper(), value=f"{translation}", inline=True)
        await ctx.send(embed=embed)


    @commands.command(brief='Zmienia nick czy cos idk')
    async def nick(self,ctx, member: discord.Member,*, nick):
        await member.edit(nick=nick)
        await ctx.send(f'Zmieniono nick {member} na: {member.mention} ')


async def setup(client):
    await client.add_cog(Utility(client))
