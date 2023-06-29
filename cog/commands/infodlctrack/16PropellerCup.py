import discord
from discord.ext import commands
from cog import config
import json
import os

class PropellerCup(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.hybrid_command(
        name="sydenysprint",
        description="Sydeny Sprint",
        help="Track Code: `bSS, bss, or 16-1`",
        aliases=["bSS","bss","16-1"]
    )
    async def _track_bSS(self,ctx):
        embedVar = discord.Embed(
            title="Propeller Cup",
            description="Tour Sydeny Sprint",
            color=discord.Color.gold()
        )
        embedVar.set_image(url=config.SydneySprint)
        embedVar.set_thumbnail(url=config.Propeller)
        embedVar.add_field(name="Track Code:",value="16-1",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)


    @commands.hybrid_command(
        name="snowland",
        description="Snow Land",
        help="Track Code: `bSL, bsl, or 16-2`",
        aliases=["bSL","bsl","16-2"]
    )
    async def _track_bSL(self,ctx):
        embedVar = discord.Embed(
            title="Propeller Cup",
            description="GBA Snow Land",
            color=discord.Color.teal()
        )
        embedVar.set_image(url=config.SnowLand)
        embedVar.set_thumbnail(url=config.Propeller)       
        embedVar.add_field(name="Track Code:",value="16-2",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)
    
    
    @commands.hybrid_command(
        name="mushroomgorge",
        description="Mushroom Gorge",
        help="Track Code: `bMG, bmg, or 16-3`",
        aliases=["bMG","bmg","16-3"]
    )
    async def _track_bMG(self,ctx):
        embedVar = discord.Embed(
            title="Propeller Cup",
            description="Wii Mushroom Gorge",
            color=discord.Color.red()
        )
        embedVar.set_image(url=config.MushroomGorge)
        embedVar.set_thumbnail(url=config.Propeller)
        embedVar.add_field(name="Track Code:",value="16-3",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)


    @commands.hybrid_command(
        name="sky-highsundae",
        description="Sky-High Sundae",
        help="Track Code: `bSHS, bshs, or 16-4`",
        aliases=["bSHS","bshs","16-4"]
    )
    async def _track_bSHS(self,ctx):
        embedVar = discord.Embed(
            title="Propeller Cup",
            description="Sky-High Sundae",
            color=discord.Color.lighter_grey()
        )
        embedVar.set_image(url=config.SkyHighSundae)
        embedVar.set_thumbnail(url=config.Propeller)
        embedVar.add_field(name="Track Code:",value="16-4",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)


async def setup(bot):
    await bot.add_cog(PropellerCup(bot))