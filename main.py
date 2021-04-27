import discord, bottoken, random, asyncio, caesarcipher, os, json
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


# @client.command(brief = "super quiz :)", description = "bajerancki quizior :D")
# async def quiz(ctx):
#     los = random.randint(0,9)
#     f = open(f'./cyfry/{los}.png', 'rb')
#     file = discord.File(f)
#     await ctx.send("Zgadnij co to za cyfra:")
#     await ctx.send(file=file)

#     def check(msg):
#         return msg.channel == ctx.channel

#     msg = await client.wait_for("message", check=check)
#     if msg.content.lower() == f"{los}":
#         await ctx.send("Brawo :)")
#     else:
#         await ctx.send("Debil")

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


# @client.command(brief = "Oznacza Gabrysia 6 razy co 2 sekundy")
# async def oznaczczecha(ctx):
#     for i in range(0,6):
#         await ctx.channel.send('<@327742627233398784>')
#         await asyncio.sleep(2)

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

            
# @client.event
# async def on_command_error(ctx, error):
#     if isinstance(error, commands.errors.CommandInvokeError):
#         await ctx.send("cos sie zepsuło :(")


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

# @client.command(brief = f"gej")
# async def test(ctx):
    
#     elif ctx.message.author.id == 252217902202093568:
#         await ctx.send("sperma")

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

@client.command(brief="Randomowa strona nhentai do id 355686 :)")
async def nhentai(ctx):
    FBI = True
    while FBI:
        id = random.randint(1,355686)
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
        elif slot1 == slot2 == slot3 == '<:monke:836303742034247752>':
            obj.update({str(ctx.message.author):stankonta+bet*50})
        elif slot1 == slot2 == slot3 == '<:slots7:835924846072430592>':
            obj.update({str(ctx.message.author):stankonta+bet*75})
        elif slot1 == slot2 == slot3 == '<:kuc:734732791413211186>':
            obj.update({str(ctx.message.author):stankonta+bet*5})
        # if slot1 == slot2 and slot2 == slot3:           
        #     obj.update({str(ctx.message.author):stankonta+bet*25})   
        else: 
            obj.update({str(ctx.message.author):stankonta-int(bet)})

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
        embed2.set_footer(text=f"stan konta: {obj.get(str(ctx.message.author))}")
        msg = await ctx.send(embed=embed2)
        await asyncio.sleep(0.7)
        await msg.edit(embed=embed1)


#<a:rolling:836322964931608586>
@client.command(brief="‎")
async def balancetop(ctx):
    with open('balance.json', encoding='utf-8') as json_file:
        obj = json.load(json_file)
    marklist = sorted(obj.items(), key=lambda item: item[1], reverse=True)
    sortdict = dict(marklist)
    chuj = json.dumps(sortdict, indent=0)
    bvalues = list(sortdict.values())
    bkeys = list(sortdict)
    embed=discord.Embed(title="Top 5")
    embed.add_field(name=f"{bkeys[0]}", value=f"{bvalues[0]}", inline=False)
    embed.add_field(name=f"{bkeys[1]}", value=f"{bvalues[1]}", inline=False)
    embed.add_field(name=f"{bkeys[2]}", value=f"{bvalues[2]}", inline=False)
    embed.add_field(name=f"{bkeys[3]}", value=f"{bvalues[3]}", inline=False)
    embed.add_field(name=f"{bkeys[4]}", value=f"{bvalues[4]}", inline=False)
    await ctx.send(embed=embed)
    # await ctx.send('```'+chuj[1:-1]+'```')


@client.command(brief="‎")
async def balance(ctx):
    with open('balance.json', encoding='utf-8') as json_file:
            obj = json.load(json_file)
    if len(ctx.message.mentions)>0:
        #embed=discord.Embed(title=str(ctx.message.mentions[0]), color=0xFF5733)
        await ctx.send(f"Stan konta {ctx.message.mentions[0]}: {obj.get(str(ctx.message.mentions[0]))}")
    else:
        await ctx.send(f"Twój stan konta: {obj.get(str(ctx.message.author))}")
    
@client.command(brief="‎przelew oznaczonej osobie")
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

@client.command(brief="‎free kasa wtf?")
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
    

@client.command(brief="‎")
async def nic(ctx):
    await ctx.send('‎\n'*40)

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