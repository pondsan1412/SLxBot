import discord
from discord.ext import commands

import discord

class eventbot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()    
    async def on_message(
        self,
        message
    ):
        try:
            if message.author == self.bot.user:
                return
            code = message.content.lower()
            if code.startswith("code"):
                await message.reply("https://cdn.discordapp.com/attachments/1123118531328872498/1172434340035174460/new_dlc_tracks.jpg?ex=65604d91&is=654dd891&hm=6b57d73b3ca71a8ee94a6945e71710851bad28b631eafef77947a575a2cbc4ea&")
                await message.reply("https://cdn.discordapp.com/attachments/875217920131727451/875218003522912306/MK8D_ABBREV.png?ex=654c50c8&is=6539dbc8&hm=52aef9ebc759a8f2d8c8db9bb58c91a8cdbaef131ae172556d964eff6f24e066&")
            
        except IndexError:
            pass
        
async def setup(bot):
    await bot.add_cog(
        eventbot(bot)
    )