import discord
from discord.ext import commands
from cog import config
from cog.button import *
class Select(discord.ui.Select):
    def __init__(self):
        options=[
            discord.SelectOption(
            label="General Command List",
            emoji=config.Fire,
            description="Show all commands"
            ),
            discord.SelectOption(
            label="Mushroom Cup",
            emoji=config.MushroomCup,
            description="Mushroom Cup Track List"
            ),
            discord.SelectOption(
            label="Flower Cup",
            emoji=config.FlowerCup,
            description="Flower Cup Track List"
            ),
            discord.SelectOption(
            label="Star Cup",
            emoji=config.StarCup,
            description="Star Cup Track List"
            ),
            discord.SelectOption(
            label="Special Cup",
            emoji=config.SpecialCup,
            description="Special Cup Track List"
            ),
            discord.SelectOption(
            label="Egg Cup",
            emoji=config.EggCup,
            description="Egg Cup Track List"
            ),
            discord.SelectOption(
            label="Crossing Cup",
            emoji=config.CrossingCup,
            description="Crossing Cup Track List"
            ),
            discord.SelectOption(
            label="Shell Cup",
            emoji=config.ShellCup,
            description="Shell Cup Track List"
            ),
            discord.SelectOption(
            label="Banana Cup",
            emoji=config.BananaCup,
            description="Banana Cup Track List"
            ),
            discord.SelectOption(
            label="Leaf Cup",
            emoji=config.LeafCup,
            description="Leaf Cup Track List"
            ),
            discord.SelectOption(
            label="Lightning Cup",
            emoji=config.LightningCup,
            description="Lightning Cup Track List"
            ),
            discord.SelectOption(
            label="Triforce Cup",
            emoji=config.TriforceCup,
            description="Triforce Cup Track List"
            ),
            discord.SelectOption(
            label="Bell Cup",
            emoji=config.BellCup,
            description="Bell Cup Track List"
            ),
            discord.SelectOption(
            label="Golden Dash Cup",
            emoji=config.GoldenDashCup,
            description="Golden Dash Cup Track List"
            ),
            discord.SelectOption(
            label="Lucky Cat Cup",
            emoji=config.LuckyCatCup,
            description="Lucky Cat Cup Track List"
            ),
            discord.SelectOption(
            label="Turnip Cup",
            emoji=config.TurnipCup,
            description="Turnip Cup Track List"
            ),
            discord.SelectOption(
            label="Propeller Cup",
            emoji=config.PropellerCup,
            description="Propeller Cup Track List"
            ),
            discord.SelectOption(
            label="Rock Cup",
            emoji=config.RockCup,
            description="Rock Cup Track List"
            ),
            discord.SelectOption(
            label="Moon Cup",
            emoji=config.MoonCup,
            description="Moon Cup Track List"
            ),
            discord.SelectOption(
            label="Fruit Cup",
            emoji=config.FruitCup,
            description="Fruit Cup Track List"
            ),
            discord.SelectOption(
            label="Boomerang Cup",
            emoji=config.BoomerangCup,
            description="Boomerang Cup Track List"
            ),
            discord.SelectOption(
            label="Developer Team",
            emoji=config.Lucky,
            description=""
            ),
        ]
        super().__init__(
            placeholder=f"🤏Select some option(s)",
            max_values=1,
            min_values=1,
            options=options
        )
    async def callback(self, int:discord.Interaction):
        if self.values[0] == "General Command List":
            await int.response.edit_message(embed=config.embedGeneral1)
        elif self.values[0] == "Mushroom Cup":
            await int.response.edit_message(embed=config.embedMushroomcup)
        elif self.values[0] == "Flower Cup":
            await int.response.edit_message(embed=config.embedFlowercup)
        elif self.values[0] == "Star Cup":
            await int.response.edit_message(embed=config.embedStarcup)
        elif self.values[0] == "Special Cup":
            await int.response.edit_message(embed=config.embedSpecialcup)
        elif self.values[0] == "Egg Cup":
            await int.response.edit_message(embed=config.embedEggcup)
        elif self.values[0] == "Crossing Cup":
            await int.response.edit_message(embed=config.embedCrossingcup)
        elif self.values[0] == "Shell Cup":
            await int.response.edit_message(embed=config.embedShellcup)
        elif self.values[0] == "Banana Cup":
            await int.response.edit_message(embed=config.embedBananacup)
        elif self.values[0] == "Leaf Cup":
            await int.response.edit_message(embed=config.embedLeafcup)
        elif self.values[0] == "Lightning Cup":
            await int.response.edit_message(embed=config.embedLightningcup)
        elif self.values[0] == "Triforce Cup":
            await int.response.edit_message(embed=config.embedTriforcecup)
        elif self.values[0] == "Bell Cup":
            await int.response.edit_message(embed=config.embedBellcup)
        elif self.values[0] == "Golden Dash Cup":
            await int.response.edit_message(embed=config.embedGoldenDashcup)
        elif self.values[0] == "Lucky Cat Cup":
            await int.response.edit_message(embed=config.embedLuckyCatcup)
        elif self.values[0] == "Turnip Cup":
            await int.response.edit_message(embed=config.embedTurnipcup)
        elif self.values[0] == "Propeller Cup":
            await int.response.edit_message(embed=config.embedPropellercup)
        elif self.values[0] == "Rock Cup":
            await int.response.edit_message(embed=config.embedRockcup)
        elif self.values[0] == "Moon Cup":
            await int.response.edit_message(embed=config.embedMooncup)
        elif self.values[0] == "Fruit Cup":
            await int.response.edit_message(embed=config.embedFruitcup)
        elif self.values[0] == "Boomerang Cup":
            await int.response.edit_message(embed=config.embedBoomerangcup)
        elif self.values[0] == "Developer Team":
            await int.response.edit_message(embed=config.embedDevsTeam)            


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