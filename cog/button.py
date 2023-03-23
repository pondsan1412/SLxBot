import discord
from discord.ext import commands

class Buttons(discord.ui.View):
    def __init__(self,*, timeout=100):
        super().__init__(timeout=timeout)
        
    @discord.ui.button(
        label="List",
        style=discord.ButtonStyle.blurple
    )
    async def gray_button(
        self,
        i:discord.Interaction,
        button:discord.ui.Button
        
    ):
        await i.response.edit_message(content=f"hello Zquka",view=self)
    @discord.ui.button(label="of",style=discord.ButtonStyle.red)
    async def red_button(
        self,
        i:discord.Interaction,
        button:discord.ui.Button
        
    ):
        await i.response.edit_message(content=f"what are you doing?",view=self)
    @discord.ui.button(label="commands",style=discord.ButtonStyle.green)
    async def green_button(
        self,
        i:discord.Interaction,
        button:discord.ui.Button
        
    ):
        await i.response.edit_message(content=f"how are you today?",view=self)          
async def setup(bot):
    await bot.add_cog(Buttons(bot))