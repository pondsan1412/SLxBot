# bot.py
from dotenv import load_dotenv
from email import message
from unicodedata import name
import time
import asyncio
import functools
import itertools
import math
import random
import os
from async_timeout import timeout
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

status = 0
bot = commands.Bot(command_prefix='.', intents=intents)

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"{client.user} has to connected Discord!")


@client.event
async def on_ready():
    print('The bot is connecting to Discord.')
    while True:
        await client.change_presence(activity=discord.Game(name=f"{len(client.guilds)} servers!"))
        await asyncio.sleep(1)

@client.event
async def on_message(message):
#1-1
    if message.content.startswith('.1-1'):#MKS number
        embedVar = discord.Embed(title="Mushroom Cup", description="Track code: MKS", color=0x9c46ff)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/1066340666436747304/1066342531597606912/MKS.png")
        embedVar.add_field(name="Mario Kart Stadium", value="European code: 1-1", inline=False)
        embedVar.set_footer(text='Developed by Silent Lightning', icon_url="https://cdn.discordapp.com/attachments/1066363054473883658/1066363539377369128/Silent_Lightning.png")
        embedVar.set_thumbnail(url="https://cdn.discordapp.com/attachments/1066340666436747304/1066342499989327892/MK8_MushroomCup.png")
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.mks'):#mks text
        embedVar = discord.Embed(title="Mushroom Cup", description="Track code: MKS", color=0x9c46ff)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/1066340666436747304/1066342531597606912/MKS.png")
        embedVar.add_field(name="Mario Kart Stadium", value="European code: 1-1", inline=False)
        embedVar.set_footer(text='Developed by Silent Lightning', icon_url="https://cdn.discordapp.com/attachments/1066363054473883658/1066363539377369128/Silent_Lightning.png")
        embedVar.set_thumbnail(url="https://cdn.discordapp.com/attachments/1066340666436747304/1066342499989327892/MK8_MushroomCup.png")
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.MKS'):#MKS text
        embedVar = discord.Embed(title="Mushroom Cup", description="Track code: MKS", color=0x9c46ff)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/1066340666436747304/1066342531597606912/MKS.png")
        embedVar.add_field(name="Mario Kart Stadium", value="European code: 1-1", inline=False)
        embedVar.set_footer(text='Developed by Silent Lightning', icon_url="https://cdn.discordapp.com/attachments/1066363054473883658/1066363539377369128/Silent_Lightning.png")
        embedVar.set_thumbnail(url="https://cdn.discordapp.com/attachments/1066340666436747304/1066342499989327892/MK8_MushroomCup.png")
        await message.channel.send(embed=embedVar)
#1-2
    if message.content.startswith('.1-2'):#WP number
        embedVar = discord.Embed(title="Mushroom Cup", description="Track code: WP", color=0x9c46ff)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/1066340666436747304/1066342564564828210/WP.png")
        embedVar.add_field(name="Water Park", value="European code: 1-2", inline=False)
        embedVar.set_footer(text='Developed by Silent Lightning', icon_url="https://cdn.discordapp.com/attachments/1066363054473883658/1066363539377369128/Silent_Lightning.png")
        embedVar.set_thumbnail(url="https://cdn.discordapp.com/attachments/1066340666436747304/1066342499989327892/MK8_MushroomCup.png")
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.wp'):#wp text
        embedVar = discord.Embed(title="Mushroom Cup", description="Track code: WP", color=0x9c46ff)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/1066340666436747304/1066342564564828210/WP.png")
        embedVar.add_field(name="Water Park", value="European code: 1-2", inline=False)
        embedVar.set_footer(text='Developed by Silent Lightning', icon_url="https://cdn.discordapp.com/attachments/1066363054473883658/1066363539377369128/Silent_Lightning.png")
        embedVar.set_thumbnail(url="https://cdn.discordapp.com/attachments/1066340666436747304/1066342499989327892/MK8_MushroomCup.png")
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.WP'):#WP text
        embedVar = discord.Embed(title="Mushroom Cup", description="Track code: WP", color=0x9c46ff)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/1066340666436747304/1066342564564828210/WP.png")
        embedVar.add_field(name="Water Park", value="European code: 1-2", inline=False)
        embedVar.set_footer(text='Developed by Silent Lightning', icon_url="https://cdn.discordapp.com/attachments/1066363054473883658/1066363539377369128/Silent_Lightning.png")
        embedVar.set_thumbnail(url="https://cdn.discordapp.com/attachments/1066340666436747304/1066342499989327892/MK8_MushroomCup.png")
        await message.channel.send(embed=embedVar)
#1-3
    if message.content.startswith('.1-3'):#SSC number
        embedVar = discord.Embed(title="Mushroom Cup", description="Track code: SSC", color=0x9c46ff)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/1066340666436747304/1066342580461256785/SSC.png")
        embedVar.add_field(name="Sweet Sweet Canyon", value="European code: 1-3", inline=False)
        embedVar.set_footer(text='Developed by Silent Lightning', icon_url="https://cdn.discordapp.com/attachments/1066363054473883658/1066363539377369128/Silent_Lightning.png")
        embedVar.set_thumbnail(url="https://cdn.discordapp.com/attachments/1066340666436747304/1066342499989327892/MK8_MushroomCup.png")
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.ssc'):#ssc text
        embedVar = discord.Embed(title="Mushroom Cup", description="Track code: SSC", color=0x9c46ff)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/1066340666436747304/1066342580461256785/SSC.png")
        embedVar.add_field(name="Sweet Sweet Canyon", value="European code: 1-3", inline=False)
        embedVar.set_footer(text='Developed by Silent Lightning', icon_url="https://cdn.discordapp.com/attachments/1066363054473883658/1066363539377369128/Silent_Lightning.png")
        embedVar.set_thumbnail(url="https://cdn.discordapp.com/attachments/1066340666436747304/1066342499989327892/MK8_MushroomCup.png")
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.SSC'):#SSC text
        embedVar = discord.Embed(title="Mushroom Cup", description="Track code: SSC", color=0x9c46ff)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/1066340666436747304/1066342580461256785/SSC.png")
        embedVar.add_field(name="Thwomp Ruins", value="European code: 1-3", inline=False)
        embedVar.set_footer(text='Developed by Silent Lightning', icon_url="https://cdn.discordapp.com/attachments/1066363054473883658/1066363539377369128/Silent_Lightning.png")
        embedVar.set_thumbnail(url="https://cdn.discordapp.com/attachments/1066340666436747304/1066342499989327892/MK8_MushroomCup.png")
        await message.channel.send(embed=embedVar)
#1-4
    if message.content.startswith('.1-4'):#TR number
        embedVar = discord.Embed(title="Mushroom Cup", description="Track code: SSC", color=0x9c46ff)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/1066340666436747304/1066342595904667699/TR.png")
        embedVar.add_field(name="Thwomp Ruins", value="European code: 1-4", inline=False)
        embedVar.set_footer(text='Developed by Silent Lightning', icon_url="https://cdn.discordapp.com/attachments/1066363054473883658/1066363539377369128/Silent_Lightning.png")
        embedVar.set_thumbnail(url="https://cdn.discordapp.com/attachments/1066340666436747304/1066342499989327892/MK8_MushroomCup.png")
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.tr'):#tr text
        embedVar = discord.Embed(title="Mushroom Cup", description="Track code: SSC", color=0x9c46ff)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/1066340666436747304/1066342595904667699/TR.png")
        embedVar.add_field(name="Sweet Sweet Canyon", value="European code: 1-4", inline=False)
        embedVar.set_footer(text='Developed by Silent Lightning', icon_url="https://cdn.discordapp.com/attachments/1066363054473883658/1066363539377369128/Silent_Lightning.png")
        embedVar.set_thumbnail(url="https://cdn.discordapp.com/attachments/1066340666436747304/1066342499989327892/MK8_MushroomCup.png")
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.TR'):#TR text
        embedVar = discord.Embed(title="Mushroom Cup", description="Track code: SSC", color=0x9c46ff)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/1066340666436747304/1066342595904667699/TR.png")
        embedVar.add_field(name="Thwomp Ruins", value="European code: 1-4", inline=False)
        embedVar.set_footer(text='Developed by Silent Lightning', icon_url="https://cdn.discordapp.com/attachments/1066363054473883658/1066363539377369128/Silent_Lightning.png")
        embedVar.set_thumbnail(url="https://cdn.discordapp.com/attachments/1066340666436747304/1066342499989327892/MK8_MushroomCup.png")
        await message.channel.send(embed=embedVar)
#2-1
    if message.content.startswith('.2-1'):#MC number
        embedVar = discord.Embed(title="Flower Cup", description="Track code: MC", color=0x9c46ff)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/1066340666436747304/1066342777845207152/MC.png")
        embedVar.add_field(name="Mario Circuit", value="European code: 2-1", inline=False)
        embedVar.set_footer(text='Developed by Silent Lightning', icon_url="https://cdn.discordapp.com/attachments/1066363054473883658/1066363539377369128/Silent_Lightning.png")
        embedVar.set_thumbnail(url="https://cdn.discordapp.com/attachments/1066340666436747304/1066342645451989062/MK8_FlowerCup.png")
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.mc'):#mc text
        embedVar = discord.Embed(title="Flower Cup", description="Track code: MC", color=0x9c46ff)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/1066340666436747304/1066342777845207152/MC.png")
        embedVar.add_field(name="Mario Circuit", value="European code: 2-1", inline=False)
        embedVar.set_footer(text='Developed by Silent Lightning', icon_url="https://cdn.discordapp.com/attachments/1066363054473883658/1066363539377369128/Silent_Lightning.png")
        embedVar.set_thumbnail(url="https://cdn.discordapp.com/attachments/1066340666436747304/1066342645451989062/MK8_FlowerCup.png")
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.MC'):#MC text
        embedVar = discord.Embed(title="Flower Cup", description="Track code: MC", color=0x9c46ff)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/1066340666436747304/1066342777845207152/MC.png")
        embedVar.add_field(name="Mario Circuit", value="European code: 2-1", inline=False)
        embedVar.set_footer(text='Developed by Silent Lightning', icon_url="https://cdn.discordapp.com/attachments/1066363054473883658/1066363539377369128/Silent_Lightning.png")
        embedVar.set_thumbnail(url="https://cdn.discordapp.com/attachments/1066340666436747304/1066342645451989062/MK8_FlowerCup.png")
        await message.channel.send(embed=embedVar)
#2-2
    if message.content.startswith('.2-2'):#TH number
        embedVar = discord.Embed(title="Flower Cup", description="Track code: TH", color=0x9c46ff)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/1066340666436747304/1066342794026823790/TH.png")
        embedVar.add_field(name="Toad Harbor", value="European code: 2-2", inline=False)
        embedVar.set_footer(text='Developed by Silent Lightning', icon_url="https://cdn.discordapp.com/attachments/1066363054473883658/1066363539377369128/Silent_Lightning.png")
        embedVar.set_thumbnail(url="https://cdn.discordapp.com/attachments/1066340666436747304/1066342645451989062/MK8_FlowerCup.png")
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.th'):#th text
        embedVar = discord.Embed(title="Flower Cup", description="Track code: TH", color=0x9c46ff)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/1066340666436747304/1066342794026823790/TH.png")
        embedVar.add_field(name="Toad Harbor", value="European code: 2-2", inline=False)
        embedVar.set_footer(text='Developed by Silent Lightning', icon_url="https://cdn.discordapp.com/attachments/1066363054473883658/1066363539377369128/Silent_Lightning.png")
        embedVar.set_thumbnail(url="https://cdn.discordapp.com/attachments/1066340666436747304/1066342645451989062/MK8_FlowerCup.png")
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.TH'):#TH text
        embedVar = discord.Embed(title="Flower Cup", description="Track code: TH", color=0x9c46ff)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/1066340666436747304/1066342794026823790/TH.png")
        embedVar.add_field(name="Toad Harbor", value="European code: 2-2", inline=False)
        embedVar.set_footer(text='Developed by Silent Lightning', icon_url="https://cdn.discordapp.com/attachments/1066363054473883658/1066363539377369128/Silent_Lightning.png")
        embedVar.set_thumbnail(url="https://cdn.discordapp.com/attachments/1066340666436747304/1066342645451989062/MK8_FlowerCup.png")
        await message.channel.send(embed=embedVar)
#2-3
    if message.content.startswith('.2-3'):#TM number
        embedVar = discord.Embed(title="Flower Cup", description="Track code: TM", color=0x9c46ff)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/1066340666436747304/1066342811563208814/TM.png")
        embedVar.add_field(name="Twisted Mansion", value="European code: 2-3", inline=False)
        embedVar.set_footer(text='Developed by Silent Lightning', icon_url="https://cdn.discordapp.com/attachments/1066363054473883658/1066363539377369128/Silent_Lightning.png")
        embedVar.set_thumbnail(url="https://cdn.discordapp.com/attachments/1066340666436747304/1066342645451989062/MK8_FlowerCup.png")
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.tm'):#tm text
        embedVar = discord.Embed(title="Flower Cup", description="Track code: TM", color=0x9c46ff)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/1066340666436747304/1066342811563208814/TM.png")
        embedVar.add_field(name="Twisted Mansion", value="European code: 2-3", inline=False)
        embedVar.set_footer(text='Developed by Silent Lightning', icon_url="https://cdn.discordapp.com/attachments/1066363054473883658/1066363539377369128/Silent_Lightning.png")
        embedVar.set_thumbnail(url="https://cdn.discordapp.com/attachments/1066340666436747304/1066342645451989062/MK8_FlowerCup.png")
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.TM'):#TM text
        embedVar = discord.Embed(title="Flower Cup", description="Track code: TM", color=0x9c46ff)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/1066340666436747304/1066342811563208814/TM.png")
        embedVar.add_field(name="Twisted Mansion", value="European code: 2-3", inline=False)
        embedVar.set_footer(text='Developed by Silent Lightning', icon_url="https://cdn.discordapp.com/attachments/1066363054473883658/1066363539377369128/Silent_Lightning.png")
        embedVar.set_thumbnail(url="https://cdn.discordapp.com/attachments/1066340666436747304/1066342645451989062/MK8_FlowerCup.png")
        await message.channel.send(embed=embedVar)
#2-4
    if message.content.startswith('.2-4'):#SGF number
        embedVar = discord.Embed(title="Flower Cup", description="Track code: SGF", color=0x9c46ff)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/1066340666436747304/1066342840956899338/SGF.png")
        embedVar.add_field(name="Twisted Mansion", value="European code: 2-3", inline=False)
        embedVar.set_footer(text='Developed by Silent Lightning', icon_url="https://cdn.discordapp.com/attachments/1066363054473883658/1066363539377369128/Silent_Lightning.png")
        embedVar.set_thumbnail(url="https://cdn.discordapp.com/attachments/1066340666436747304/1066342645451989062/MK8_FlowerCup.png")
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.sgf'):#sgf text
        embedVar = discord.Embed(title="Flower Cup", description="Track code: SGF", color=0x9c46ff)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/1066340666436747304/1066342840956899338/SGF.png")
        embedVar.add_field(name="Twisted Mansion", value="European code: 2-3", inline=False)
        embedVar.set_footer(text='Developed by Silent Lightning', icon_url="https://cdn.discordapp.com/attachments/1066363054473883658/1066363539377369128/Silent_Lightning.png")
        embedVar.set_thumbnail(url="https://cdn.discordapp.com/attachments/1066340666436747304/1066342645451989062/MK8_FlowerCup.png")
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.SGF'):#SGF text
        embedVar = discord.Embed(title="Flower Cup", description="Track code: SGF", color=0x9c46ff)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/1066340666436747304/1066342840956899338/SGF.png")
        embedVar.add_field(name="Twisted Mansion", value="European code: 2-3", inline=False)
        embedVar.set_footer(text='Developed by Silent Lightning', icon_url="https://cdn.discordapp.com/attachments/1066363054473883658/1066363539377369128/Silent_Lightning.png")
        embedVar.set_thumbnail(url="https://cdn.discordapp.com/attachments/1066340666436747304/1066342645451989062/MK8_FlowerCup.png")
        await message.channel.send(embed=embedVar)
#3-1

#3-2

#3-3

#3-4

#4-1

#4-2

#4-3

#4-4

#5-1

#5-2

#5-3

#5-4

#6-1

#6-2

#6-3

#6-4

#7-1

#7-2

#7-3

#7-4

#8-1

#8-2 

#8-3 

#8-4

#9-1

#9-2

#9-3

#9-4

#10-1

#10-2

#10-3

#10-4

#11-1

#11-2

#11-3

#11-4

#12-1

#12-2

#12-3

#12-4

#13-1

#13-2

#13-3

#13-4

#14-1

#14-2

#14-3

#14-4

#15-1

#15-2

#15-3

#15-4

#16-1

#16-2

#16-3

#16-4

#17-1

#17-2

#17-3

#17-4

#18-1

#18-2

#18-3

#18-4

#19-1

#19-2

#19-3

#19-4

#20-1

#20-2

#20-3

#20-4
    if message.content.startswith('.20-4'):#bSSy number
        embedVar = discord.Embed(title="Boomerang Cup", description="Track code: bSSy", color=0x9c46ff)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/1066340666436747304/1085894036101009498/bSSy.png")
        embedVar.add_field(name="Singapore Speedway", value="European code: 20-4", inline=False)
        embedVar.set_footer(text='Developed by Silent Lightning', icon_url="https://cdn.discordapp.com/attachments/1066363054473883658/1066363539377369128/Silent_Lightning.png")
        embedVar.set_thumbnail(url="https://cdn.discordapp.com/attachments/1066340666436747304/1085893823189753876/MK8D_BCP_Boomerang_Emblem.png")
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.bssy'):#bssy text
        embedVar = discord.Embed(title="Boomerang Cup", description="Track code: bSSy", color=0x9c46ff)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/1066340666436747304/1085894036101009498/bSSy.png")
        embedVar.add_field(name="Singapore Speedway", value="European code: 20-4", inline=False)
        embedVar.set_footer(text='Developed by Silent Lightning', icon_url="https://cdn.discordapp.com/attachments/1066363054473883658/1066363539377369128/Silent_Lightning.png")
        embedVar.set_thumbnail(url="https://cdn.discordapp.com/attachments/1066340666436747304/1085893823189753876/MK8D_BCP_Boomerang_Emblem.png")
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.bSSy'):#bSSy text
        embedVar = discord.Embed(title="Boomerang Cup", description="Track code: bSSy", color=0x9c46ff)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/1066340666436747304/1085894036101009498/bSSy.png")
        embedVar.add_field(name="Singapore Speedway", value="European code: 20-4", inline=False)
        embedVar.set_footer(text='Developed by Silent Lightning', icon_url="https://cdn.discordapp.com/attachments/1066363054473883658/1066363539377369128/Silent_Lightning.png")
        embedVar.set_thumbnail(url="https://cdn.discordapp.com/attachments/1066340666436747304/1085893823189753876/MK8D_BCP_Boomerang_Emblem.png")
        await message.channel.send(embed=embedVar)
#21-1

#21-2

#21-3

#21-4

#22-1

#22-2

#22-3

#22-4

#23-1

#23-2

#23-3

#23-4

#24-1

#24-2

#24-3

#24-4

#25-1

#25-2

#25-3

#25-4
    if message.content.startswith('.help'):
        embedVar = discord.Embed(title=":star: Command for use the bot", description="prefix command using dot (.) infront of anytracks you want. please go with right words don't type only lowercase letter. for example > .dHC .rGV .dRR", color=0x00ff00)
        embedVar.set_thumbnail(url="https://media.tenor.com/images/1625d3706ed4a53aeba484e32fa8ea40/tenor.gif")
        embedVar.set_author(name="Pond サンダー ", url="https://twitter.com/pondsan1412", icon_url="https://cdn-icons-png.flaticon.com/512/124/124021.png")
        embedVar.add_field(name=":bookmark_tabs: Tracks code list",value='[sheet link for tracks code](https://docs.google.com/document/d/1P4CJbTEPskvFAREHMhZrkzSi5EJ3Onqlgyv3NRJyczw/edit?usp=sharing)',inline=False)
        embedVar.add_field(name=":magnet: invite bot to your server", value='[click here to create invite!](https://discord.com/api/oauth2/authorize?client_id=926061900813451264&permissions=517544007744&scope=bot)' , inline=False)
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
        
@bot.command()
async def rTT(ctx):
    rTT=discord.Embed(title="Toad's Turnpike",color=0xFF5733)
    rTT.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/967864470972010596/rTT.png")#rTT Track
    rTT.set_footer(text='Developed by Silent Lightning')
    message = await ctx.send(embed=rTT)
    await message.add_reaction('✅')
    await message.add_reaction('❌')

client.run(TOKEN)