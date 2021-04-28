import discord, bottoken, random, asyncio, caesarcipher, os, json, monkies
from discord import guild
from discord import voice_client
from discord import message, FFmpegPCMAudio
from discord.ext import commands, tasks
from discord.ext.commands import Bot, has_permissions
from discord.voice_client import VoiceClient
from hentai import Hentai, Format
from translate import Translator


prefix = '%'
client = commands.Bot(command_prefix = prefix)


@client.event
async def on_ready():
    print('dzialam kurwa {0.user}\nhttps://discord.com/oauth2/authorize?client_id=811696300285362207&scope=bot&permissions=8'.format(client))
    await client.change_presence(status=discord.Status.online, activity=discord.Game(f'piwko :)) | {prefix}help'))
    user = await client.fetch_user('252217902202093568')
    channel = await user.create_dm()
    await channel.send("Dziala")

@client.command(brief = "Pong")
async def ping(ctx):
    await ctx.channel.send(f'Pong! ({round(client.latency*1000)}ms)')

@client.command(brief = "super quiz :)", description = "bajerancki quizior :D")
async def avatarquiz(ctx):
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

@client.command(brief = "MMA Fighter")
async def zagus(ctx):
    await ctx.channel.send(f':grinning: :right_facing_fist: :woman_red_haired:')

@client.event
async def on_message(message):
    if message.content.startswith("hej"):
        await message.channel.send('cześć :)')

    if message.content.startswith("sobi"):
        await message.channel.send('łysol')

    # if 'kurwa' in message.content:
    #     los = random.randint(0,100)
    #     if los <= 25:
    #         await message.channel.send('<@327742627233398784> <:tf:805707103628951592>')

    await client.process_commands(message)


@client.command(brief = "Wynik z dodawania")
async def sum(ctx, x, y):
    try:
        wynik = float(x)+float(y)
        if str(wynik).endswith(".0"):
            wynik = round(wynik)
        await ctx.channel.send(f"{x}+{y}="+str(wynik))
    except:
        await ctx.channel.send("To nie są poprawne liczby!")

@client.command(brief = "Szyfruje wiadomość szyfrem cezara", )
async def cencrypt(ctx, shift,*,msg):
    await ctx.channel.send(caesarcipher.cipher_encrypt(msg,int(shift)))

@client.command(brief = "Odszyfrowuje wiadomość napisaną szyfrem cezara")
async def cdecrypt(ctx, shift,*,msg):
    await ctx.channel.send(caesarcipher.cipher_decrypt(msg,int(shift)))

@client.command(brief = "test")
async def dmtest(ctx, uid,*,msg):
    user = await client.fetch_user(uid)
    channel = await user.create_dm()
    await channel.send(msg)

@client.command(brief="Wynik z odejmowania")
async def subt(ctx, x, y):
    try:
        wynik = float(x)-float(y)
        if str(wynik).endswith(".0"):
            wynik = round(wynik)
        await ctx.channel.send(f"{x}-{y}="+str(wynik))
    except:
        await ctx.channel.send("To nie są poprawne liczby!")

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
    f = open('slimak.txt',encoding='utf-8')
    slimakhuj = f.readlines()
    # await asyncio.sleep(0.01)   #nie wiem po co to tu w sumie dałem ale dla pewności zostawie bo czemu nie
    randomslimak = random.randint(0,len(slimakhuj)-1)
    await ctx.send(slimakhuj[randomslimak])

    #await client.get_guild(338268917497856001).get_channel(706908751424258128).send("Test")

@client.command(brief="Pokazuje informacje o Tobie albo o oznaczonej osobie")
async def id(ctx):
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


@client.command(brief = f"Twój avatar (bezużyteczne bo {prefix}id istnieje)")
async def avatar(ctx):
    if len(ctx.message.mentions)>0:
        embed=discord.Embed(title="avatar "+str(ctx.message.mentions[0]), color=0xFF5733)
        embed.set_image(url = ctx.message.mentions[0].avatar_url)
        await ctx.send(embed=embed)
    else:
        embed=discord.Embed(title=ctx.author.display_name, description="twój avatar", color=0xff0000)
        embed.set_image(url = ctx.author.avatar_url)
        await ctx.send(embed=embed)

@client.command(brief = f"Avatar ale wpisujesz id i tlye w sumie xd")
async def avatarid(ctx, id):
    user = await client.fetch_user(id)
    embed=discord.Embed(title='', color=0xFF5733)
    embed.set_image(url = user.avatar_url)
    await ctx.send(embed=embed)

@client.command(brief = f"Ankieta")
async def poll(ctx, a, b=None, c=None, d=None, e=None, f=None):
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


#@client.command(pass_context=True, brief="Dołącza do kanału i to w sumie tyle")
#async def join(ctx):
#    channel = ctx.author.voice.channel
#    voice = await channel.connect()
#    source = FFmpegPCMAudio('cwel.mp3')
#    player = voice.play(source)

#@client.command(brief="Wychodzi z kanału")
#async def dc(ctx):
#    await ctx.voice_client.disconnect()

@client.command(brief='Zmienia nick czy cos idk')
async def nick(ctx, member: discord.Member,*, nick):
    await member.edit(nick=nick)
    await ctx.send(f'Zmieniono nick {member} na: {member.mention} ')

@client.command(brief="IQ Szymona")
async def iqsobiego(ctx):
    f = open("iq.txt","r")
    content = int(f.read()) - 1
    f.close()
    f = open("iq.txt","w")
    f.write(str(content))
    f.close()
    await ctx.send(f'Sobi ma {content} IQ')

@client.command(brief="Pokazuje prawdziwą liczbę ojców Gabriela")
async def starzygabrysia(ctx):
    f = open("starzy.txt","r")
    content = int(f.read()) + 1
    f.close()
    f = open("starzy.txt","w")
    f.write(str(content))
    f.close()
    await ctx.send(f"Gabryś ma {content} ojców")


@client.command(brief="Losuje randomową liczbę w wybranym zakresie")
async def roll(ctx,a,b):
    await ctx.send(str(random.randint(int(a),int(b))))

@client.command(brief="Randomowa strona nhentai do id 356714 :)")
async def nhentai(ctx):
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

@client.command(brief="Kopnij se sobiego :)")
async def rndmalpa(ctx):
    malpy = monkies.malpiszony
    mKeys = list(malpy.keys())
    randomLang = mKeys[random.randint(0,len(mKeys)-1)]
    randomLangMonky = malpy.get(randomLang)
    embed=discord.Embed(title='Randomowa małpa')
    embed.add_field(name=randomLang, value=randomLangMonky, inline=False)
    await ctx.send(embed=embed)



@client.command(brief="Mój kolega :)")
async def czechu(ctx):
    await ctx.channel.send('<@327742627233398784>')

@client.command(brief="Gra komputerowa")
async def ligalegend(ctx):
    await ctx.channel.send('Liga Legend to kurwa, nie graj w to')

@client.command(brief="Usuwa x wiadomości")
@has_permissions(manage_messages=True)
async def clear(ctx,amount=1):
    if ctx.message.author.id == 328989571947823104 or ctx.message.author.id == 252217902202093568:
        if amount <= 20: 
            await ctx.channel.purge(limit=amount+1)
        else:
            await ctx.channel.send('pojebalo cie chyba')
    else:
        ctx.channel.send("nie jestes dababy pierdol sei")

@client.command(brief="Slotsy")
async def slots(ctx, bet=1):
    # with open('balance.json', 'r') as balances:
    #     balance=balances.read()
    with open('balance.json', encoding='utf-8') as json_file:
        obj = json.load(json_file)
    emojis = ['<:diamond:836303727093743707>','<:monke:836303742034247752>','<:slots7:835924846072430592>','<:kuc:734732791413211186>']
    if str(ctx.message.author) not in obj:
            obj.update({str(ctx.message.author):50})
    stankonta = obj.get(str(ctx.message.author))
    if int(bet) > stankonta:
        await ctx.send(f'Nie stać cie na to (ale zawsze jest {prefix}freekasa <:tf:805707103628951592>)')
    elif int(bet) < 1:
        await ctx.send(f'Chciało sie pocheatować co <:tf:805707103628951592>')
    else:
        slot1 = emojis[random.randint(0,len(emojis)-1)]
        slot2 = emojis[random.randint(0,len(emojis)-1)]
        slot3 = emojis[random.randint(0,len(emojis)-1)]

        if slot1 == slot2 == slot3 == '<:diamond:836303727093743707>':
            obj.update({str(ctx.message.author):stankonta+bet*25})
            wincheck = 'wygrałeś'
        elif slot1 == slot2 == slot3 == '<:monke:836303742034247752>':
            obj.update({str(ctx.message.author):stankonta+bet*50})
            wincheck = 'wygrałeś'
        elif slot1 == slot2 == slot3 == '<:slots7:835924846072430592>':
            obj.update({str(ctx.message.author):stankonta+bet*75})
            wincheck = 'wygrałeś'
        elif slot1 == slot2 == slot3 == '<:kuc:734732791413211186>':
            obj.update({str(ctx.message.author):stankonta+bet*5})
            wincheck = 'wygrałeś'  
        else: 
            obj.update({str(ctx.message.author):stankonta-int(bet)})
            # Podatek od przegranej bo też musze z czegoś żyć
            if ctx.message.author.id != 252217902202093568:
                stankonta1 = obj.get('sevu#0849')
                obj.update({'sevu#0849':stankonta1+int(bet/8)+1})
            wincheck = 'przegrałeś'

        with open('balance.json','w') as balances:
            json.dump(obj, balances)
        balances.close()

        embed1=discord.Embed(title=f"Slotsy {ctx.message.author}")
        embed1.add_field(name="1", value=f"{slot1}", inline=True)
        embed1.add_field(name="2", value=f"{slot2}", inline=True)
        embed1.add_field(name="3", value=f"{slot3}", inline=True)
        embed1.set_footer(text=f"stan konta: {obj.get(str(ctx.message.author))}")

        embed2=discord.Embed(title=f"Slotsy {ctx.message.author}")
        embed2.add_field(name="1", value=f"<a:rolling:836322964931608586>", inline=True)
        embed2.add_field(name="2", value=f"<a:rolling:836322964931608586>", inline=True)
        embed2.add_field(name="3", value=f"<a:rolling:836322964931608586>", inline=True)
        embed2.set_footer(text=f"stan konta: ")

        msg = await ctx.send(embed=embed2)
        await asyncio.sleep(0.7)
        await msg.edit(embed=embed1)



@client.command(brief="ruleta")
async def ruletka(ctx, bet, color):
    with open('balance.json', encoding='utf-8') as json_file:
        obj = json.load(json_file)
    #Kolejność w liście: B - R - G
    emojisselected = ['<:black:836695075646865458>','<:red:836677875235160094>','<:green:836850106740637696>']

    bet = int(bet)

    number = random.randint(0,19)
    if (number % 2) == 0 and number != 0:
        slot1 = emojisselected[1]
    if (number % 2) == 1:
        slot1 = emojisselected[0]
    if number == 0:
        slot1 = emojisselected[2]

    #wiem że to wygląda okropnie ale jak robiłem to inaczej to nie działało
    if color == 'r' or color == 'b' or color == 'g': 
        if str(ctx.message.author) not in obj:
                obj.update({str(ctx.message.author):50})
        stankonta = obj.get(str(ctx.message.author))
        if int(bet) > stankonta:
            await ctx.send(f'Nie stać cie na to (ale zawsze jest {prefix}freekasa <:tf:805707103628951592>)')
        elif int(bet) < 1:
            await ctx.send(f'Chciało sie pocheatować co <:tf:805707103628951592>')
        else:
            # slot1 = emojisselected[random.randint(0,len(emojisselected)-1)]

            if slot1 == emojisselected[1]:
                slotL = '<:black:836695075646865458>'
                slotR = '<:black:836695075646865458>'

            if slot1 == emojisselected[0]:
                slotL = '<:red:836677875235160094>'
                slotR = '<:red:836677875235160094>'

            if slot1 == emojisselected[2]:
                slotL = '<:red:836677875235160094>'
                slotR = '<:black:836695075646865458>'

            if slot1 == '<:red:836677875235160094>' and color == 'r':
                obj.update({str(ctx.message.author):stankonta+bet})
                wincheck = 'wygrałeś'

            elif slot1 == '<:black:836695075646865458>' and color == 'b':
                obj.update({str(ctx.message.author):stankonta+bet})
                wincheck = 'wygrałeś'
            
            elif slot1 == '<:green:836850106740637696>' and color == 'g':
                obj.update({str(ctx.message.author):stankonta+bet*14})
                wincheck = 'wygrałeś'

            else: 
                obj.update({str(ctx.message.author):stankonta-int(bet)})
                if ctx.message.author.id != 252217902202093568:
                    stankonta1 = obj.get('sevu#0849')
                    obj.update({'sevu#0849':stankonta1+int(bet/8)+1})
                wincheck = 'przegrałeś'

            with open('balance.json','w') as balances:
                json.dump(obj, balances)
            balances.close()

            embed2=discord.Embed(title=f"Ruletka {ctx.message.author}")
            embed2.add_field(name="-", value=f"{slotL}", inline=True)
            embed2.add_field(name="⬇️", value=f"{slot1}", inline=True)
            embed2.add_field(name="-", value=f"{slotR}", inline=True)
            embed2.set_footer(text=f"stan konta: {obj.get(str(ctx.message.author))}")

            embed1=discord.Embed(title=f"Ruletka {ctx.message.author}")
            embed1.add_field(name="-", value=f"<a:roulette:836696081994743879>", inline=True)
            embed1.add_field(name="⬇️", value=f"<a:roulette2:836697084266676274>", inline=True)
            embed1.add_field(name="-", value=f"<a:roulette:836696081994743879>", inline=True)
            embed1.set_footer(text=f"stan konta: ")

            msg = await ctx.send(embed=embed1)
            await asyncio.sleep(0.7)
            await msg.edit(embed=embed2)
    else:
        await ctx.send('Nie ma takiego koloru!')

@client.command(brief="crash")
async def crash(ctx, bet, multiplier):
    multiplier = float(multiplier)
    bet = int(bet)
    with open('balance.json', encoding='utf-8') as json_file:
        obj = json.load(json_file)
    rndmultiplier = (random.randint(1,100)/10)
    stankonta = int(obj.get(str(ctx.message.author)))
    stankonta = float(stankonta)
    if bet > stankonta:
        await ctx.send(f'Nie stać cie na to (ale zawsze jest {prefix}freekasa <:tf:805707103628951592>)')
    elif bet < 1:
        await ctx.send(f'Chciało sie pocheatować co <:tf:805707103628951592>')
    elif multiplier <= rndmultiplier:
        obj.update({str(ctx.message.author):stankonta+bet*multiplier})
        embed=discord.Embed(title="Crash", description=f"Wygrałeś {bet*multiplier}", color=0x00ff08)
        embed.add_field(name="Crashed at:", value=f"{rndmultiplier}", inline=True)
        embed.add_field(name="Twój mnożnik:", value=f"{multiplier}", inline=True)
        embed.set_footer(text=f"stan konta: {obj.get(str(ctx.message.author))}")
        await ctx.send(embed=embed)
    elif multiplier > rndmultiplier:
        obj.update({str(ctx.message.author):stankonta-int(bet)})
        embed=discord.Embed(title="Crash", description="Przegrałeś", color=0xff0000)
        embed.add_field(name="Crashed at:", value=f"{rndmultiplier}", inline=True)
        embed.add_field(name="Twój mnożnik:", value=f"{multiplier}", inline=True)
        embed.set_footer(text=f"stan konta: {obj.get(str(ctx.message.author))}")
        await ctx.send(embed=embed)
    with open('balance.json','w') as balances:
        json.dump(obj, balances)
    balances.close()
    

@client.command(brief="‎top 5 gambling addictów")
async def members(ctx):
    member_list = ''
    for member in ctx.message.guild.members:
        member_list += member.name
    print(member_list)

@client.command(brief="‎top 5 gambling addictów")
async def balancetop(ctx):
    with open('balance.json', encoding='utf-8') as f:
        gambling = json.load(f)
    marklist = sorted(gambling.items(), key=lambda item: item[1], reverse=True)
    sortdict = dict(marklist)
    # sort = json.dumps(sortdict, indent=0)
    bkeys = list(sortdict)
    bvalues = list(sortdict.values())
    embed=discord.Embed(title="Top 5 gambling addictów")
    num = 0
    for i in range(5):
        if 0 <= num < len(bkeys):
            embed.add_field(name=f"{bkeys[num]}", value=f"{bvalues[num]}", inline=False)
        else:
            break
        num += 1
    await ctx.send(embed=embed)

@client.command(brief="")
async def balance(ctx):
    with open('balance.json', encoding='utf-8') as json_file:
            obj = json.load(json_file)
    if len(ctx.message.mentions)>0:
        #embed=discord.Embed(title=str(ctx.message.mentions[0]), color=0xFF5733)
        await ctx.send(f"Stan konta {ctx.message.mentions[0]}: {obj.get(str(ctx.message.mentions[0]))}")
    else:
        await ctx.send(f"Twój stan konta: {obj.get(str(ctx.message.author))}")
    
@client.command(brief="przelew oznaczonej osobie")
async def przelew(ctx, amount=1):
    with open('balance.json', encoding='utf-8') as json_file:
        obj = json.load(json_file)
    stankonta1 = obj.get(str(ctx.message.author))
    stankonta2 = obj.get(str(ctx.message.mentions[0]))
    if amount > stankonta1:
        await ctx.send('Nie stać cie na to')
    if amount < 0:
        await ctx.send('Jebany złodziej')
    else:
        obj.update({str(ctx.message.author):stankonta1-amount})
        obj.update({str(ctx.message.mentions[0]):stankonta2+amount})
        with open('balance.json','w') as balances:
            json.dump(obj, balances)
        balances.close()    
        await ctx.send(f"Przelano {amount} użytkownikowi {ctx.message.mentions[0]}")

@client.command(brief="tu sie kupuje")
async def sklep(ctx, option=''):
    with open('balance.json', encoding='utf-8') as json_file:
        obj = json.load(json_file)
    stankonta = obj.get(str(ctx.message.author))
    if option == '':
        embed=discord.Embed(title="Sklep", description=f"{prefix}sklep <opcja>", color=0x00a7b3)
        embed.add_field(name="1. Uzależnieniec...", value="100000", inline=True)
        embed.add_field(name="2. 5 pingów @everyone", value="25000", inline=True)
        embed.add_field(name="3. 5 pingów Sobiego", value="100", inline=True)
        embed.add_field(name="4. Autograf", value="10", inline=True)
        embed.set_footer(text=f"stan konta: {obj.get(str(ctx.message.author))}")
        await ctx.send(embed=embed)
    elif option == '1':
        price = 100000
        if price > stankonta:
            await ctx.send('Nie stać cie na to')
        else:
            obj.update({str(ctx.message.author):stankonta-price})
            member = ctx.message.author
            role = discord.utils.get(member.guild.roles, name='Gambling addict')
            await member.add_roles(role)
    elif option == '2':
        price = 25000
        if price > stankonta:
            await ctx.send('Nie stać cie na to')
        else:
            obj.update({str(ctx.message.author):stankonta-price})
            for i in range(5):
                await ctx.send(f"{ctx.message.guild.default_role}  <:tf:805707103628951592>")
                await asyncio.sleep(0.7)
    elif option == '3':
        price = 100
        if price > stankonta:
            await ctx.send('Nie stać cie na to')
        else:
            obj.update({str(ctx.message.author):stankonta-price})
            for i in range(5):
                await ctx.send('<@439848715264720896>')
                await asyncio.sleep(0.7)
    elif option == '4':
        price = 10
        if price > stankonta:
            await ctx.send('Nie stać cie na to')
        else:
            obj.update({str(ctx.message.author):stankonta-price})
            embed=discord.Embed(title="Mój autograf specjalnie dla ciebie :)")
            embed.set_image(url = 'https://i.imgur.com/pnNGFSw.png')
            await ctx.send(embed=embed)
    else:
        await ctx.send('nie ma takiej opcji')

    with open('balance.json','w') as balances:
        json.dump(obj, balances)
    balances.close()


@client.command(brief="free kasa wtf?")
async def freekasa(ctx):
    with open('balance.json', encoding='utf-8') as json_file:
        obj = json.load(json_file)
    check = obj.get(str(ctx.message.author))
    if check == 0:
        obj.update({str(ctx.message.author):20})
        await ctx.send(':)')
    with open('balance.json','w') as balances:
            json.dump(obj, balances)
    balances.close()
    

@client.command(brief="host info")
async def hostinfo(ctx):
    myCmd = int(os.popen('cat /sys/class/thermal/thermal_zone0/temp').read())
    await ctx.send(f'CPU temp: {myCmd/1000} °C')

@client.command(brief="krowa mówi wtf?", description='https://en.wikipedia.org/wiki/Cowsay')
async def cowsay(ctx,*,msg):
    myCmd = os.popen(f'cowsay {msg}').read()
    await ctx.send(f'```{myCmd}```')

@client.command(brief="wolny ram")
async def freem(ctx):
    myCmd = os.popen(f'free -h -m').read()
    await ctx.send(f'```{myCmd}```')

@client.command(brief="‎")
async def nic(ctx):
    await ctx.send('‎\n'*40)

@client.command(brief="link do bota")
async def invite(ctx):
    await ctx.send('‎https://discord.com/oauth2/authorize?client_id=811696300285362207&scope=bot&permissions=8')


@client.command(brief="Status komend używających plików")
async def filestatus(ctx):
    f = open("iq.txt","r")
    f2 = open("starzy.txt","r")
    content = f.read()
    content2 = f2.read()
    f.close()
    f2.close()
    await ctx.channel.send(f'iq: {content}; starzy: {content2}')

# @client.command(brief=":tf:")
# async def pong(ctx):
#     await ctx.send(f"{ctx.message.guild.default_role}  <:tf:805707103628951592>")

@client.command(brief="Losowy fakt")
async def randomfact(ctx):
    facts =["wojtek to calkiem gejowe imie",
            'Ilość ojców gabrysia można poznać za pomocą komendy '+prefix+'starzygabrysia',
            'Sobi lubi grać w grę valorant','Jan Popczyk nie znosi żydów',
            'ten bot jest bezużyteczny','jakub kuc dostał dmuchaną lale',
            'superwojtek3000 zmienił nazwę kanału na Woitaz',
            'kurwa mać']
    await ctx.send(str(facts[random.randint(0,len(facts)-1)]))

@client.command(brief=f"Translator (Lista kodów: https://is.gd/VwiXUH)")
async def translate(ctx,fromlang,tolang,*,text):
    translator= Translator(to_lang=tolang, from_lang=fromlang)
    translation = translator.translate(text)
    # await ctx.send(translation)
    embed=discord.Embed(title="Translator")
    embed.add_field(name=f"{fromlang}".upper(), value=f"{text}", inline=True)
    embed.add_field(name=f"{tolang}".upper(), value=f"{translation}", inline=True)
    await ctx.send(embed=embed)

@client.command(brief="Nasz kolega :)")
async def zagusi(ctx):
    f = open('zagus1.txt')
    content = f.read()
    f.close()
    zaguslista = content.splitlines()
    msg = await ctx.channel.send(":grinning:                                                     :woman_red_haired: ")
    for i in zaguslista:
        await asyncio.sleep(1)
        await msg.edit(content=i)






client.run(bottoken.token)
