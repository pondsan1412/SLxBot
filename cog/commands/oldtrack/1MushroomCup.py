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
        help="Mario Kart Stadium Track",
        aliases=["mks","MKS","mKs","MkS","mkS","mKS","1-1"]
    )
    async def _track_MKS(self,ctx):
        embedVar = discord.Embed(
            title="Mushroom Cup",
            description="Mario Kart Stadium",
            color=discord.Color.dark_purple()
        )
        embedVar.set_image(url=config.MarioKartStadium)
        embedVar.set_thumbnail(url=config.Mushroom)
        embedVar.add_field(name="Track Code:",value="1-1",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)


    @commands.hybrid_command(
        name="waterpark",
        description="Water Park",
        help="Water Park Track",
        aliases=["WP","wp","Wp","wP","1-2"]
    )
    async def _track_WP(self,ctx):
        embedVar = discord.Embed(
            title="Mushroom Cup",
            description="Water Park",
            color=discord.Color.dark_purple()
        )
        embedVar.set_image(url=config.WaterPark)
        embedVar.set_thumbnail(url=config.Mushroom)       
        embedVar.add_field(name="Track Code:",value="1-2",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)
    
    
    @commands.hybrid_command(
        name="sweetsweetcanyon",
        description="Sweet Sweet Canyon",
        help="Sweet Sweet Canyon Track",
        aliases=["SSC","ssc","Ssc","sSc","ssC","SSc","sSC","1-3"]
    )
    async def _track_SSC(self,ctx):
        embedVar = discord.Embed(
            title="Mushroom Cup",
            description="Sweet Sweet Canyon",
            color=discord.Color.dark_purple()
        )
        embedVar.set_image(url=config.SweetSweetCanyon)
        embedVar.set_thumbnail(url=config.Mushroom)
        embedVar.add_field(name="Track Code:",value="1-3",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)


    @commands.hybrid_command(
        name="thwompruins",
        description="Thwomp Ruins",
        help="Thwomp Ruins Track",
        aliases=["tr","TR","tR","Tr","1-4"]
    )
    async def _track_TR(self,ctx):
        embedVar = discord.Embed(
            title="Mushroom Cup",
            description="Thwomp Ruins",
            color=discord.Color.dark_purple()
        )
        embedVar.set_image(url=config.ThwompRuins)
        embedVar.set_thumbnail(url=config.Mushroom)
        embedVar.add_field(name="Track Code:",value="1-4",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)


async def setup(bot):
    await bot.add_cog(MushroomCup(bot))