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
                await message.reply("https://cdn.discordapp.com/attachments/1123118531328872498/1163411249674076181/dddddddd.jpg?ex=653f7a29&is=652d0529&hm=6b6db29bc42dc667cee461708e08389ddaf18c950685f28bb8babf2aadb50856&")
                await message.reply("https://cdn.discordapp.com/attachments/875217920131727451/875218003522912306/MK8D_ABBREV.png?ex=654c50c8&is=6539dbc8&hm=52aef9ebc759a8f2d8c8db9bb58c91a8cdbaef131ae172556d964eff6f24e066&")
            
        except IndexError:
            pass
async def setup(bot):
    await bot.add_cog(
        eventbot(bot)
    )