import discord
from discord.ext import commands
import asyncio
from discord import Embed
from googletrans import Translator
import random  
from langdetect import detect
import json
from new_command import player_id
import function
from easygoogletranslate import EasyGoogleTranslate
from googletrans import Translator
class Button(discord.ui.View):
    def __init__(self, message):
        super().__init__(timeout=600000)
        self.value = None
        self.message = message

    @discord.ui.button(label='delete', style=discord.ButtonStyle.red)
    async def delete(self, i: discord.Interaction,button: discord.ui.Button):
        await self.message.delete()

class tracking_tl(commands.Cog):
    def __init__(self, bot:commands.Bot) ->None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author == self.bot.user:
            return
        
        def filter_translate(result): 
            translate = EasyGoogleTranslate(source_language='auto',target_language='en')
            result = translate.translate(text=f"{message.content}")
            return result
       
        def detect_lang():
            translator_ = Translator()
            message_=translator_.detect(text=f'{message.content}')
            detected_language = message_.lang
            return detected_language
        stan_=self.bot.get_user(player_id.Stan)
        robert_=self.bot.get_user(player_id.Robertala)
        pond_ = self.bot.get_user(player_id.Pond)
        detect_ = detect_lang()
        translator= filter_translate(result="")
        lang_list = ['fr','th','de','ja','nl']
        player_list=[pond_,robert_,stan_]
        if message.author in player_list:
            if detect_ not in lang_list:
                return
            else:
                embed = Embed()
                embed.add_field(name='', value=f'`{message.content}` \n meaning is: **{translator}**')
                embed.set_author(name=f'{message.author.name} said:', icon_url=message.author.display_avatar)
                view = Button(message=message)
                sent_message = await message.channel.send(embed=embed, view=view)
                # Save the ID of the sent message to use in the Button class
                view.message = sent_message
        else:
            return

async def setup(bot):
    await bot.add_cog(
        tracking_tl(bot)
    )