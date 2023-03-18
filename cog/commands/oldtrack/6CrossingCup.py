import discord
from discord.ext import commands
from cog import config
import json
import os

class CrossingCup(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.hybrid_command(
        name="babypark",
        description="Baby Park",
        help="Baby Park Track",
        aliases=["bp","BP","dBP","dbp","DBP","dBp","dbP","6-1"]
    )
    async def _track_dBP(self,ctx):
        embedVar = discord.Embed(
            title="Crossing Cup",
            description="GCN Baby Park",
            color=discord.Color.dark_purple()
        )
        embedVar.set_image(url=config.BabyPark)
        embedVar.set_thumbnail(url=config.Crossing)
        embedVar.add_field(name="Track Code:",value="6-1",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)


    @commands.hybrid_command(
        name="cheeseland",
        description="Cheese Land",
        help="Cheese Land Track",
        aliases=["cl","CL","dCL","dcl","DCl","dcL","DcL", "6-2"]
    )
    async def _track_dCL(self,ctx):
        embedVar = discord.Embed(
            title="Crossing Cup",
            description="GBA Cheese Land",
            color=discord.Color.dark_purple()
        )
        embedVar.set_image(url=config.CheeseLand)
        embedVar.set_thumbnail(url=config.Crossing)       
        embedVar.add_field(name="Track Code:",value="6-2",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)
    
    
    @commands.hybrid_command(
        name="wildwoods",
        description="Wild Woods",
        help="Wild Woods Track",
        aliases=["ww","WW","dWW","dww","DWW","DwW","dWw","dwW","6-3"]
    )
    async def _track_dWW(self,ctx):
        embedVar = discord.Embed(
            title="Crossing Cup",
            description="Wild Woods",
            color=discord.Color.dark_purple()
        )
        embedVar.set_image(url=config.WildWoods)
        embedVar.set_thumbnail(url=config.Crossing)
        embedVar.add_field(name="Track Code:",value="6-3",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)


    @commands.hybrid_command(
        name="animalcrossing",
        description="Animal Crossing",
        help="Animal Crossing Track",
        aliases=["ac","AC","dAC","dac","DAC","DaC","dAc","daC","6-4"]
    )
    async def _track_dAC(self,ctx):
        embedVar = discord.Embed(
            title="Crossing Cup",
            description="Animal Crossing",
            color=discord.Color.dark_purple()
        )
        embedVar.set_image(url=config.AnimalCrossing)
        embedVar.set_thumbnail(url=config.Crossing)
        embedVar.add_field(name="Track Code:",value="6-4",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)


async def setup(bot):
    await bot.add_cog(CrossingCup(bot))