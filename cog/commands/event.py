import discord
from discord.ext import commands
from cog import config
from cog import embedconfig
from cog import embedtrack
import os
import openai
import asyncio
import discord

class eventbot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()    
    async def on_message(
        self,
        message
    ):
        config.annoying_channel
        
        try:
            if message.author == self.bot.user:
                return
            code = message.content.lower()
            if code.startswith("code"):
                await message.reply("https://cdn.discordapp.com/attachments/1123118531328872498/1163411249674076181/dddddddd.jpg?ex=653f7a29&is=652d0529&hm=6b6db29bc42dc667cee461708e08389ddaf18c950685f28bb8babf2aadb50856&")
           
            
        except IndexError:
            pass
            