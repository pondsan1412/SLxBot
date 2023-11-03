import discord
from discord.ext import commands, tasks
import random
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
class Slxbot(commands.AutoShardedBot):

    def __init__(self, command_prefix=commands.when_mentioned_or("."), *, intents: discord.Intents = intents) -> None:
        super().__init__(command_prefix, intents=intents)

    async def setup_hook(self) -> None:
        await bot.tree.sync()
bot = Slxbot(intents=intents)
activity_messages = [
    ".show rgv",
    ".tl ฉันรักคุณ",
    "/submit",
]

# สร้างฟังก์ชันสำหรับอัปเดตกิจกรรมของบอท
async def update_activity():
    random_message = random.choice(activity_messages)
    activity = discord.Activity(name=f'{random_message} ', type=discord.ActivityType.playing)
    await bot.change_presence(activity=activity, status=discord.Status.do_not_disturb)

@bot.event
async def on_ready():
    await update_activity()
    random_activity_loop.start()
    msg = bot.get_channel(1163800972867416064)
    await msg.send("ready")
    

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
from cog import secret

from new_command.context import context
from cog.commands.event import eventbot
from cog.commands.General import General
from cog.commands.leaderboard import Slxleaderboard
from cog.commands.TTUpdate import UpdateTimeTrials
async def main():
        for cog in{
            context,
            General,
            eventbot,
            Slxleaderboard,
            UpdateTimeTrials,
            
        }:
            await bot.add_cog(cog(bot))
        random_activity_loop.start()
        await update_activity()
        
        await bot.start(secret.discord_token)
        


import asyncio
asyncio.run(main())
