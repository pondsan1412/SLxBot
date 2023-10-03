import discord
from discord.ext import commands
from cog import config
import json
import os

class FeatherCup(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.hybrid_command(
        name="athensdash",
        description="Athens Dash",
        help="Track Code: `bAtD, batd, or 21-1`",
        aliases=["bAtD","batd","21-1"]
    )
    async def _track_bAtD(self,ctx):
        embedVar = discord.Embed(
            title="Feather Cup",
            description="Tour Athens Dash",
            color=discord.Color.orange()
        )
        embedVar.set_image(url=config.AthensDash)
        embedVar.set_thumbnail(url=config.Feather)
        embedVar.add_field(name="Track Code:",value="21-1",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)


    @commands.hybrid_command(
        name="daisycruiser",
        description="Daisy Cruiser",
        help="Track Code: `bDC, bdc, or 21-2`",
        aliases=["bDC","bdc","21-2"]
    )
    async def _track_bDC(self,ctx):
        embedVar = discord.Embed(
            title="Feather Cup",
            description="GCN Daisy Cruiser",
            color=discord.Color.dark_orange()
        )
        embedVar.set_image(url=config.DaisyCrusier)
        embedVar.set_thumbnail(url=config.Feather)       
        embedVar.add_field(name="Track Code:",value="21-2",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)
    
    
    @commands.hybrid_command(
        name="moonviewhighway",
        description="Moonview Highway",
        help="Track Code: `bMH, bmh, or 21-3`",
        aliases=["bMH","bmh","21-3"]
    )
    async def _track_bMH(self,ctx):
        embedVar = discord.Embed(
            title="Feather Cup",
            description="Wii Moonview Highway",
            color=discord.Color.dark_grey()
        )
        embedVar.set_image(url=config.MoonviewHighway)
        embedVar.set_thumbnail(url=config.Feather)
        embedVar.add_field(name="Track Code:",value="21-3",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)


    @commands.hybrid_command(
        name="squeakycleansprint",
        description="Singapore Speedway",
        help="Track Code: `bSCS, bscs or 21-4`",
        aliases=["bSCS","bscs","21-4"]
    )
    async def _track_bSCS(self,ctx):
        embedVar = discord.Embed(
            title="Feather Cup",
            description="Squeaky Clean Sprint",
            color=discord.Color.yellow()
        )
        embedVar.set_image(url=config.SqueakyCleanSprint)
        embedVar.set_thumbnail(url=config.Feather)
        embedVar.add_field(name="Track Code:",value="21-4",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)


async def setup(bot):
    await bot.add_cog(FeatherCup(bot))