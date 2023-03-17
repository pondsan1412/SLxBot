import discord
from discord.ext import commands
import os
from cog import config
from cog.commands import TracksList
from cog import secret
from cog.commands import General
class CustomHelpCommand(commands.DefaultHelpCommand):
    def __init__(self, **options):
        super().__init__(**options)
        self.default_category = None
class bot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=commands.when_mentioned_or("."),
            intents=discord.Intents.all(),
            help_command= CustomHelpCommand(no_category = None),
        )
    async def on_ready(self):
        print(self.user)
        ch_ready = int(secret.ch_onready)
        print(ch_ready)
        bot = self.get_channel(ch_ready)
        await bot.send("I'm ready sir")
    async def setup_hook(self):
        await bot.load_extension("cog.commands.TracksList")
        await bot.load_extension("cog.commands.General")
        await bot.tree.sync()

bot = bot()
bot.run(secret.discord_token, reconnect=True)