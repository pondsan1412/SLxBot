import discord
from discord.ext import commands


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
        if message.content =="emojisend":
            await message.reply(content="https://cdn.discordapp.com/emojis/1087361067568607232.webp?size=96&quality=lossless")
        


    
async def setup(bot):
    await bot.add_cog(eventbot(bot))