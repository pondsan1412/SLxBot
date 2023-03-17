import discord
from discord.ext import commands
import json
from cog import config
import os
import asyncio
class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.hybrid_command(
            name="test",
            help="|to test next page button using emoji"
    )
    async def _test(self,ctx):
         # Create Embed object
        embed = discord.Embed(title="Title", description="Description", color=discord.Color.blue())

        #Add fields to Embed object
        embed.add_field(name="Field 1", value="Value 1", inline=False)
        embed.add_field(name="Field 2", value="Value 2", inline=False)

       # Send an Embed object and store the sent message in the message variable
        message = await ctx.send(embed=embed)

        
# Add a button to the message to switch to the second page
        await message.add_reaction("➡️")

        # Add a button to go back to the previous page
        await message.add_reaction("⬅️")

        # Create a function to check the user's reaction
        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) in ["➡️", "⬅️"]

        current_embed_page = 1

        while True:
            try:
                reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
            except asyncio.TimeoutError:
               # If user does not reply within 60 seconds
                await message.clear_reactions()
                break
            else:
                if str(reaction.emoji) == "➡️" and current_embed_page == 1:
                   
            # Send the second Embed object
                    embed2 = discord.Embed(title="Page 2", description="This is page 2", color=discord.Color.green())
                    await message.edit(embed=embed2)
                    current_embed_page = 2
                elif str(reaction.emoji) == "⬅️" and current_embed_page == 2:
                    # Send Embed object page one
                    await message.edit(embed=embed)
                    current_embed_page = 1
                await message.remove_reaction(str(reaction.emoji), user)
async def setup(bot):
    await bot.add_cog(General(bot))