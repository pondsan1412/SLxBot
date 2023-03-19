import discord
from discord.ext import commands
from cog import config
import json
import os

class ShellCup(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.hybrid_command(
        name="moomoomeadows",
        description="Moo Moo Meadows",
        help="Track Code: `rMMM, rmmm, 7-1`",
        aliases=["rMMM","rmmm","7-1"]
    )
    async def _track_rMMM(self,ctx):
        embedVar = discord.Embed(
            title="Shell Cup",
            description="Wii Moo Moo Meadows",
            color=discord.Color.dark_purple()
        )
        embedVar.set_image(url=config.MooMooMeadows)
        embedVar.set_thumbnail(url=config.Shell)
        embedVar.add_field(name="Track Code:",value="7-1",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)


    @commands.hybrid_command(
        name="rmariocircuit",
        description="Mario Circuit",
        help="Track Code: `rMC, rmc, 7-2`",
        aliases=["rMC","rmc","7-2"]
    )
    async def _track_rMC(self,ctx):
        embedVar = discord.Embed(
            title="Shell Cup",
            description="GBA Mario Circuit",
            color=discord.Color.dark_purple()
        )
        embedVar.set_image(url=config.rMarioCircuit)
        embedVar.set_thumbnail(url=config.Shell)       
        embedVar.add_field(name="Track Code:",value="7-2",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)
    
    
    @commands.hybrid_command(
        name="cheepcheepbeach",
        description="Cheep Cheep Beach",
        help="Track Code: `rCCB, rccb, 7-3`",
        aliases=["rCCB","rccb","7-3"]
    )
    async def _track_rCCB(self,ctx):
        embedVar = discord.Embed(
            title="Shell Cup",
            description="DS Cheep Cheep Beach",
            color=discord.Color.dark_purple()
        )
        embedVar.set_image(url=config.CheepCheepBeach)
        embedVar.set_thumbnail(url=config.Shell)
        embedVar.add_field(name="Track Code:",value="7-3",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)


    @commands.hybrid_command(
        name="toadturnpike",
        description="Toad\'s Turnpike",
        help="Track Code: `rTT, rtt, 7-4`",
        aliases=["rTT","rtt","7-4"]
    )
    async def _track_rTT(self,ctx):
        embedVar = discord.Embed(
            title="Shell Cup",
            description="N64 Toad\'s Turnpike",
            color=discord.Color.dark_purple()
        )
        embedVar.set_image(url=config.ToadsTurnpike)
        embedVar.set_thumbnail(url=config.Shell)
        embedVar.add_field(name="Track Code:",value="7-4",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)


async def setup(bot):
    await bot.add_cog(ShellCup(bot))