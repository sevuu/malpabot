import discord, random, asyncio, os
from discord.ext import commands
from hentai import Hentai, Format
from lib import  caesarcipher, monkies, morsecode



prefix = '%'
client = commands.Bot(command_prefix = prefix)

class Fun(commands.Cog):

    def __init__(self,client):
        self.client = client

    @commands.command(brief="test")
    async def test(self,ctx):
        await ctx.send(f'test')

    @commands.command(brief="test")
    async def morseencrypt(self,ctx, *,msg):
        await ctx.send(morsecode.morseEncrypt(msg))

    @commands.command(brief="test")
    async def morsedecrypt(self,ctx, *,msg):
        await ctx.send(morsecode.morseDecrypt(msg))

    @commands.command(brief="IQ Szymona")
    async def iqsobiego(self,ctx):
        f = open("./datafiles/iq.txt","r")
        content = int(f.read()) - 1
        f.close()
        f = open("./datafiles/iq.txt","w")
        f.write(str(content))
        f.close()
        await ctx.send(f'Sobi ma {content} IQ')

    @commands.command(brief="Pokazuje prawdziwą liczbę ojców Gabriela")
    async def starzygabrysia(self,ctx):
        f = open("./datafiles/starzy.txt","r")
        content = int(f.read()) + 1
        f.close()
        f = open("./datafiles/starzy.txt","w")
        f.write(str(content))
        f.close()
        await ctx.send(f"Gabryś ma {content} ojców")

    @commands.command(brief="Randomowa strona nhentai do id 356714 :)")
    async def nhentai(self,ctx):
        FBI = True
        while FBI:
            id = random.randint(1,356714)
            doujin = Hentai(id)
            tagi = [tag.name for tag in doujin.tag]
            blacklist = ["lolicon","shotacon","rape","incest","scat"]
            check = any(item in tagi for item in blacklist)
            if check is False:
                embed=discord.Embed(title=doujin.title(Format.Pretty),url=f"https://nhentai.net/g/{id}/",description=f"#{id}",color=discord.Color.purple())
                embed.set_thumbnail(url=doujin.image_urls[0])
                embed.add_field(name="Tags", value=", ".join(tagi), inline=False)
                await ctx.send(embed=embed)
                FBI = False
            else:
                continue

    @commands.command(brief="małpa w losowym języku")
    async def rndmalpa(self,ctx):
        malpy = monkies.malpiszony
        mKeys = list(malpy.keys())
        randomLang = mKeys[random.randint(0,len(mKeys)-1)]
        randomLangMonky = malpy.get(randomLang)
        embed=discord.Embed(title='Randomowa małpa')
        embed.add_field(name=randomLang, value=randomLangMonky, inline=False)
        await ctx.send(embed=embed)

    @commands.command(brief="Mój kolega :)")
    async def czechu(self,ctx):
        await ctx.channel.send('<@327742627233398784>')

    @commands.command(brief="Gra komputerowa")
    async def ligalegend(self,ctx):
        await ctx.channel.send('Liga Legend to kurwa, nie graj w to')

    @commands.command(brief="krowa mówi wtf?", description='https://en.wikipedia.org/wiki/Cowsay')
    async def cowsay(self,ctx,*,msg):
        myCmd = os.popen(f'cowsay {msg}').read()
        await ctx.send(f'```{myCmd}```')

    @commands.command(brief="Losowy fakt")
    async def randomfact(self,ctx):
        facts =["wojtek to calkiem gejowe imie",
                'Ilość ojców gabrysia można poznać za pomocą komendy '+prefix+'starzygabrysia',
                'Sobi lubi grać w grę valorant','Jan Popczyk nie znosi żydów',
                'ten bot jest bezużyteczny','jakub kuc dostał dmuchaną lale',
                'superwojtek3000 zmienił nazwę kanału na Woitaz',
                'kurwa mać']
        await ctx.send(str(facts[random.randint(0,len(facts)-1)]))

    @commands.command(brief="Nasz kolega :)")
    async def zagusi(self,ctx):
        f = open('./datafiles/zagus1.txt')
        content = f.read()
        f.close()
        zaguslista = content.splitlines()
        msg = await ctx.channel.send(":grinning:                                                     :woman_red_haired: ")
        for i in zaguslista:
            await asyncio.sleep(1)
            await msg.edit(content=i)

    @commands.command(brief="troled")
    async def tf(self,ctx):
        f = open('./datafiles/tf.txt')
        content = f.read()
        f.close()
        trollista = content.splitlines()    
        for i in trollista:
            await ctx.send(content=i)
            await asyncio.sleep(0.8)      

    @commands.command(brief="amogus")
    async def amogus(self,ctx):
        f = open('./datafiles/amogus.txt')
        content = f.read()
        f.close()
        amoguslista = content.splitlines()    
        for i in amoguslista:
            await ctx.send(content=i)
            await asyncio.sleep(0.8)
                
    @commands.command(brief = "Wynik z dodawania")
    async def sum(self,ctx, x, y):
        try:
            wynik = float(x)+float(y)
            if str(wynik).endswith(".0"):
                wynik = round(wynik)
            await ctx.channel.send(f"{x}+{y}="+str(wynik))
        except:
            await ctx.channel.send("To nie są poprawne liczby!")

    @commands.command(brief = "Szyfruje wiadomość szyfrem cezara", )
    async def cencrypt(self,ctx, shift,*,msg):
        await ctx.channel.send(caesarcipher.cipher_encrypt(msg,int(shift)))

    @commands.command(brief = "Odszyfrowuje wiadomość napisaną szyfrem cezara")
    async def cdecrypt(self,ctx, shift,*,msg):
        await ctx.channel.send(caesarcipher.cipher_decrypt(msg,int(shift)))


    @commands.command(brief="Wynik z odejmowania")
    async def subt(self,ctx, x, y):
        try:
            wynik = float(x)-float(y)
            if str(wynik).endswith(".0"):
                wynik = round(wynik)
            await ctx.channel.send(f"{x}-{y}="+str(wynik))
        except:
            await ctx.channel.send("To nie są poprawne liczby!")

    @commands.command(brief="‎")
    async def nic(self,ctx):
        await ctx.send('‎\n'*40)

        
    @commands.command(brief = "super quiz :)", description = "bajerancki quizior :D")
    async def avatarquiz(self,ctx):
        avatary = os.listdir('avatar')
        los = random.randint(0,len(avatary)-1)
        filename = avatary[los]
        f = open(f'./avatar/{filename[:-4]}.png', 'rb')
        file = discord.File(f)
        await ctx.send("Zgadnij czyj to avatar:")
        await ctx.send(file=file)

        def check(msg):
            return msg.channel == ctx.channel

        msg = await client.wait_for("message", check=check)
        if msg.content.lower() == f"{filename[:-4]}":
            await ctx.send("Brawo :)")
        else:
            await ctx.send("Debil")

    @commands.command(brief = "MMA Fighter")
    async def zagus(self,ctx):
        await ctx.channel.send(f':grinning: :right_facing_fist: :woman_red_haired:')

    # @commands.command(brief=":tf:")
    # async def pong(self,ctx):
    #     await ctx.send(f"{ctx.message.guild.default_role}  <:tf:805707103628951592>")

    @commands.command(brief = "Losowa piosenka hatsune michael")
    async def miku(self,ctx):
        f = open('./datafiles/miku.txt',encoding='utf-8')
        mikusongs = f.readlines()
        randommikusong = random.randint(0,len(mikusongs)-1)
        await ctx.send(mikusongs[randommikusong])

    
def setup(client):
    client.add_cog(Fun(client))