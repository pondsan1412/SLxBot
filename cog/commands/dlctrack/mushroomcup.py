import discord
from discord.ext import commands

class mushroomcup(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.hybrid_command(
        name="1",
    )
    async def _1(self,ctx):
        """this is mushroom command"""
        pass
async def setup(bot):
    await bot.add_cog(mushroomcup(bot))
