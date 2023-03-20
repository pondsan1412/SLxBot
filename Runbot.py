import discord
from discord.ext import commands
import os
from cog import config
from cog import secret
from googletrans import Translator
from event import eventbot
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
        await bot.load_extension("cog.commands.General")
        await bot.load_extension("event")
        await bot.load_extension("cog.commands.oldtrack.1MushroomCup")
        await bot.load_extension("cog.commands.oldtrack.2FlowerCup")
        await bot.load_extension("cog.commands.oldtrack.3StarCup")
        await bot.load_extension("cog.commands.oldtrack.4SpecialCup")
        await bot.load_extension("cog.commands.oldtrack.5EggCup")        
        await bot.load_extension("cog.commands.oldtrack.6CrossingCup")
        await bot.load_extension("cog.commands.oldtrack.7ShellCup")
        await bot.load_extension("cog.commands.oldtrack.8BananaCup")
        await bot.load_extension("cog.commands.oldtrack.9LeafCup")
        await bot.load_extension("cog.commands.oldtrack.10LightningCup")
        await bot.load_extension("cog.commands.oldtrack.11TriforceCup")
        await bot.load_extension("cog.commands.oldtrack.12BellCup")
        await bot.load_extension("cog.commands.dlctrack.13GoldenDashCup")
        await bot.load_extension("cog.commands.dlctrack.14LuckyCatCup")
        await bot.load_extension("cog.commands.dlctrack.15TurnipCup")
        await bot.load_extension("cog.commands.dlctrack.16PropellerCup")
        await bot.load_extension("cog.commands.dlctrack.17RockCup")
        await bot.load_extension("cog.commands.dlctrack.18MoonCup")
        await bot.load_extension("cog.commands.dlctrack.19FruitCup")
        await bot.load_extension("cog.commands.dlctrack.20BoomerangCup")
        bot.remove_command("help")
        await bot.load_extension("cog.help")
        await bot.tree.sync()
    
       
    
   

bot = bot()
bot.run(secret.discord_token, reconnect=True)