import discord
from discord.ext import commands
from cog import config
from cog import embedconfig
from cog import embedtrack

class eventbot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()    
    async def on_message(
        self,
        message
    ):
        if message.author == self.bot.user:
            return
        if "fire" in message.content.split()[0]:
            await message.channel.send(content=config.x3Fire)
        if "Fire" in message.content.split()[0]:
            await message.channel.send(content=config.x3Fire)
        if "1-1" in message.content.split()[0]:
            await message.channel.send(embed=embedtrack.embedMKS)
        if "1-2" in message.content.split()[0]:
            await message.channel.send(embed=embedtrack.embedWP)
        if "1-3" in message.content.split()[0]:
            await message.channel.send(embed=embedtrack.embedSSC)
        if "1-4" in message.content.split()[0]:
            await message.channel.send(embed=embedtrack.embedTR)
        if "2-1" in message.content.split()[0]:
            await message.channel.send(embed=embedtrack.embedMC)
        if "2-2" in message.content.split()[0]:
            await message.channel.send(embed=embedtrack.embedTH)
        if "2-3" in message.content.split()[0]:
            await message.channel.send(embed=embedtrack.embedTM)
        if "2-4" in message.content.split()[0]:
            await message.channel.send(embed=embedtrack.embedSGF)
        if "3-1" in message.content.split()[0]:
            await message.channel.send(embed=embedtrack.embedSA)
        if "3-2" in message.content.split()[0]:
            await message.channel.send(embed=embedtrack.embedDS)
        if "3-3" in message.content.split()[0]:
            await message.channel.send(embed=embedtrack.embedEd)
        if "3-4" in message.content.split()[0]:
            await message.channel.send(embed=embedtrack.embedMW)
        if "4-1" in message.content.split()[0]:
            await message.channel.send(embed=embedtrack.embedCC)
        if "4-2" in message.content.split()[0]:
            await message.channel.send(embed=embedtrack.embedBDD)
        if "4-3" in message.content.split()[0]:
            await message.channel.send(embed=embedtrack.embedBC)
        if "4-4" in message.content.split()[0]:
            await message.channel.send(embed=embedtrack.embedRR)
        if "5-1" in message.content.split()[0]:
            await message.channel.send(embed=embedtrack.embeddYC)
        if "5-2" in message.content.split()[0]:
            await message.channel.send(embed=embedtrack.embeddEA)
        if "5-3" in message.content.split()[0]:
            await message.channel.send(embed=embedtrack.embeddDD)
        if "5-4" in message.content.split()[0]:
            await message.channel.send(embed=embedtrack.embeddMC)
        if "6-1" in message.content.split()[0]:
            await message.channel.send(embed=embedtrack.embeddBP)
        if "6-2" in message.content.split()[0]:
            await message.channel.send(embed=embedtrack.embeddCL)
        if "6-3" in message.content.split()[0]:
            await message.channel.send(embed=embedtrack.embeddWW)
        if "6-4" in message.content.split()[0]:
            await message.channel.send(embed=embedtrack.embeddAC)
        if "7-1" in message.content.split()[0]:
            await message.channel.send(embed=embedtrack.embeddrMMM)
        if "7-2" in message.content.split()[0]:
            await message.channel.send(embed=embedtrack.embedrMC)
        if "7-3" in message.content.split()[0]:
            await message.channel.send(embed=embedtrack.embedrCCB)
        if "7-4" in message.content.split()[0]:
            await message.channel.send(embed=embedtrack.embedrTT)
        if "8-1" in message.content.split()[0]:
            await message.channel.send(embed=embedtrack.embedrDDD)
        if "8-2" in message.content.split()[0]:
            await message.channel.send(embed=embedtrack.embedrDP3)
        if "8-3" in message.content.split()[0]:
            await message.channel.send(embed=embedtrack.embedrRRy)
        if "8-4" in message.content.split()[0]:
            await message.channel.send(embed=embedtrack.embedrDKJ)
        if "9-1" in message.content.split()[0]:
            await message.channel.send(embed=embedtrack.embedrWS)
        if "9-2" in message.content.split()[0]:
            await message.channel.send(embed=embedtrack.embeddrSL)
        if "9-3" in message.content.split()[0]:
            await message.channel.send(embed=embedtrack.embedrMP)
        if "9-4" in message.content.split()[0]:
            await message.channel.send(embed=embedtrack.embedrYV)
        if "10-1" in message.content.split()[0]:
            await message.channel.send(embed=embedtrack.embedrTTC)
        if "10-2" in message.content.split()[0]:
            await message.channel.send(embed=embedtrack.embedrPPS)
        if "10-3" in message.content.split()[0]:
            await message.channel.send(embed=embedtrack.embedrGV)
        if "10-4" in message.content.split()[0]:
            await message.channel.send(embed=embedtrack.embedrRRd)
        if "11-1" in message.content.split()[0]:
            await message.channel.send(embed=embedtrack.embeddWGM)
        if "11-2" in message.content.split()[0]:
            await message.channel.send(embed=embedtrack.embeddRR)
        if "11-3" in message.content.split()[0]:
            await message.channel.send(embed=embedtrack.embeddIIO)
        if "11-4" in message.content.split()[0]:
            await message.channel.send(embed=embedtrack.embeddHC)
        if "12-1" in message.content.split()[0]:
            await message.channel.send(embed=embedtrack.embeddNBC)
        if "12-2" in message.content.split()[0]:
            await message.channel.send(embed=embedtrack.embeddRiR)
        if "12-3" in message.content.split()[0]:
            await message.channel.send(embed=embedtrack.embeddSBS)
        if "12-4" in message.content.split()[0]:
            await message.channel.send(embed=embedtrack.embeddBB)


async def setup(bot):
    await bot.add_cog(eventbot(bot))