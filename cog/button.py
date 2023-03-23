import discord
from discord.ext import commands
from cog import config
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
        embedGeneral1 = discord.Embed(
            title="General Command List",
            color=discord.Color.gold,
            type='rich',
        )
        embedGeneral1.set_author(name=i.author,url=config.some_of_anime_girl)
        embedGeneral1.add_field(name="default command",value="translate: any")
        await i.response.edit_message(embed=embedGeneral1,view=self)
            
async def setup(bot):
    await bot.add_cog(Buttons(bot))