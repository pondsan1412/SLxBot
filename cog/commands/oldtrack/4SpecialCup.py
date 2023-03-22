import discord
from discord.ext import commands
from cog import config
import json
import os

class SpecialCup(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.hybrid_command(
        name="cloudtopcruise",
        description="Cloudtop Cruise",
        help="Track Code: `CC, cc, or 4-1`",
        aliases=["CC","cc","4-1"]
    )
    async def _track_CC(self,ctx):
        embedVar = discord.Embed(
            title="Special Cup",
            description="Cloudtop Cruise",
            color=discord.Color.greyple()
        )
        embedVar.set_image(url=config.CloudtopCruise)
        embedVar.set_thumbnail(url=config.Special)
        embedVar.add_field(name="Track Code:",value="4-1",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)


    @commands.hybrid_command(
        name="bone-drydunes",
        description="Bone-Dry Dunes",
        help="Track Code: `BDD, bdd, or 4-2`",
        aliases=["BDD","bdd","4-2"]
    )
    async def _track_BDD(self,ctx):
        embedVar = discord.Embed(
            title="Special Cup",
            description="Bone-Dry Dunes",
            color=discord.Color.dark_orange()
        )
        embedVar.set_image(url=config.BoneDryDunes)
        embedVar.set_thumbnail(url=config.Special)       
        embedVar.add_field(name="Track Code:",value="4-2",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)
    
    
    @commands.hybrid_command(
        name="bowserscastle",
        description="Bowser\'s Castle",
        help="Track Code: `BC, bc, or 4-3`",
        aliases=["BC","bc","4-3"]
    )
    async def _track_BC(self,ctx):
        embedVar = discord.Embed(
            title="Special Cup",
            description="Bowser\'s Castle",
            color=discord.Color.orange()
        )
        embedVar.set_image(url=config.BowserCastle)
        embedVar.set_thumbnail(url=config.Special)
        embedVar.add_field(name="Track Code:",value="4-3",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)


    @commands.hybrid_command(
        name="rainbowroad",
        description="Rainbow Road",
        help="Track Code: `RR, rr, or 4-4`",
        aliases=["RR","rr","4-4"]
    )
    async def _track_RR(self,ctx):
        embedVar = discord.Embed(
            title="Special Cup",
            description="Rainbow Road",
            color=discord.Color.greyple()
        )
        embedVar.set_image(url=config.RainbowRoad)
        embedVar.set_thumbnail(url=config.Special)
        embedVar.add_field(name="Track Code:",value="4-4",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)


async def setup(bot):
    await bot.add_cog(SpecialCup(bot))