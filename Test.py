import discord
from discord.ext import commands
from cog import config
from cog import embedconfig
from cog import embedtrack

class trackbot(commands.Cog):
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
            command = message.content.split()[0]
            if command == "1-1":
                do what ever here
        except IndexError:
            pass

        