import discord
from discord.ext import commands
import json
from cog import config
import os
class Crossing(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.hybrid_command(
        name="babypark",
        description="",
        help="Baby Park Track",
        aliases=["dBP","dbp","DBP","dBp","dbP","6-1"]
    )
    async def _track_dBP(self,ctx):
        embedVar = discord.Embed(
            title="Baby Park",
            description="GCN Baby Park",
            color=discord.Color.dark_purple()
        )
        embedVar.set_image(url=config.BabyPark)
        embedVar.add_field(name="babypark",value="None",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)

    @commands.hybrid_command(
        name="cheeseland",
        description="",
        help="Cheese Land Track",
        aliases=["dCL","dcl","DCl","dcL","6-2"]
    )
    async def _track_dBP(self,ctx):
        embedVar = discord.Embed(
            title="Cheese Land",
            description="GBA Cheese Land",
            color=discord.Color.dark_purple()
        )
        embedVar.set_image(url=config.CheeseLand)
        embedVar.add_field(name="cheeseland",value="None",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)
    
async def setup(bot):
    await bot.add_cog(Crossing(bot))