import discord
from discord.ext import commands
import json
from cog import config
import os
class TracksList(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    
async def setup(bot):
    await bot.add_cog(TracksList(bot))