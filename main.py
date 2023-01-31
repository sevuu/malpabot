import discord, random, os
from discord.ext import commands, tasks
from lib import bottoken
from bs4 import BeautifulSoup
import urllib.request as urllib

prefix = '%'
client = commands.Bot(command_prefix = prefix)

@client.event
async def on_ready():
    print('dzialam kurwa {0.user}\nhttps://discord.com/oauth2/authorize?client_id=811696300285362207&scope=bot&permissions=8'.format(client))
    await client.change_presence(status=discord.Status.online, activity=discord.Game(f'piwko :)) | {prefix}help'))
    user = await client.fetch_user('252217902202093568')
    channel = await user.create_dm()
    await channel.send("Dziala")

# blacklist = ['kizo','_29dLT6OMTU','6E-gg25T84g','BjMcH1BF2hw',
# 'kDLbsNlNll8','DOs8S3Iwcvw','peQJOeAICWo','38pLR7eKA6k','rAiIrtEmsxg',
# 'Z-pmsb8UHuM','xN09Nwb1hzs','Rq1FPoGCTDg','N3XIi2zCNWQ','2MZrhk6slck','aEuk9FFqmsE',
# 'Qtp1Qb0pYGU','e-c0U6uQORw','pDg6mV79AC4','pF9Vn7VZhq0','k0QHxjnrpwU','EvSnWjbxu2o',
# '7Uj1YnKCo6w','yK3RPK3YnsI','lDV6UZL8DfQ','YvtvAhN2m8M','3n1wae0RJZ8','mPzUYmHsb4Y',
# 'MbwElOfRMWM','b-Hy7QxaCC0','AEM2EBs7TFQ','EYhCF2qeBA0','me5ge27XlL8','7YphHO9T9As',
# '1YwYCdH8u3c','7YphHO9T9As','ZqAAjoeu0m4','0TOvjoxPPxI','aJ1VQhU6Dlc','p-wBjqUjziA',
# 'MbwElOfRMWM','AEM2EBs7TFQ','EYhCF2qeBA0','me5ge27XlL8','1YwYCdH8u3c','JZ9WJsT83WQ',
# 'jBwgowp2g8Y','q-_KpAbdA2k','ZYcMAz4-hU8','9xqvyno21RQ','AzAIimi-_3I','8r0UCRxU1_M',
# 'Vs0c7Di3c94','rpG90ARD3fE','KGw1Np5Q9AY','lb0VZgWrkNY','4yN0RcYhG-A','iiWE2XkCInI',
# '6V8MYDMwknY','m3tLCwv1MNI','hUDFz7Jw-ag','t2a-RpJuqFE','XE5G004diWE','bvtzcGhd8FY',
# 'mRTYVIH6h0o','CSThbl1q0Gg','T_RAx6A5NCg','e0-eFD7i-vg','vqBxHt33q98','oc8pb9xv-WM']


# @client.event
# async def on_message(message):
#     if message.content.startswith("hej"):
#         await message.channel.send('cześć :)')

#     if message.content.startswith("sobi"):
#         await message.channel.send('łysol')
#     await client.process_commands(message)

#     if any(word in message.content.lower() for word in blacklist):
#         await message.channel.send("spierdalaj")
#         await message.author.kick()


@client.command()
async def load(ctx,extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx,extension):
    client.unload_extension(f'cogs.{extension}')

@client.command()
async def reload(ctx,extension):
    client.reload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(bottoken.token)
