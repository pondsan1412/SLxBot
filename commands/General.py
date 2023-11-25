import discord
from discord.ext import commands
import asyncio
from googletrans import Translator
import random  
import json
from cog import player_id
#from cog.commands.TTUpdate import SelectTTupdater

DATA_FILE = "player_data.txt"

# อ่านข้อมูลผู้เล่นจากไฟล์ JSON
def load_player_data():
    player_data = {}
    try:
        with open(DATA_FILE, "r") as file:
            for line in file:
                discord_id, twitch_link = line.strip().split(",")
                player_data[int(discord_id)] = twitch_link
    except FileNotFoundError:
        pass
    return player_data

# บันทึกข้อมูลผู้เล่นไปยังไฟล์ข้อความ
def save_player_data(player_data):
    with open(DATA_FILE, "w") as file:
        for discord_id, twitch_link in player_data.items():
            file.write(f"{discord_id},{twitch_link}\n")
class General(commands.Cog):
    def __init__(self, bot) ->None:
        self.bot = bot
       
        self.words_txt = ""
        
    def cog_unload(self):
        self.bot.help_command = self._original_help_command
    
    
    @commands.command(
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
                reaction, user = await self.bot.wait_for('reaction_add', timeout=600.0, check=check)
            except asyncio.TimeoutError:
                asyncio.create_task(message.edit(content=f"Timeout❌"))
                break
    
    @commands.command(name="remove") #this is text remove command
    async def _removetext(self,ctx:commands.Context,value:int):
        try:
            await ctx.send("Removing messages...", delete_after=1)  # ส่งข้อความ "Removing messages..." และลบมันหลังจาก 3 วินาที

            # หากคุณต้องการเพิ่มความสาธารณะให้คำสั่ง "removing" ให้ไม่ใช้ ephemeral=True
            await asyncio.sleep(3)
            await ctx.channel.purge(limit=value)  # ลบข้อความตามจำนวนที่ระบุ
        except commands.MissingRequiredArgument:
            await ctx.send("Please provide the number of messages to remove.")
        except discord.Forbidden:
            await ctx.send("I can't remove the message due to permissions!")

    @commands.command(name="mystream")
    async def _mystream(self,ctx):
        discord_id = ctx.author.id
        player_data = load_player_data()

        if discord_id in player_data:
            player_link = player_data[discord_id]
            await ctx.send(player_link)
        else:
            await ctx.send("You have not registered yet. Please use .register {yourlink}")
                
    @commands.command(name="register")
    async def _register(self,ctx, twitch_link):
        discord_id = ctx.author.id
        player_data = load_player_data()
        player_data[discord_id] = twitch_link
        save_player_data(player_data)
        await ctx.send(f"Registered your Twitch stream: {twitch_link}")

    

    
async def setup(bot):
    await bot.add_cog(
        General(bot)
    )
    
