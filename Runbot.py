import discord
from discord.ext import commands, tasks
from mk8dx import lounge_api,Track
from typing import Optional
import os

from lounge.cog import LoungeCog
from cog.commands.leaderboard import Slxleaderboard
from cog.commands.General import General
from cog.commands.event import eventbot
from cog.commands.error import error
from cog.commands.TTUpdate import UpdateTimeTrials
from cog.commands.leaderboard import Slxleaderboard

import task
import random
intents=discord.Intents.all()
prefix=commands.when_mentioned_or(".")
intents.message_content = True
intents = discord.Intents.all()
prefix = commands.when_mentioned_or(".")
intents.message_content = True

activity_messages = [
    "Got idea? inbox Pond",
    "SLx's bot!",
    "Guess I can speak like humans?",
    "yes I am base on chatgpt!",
]

# สร้างฟังก์ชันสำหรับอัปเดตกิจกรรมของบอท
async def update_activity():
    random_message = random.choice(activity_messages)
    activity = discord.Activity(name=f'{random_message} ', type=discord.ActivityType.playing)
    await bot.change_presence(activity=activity, status=discord.Status.do_not_disturb)

bot = commands.Bot(intents=intents, command_prefix=prefix, help_command=None)

@bot.event
async def on_ready():
    await update_activity()
    random_activity_loop.start()
    print("ready")
# เริ่มลูปสุ่มกิจกรรม
@tasks.loop(seconds=7)
async def random_activity_loop():
    await update_activity()
@bot.event
async def on_guild_join(_: discord.Guild):
    await update_activity()
@bot.event
async def on_guild_remove(_: discord.Guild):
    await update_activity()
    
for cog in {
    LoungeCog,
    General,
    eventbot,
    error,
    UpdateTimeTrials,
    Slxleaderboard,
}:
   
    bot.add_cog(cog(bot))

from cog import secret
bot.run(secret.discord_token)