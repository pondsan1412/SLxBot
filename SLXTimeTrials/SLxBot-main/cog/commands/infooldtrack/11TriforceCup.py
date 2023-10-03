import discord
from discord.ext import commands
from cog import config
import json
import os

class TriforceCup(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.hybrid_command(
        name="wariosgoldmine",
        description="Wario\'s Gold Mine",
        help="Track Code: `dWGM, dwgm, 11-1`",
        aliases=["dWGM","dwgm","11-1"]
    )
    async def _track_dWGM(self,ctx):
        embedVar = discord.Embed(
            title="Triforce Cup",
            description="Wii Wario\'s Gold Mine",
            color=discord.Color.dark_gold()
        )
        embedVar.set_image(url=config.WariosGoldMine)
        embedVar.set_thumbnail(url=config.Triforce)
        embedVar.add_field(name="Track Code:",value="11-1",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)


    @commands.hybrid_command(
        name="snesrainbowroad",
        description="Rainbow Road",
        help="Track Code: `dRR, drr, 11-2`",
        aliases=["dRR","drr","11-2"]
    )
    async def _track_dRR(self,ctx):
        embedVar = discord.Embed(
            title="Triforce Cup",
            description="SNES Rainbow Road",
            color=discord.Color.purple()
        )
        embedVar.set_image(url=config.dRainbowRoad)
        embedVar.set_thumbnail(url=config.Triforce)       
        embedVar.add_field(name="Track Code:",value="11-2",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)
    
    
    @commands.hybrid_command(
        name="iceiceoutpost",
        description="Ice Ice Outpost",
        help="Track Code: `dIIO, diio, 11-3`",
        aliases=["dIIO","diio","11-3"]
    )
    async def _track_dIIO(self,ctx):
        embedVar = discord.Embed(
            title="Triforce Cup",
            description="Ice Ice Outpost",
            color=discord.Color.yellow()
        )
        embedVar.set_image(url=config.IceIceOutpost)
        embedVar.set_thumbnail(url=config.Triforce)
        embedVar.add_field(name="Track Code:",value="11-3",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)


    @commands.hybrid_command(
        name="hyrulecircuit",
        description="Hyrule Circuit",
        help="Track Code: `dHC, dhc, 11-4`",
        aliases=["dHC","dhc","11-4"]
    )
    async def _track_dHC(self,ctx):
        embedVar = discord.Embed(
            title="Triforce Cup",
            description="Hyrule Circuit",
            color=discord.Color.dark_green()
        )
        embedVar.set_image(url=config.HyruleCircuit)
        embedVar.set_thumbnail(url=config.Triforce)
        embedVar.add_field(name="Track Code:",value="11-4",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)


async def setup(bot):
    await bot.add_cog(TriforceCup(bot))