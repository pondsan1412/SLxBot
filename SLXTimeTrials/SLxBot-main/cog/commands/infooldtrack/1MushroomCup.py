import discord
from discord.ext import commands
from cog import config
import json
import os

class MushroomCup(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.hybrid_command(
        name="mariokartstadium",
        description="Mario Kart Stadium",
        help="Track Code: `MKS, mks, or 1-1`",
        aliases=["mks","MKS","1-1"]
    )
    async def _track_MKS(self,ctx):
        embedVar = discord.Embed(
            title="Mushroom Cup",
            description="Mario Kart Stadium",
            color=discord.Color.brand_red()
        )
        embedVar.set_image(url=config.MarioKartStadium)
        embedVar.set_thumbnail(url=config.Mushroom)
        embedVar.add_field(name="Track Code:",value="1-1",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)


    @commands.hybrid_command(
        name="waterpark",
        description="Water Park",
        help="Track Code: `WP, wp, or 1-2`",
        aliases=["WP","wp","1-2"]
    )
    async def _track_WP(self,ctx):
        embedVar = discord.Embed(
            title="Mushroom Cup",
            description="Water Park",
            color=discord.Color.brand_green()
        )
        embedVar.set_image(url=config.WaterPark)
        embedVar.set_thumbnail(url=config.Mushroom)       
        embedVar.add_field(name="Track Code:",value="1-2",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)
    
    
    @commands.hybrid_command(
        name="sweetsweetcanyon",
        description="Sweet Sweet Canyon",
        help="Track Code: `SSC, ssc, or 1-3`",
        aliases=["SSC","ssc","1-3"]
    )
    async def _track_SSC(self,ctx):
        embedVar = discord.Embed(
            title="Mushroom Cup",
            description="Sweet Sweet Canyon",
            color=discord.Color.orange()
        )
        embedVar.set_image(url=config.SweetSweetCanyon)
        embedVar.set_thumbnail(url=config.Mushroom)
        embedVar.add_field(name="Track Code:",value="1-3",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)


    @commands.hybrid_command(
        name="thwompruins",
        description="Thwomp Ruins",
        help="Track Code: `TR, tr, or 1-4`",
        aliases=["TR","tr","1-4"]
    )
    async def _track_TR(self,ctx):
        embedVar = discord.Embed(
            title="Mushroom Cup",
            description="Thwomp Ruins",
            color=discord.Color.greyple()
        )
        embedVar.set_image(url=config.ThwompRuins)
        embedVar.set_thumbnail(url=config.Mushroom)
        embedVar.add_field(name="Track Code:",value="1-4",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)


async def setup(bot):
    await bot.add_cog(MushroomCup(bot))