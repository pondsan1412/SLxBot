import discord
from discord.ext import commands
import json
from cog import config
import os
import asyncio,time
from discord.ext.commands import HelpCommand, CommandNotFound
from discord import app_commands
from discord.ui import View,Button
from googletrans import Translator
from cog.SelectMenus import *

class General(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
        self.words_txt = ""
        
    def cog_unload(self):
        self.bot.help_command = self._original_help_command
    
    async def help(self, ctx):
        pass
    @commands.hybrid_command(
            name="test",
            help="to test next page button using emoji"
    )
    async def _test(self,ctx):
         # Create Embed object
        embed = discord.Embed(title="Page 1/2", description="Description", color=discord.Color.blue())

        #Add fields to Embed object
        embed.add_field(name="Field 1", value="Value 1", inline=False)
        embed.add_field(name="Field 2", value="Value 2", inline=False)

       # Send an Embed object and store the sent message in the message variable
        message = await ctx.send(embed=embed)

        
# Add a button to the message to switch to the second page
        await message.add_reaction("⬅️")

        # Add a button to go back to the previous page
        await message.add_reaction("➡️")

        # Create a function to check the user's reaction
        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) in ["⬅️", "➡️"]

        current_embed_page = 1

        while True:
            try:
                reaction, user = await self.bot.wait_for('reaction_add', timeout=5.0,check=check)
            except asyncio.TimeoutError:
                embed_timeout = discord.Embed(title="Timeout", description="this page was delete so try to command again I was set timeout in 10s", color=discord.Color.red())
                await message.edit(embed=embed_timeout)
                await message.clear_reactions()
                break
            else:
                if str(reaction.emoji) == "➡️" and current_embed_page == 1:
                # Your code for switching to page 2
                    # Send the second Embed object
                    embed2 = discord.Embed(title="Page 2/2", description="This is page 2 Zquka kung", color=discord.Color.green())
                    embed2.add_field(name="Field 1", value="Value 1", inline=False)
                    embed2.add_field(name="Field 2", value="Value 2", inline=False)
                    await message.edit(embed=embed2)
                    current_embed_page = 2
                elif str(reaction.emoji) == "⬅️" and current_embed_page == 2:
                    # Send Embed object page one
                    await message.edit(embed=embed)
                    current_embed_page = 1
                await message.remove_reaction(str(reaction.emoji), user)
    @commands.hybrid_command(
        name="button",
        help="test button",
        description="test button"
    )
    async def _buttontest(
        self,
        ctx: commands.Context
    ):
        button1 = discord.ui.Button(
            style=discord.ButtonStyle.blurple,
            label="Zquka baka",
        )
        button2 = discord.ui.Button(
            style=discord.ButtonStyle.red,
            label="Sleeping allday",
        )
        button3 = discord.ui.Button(
            style=discord.ButtonStyle.green,
            label="when you wakeup",
        )
        view = discord.ui.View()
        view.add_item(button1)
        view.add_item(button2)
        view.add_item(button3)
        embed = discord.Embed()
        embed.set_image(url="https://cdn.discordapp.com/attachments/960467344826720277/1086732556369661993/image.png")
        
        await ctx.send(embed=embed,view=view)
    
    @commands.hybrid_command(
        name="translate",
        help="useful command to translate ",
        description="useful command to translate",
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
        translated_text = translator.translate(message, dest="de")
        
        # Create the message with the translated text and the flag emoji
        message_with_emoji = f"`Default is German`: {translated_text.text}"
        
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
                reaction, user = await self.bot.wait_for('reaction_add', timeout=10.0, check=check)
            except asyncio.TimeoutError:
                asyncio.create_task(message.edit(content=f"timeout❌"))
                break
    @commands.hybrid_command(
        name="select",
        description="test select menus"
    )
    async def _selectmenus(
        self,
        ctx
    ):
        await ctx.send(
            embed=config.embedSelect,
            view=SelectView()
        )
    @commands.has_any_role('dev')            
    @commands.hybrid_command(
        name="send",
        help="send messages into channel author",
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
            
        
async def setup(bot):
    await bot.add_cog(General(bot))