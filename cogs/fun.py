import discord, random, asyncio, os, requests, interactions
from discord.ext import commands
from bs4 import BeautifulSoup
from lib import caesarcipher, monkies, morsecode

prefix = '%'
intents = discord.Intents.all()
client = commands.Bot(command_prefix = prefix, intents=intents)

class Fun(commands.Cog):

    def __init__(self,client):
        self.client = client

    @commands.command(brief="test")
    async def test(self,ctx):
        await ctx.send(f'gittest')

    @client.command()
    async def status(self, ctx, member : discord.Member=None):
        if member is None:
            member = ctx.author
        embed=discord.Embed(title=f"{member.name} your current status is", description= f'{member.activities[0].name}', color=0xcd32a7)
        await ctx.send(embed=embed)

    @commands.command(brief="yes..")
    async def ben(self,ctx,*,msg):
        audio = os.listdir('./media/ben/')
        audioString = random.choice(audio)  # Selects a random element from the list
        path = "./media/ben/" + audioString
        await ctx.send(file=discord.File(path))
        
    @commands.command(brief="Wiadomość kodem Morse'a")
    async def morse(self,ctx,*,msg):
        await ctx.send(morsecode.morseEncrypt(msg))

    @commands.command(brief="Odszyfrowuje wiadomość zapisaną kodem Morse'a")
    async def morsedecrypt(self,ctx,*,msg):
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

    @commands.command(brief="Randomowa stronka nhentai :D")
    async def nhentai(self,ctx):
        id = random.randint(1,439759)
        source = requests.get(f'https://nhentai-net.translate.goog/g/{id}/?_x_tr_sl=auto&_x_tr_tl=pl&_x_tr_hl=pl&_x_tr_pto=wapp').text
        soup = BeautifulSoup(source, features="html.parser")

        title = soup.find("meta", attrs={'itemprop': 'name'})
        image = soup.find("meta", attrs={'itemprop': 'image'})
        tags = soup.find("meta", attrs={'name': 'twitter:description'})
     
        titlec = title["content"]
        tagsc = tags["content"]

        tagslist = tags["content"].split(', ')
        blacklist = ["lolicon","shotacon","rape", "incest"]

        check = any(item in tagslist for item in blacklist)
        if check is False:
            embed=discord.Embed(title=titlec if title is not None else "Brak tytułu", url=f'https://nhentai.net/g/{id}',color=0xf22653)
            embed.set_thumbnail(url=image["content"])
            embed.add_field(name="Tagi: ", value=tagsc if tags is not None else "Brak tagów", inline=False)
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(title=f"||{titlec}||" if title is not None else "Brak tytułu", url=f'https://nhentai.net/g/{id}',color=0xf22653)
            embed.add_field(name="Tagi (:face_with_raised_eyebrow:): ", value=f"||{tagsc}||" if tags is not None else "Brak tagów", inline=False)
            await ctx.send(embed=embed)

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

#    @commands.command(brief="krowa mówi wtf?", description='https://en.wikipedia.org/wiki/Cowsay')
#    async def cowsay(self,ctx,*,msg):
#        myCmd = os.popen(f'cowsay {msg}').read()
#        await ctx.send(f'```{myCmd}```')

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
        await ctx.send('‎\n'*100)


    @commands.command(brief = "Wojtek of the wisdom")
    async def wojtek(self,ctx):
        embed=discord.Embed(title="Wojtek of the wisdom")
        embed.add_field(name="Wojtek mówi:", value="pierdol sie", inline=False)
        embed.set_image(url="https://i.imgur.com/6UmHSH6.png")
        await ctx.send(embed=embed)


    @commands.command(brief = "Scav, Tetris, Wywóz.")
    async def stw(self,ctx):
        embed=discord.Embed(title="STW S.A z.o.o.- Scav, Tetris, Wywóz", description="Młoda firma utworzona w 2023 r. specjalizująca się w usłudze sprzątania nie tylko przedmiotów oraz transporcie dóbr materialnych na terenie miasta Tarkov położonego na terenie Rosji. ", color=0x00ffcc)
        embed.add_field(name=" ", value="Usługi scav (pmc na własne ryzyko!) których się podejmujemy: - eksploracja miasta wraz z poszukiwaniem przedmiotów - Eliminowanie przeciwników na terenie miasta Tarkov - Sprzątanie oraz układanie miejsca w schowkach - Wykonywanie zleceń handlarzy - Sprzedaż przedmiotów na rynku - Usługa jako trener personalny na twojej własnej siłowni w kryjówce - Rozbudowa kryjówki - Odbieranie oraz robienie zrzutów ekranu przyniesionych przedmiotów od pracownika SCAV -  Wysyłanie pracownika SCAV na poszukiwanie nowych przedmiotów w rejonie miasta Tarkov", inline=True)
        embed.add_field(name="W razie jakichkolwiek pytań lub wyceny danych usług prosimy o kontakt do naszego biura.", value=" ", inline=False)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/338268917497856001/1069989635167629343/LOGO.png")
        embed.set_image(url="https://cdn.discordapp.com/attachments/338268917497856001/1069989638774734899/nie_wiem_srednio_wyszlo_2.png")
        embed.add_field(name="Dane firmy:", value="STW sa. z.o.o.- scav, tetris, wywóz Nikitskaya st. 48 (na przeciwko teatru) 171271 Tarkov NIP: 11037 KRS: 251003", inline=False)
        embed.add_field(name="Biuro: ", value="- Czechubuisnes@wp.pl \n - czechu#8854 (okres oczekiwania: od razu - 1 dzień)", inline=False)
        embed.set_footer(text=" Zarejestrowana przez Sąd Rejonowy dla Tarkova-Śródmieścia w Tarkovie XIX Wydział Gospodarczy KRS.Wysokość kapitału zakładowego: 32,21 RUB")
        await ctx.send(embed=embed)
    

    @commands.command(brief = "MMA Fighter")
    async def zagus(self,ctx):
        await ctx.channel.send(f':grinning: :right_facing_fist: :woman_red_haired:')

    @commands.command(brief = "Losowa piosenka hatsune michael")
    async def miku(self,ctx):
        f = open('./datafiles/miku.txt',encoding='utf-8')
        mikusongs = f.readlines()
        randommikusong = random.randint(0,len(mikusongs)-1)
        await ctx.send(mikusongs[randommikusong])

async def setup(client):
    await client.add_cog(Fun(client))
