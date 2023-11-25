import discord
from discord.ext import commands, tasks
import random
import os
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
intents.guilds = True
class SlxBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=commands.when_mentioned_or("."),intents=intents)
       
    async def on_ready(self):
        print("ready")
    
    async def setup_hook(self):
        cog_folder = "commands"  

        for filename in os.listdir(cog_folder):
            if filename.endswith(".py") and not filename.startswith("__"):
                module_name = f"{cog_folder}.{filename[:-3]}"
                try:
                    await self.load_extension(module_name)
                    print(f"Loaded extension: {module_name}")
                except Exception as e:
                    print(f"Failed to load extension {module_name}: {e}")


    async def update_activity(self):
        activity_messages = [
        ".show rgv",
        ".tl ฉันรักคุณ",
        "/submit",
    ]
        random_message = random.choice(activity_messages)
        activity = discord.Activity(name=f'{random_message} ', type=discord.ActivityType.playing)
        await self.change_presence(activity=activity, status=discord.Status.do_not_disturb)
from cog import secret
bot = SlxBot()
bot.run(token=secret.discord_token)

