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
    "cog.commands.oldtrack.1MushroomCup",
    "cog.commands.oldtrack.2FlowerCup",
    "cog.commands.oldtrack.3StarCup",
    "cog.commands.oldtrack.4SpecialCup",
    "cog.commands.oldtrack.5EggCup",
    "cog.commands.oldtrack.6CrossingCup",
    "cog.commands.oldtrack.7ShellCup",
    "cog.commands.oldtrack.8BananaCup",
    "cog.commands.oldtrack.9LeafCup",
    "cog.commands.oldtrack.10LightningCup",
    "cog.commands.oldtrack.11TriforceCup",
    "cog.commands.oldtrack.12BellCup",
    "cog.commands.dlctrack.13GoldenDashCup",
    "cog.commands.dlctrack.14LuckyCatCup",
    "cog.commands.dlctrack.15TurnipCup",
    "cog.commands.dlctrack.16PropellerCup",
    "cog.commands.dlctrack.17RockCup",
    "cog.commands.dlctrack.18MoonCup",
    "cog.commands.dlctrack.19FruitCup",
    "cog.commands.dlctrack.20BoomerangCup",
]
        bot.remove_command("help")
        for extension in extensions:
            await bot.load_extension(extension)
 
              
        await bot.tree.sync()
    
       
    
   

bot = bot()
bot.run(secret.discord_token, reconnect=True)