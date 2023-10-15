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
            if message.guild and message.guild.id == 1039904904833150986:
                return
            if message.channel.id in config.annoying_channel:
                return
            # สร้าง Embed
            embed = discord.Embed(
                title='message',
                description=message.content,
                color=0x3498db  # สีของ Embed
            )

            embed.set_author(name=message.author.name, icon_url=message.author.display_avatar.url)  # ข้อมูลผู้ส่ง
            
            embed.add_field(name='server', value=message.guild.name, inline=True)
            embed.add_field(name='channel', value=message.channel.mention, inline=True)

            # ตรวจสอบว่าข้อความมีรูปภาพหรือไม่
            if message.attachments:
                for attachment in message.attachments:
                    image_url = attachment.url
                    embed.set_image(url=image_url)  # เพิ่มรูปภาพลงใน Embed

            target_channel = self.bot.get_channel(config.network_community_dc)

            if target_channel:
                await target_channel.send(embed=embed)
            
        except IndexError:
            pass
            