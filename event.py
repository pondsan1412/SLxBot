import discord
from discord.ext import commands
from discord.utils import get


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
        if message.content =="emoji":
            await message.reply("<:Boomerang:1087361059247104060>")
        


    
async def setup(bot):
    await bot.add_cog(eventbot(bot))