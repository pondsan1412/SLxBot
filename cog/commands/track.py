import discord
from discord.ext import commands
from cog import config
from cog import embedconfig
from cog import embedtrack

commands_info = {
            "1-1": embedtrack.embedMKS,
            "1-2": embedtrack.embedWP,
            "1-3": embedtrack.embedSSC,
        }
class trackbot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    #here for loop    

    @commands.Cog.listener()    
    async def on_message(
        self,
        message
    ):
        if message.author == self.bot.user:
            return
        command = message.content.split()[0]
        try:
            response_embed = commands_info[command]
            await message.channel.send(embed=response_embed)
        except KeyError:
            pass
        except IndexError:
            pass

        

async def setup(bot):
    await bot.add_cog(trackbot(bot))
