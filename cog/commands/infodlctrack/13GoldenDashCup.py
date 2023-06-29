import discord
from discord.ext import commands
from cog import config
import json
import os

class GoldenDashCup(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.hybrid_command(
        name="parispromenade",
        description="Paris Promenade",
        help="Track Code: `bPP, bpp, or 13-1`",
        aliases=["bPP","bpp","13-1"]
    )
    async def _track_bPP(self,ctx):
        embedVar = discord.Embed(
            title="Golden Dash Cup",
            description="Tour Paris Promenade",
            color=discord.Color.orange()
        )
        embedVar.set_image(url=config.ParisPromenade)
        embedVar.set_thumbnail(url=config.GoldenDash)
        embedVar.add_field(name="Track Code:",value="13-1",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)


    @commands.hybrid_command(
        name="toadcircuit",
        description="Toad Circuit",
        help="Track Code: `bTC, btc, or 13-2`",
        aliases=["bTC","btc","13-2"]
    )
    async def _track_bTC(self,ctx):
        embedVar = discord.Embed(
            title="Golden Dash Cup",
            description="3DS Toad Circuit",
            color=discord.Color.yellow()
        )
        embedVar.set_image(url=config.ToadCircuit)
        embedVar.set_thumbnail(url=config.GoldenDash)       
        embedVar.add_field(name="Track Code:",value="13-2",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)
    
    
    @commands.hybrid_command(
        name="chocomountain",
        description="Choco Mountain",
        help="Track Code: `bMCo, bmco, or 13-3`",
        aliases=["bMCo","bmco","13-3"]
    )
    async def _track_bMC(self,ctx):
        embedVar = discord.Embed(
            title="Golden Dash Cup",
            description="N64 Choco Mountain",
            color=discord.Color.dark_orange()
        )
        embedVar.set_image(url=config.ChocoMountain)
        embedVar.set_thumbnail(url=config.GoldenDash)
        embedVar.add_field(name="Track Code:",value="13-3",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)


    @commands.hybrid_command(
        name="coconutmall",
        description="Coconut Mall",
        help="Track Code: `bMCa, bmca, or 13-4`",
        aliases=["bMCa","bmca","13-4"]
    )
    async def _track_bMCa(self,ctx):
        embedVar = discord.Embed(
            title="Golden Dash Cup",
            description="Wii Coconut Mall",
            color=discord.Color.orange()
        )
        embedVar.set_image(url=config.CoconutMall)
        embedVar.set_thumbnail(url=config.GoldenDash)
        embedVar.add_field(name="Track Code:",value="13-4",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)


async def setup(bot):
    await bot.add_cog(GoldenDashCup(bot))