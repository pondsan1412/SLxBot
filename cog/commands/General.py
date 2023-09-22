import discord
from discord.ext import commands
import json
from cog import embedconfig
import os
import asyncio,time
from discord.ext.commands import HelpCommand, CommandNotFound
from discord import app_commands
from discord.ui import View,Button
from googletrans import Translator
from cog.SelectMenus import *
from cog.button import *
class General(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
        self.words_txt = ""
        
    def cog_unload(self):
        self.bot.help_command = self._original_help_command
    
    async def help(self, ctx):
        pass
    @commands.hybrid_command(
        name="translate",
        help="useful command to translate ",
        description="Useful command to translate",
        aliases=["tl","แปล","trans"]
    )
    async def _translate(self, ctx:commands.Context, *, message):
        # Define the flag emoji for Germany and Japan
        flag_emoji_ger = "🇩🇪"
        flag_emoji_jp = "🇯🇵"
        flag_emoji_nl = "🇳🇱"
        flag_emoji_us = "🇺🇸"
        flag_emoji_th = "🇹🇭"
        # Translate the message to English
        translator = Translator()
        translated_text = translator.translate(message, dest="en")
        
        # Create the message with the translated text and the flag emoji
        message_with_emoji = f"`Default is English`: {translated_text.text}"
        
        # Send the message to the channel
        message = await ctx.send(message_with_emoji)
        
        # Add the flag emoji as a reaction to the message
        await message.add_reaction(flag_emoji_ger)
        await message.add_reaction(flag_emoji_jp)
        await message.add_reaction(flag_emoji_nl)
        await message.add_reaction(flag_emoji_us)
        await message.add_reaction(flag_emoji_th)
        
        # Define a check function to filter the reactions
        def check(reaction, user):
            if str(reaction.emoji) in [
                flag_emoji_ger,flag_emoji_jp,
                flag_emoji_nl,flag_emoji_us,
                flag_emoji_th
            ]:
                if user != self.bot.user:
                    dest_lang = None
                
                    if str(reaction.emoji) == flag_emoji_ger:
                        dest_lang = "de"
                    elif str(reaction.emoji) == flag_emoji_jp:
                        dest_lang = "ja"
                    elif str(reaction.emoji) == flag_emoji_nl:
                        dest_lang = "nl"
                    elif str(reaction.emoji) == flag_emoji_us:
                        dest_lang = "en"
                    elif str(reaction.emoji) == flag_emoji_th:
                        dest_lang = "th"

                    if dest_lang is not None:
                        new_translate = translator.translate(translated_text.text, dest=dest_lang)
                        asyncio.create_task(message.edit(content=f"`{new_translate.dest}`: {new_translate.text}"))
                        return True
            return False       
        # Wait for the user to react with the flag emoji
        while True:
            try:
                reaction, user = await self.bot.wait_for('reaction_add', timeout=15.0, check=check)
            except asyncio.TimeoutError:
                asyncio.create_task(message.edit(content=f"Timeout❌"))
                break
    @commands.hybrid_command(
        name="help",
        description="Help Information"
    )
    async def _selectmenus(
        self,
        ctx:commands.Context
    ):
        await ctx.send(
            embed=embedconfig.embedSelect,
            view=SelectView(),
            delete_after=100
        )
    @commands.has_any_role('dev')            
    @commands.hybrid_command(
        name="send",
        help="Bot send a message to any channel with commands",
        description="send messages to channel"
    )
    async def _send_messages(
        self,
        ctx:commands.Context,
        channel_to_send:discord.TextChannel,
        messages_to_send:str
    ):
        channel = discord.utils.get(
            ctx.guild.channels,
            name=f"{channel_to_send}"
        )
        channel_id = channel.id
        ch_to_send = self.bot.get_channel(channel_id)
        await ch_to_send.send(messages_to_send)
        await ctx.send(
            f"channel id is :{channel_id}",
            delete_after=0.1
        )

    @commands.hybrid_command(name="remove") #this is text remove command
    async def _removetext(self,ctx:commands.Context,value:int):
        try:
            await ctx.send("removing",ephemeral=True, delete_after=3)
            await ctx.channel.purge(limit=value) #put value to remove
            await ctx.message.delete()#here for delete message
            
        except discord.Forbidden:
            await ctx.send("I can't remove the message due permission!!")

   
   
async def setup(bot):
    await bot.add_cog(General(bot))