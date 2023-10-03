import discord
from discord.ext import commands
from cog import config
import json
import os

class CherryCup(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.hybrid_command(
        name="losangeleslaps",
        description="Los Angeles Laps",
        help="Track Code: `bLAL, blal, or 22-1`",
        aliases=["bLAL","blal","22-1"]
    )
    async def _track_bLAL(self,ctx):
        embedVar = discord.Embed(
            title="Cherry Cup",
            description="Tour Los Angeles Laps",
            color=discord.Color.yellow()
        )
        embedVar.set_image(url=config.LosAngelesLaps)
        embedVar.set_thumbnail(url=config.Cherry)
        embedVar.add_field(name="Track Code:",value="22-1",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)


    @commands.hybrid_command(
        name="sunsetwilds",
        description="Sunset Wilds",
        help="Track Code: `bSW, bsw, or 22-2`",
        aliases=["bSW","bsw","22-2"]
    )
    async def _track_bSW(self,ctx):
        embedVar = discord.Embed(
            title="Cherry Cup",
            description="GBA Sunset Wilds",
            color=discord.Color.dark_orange()
        )
        embedVar.set_image(url=config.SunsetWilds)
        embedVar.set_thumbnail(url=config.Cherry)       
        embedVar.add_field(name="Track Code:",value="22-2",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)
    
    
    @commands.hybrid_command(
        name="koopacape",
        description="Koopa Cape",
        help="Track Code: `bKC, bkc, or 22-3`",
        aliases=["bKC","bkc","22-3"]
    )
    async def _track_bKC(self,ctx):
        embedVar = discord.Embed(
            title="Cherry Cup",
            description="Wii Koopa Cape",
            color=discord.Color.teal()
        )
        embedVar.set_image(url=config.KoopaCape)
        embedVar.set_thumbnail(url=config.Cherry)
        embedVar.add_field(name="Track Code:",value="22-3",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)


    @commands.hybrid_command(
        name="vancouvervelocity",
        description="Vancouver Velocity",
        help="Track Code: `bVV, bvv, or 22-4`",
        aliases=["bVV","bvv","22-4"]
    )
    async def _track_bVV(self,ctx):
        embedVar = discord.Embed(
            title="Cherry Cup",
            description="Tour Vancouver Velocity",
            color=discord.Color.dark_blue()
        )
        embedVar.set_image(url=config.VancouverVelocity)
        embedVar.set_thumbnail(url=config.Cherry)
        embedVar.add_field(name="Track Code:",value="22-4",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)


async def setup(bot):
    await bot.add_cog(CherryCup(bot))