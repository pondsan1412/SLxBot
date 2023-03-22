import discord
from discord.ext import commands
from cog import config
import json
import os

class LeafCup(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.hybrid_command(
        name="wariostadium",
        description="Wario Stadium",
        help="Track Code: `rWS, rws, 9-1`",
        aliases=["rWS","rws","9-1"]
    )
    async def _track_rWS(self,ctx):
        embedVar = discord.Embed(
            title="Leaf Cup",
            description="DS Wario Stadium",
            color=discord.Color.dark_gold()
        )
        embedVar.set_image(url=config.WarioStadium)
        embedVar.set_thumbnail(url=config.Leaf)
        embedVar.add_field(name="Track Code:",value="9-1",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)


    @commands.hybrid_command(
        name="sherbetland",
        description="Sherbet Land",
        help="Track Code: `rSL, rsl, 9-2`",
        aliases=["rSL","rsl","9-2"]
    )
    async def _track_rSL(self,ctx):
        embedVar = discord.Embed(
            title="Leaf Cup",
            description="GCN Sherbet Land",
            color=discord.Color.teal()
        )
        embedVar.set_image(url=config.SherbetLand)
        embedVar.set_thumbnail(url=config.Leaf)       
        embedVar.add_field(name="Track Code:",value="9-2",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)
    
    
    @commands.hybrid_command(
        name="musicpark",
        description="Mario Park",
        help="Track Code: `rMP, rmp, 9-3`",
        aliases=["rMP","rmp","9-3"]
    )
    async def _track_rMP(self,ctx):
        embedVar = discord.Embed(
            title="Leaf Cup",
            description="3DS Music Park",
            color=discord.Color.orange()
        )
        embedVar.set_image(url=config.MusicPark)
        embedVar.set_thumbnail(url=config.Leaf)
        embedVar.add_field(name="Track Code:",value="9-3",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)


    @commands.hybrid_command(
        name="yoshivalley",
        description="N64 Yoshi Valley",
        help="Track Code: `rYV, ryv, 9-4`",
        aliases=["rYV","ryv","9-4"]
    )
    async def _track_rYV(self,ctx):
        embedVar = discord.Embed(
            title="Leaf Cup",
            description="N64 Yoshi Valley",
            color=discord.Color.dark_orange()
        )
        embedVar.set_image(url=config.YoshiValley)
        embedVar.set_thumbnail(url=config.Leaf)
        embedVar.add_field(name="Track Code:",value="9-4",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)


async def setup(bot):
    await bot.add_cog(LeafCup(bot))