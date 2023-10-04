import discord
from discord.ext import commands
from cog import config
from cog import embedconfig
from cog import embedtrack

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
            if message.guild and message.guild.id == 1039904904833150986:
                return
            if "Fire" in message.content.split()[0]:
                await message.channel.send(content=config.x3Fire)
            

            # สร้าง Embed
            embed = discord.Embed(
                title='message',
                description=message.content,
                color=0x3498db  # สีของ Embed
            )

            embed.set_author(name=message.author.name, icon_url=message.author.display_avatar.url)  # ข้อมูลผู้ส่ง
            
            embed.add_field(name='server', value=message.guild.name, inline=True)
            embed.add_field(name='channel', value=message.channel.mention, inline=True)

            target_channel = self.bot.get_channel(1158721318200549446)
        
            
            if target_channel:
                await target_channel.send(embed=embed)
        except IndexError:
            pass
    
