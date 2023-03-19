import discord
from discord.ext import commands
from cog import config
import json
import os

class StarCup(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.hybrid_command(
        name="sunshineairport",
        description="Sunshine Airport",
        help="Track Code: `SA, sa, or 3-1`",
        aliases=["SA","sa","3-1"]
    )
    async def _track_SA(self,ctx):
        embedVar = discord.Embed(
            title="Star Cup",
            description="Sunshine Airport",
            color=discord.Color.dark_purple()
        )
        embedVar.set_image(url=config.SunshineAirport)
        embedVar.set_thumbnail(url=config.Star)
        embedVar.add_field(name="Track Code:",value="3-1",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)


    @commands.hybrid_command(
        name="dolphinshoals",
        description="Dolphin Shoals",
        help="Track Code: `DS, ds, or 3-2`",
        aliases=["DS","ds","3-2"]
    )
    async def _track_DS(self,ctx):
        embedVar = discord.Embed(
            title="Star Cup",
            description="Dolphin Shoals",
            color=discord.Color.dark_purple()
        )
        embedVar.set_image(url=config.DolphinShoals)
        embedVar.set_thumbnail(url=config.Star)       
        embedVar.add_field(name="Track Code:",value="3-2",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)
    
    
    @commands.hybrid_command(
        name="electrodrome",
        description="Electrodrome",
        help="Track Code: `Ed, ed, or 3-3`",
        aliases=["Ed","ed","3-3"]
    )
    async def _track_Ed(self,ctx):
        embedVar = discord.Embed(
            title="Star Cup",
            description="Electrodrome",
            color=discord.Color.dark_purple()
        )
        embedVar.set_image(url=config.Electrodrome)
        embedVar.set_thumbnail(url=config.Star)
        embedVar.add_field(name="Track Code:",value="3-3",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)


    @commands.hybrid_command(
        name="mountwario",
        description="Mount Wario",
        help="Track Code: `MW, mw, or 3-4`",
        aliases=["MW","mw","3-4"]
    )
    async def _track_MW(self,ctx):
        embedVar = discord.Embed(
            title="Star Cup",
            description="Mount Wario",
            color=discord.Color.dark_purple()
        )
        embedVar.set_image(url=config.MountWario)
        embedVar.set_thumbnail(url=config.Star)
        embedVar.add_field(name="Track Code:",value="3-4",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)


async def setup(bot):
    await bot.add_cog(StarCup(bot))