import discord
from discord.ext import commands
from cog import config
import json
import os

class MoonCup(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.hybrid_command(
        name="berlinbyways",
        description="Berlin Byways",
        help="Track Code: `bBB, bbb, or 18-1`",
        aliases=["bBB","bbb","18-1"]
    )
    async def _track_bBB(self,ctx):
        embedVar = discord.Embed(
            title="Moon Cup",
            description="Tour Berlin Byways",
            color=discord.Color.dark_purple()
        )
        embedVar.set_image(url=config.BerlinByways)
        embedVar.set_thumbnail(url=config.Moon)
        embedVar.add_field(name="Track Code:",value="18-1",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)


    @commands.hybrid_command(
        name="peachgardens",
        description="Peach Gardens",
        help="Track Code: `bPG, bpg, or 18-2`",
        aliases=["bPG","bpg","18-2"]
    )
    async def _track_bPG(self,ctx):
        embedVar = discord.Embed(
            title="Moon Cup",
            description="DS Peach Gardens",
            color=discord.Color.dark_purple()
        )
        embedVar.set_image(url=config.PeachGardens)
        embedVar.set_thumbnail(url=config.Moon)       
        embedVar.add_field(name="Track Code:",value="18-2",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)
    
    
    @commands.hybrid_command(
        name="merrymountain",
        description="Merry Mountain",
        help="Track Code: `bMM, bmm, or 18-3`",
        aliases=["bMM","bmm","18-3"]
    )
    async def _track_bMM(self,ctx):
        embedVar = discord.Embed(
            title="Moon Cup",
            description="Merry Mountain",
            color=discord.Color.dark_purple()
        )
        embedVar.set_image(url=config.MerryMountain)
        embedVar.set_thumbnail(url=config.Moon)
        embedVar.add_field(name="Track Code:",value="18-3",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)


    @commands.hybrid_command(
        name="rainbowroad7",
        description="Rainbow Road",
        help="Track Code: `bRR7, brr7, or 18-4`",
        aliases=["bRR7","brr7","18-4"]
    )
    async def _track_bRR7(self,ctx):
        embedVar = discord.Embed(
            title="Moon Cup",
            description="3DS Rainbow Road",
            color=discord.Color.dark_purple()
        )
        embedVar.set_image(url=config.RainbowRoad7)
        embedVar.set_thumbnail(url=config.Moon)
        embedVar.add_field(name="Track Code:",value="18-4",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)


async def setup(bot):
    await bot.add_cog(MoonCup(bot))