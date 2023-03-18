import discord
from discord.ext import commands

class starcup(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    @commands.hybrid_command(name="55")
    async def _55(self,ctx):
        """this is starcup command"""
        pass
async def setup(bot):
    await bot.add_cog(starcup(bot))