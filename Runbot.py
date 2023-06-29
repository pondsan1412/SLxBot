import discord
from discord.ext import commands
import os
from cog import config
from cog import secret
from googletrans import Translator
from cog.commands.event import eventbot
class bot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=commands.when_mentioned_or("."),
            intents=discord.Intents.all(),
            no_category=None
            )
            
        
    async def on_ready(self):
        print(self.user)
        ch_ready = int(secret.ch_onready)
        print(ch_ready)
    async def setup_hook(self):
        extensions = [
    "cog.commands.General",
    "cog.commands.event",
    "cog.commands.error",
    "cog.commands.TTUpdate",
    "cog.commands.infooldtrack.1MushroomCup",
    "cog.commands.infooldtrack.2FlowerCup",
    "cog.commands.infooldtrack.3StarCup",
    "cog.commands.infooldtrack.4SpecialCup",
    "cog.commands.infooldtrack.5EggCup",
    "cog.commands.infooldtrack.6CrossingCup",
    "cog.commands.infooldtrack.7ShellCup",
    "cog.commands.infooldtrack.8BananaCup",
    "cog.commands.infooldtrack.9LeafCup",
    "cog.commands.infooldtrack.10LightningCup",
    "cog.commands.infooldtrack.11TriforceCup",
    "cog.commands.infooldtrack.12BellCup",
    "cog.commands.infodlctrack.13GoldenDashCup",
    "cog.commands.infodlctrack.14LuckyCatCup",
    "cog.commands.infodlctrack.15TurnipCup",
    "cog.commands.infodlctrack.16PropellerCup",
    "cog.commands.infodlctrack.17RockCup",
    "cog.commands.infodlctrack.18MoonCup",
    "cog.commands.infodlctrack.19FruitCup",
    "cog.commands.infodlctrack.20BoomerangCup",
]
        bot.remove_command("help")
        for extension in extensions:
            await bot.load_extension(extension)
        await bot.tree.sync()
    
       
    
   

bot = bot()
bot.run(secret.discord_token, reconnect=True)