import discord
from discord.ext import commands
from cog import config

class eventbot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()    
    async def on_message(
        self,
        message
    ):
        if message.author == self.bot.user:
            return
        if message.content =="emojitest":
            await message.reply(config.emoji_mushroom)
        


    
async def setup(bot):
    await bot.add_cog(eventbot(bot))