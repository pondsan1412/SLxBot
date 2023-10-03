import discord
from discord.ext import commands, tasks
import os
from cog import embedconfig
from cog import config
from cog import secret
from googletrans import Translator
from cog.commands.event import eventbot
import random
import asyncio
import sys
from discord.gateway import DiscordWebSocket, _log
from discord.ext.commands import Bot


async def identify(self):
    payload = {
        'op': self.IDENTIFY,
        'd': {
            'token': self.token,
            'properties': {
                '$os': sys.platform,
                '$browser': 'Discord Android',
                '$device': 'Discord Android',
                '$referrer': '',
                '$referring_domain': ''
            },
            'compress': True,
            'large_threshold': 250,
            'v': 3
        }
    }

    if self.shard_id is not None and self.shard_count is not None:
        payload['d']['shard'] = [self.shard_id, self.shard_count]

    state = self._connection
    if state._activity is not None or state._status is not None:
        payload['d']['presence'] = {
            'status': state._status,
            'game': state._activity,
            'since': 0,
            'afk': False
        }

    if state._intents is not None:
        payload['d']['intents'] = state._intents.value

    await self.call_hooks('before_identify', self.shard_id, initial=self._initial_identify)
    await self.send_as_json(payload)
    _log.info('Shard ID %s has sent the IDENTIFY payload.', self.shard_id)
DiscordWebSocket.identify = identify

class bot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=commands.when_mentioned_or("."),
            intents=discord.Intents.all(),
            
            no_category=None
            )
            
        
    async def on_ready(self):
        print(self.user)
        @tasks.loop(seconds=5) #using module tasks
        async def loop_status(): #create func
            #create variable for text to loop it
            status = [
                "who is ass"
            ]
            await self.change_presence(activity=discord.Game(random.choice(status)))
            
        loop_status.start()


    async def setup_hook(self):
        extensions = [
    "cog.commands.General",
    "cog.commands.event",
    "cog.commands.track",
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
    "cog.commands.infodlctrack.21FeatherCup",
    "cog.commands.infodlctrack.22CherryCup",
    "cog.commands.leaderboard"
]
        bot.remove_command("help")
        for extension in extensions:
            await bot.load_extension(extension)
        await bot.tree.sync()
    


bot = bot()
bot.run(secret.discord_token, reconnect=True)