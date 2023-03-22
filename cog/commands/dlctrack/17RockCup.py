import discord
from discord.ext import commands
from cog import config
import json
import os

class RockCup(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.hybrid_command(
        name="londonloop",
        description="London Loop",
        help="Track Code: `bLL, bll, or 17-1`",
        aliases=["bLL","bll","17-1"]
    )
    async def _track_bLL(self,ctx):
        embedVar = discord.Embed(
            title="Rock Cup",
            description="Tour London Loop",
            color=discord.Color.greyple()
        )
        embedVar.set_image(url=config.LondonLoop)
        embedVar.set_thumbnail(url=config.Rock)
        embedVar.add_field(name="Track Code:",value="17-1",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)


    @commands.hybrid_command(
        name="boolake",
        description="Boo Lake",
        help="Track Code: `bBL, bbl, or 17-2`",
        aliases=["bBL","bbl","17-2"]
    )
    async def _track_bBL(self,ctx):
        embedVar = discord.Embed(
            title="Rock Cup",
            description="GBA Boo Lake",
            color=discord.Color.teal()
        )
        embedVar.set_image(url=config.BooLake)
        embedVar.set_thumbnail(url=config.Rock)       
        embedVar.add_field(name="Track Code:",value="17-2",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)
    
    
    @commands.hybrid_command(
        name="rockrockmountain",
        description="Rock Rock Mountain",
        help="Track Code: `bRRM, brrm, or 17-3`",
        aliases=["bRRM","brrm","17-3"]
    )
    async def _track_bRRM(self,ctx):
        embedVar = discord.Embed(
            title="Rock Cup",
            description="3DS Rock Rock Mountain",
            color=discord.Color.red()
        )
        embedVar.set_image(url=config.RockRockMountain)
        embedVar.set_thumbnail(url=config.Rock)
        embedVar.add_field(name="Track Code:",value="17-3",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)


    @commands.hybrid_command(
        name="mapletreeway",
        description="MapleTreeway",
        help="Track Code: `bMT, bmt, or 17-4`",
        aliases=["bMT","bmt","17-4"]
    )
    async def _track_bMT(self,ctx):
        embedVar = discord.Embed(
            title="Rock Cup",
            description="Wii MapleTreeway",
            color=discord.Color.orange()
        )
        embedVar.set_image(url=config.MapleTreeway)
        embedVar.set_thumbnail(url=config.Rock)
        embedVar.add_field(name="Track Code:",value="17-4",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)


async def setup(bot):
    await bot.add_cog(RockCup(bot))