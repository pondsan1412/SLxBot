import discord
from discord.ext import commands
from cog import config
import json
import os

class LuckyCatCup(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.hybrid_command(
        name="tokyoblur",
        description="Tokyo Blur",
        help="Track Code: `bTB, btb, or 14-1`",
        aliases=["bTB","btb","14-1"]
    )
    async def _track_bBR(self,ctx):
        embedVar = discord.Embed(
            title="Lucky Cat Cup",
            description="Tour Tokyo Blur",
            color=discord.Color.dark_purple()
        )
        embedVar.set_image(url=config.TokyoBlur)
        embedVar.set_thumbnail(url=config.LuckyCat)
        embedVar.add_field(name="Track Code:",value="14-1",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)


    @commands.hybrid_command(
        name="shroomridge",
        description="Shroom Ridge",
        help="Track Code: `bSR, bsr, or 14-2`",
        aliases=["bSR","bsr","14-2"]
    )
    async def _track_bMC(self,ctx):
        embedVar = discord.Embed(
            title="Lucky Cat Cup",
            description="DS Shroom Ridge",
            color=discord.Color.dark_purple()
        )
        embedVar.set_image(url=config.ShroomRidge)
        embedVar.set_thumbnail(url=config.LuckyCat)       
        embedVar.add_field(name="Track Code:",value="14-2",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)
    
    
    @commands.hybrid_command(
        name="skygarden",
        description="Sky Garden",
        help="Track Code: `bSG, bsg, or 14-3`",
        aliases=["bSG","bsg","14-3"]
    )
    async def _track_bSG(self,ctx):
        embedVar = discord.Embed(
            title="Lucky Cat Cup",
            description="GBA Sky Garden",
            color=discord.Color.dark_purple()
        )
        embedVar.set_image(url=config.SkyGarden)
        embedVar.set_thumbnail(url=config.LuckyCat)
        embedVar.add_field(name="Track Code:",value="14-3",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)


    @commands.hybrid_command(
        name="ninjahideaway",
        description="Ninja Hideaway",
        help="Track Code: `bNH, bnh, or 14-4`",
        aliases=["bNH","bnh","14-4"]
    )
    async def _track_bNH(self,ctx):
        embedVar = discord.Embed(
            title="Lucky Cat Cup",
            description="Ninja Hideaway",
            color=discord.Color.dark_purple()
        )
        embedVar.set_image(url=config.NinjaHideaway)
        embedVar.set_thumbnail(url=config.LuckyCat)
        embedVar.add_field(name="Track Code:",value="14-4",inline=False)
        embedVar.set_footer(text=f"Using a command by {ctx.author}")
        await ctx.send(embed=embedVar)


async def setup(bot):
    await bot.add_cog(LuckyCatCup(bot))