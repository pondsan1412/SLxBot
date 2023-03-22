import discord
from discord.ext import commands
from cog import config
import json
import os

class BananaCup(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.hybrid_command(
        name="drydrydesert",
        description="Dry Dry Desert",
        help="Track Code: `rDDD, rddd, 8-1`",
        aliases=["rDDD","rddd","8-1"]
    )
    async def _track_rDDD(self,ctx):
        embedVar = discord.Embed(
            title="Banana Cup",
            description="GCN Dry Dry Desert",
            color=discord.Color.gold()
        )
        embedVar.set_image(url=config.DryDryDesert)
        embedVar.set_thumbnail(url=config.Banana)
        embedVar.add_field(name="Track Code:",value="8-1",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)


    @commands.hybrid_command(
        name="donutplains3",
        description="Donut Plains 3",
        help="Track Code: `rDP3, rdp3, 8-2`",
        aliases=["rDP3","rdp3","8-2"]
    )
    async def _track_rDP3(self,ctx):
        embedVar = discord.Embed(
            title="Banana Cup",
            description="SNES Donut Plains 3",
            color=discord.Color.green()
        )
        embedVar.set_image(url=config.DonutPlains3)
        embedVar.set_thumbnail(url=config.Banana)       
        embedVar.add_field(name="Track Code:",value="8-2",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)
    
    
    @commands.hybrid_command(
        name="royalraceway",
        description="Royal Raceway",
        help="Track Code: `rRRy, rrry, 8-3`",
        aliases=["rRRy","rrry","8-3"]
    )
    async def _track_rRRy(self,ctx):
        embedVar = discord.Embed(
            title="Banana Cup",
            description="N64 Royal Raceway",
            color=discord.Color.magenta()
        )
        embedVar.set_image(url=config.RoyalRaceway)
        embedVar.set_thumbnail(url=config.Banana)
        embedVar.add_field(name="Track Code:",value="8-3",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)


    @commands.hybrid_command(
        name="dkjungle",
        description="DK Jungle",
        help="Track Code: `rDKJ, rdkj, 8-4`",
        aliases=["rDKJ","rdkj","8-4"]
    )
    async def _track_rDKJ(self,ctx):
        embedVar = discord.Embed(
            title="Banana Cup",
            description="3DS DK Jungle",
            color=discord.Color.dark_orange()
        )
        embedVar.set_image(url=config.DKJungle)
        embedVar.set_thumbnail(url=config.Banana)
        embedVar.add_field(name="Track Code:",value="8-4",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)


async def setup(bot):
    await bot.add_cog(BananaCup(bot))