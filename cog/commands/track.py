import discord
from discord.ext import commands
from cog import config
from cog import embedconfig
from cog import embedtrack


class trackbot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()    
    async def on_message(
        self,
        message
    ):
        try:
            if message.author == self.bot.user:
                return
            command = message.content.split()[0]
            if command == "1-1":
                await message.channel.send(embed=embedtrack.embedMKS)
            elif command == "1-2":
                await message.channel.send(embed=embedtrack.embedWP)
            elif command == "1-3":
                await message.channel.send(embed=embedtrack.embedSSC)
            elif command == "1-4":
                await message.channel.send(embed=embedtrack.embedTR)
            elif command == "2-1":
                await message.channel.send(embed=embedtrack.embedMC)
            elif command == "2-2":
                await message.channel.send(embed=embedtrack.embedTH)
            elif command == "2-3":
                await message.channel.send(embed=embedtrack.embedTM)
            elif command == "2-4":
                await message.channel.send(embed=embedtrack.embedSGF)
            elif command == "3-1":
                await message.channel.send(embed=embedtrack.embedSA)
            elif command == "3-2":
                await message.channel.send(embed=embedtrack.embedDS)
            elif command == "3-3":
                await message.channel.send(embed=embedtrack.embedEd)
            elif command == "3-4":
                await message.channel.send(embed=embedtrack.embedMW)
            elif command == "4-1":
                await message.channel.send(embed=embedtrack.embedCC)
            elif command == "4-2":
                await message.channel.send(embed=embedtrack.embedBDD)
            elif command == "4-3":
                await message.channel.send(embed=embedtrack.embedBC)
            elif command == "4-4":
                await message.channel.send(embed=embedtrack.embedRR)
            elif command == "5-1":
                await message.channel.send(embed=embedtrack.embeddYC)
            elif command == "5-2":
                await message.channel.send(embed=embedtrack.embeddEA)
            elif command == "5-3":
                await message.channel.send(embed=embedtrack.embeddDD)
            elif command == "5-4":
                await message.channel.send(embed=embedtrack.embeddMC)
            elif command == "6-1":
                await message.channel.send(embed=embedtrack.embeddBP)
            elif command == "6-2":
                await message.channel.send(embed=embedtrack.embeddCL)
            elif command == "6-3":
                await message.channel.send(embed=embedtrack.embeddWW)
            elif command == "6-4":
                await message.channel.send(embed=embedtrack.embeddAC)
            elif command == "7-1":
                await message.channel.send(embed=embedtrack.embeddrMMM)
            elif command == "7-2":
                await message.channel.send(embed=embedtrack.embedrMC)
            elif command == "7-3":
                await message.channel.send(embed=embedtrack.embedrCCB)
            elif command == "7-4":
                await message.channel.send(embed=embedtrack.embedrTT)
            elif command == "8-1":
                await message.channel.send(embed=embedtrack.embedrDDD)
            elif command == "8-2":
                await message.channel.send(embed=embedtrack.embedrDP3)
            elif command == "8-3":
                await message.channel.send(embed=embedtrack.embedrRRy)
            elif command == "8-4":
                await message.channel.send(embed=embedtrack.embedrDKJ)
            elif command == "9-1":
                await message.channel.send(embed=embedtrack.embedrWS)
            elif command == "9-2":
                await message.channel.send(embed=embedtrack.embeddrSL)
            elif command == "9-3":
                await message.channel.send(embed=embedtrack.embedrMP)
            elif command == "9-4":
                await message.channel.send(embed=embedtrack.embedrYV)
            elif command == "10-1":
                await message.channel.send(embed=embedtrack.embedrTTC)
            elif command == "10-2":
                await message.channel.send(embed=embedtrack.embedrPPS)
            elif command == "10-3":
                await message.channel.send(embed=embedtrack.embedrGV)
            elif command == "10-4":
                await message.channel.send(embed=embedtrack.embedrRRd)
            elif command == "11-1":
                await message.channel.send(embed=embedtrack.embeddWGM)
            elif command == "11-2":
                await message.channel.send(embed=embedtrack.embeddRR)
            elif command == "11-3":
                await message.channel.send(embed=embedtrack.embeddIIO)
            elif command == "11-4":
                await message.channel.send(embed=embedtrack.embeddHC)
            elif command == "12-1":
                await message.channel.send(embed=embedtrack.embeddNBC)
            elif command == "12-2":
                await message.channel.send(embed=embedtrack.embeddRiR)
            elif command == "12-3":
                await message.channel.send(embed=embedtrack.embeddSBS)
            elif command == "12-4":
                await message.channel.send(embed=embedtrack.embeddBB)
        except IndexError:
            pass

        

async def setup(bot):
    await bot.add_cog(trackbot(bot))
