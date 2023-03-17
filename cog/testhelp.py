from discord.ext import commands
import discord
import asyncio
class testhelp(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(
        name="help"
    )
    async def help(self,ctx):
        # help pages
        page1 = discord.Embed(title="Bot Help 1", description="Use the buttons below to navigate between help pages.", colour=discord.Colour.orange())
        page2 = discord.Embed(title="Bot Help 2", description="Page 2", colour=discord.Colour.orange())
        page3 = discord.Embed(title="Bot Help 3", description="Page 3", colour=discord.Colour.orange())

        self.bot.help_pages = [page1, page2, page3]
        buttons = [u"\u23EA", u"\u2B05", u"\u27A1", u"\u23E9"] # skip to start, left, right, skip to end
        current = 0
        msg = await ctx.send(embed=self.bot.help_pages[current])
        for button in buttons:
            await msg.add_reaction(button)
        
        while True:
            try:
                reaction, user = await self.bot.wait_for("reaction_add", check=lambda reaction, user: user == ctx.author and reaction.emoji in buttons, timeout=60.0)

            except asyncio.TimeoutError:
                return print("test")

            else:
                previous_page = current
                if reaction.emoji == u"\u23EA":
                    current = 0
                    
                elif reaction.emoji == u"\u2B05":
                    if current > 0:
                        current -= 1
                        
                elif reaction.emoji == u"\u27A1":
                    if current < len(self.bot.help_pages)-1:
                        current += 1

                elif reaction.emoji == u"\u23E9":
                    current = len(self.bot.help_pages)-1

                for button in buttons:
                    await msg.remove_reaction(button, ctx.author)

                if current != previous_page:
                    await msg.edit(embed=self.bot.help_pages[current])
async def setup(bot):
    await bot.add_cog(testhelp(bot))