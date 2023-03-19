import discord
from discord.ext import commands
from cog import config
import json
import os

class EggCup(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.hybrid_command(
        name="yoshicircuit",
        description="Yoshi Circuit",
        help="Track Code: `dYC, dyc, or 5-1`",
        aliases=["dYC","dyc","5-1"]
    )
    async def _track_dYC(self,ctx):
        embedVar = discord.Embed(
            title="Egg Cup",
            description="GCN Yoshi Circuit",
            color=discord.Color.dark_purple()
        )
        embedVar.set_image(url=config.YoshiCircuit)
        embedVar.set_thumbnail(url=config.Egg)
        embedVar.add_field(name="Track Code:",value="5-1",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)


    @commands.hybrid_command(
        name="excitebikearena",
        description="Excitebike Arena",
        help="Track Code: `dEA, dea, or 5-2`",
        aliases=["dEA","dea","5-2"]
    )
    async def _track_dEA(self,ctx):
        embedVar = discord.Embed(
            title="Egg Cup",
            description="Excitebike Arena",
            color=discord.Color.dark_purple()
        )
        embedVar.set_image(url=config.ExcitebikeArena)
        embedVar.set_thumbnail(url=config.Egg)       
        embedVar.add_field(name="Track Code:",value="5-2",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)
    
    
    @commands.hybrid_command(
        name="dragondriftway",
        description="Dragon Driftway",
        help="Track Code: `dDD, ddd, or 5-3`",
        aliases=["dDD","ddd","5-3"]
    )
    async def _track_dDD(self,ctx):
        embedVar = discord.Embed(
            title="Egg Cup",
            description="Dragon Driftway",
            color=discord.Color.dark_purple()
        )
        embedVar.set_image(url=config.DragonDriftway)
        embedVar.set_thumbnail(url=config.Egg)
        embedVar.add_field(name="Track Code:",value="5-3",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)


    @commands.hybrid_command(
        name="mutecity",
        description="Mute City",
        help="Track Code: `dMC, dmc, or 5-4`",
        aliases=["dMC","dmc","5-4"]
    )
    async def _track_dMC(self,ctx):
        embedVar = discord.Embed(
            title="Egg Cup",
            description="Mute City",
            color=discord.Color.dark_purple()
        )
        embedVar.set_image(url=config.MuteCity)
        embedVar.set_thumbnail(url=config.Egg)
        embedVar.add_field(name="Track Code:",value="5-4",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)


async def setup(bot):
    await bot.add_cog(EggCup(bot))