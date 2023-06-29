import discord
from discord.ext import commands
from cog import config
import json
import os

class TurnipCup(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.hybrid_command(
        name="newyorkminute",
        description="New York Minute",
        help="Track Code: `bNYM, bnym, or 15-1`",
        aliases=["bNYM","bnym","15-1"]
    )
    async def _track_bNYM(self,ctx):
        embedVar = discord.Embed(
            title="Turnip Cup",
            description="Tour New York Minute",
            color=discord.Color.darker_grey()
        )
        embedVar.set_image(url=config.NewYorkMinute)
        embedVar.set_thumbnail(url=config.Turnip)
        embedVar.add_field(name="Track Code:",value="15-1",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)


    @commands.hybrid_command(
        name="mariocircuit3",
        description="Mario Circuit",
        help="Track Code: `bMC3, bmc3, or 15-2`",
        aliases=["bMC3","bmc3","15-2"]
    )
    async def _track_bMC3(self,ctx):
        embedVar = discord.Embed(
            title="Turnip Cup",
            description="SNES Mario Circuit 3",
            color=discord.Color.dark_green()
        )
        embedVar.set_image(url=config.MarioCircuit3)
        embedVar.set_thumbnail(url=config.Turnip)       
        embedVar.add_field(name="Track Code:",value="15-2",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)
    
    
    @commands.hybrid_command(
        name="kalimaridesert",
        description="Kalimari Desert",
        help="Track Code: `bKD, bkd, or 15-3`",
        aliases=["bKD","bkd","15-3"]
    )
    async def _track_bKD(self,ctx):
        embedVar = discord.Embed(
            title="Turnip Cup",
            description="N64 Kalimari Desert",
            color=discord.Color.orange()
        )
        embedVar.set_image(url=config.KalimariDesert)
        embedVar.set_thumbnail(url=config.Turnip)
        embedVar.add_field(name="Track Code:",value="15-3",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)


    @commands.hybrid_command(
        name="waluigipinball",
        description="Waluigi Pinball",
        help="Track Code: `bWP, bwp, or 15-4`",
        aliases=["bWP","bwp","15-4"]
    )
    async def _track_bWP(self,ctx):
        embedVar = discord.Embed(
            title="Turnip Cup",
            description="DS Waluigi Pinball",
            color=discord.Color.dark_purple()
        )
        embedVar.set_image(url=config.WaluigiPinball)
        embedVar.set_thumbnail(url=config.Turnip)
        embedVar.add_field(name="Track Code:",value="15-4",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)


async def setup(bot):
    await bot.add_cog(TurnipCup(bot))