import discord
from discord.ext import commands
from cog import config
from cog import embedconfig
from cog import embedtrack
from googletrans import Translator
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
        if "Fire" in message.content.split()[0]:
            await message.channel.send(content=config.x3Fire)
    
async def setup(bot):
    await bot.add_cog(eventbot(bot))