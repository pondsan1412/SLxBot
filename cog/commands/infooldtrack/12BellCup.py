import discord
from discord.ext import commands
from cog import config
import json
import os

class BellCup(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.hybrid_command(
        name="neobowsercity",
        description="Neo Bowser City",
        help="Track Code: `dNBC, dnbc, 12-1`",
        aliases=["dNBC","dnbc","12-1"]
    )
    async def _track_dNBC(self,ctx):
        embedVar = discord.Embed(
            title="Bell Cup",
            description="3DS Neo Bowser City",
            color=discord.Color.dark_purple()
        )
        embedVar.set_image(url=config.NeoBowserCity)
        embedVar.set_thumbnail(url=config.Bell)
        embedVar.add_field(name="Track Code:",value="12-1",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)


    @commands.hybrid_command(
        name="ribbonroad",
        description="Ribbon Road",
        help="Track Code: `dRiR, drir, 12-2`",
        aliases=["dRiR","drir","12-2"]
    )
    async def _track_dRiR(self,ctx):
        embedVar = discord.Embed(
            title="Bell Cup",
            description="GBA Ribbon Road",
            color=discord.Color.magenta()
        )
        embedVar.set_image(url=config.RibbonRoad)
        embedVar.set_thumbnail(url=config.Bell)       
        embedVar.add_field(name="Track Code:",value="12-2",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)
    
    
    @commands.hybrid_command(
        name="superbellsubway",
        description="Super Bell Subway",
        help="Track Code: `dSBS, dsbs, 12-3`",
        aliases=["dSBS","dsbs","12-3"]
    )
    async def _track_dSBS(self,ctx):
        embedVar = discord.Embed(
            title="Bell Cup",
            description="Super Bell Subway",
            color=discord.Color.blurple()
        )
        embedVar.set_image(url=config.SuperBellSubway)
        embedVar.set_thumbnail(url=config.Bell)
        embedVar.add_field(name="Track Code:",value="12-3",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)


    @commands.hybrid_command(
        name="bigblue",
        description="Big Blue",
        help="Track Code: `dBB, dbb, 12-4`",
        aliases=["dBB","dbb","12-4"]
    )
    async def _track_dBB(self,ctx):
        embedVar = discord.Embed(
            title="Bell Cup",
            description="Big Blue",
            color=discord.Color.blue()
        )
        embedVar.set_image(url=config.BigBlue)
        embedVar.set_thumbnail(url=config.Bell)
        embedVar.add_field(name="Track Code:",value="12-4",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)


async def setup(bot):
    await bot.add_cog(BellCup(bot))