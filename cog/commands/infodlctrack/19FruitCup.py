import discord
from discord.ext import commands
from cog import config
import json
import os

class FruitCup(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.hybrid_command(
        name="amsterdamdrift",
        description="Amsterdam Drift",
        help="Track Code: `bAD, bad, or 19-1`",
        aliases=["bAD","bad","19-1"]
    )
    async def _track_bAD(self,ctx):
        embedVar = discord.Embed(
            title="Fruit Cup",
            description="Tour Amsterdam Drift",
            color=discord.Color.orange()
        )
        embedVar.set_image(url=config.AmsterdamDrift)
        embedVar.set_thumbnail(url=config.Fruit)
        embedVar.add_field(name="Track Code:",value="19-1",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)


    @commands.hybrid_command(
        name="riversidepark",
        description="Riverside Park",
        help="Track Code: `bRP, brp, or 19-2`",
        aliases=["bRP","brp","19-2"]
    )
    async def _track_bRP(self,ctx):
        embedVar = discord.Embed(
            title="Fruit Cup",
            description="GBA Riverside Park",
            color=discord.Color.dark_orange()
        )
        embedVar.set_image(url=config.RiversidePark)
        embedVar.set_thumbnail(url=config.Fruit)       
        embedVar.add_field(name="Track Code:",value="19-2",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)
    
    
    @commands.hybrid_command(
        name="dksummit",
        description="DK Summit",
        help="Track Code: `bDKS, bdks, or 19-3`",
        aliases=["bDKS","bdks","19-3"]
    )
    async def _track_bDKS(self,ctx):
        embedVar = discord.Embed(
            title="Fruit Cup",
            description="Wii DK Summit",
            color=discord.Color.teal()
        )
        embedVar.set_image(url=config.DKSummit)
        embedVar.set_thumbnail(url=config.Fruit)
        embedVar.add_field(name="Track Code:",value="19-3",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)


    @commands.hybrid_command(
        name="yoshisisland",
        description="Yoshi\'s Island",
        help="Track Code: `bYI, byi, or 19-4`",
        aliases=["bYI","byi","19-4"]
    )
    async def _track_bYI(self,ctx):
        embedVar = discord.Embed(
            title="Fruit Cup",
            description="Yoshi\'s Island",
            color=discord.Color.teal()
        )
        embedVar.set_image(url=config.YoshisIsland)
        embedVar.set_thumbnail(url=config.Fruit)
        embedVar.add_field(name="Track Code:",value="19-4",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)


async def setup(bot):
    await bot.add_cog(FruitCup(bot))