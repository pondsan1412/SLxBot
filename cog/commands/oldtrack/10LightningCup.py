import discord
from discord.ext import commands
from cog import config
import json
import os

class LightningCup(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.hybrid_command(
        name="tick-tockclock",
        description="Tick-Tock Clock",
        help="Track Code: `rTTC, rttc, 10-1`",
        aliases=["rTTC","rttc","10-1"]
    )
    async def _track_rTTC(self,ctx):
        embedVar = discord.Embed(
            title="Lightning Cup",
            description="DS Tick-Tock Clock",
            color=discord.Color.dark_purple()
        )
        embedVar.set_image(url=config.TickTockClock)
        embedVar.set_thumbnail(url=config.Lightning)
        embedVar.add_field(name="Track Code:",value="10-1",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)


    @commands.hybrid_command(
        name="piranhaplantslide",
        description="Piranha Plant Slide",
        help="Track Code: `rPPS, rpps, 10-2`",
        aliases=["rPPS","rpps","10-2"]
    )
    async def _track_rPPS(self,ctx):
        embedVar = discord.Embed(
            title="Lightning Cup",
            description="3DS Piranha Plant Slide",
            color=discord.Color.dark_purple()
        )
        embedVar.set_image(url=config.PiranhaPlantSlide)
        embedVar.set_thumbnail(url=config.Lightning)       
        embedVar.add_field(name="Track Code:",value="10-2",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)
    
    
    @commands.hybrid_command(
        name="grumblevolcano",
        description="Grumble Volcano",
        help="Track Code: `rGV, rgv, 10-3`",
        aliases=["rGV","rgv","10-3"]
    )
    async def _track_rGV(self,ctx):
        embedVar = discord.Embed(
            title="Lightning Cup",
            description="Wii Grumble Volcano",
            color=discord.Color.dark_purple()
        )
        embedVar.set_image(url=config.GrumbleVolcano)
        embedVar.set_thumbnail(url=config.Lightning)
        embedVar.add_field(name="Track Code:",value="10-3",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)


    @commands.hybrid_command(
        name="n64rainbowroad",
        description="Rainbow Road",
        help="Track Code: `rRRd, rrrd, 10-4`",
        aliases=["rRRd","rrrd","10-4"]
    )
    async def _track_rRRd(self,ctx):
        embedVar = discord.Embed(
            title="Lightning Cup",
            description="N64 Rainbow Road",
            color=discord.Color.dark_purple()
        )
        embedVar.set_image(url=config.nRainbowRoad)
        embedVar.set_thumbnail(url=config.Lightning)
        embedVar.add_field(name="Track Code:",value="10-4",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)


async def setup(bot):
    await bot.add_cog(LightningCup(bot))