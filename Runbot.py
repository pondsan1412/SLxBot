import discord
from discord.ext import commands
import os
from cog import config
from cog import TracksList
class bot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=commands.when_mentioned_or("."),
            intents=discord.Intents.all(),
            help_command= commands.DefaultHelpCommand(
            no_category = "other commands"
            )
        )
    async def on_ready(self):
        print(self.user)
        ch_ready = int(config.ch_onready)
        print(ch_ready)
        bot = self.get_channel(ch_ready)
        await bot.send("I'm ready sir")
    async def setup_hook(self):
        await bot.load_extension("cog.TracksList")
        await bot.tree.sync()

bot = bot()
bot.run(config.discord_token, reconnect=True)