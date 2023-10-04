import discord
from discord.ext import commands, tasks
from mk8dx import lounge_api,Track
from typing import Optional
import os
from track.cog import TrackCog
from lounge.cog import LoungeCog
from cog.commands.leaderboard import Slxleaderboard
from cog.commands.General import General
from cog.commands.event import eventbot
from cog.commands.error import error
from cog.commands.TTUpdate import UpdateTimeTrials
from sokuji.cog import SokujiCog
import task
intents=discord.Intents.all()
prefix=commands.when_mentioned_or(".")
intents.message_content = True
bot = commands.Bot(intents=intents,command_prefix=prefix,help_command=None)



    

    


@bot.event
async def on_ready():
    print('bot ready.')
    await update_activity()

@bot.event
async def on_guild_join(_: discord.Guild):
    await update_activity()

@bot.event
async def on_guild_remove(_: discord.Guild):
    await update_activity()
    
for cog in {
    
    LoungeCog,
    TrackCog,
    General,
    eventbot,
    error,
    SokujiCog
    
}:
   
    bot.add_cog(cog(bot))
    
async def update_activity():
    activity = discord.Activity(name=f'YO WTF AMDX - {len(bot.guilds)} servers', type=discord.ActivityType.playing)
    await bot.change_presence(activity=activity,status=discord.Status.do_not_disturb)




from cog import secret
bot.run(secret.discord_token)