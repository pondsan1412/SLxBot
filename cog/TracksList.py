import discord
from discord.ext import commands
import json
from cog import config
import os
class TracksList(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.hybrid_command(
        name="babypark",
        description="",
        help="a babypark track",
        aliases=["dBP","dbp","DBP","Dbp","dbP","5-1"]
    )
    async def _track_dBP(self,ctx):
        embedVar = discord.Embed(
            title="dBP baby park ベビパ 5-1",
            description="GCN Baby Park",
            color=discord.Color.dark_blue()
        )
        embedVar.set_image(url=config.babypark)
        embedVar.add_field(name="babypark",value="None",inline=False)
        embedVar.set_footer(text=f"using command by{ctx.author}")
        await ctx.send(embed=embedVar)
    @commands.hybrid_command(name="testpage")
    async def page(self,ctx):
        page1 = discord.Embed(
            title="Page1/2",
            description="55",
            colour = discord.Colour.orange()
        )
        page2 = discord.Embed(
            title="Page2/2",
            description="5dasdasd5555",
            colour = discord.Colour.orange()
        )
        pages = [page1,page2]
        message = await ctx.send(embed= page1)
        await message.add_reaction(message,"⏮")
        i = 0
        emoji = ''
        while True:
            if emoji == '⏮':
                i = 0
                await message.edit_message(message,embed=pages[i])
            res = await message.wait_for_reaction(message=message,timeout=30.0)
            if res == None:
                break
            if str(res[i]) != '<b':
                emoji = str(res[0].emoji)
                await message.remove_reaction(message,res[0].emoji,res[1])
        await message.clear_reactions(message)
async def setup(bot):
    await bot.add_cog(TracksList(bot))