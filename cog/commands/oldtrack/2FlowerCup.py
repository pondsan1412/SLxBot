import discord
from discord.ext import commands
from cog import config
import json
import os

class FlowerCup(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.hybrid_command(
        name="mariocircuit",
        description="Mario Circuit",
        help="Track Code: `MC, mc, or 2-1`",
        aliases=["MC","mc","2-1"]
    )
    async def _track_MC(self,ctx):
        embedVar = discord.Embed(
            title="Flower Cup",
            description="Mario Circuit",
            color=discord.Color.magenta()
        )
        embedVar.set_image(url=config.MarioCiruit)
        embedVar.set_thumbnail(url=config.Flower)
        embedVar.add_field(name="Track Code:",value="2-1",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)


    @commands.hybrid_command(
        name="toadharbor",
        description="Toad Harbor",
        help="Track Code: `TH, th, or 2-2`",
        aliases=["TH","th","2-2"]
    )
    async def _track_TH(self,ctx):
        embedVar = discord.Embed(
            title="Flower Cup",
            description="Toad Harbor",
            color=discord.Color.dark_red()
        )
        embedVar.set_image(url=config.ToadHarbor)
        embedVar.set_thumbnail(url=config.Flower)       
        embedVar.add_field(name="Track Code:",value="2-2",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)
    
    
    @commands.hybrid_command(
        name="twistedmansion",
        description="Twisted Mansion",
        help="Track Code: `TM, tm, or 2-3`",
        aliases=["TM","tm","2-3"]
    )
    async def _track_TM(self,ctx):
        embedVar = discord.Embed(
            title="Flower Cup",
            description="Twisted Mansion",
            color=discord.Color.darker_grey()
        )
        embedVar.set_image(url=config.TwistedMansion)
        embedVar.set_thumbnail(url=config.Flower)
        embedVar.add_field(name="Track Code:",value="2-3",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)


    @commands.hybrid_command(
        name="shyguyfalls",
        description="Shy Guy Falls",
        help="Track Code: `SGF, sgf, or 2-4`",
        aliases=["SGF","sgf","2-4"]
    )
    async def _track_SGF(self,ctx):
        embedVar = discord.Embed(
            title="Flower Cup",
            description="Shy Guy Falls",
            color=discord.Color.dark_red()
        )
        embedVar.set_image(url=config.ShyGuyFalls)
        embedVar.set_thumbnail(url=config.Flower)
        embedVar.add_field(name="Track Code:",value="2-4",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)


async def setup(bot):
    await bot.add_cog(FlowerCup(bot))