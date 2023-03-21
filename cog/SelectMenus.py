import discord
from discord.ext import commands
from cog import config

class Select(discord.ui.Select):
    def __init__(self):
        options=[
            discord.SelectOption(
            label="Zquka is programmer",
            emoji=config.Working,
            description="nothing special this is Select Menus"
            ),
            discord.SelectOption(
            label="Pond is developer",
            emoji=config.Fire,
            description="Option 2 "
            ),
        ]
        super().__init__(
            placeholder=f"🤏Select some option",
            max_values=1,
            min_values=1,
            options=options
        )
class SelectView(discord.ui.View):
    def __init__(
            self,
            *, 
            timeout = 100
    ):
        super().__init__(timeout=timeout)
        self.add_item(Select())

async def setup(bot):
    await bot.add_cog(Select(bot))