import discord
from discord.ext import commands
from cog import config
import json
import os

class BoomerangCup(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.hybrid_command(
        name="bangkokrush",
        description="Bangkok Rush",
        help="Track Code: `bBR, bbr, or 20-1`",
        aliases=["bBR","bbr","20-1"]
    )
    async def _track_bBR(self,ctx):
        embedVar = discord.Embed(
            title="Boomerang Cup",
            description="Tour Bangkok Rush",
            color=discord.Color.dark_purple()
        )
        embedVar.set_image(url=config.BangkokRush)
        embedVar.set_thumbnail(url=config.Boomerang)
        embedVar.add_field(name="Track Code:",value="20-1",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)


    @commands.hybrid_command(
        name="bmariocircuit",
        description="Mario Circuit",
        help="Track Code: `bMC, bmc, or 20-2`",
        aliases=["bMC","bmc","20-2"]
    )
    async def _track_bMC(self,ctx):
        embedVar = discord.Embed(
            title="Boomerang Cup",
            description="DS Mario Circuit",
            color=discord.Color.dark_purple()
        )
        embedVar.set_image(url=config.WaterPark)
        embedVar.set_thumbnail(url=config.Mushroom)       
        embedVar.add_field(name="Track Code:",value="20-2",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)
    
    
    @commands.hybrid_command(
        name="waluigistadium",
        description="Waluigi Stadium",
        help="Track Code: `bWS, bws, or 20-3`",
        aliases=["bWS","bws","20-3"]
    )
    async def _track_SSC(self,ctx):
        embedVar = discord.Embed(
            title="Boomerang Cup",
            description="GCN Waluigi Stadium",
            color=discord.Color.dark_purple()
        )
        embedVar.set_image(url=config.WaluigiStadium)
        embedVar.set_thumbnail(url=config.Boomerang)
        embedVar.add_field(name="Track Code:",value="20-3",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)


    @commands.hybrid_command(
        name="singaporespeedway",
        description="Singapore Speedway",
        help="Track Code: `bSSy, bssy, or 20-4`",
        aliases=["bSSy","bssy","20-4"]
    )
    async def _track_TR(self,ctx):
        embedVar = discord.Embed(
            title="Boomerang Cup",
            description="Tour Singapore Speedway",
            color=discord.Color.dark_purple()
        )
        embedVar.set_image(url=config.SingaporeSpeedway)
        embedVar.set_thumbnail(url=config.Boomerang)
        embedVar.add_field(name="Track Code:",value="20-4",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)


async def setup(bot):
    await bot.add_cog(BoomerangCup(bot))