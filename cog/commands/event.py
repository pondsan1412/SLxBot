import discord
from discord.ext import commands
from cog import config
from cog import embedconfig

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
            await message.channel.send(embed=embedconfig.embedMKS)

        if "1-2" in message.content.split()[0]:
            await message.channel.send(embed=embedconfig.embedWP)

async def setup(bot):
    await bot.add_cog(eventbot(bot))