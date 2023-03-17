import discord
from discord.ext import commands
import json
from cog import config
import os
class TracksList(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.hybrid_command(
        name="babypark",
        description="",
        help="babypark track",
        aliases=["dBP","dbp","DBP","Dbp","dbP","5-1"]
    )
    async def _track_dBP(self,ctx):
        embedVar = discord.Embed(
            title="dBP baby park ベビパ 5-1",
            description="GCN Baby Park",
            color=discord.Color.dark_blue()
        )
        embedVar.set_image(url=config.babypark)
        embedVar.add_field(name="babypark",value="None",inline=False)
        embedVar.set_footer(text=f"using command by{ctx.author}")
        await ctx.send(embed=embedVar)
    
async def setup(bot):
    await bot.add_cog(TracksList(bot))