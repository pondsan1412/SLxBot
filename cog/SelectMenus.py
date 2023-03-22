import discord
from discord.ext import commands
from cog import config

class Select(discord.ui.Select):
    def __init__(self):
        options=[
            discord.SelectOption(
            label="Mushroom Cup Commands",
            emoji=config.MushroomCup,
            description="Mushroom Cup Track List"
            ),
            discord.SelectOption(
            label="Flower Cup Commands",
            emoji=config.FlowerCup,
            description="Flower Cup Track List"
            ),
            discord.SelectOption(
            label="Star Cup Commands",
            emoji=config.StarCup,
            description="Star Cup Track List"
            ),
            discord.SelectOption(
            label="Special Cup Commands",
            emoji=config.SpecialCup,
            description="Special Cup Track List"
            ),
            discord.SelectOption(
            label="Egg Cup Commands",
            emoji=config.EggCup,
            description="Egg Cup Track List"
            ),
            discord.SelectOption(
            label="Crossing Cup Commands",
            emoji=config.CrossingCup,
            description="Crossing Cup Track List"
            ),
            discord.SelectOption(
            label="Shell Cup Commands",
            emoji=config.ShellCup,
            description="Shell Cup Track List"
            ),
            discord.SelectOption(
            label="Banana Cup Commands",
            emoji=config.BananaCup,
            description="Banana Cup Track List"
            ),
            discord.SelectOption(
            label="Leaf Cup Commands",
            emoji=config.LeafCup,
            description="Leaf Cup Track List"
            ),
            discord.SelectOption(
            label="Lightning Cup Commands",
            emoji=config.LightningCup,
            description="Lightning Cup Track List"
            ),
            discord.SelectOption(
            label="Triforce Cup Commands",
            emoji=config.TriforceCup,
            description="Triforce Cup Track List"
            ),
            discord.SelectOption(
            label="Bell Cup Commands",
            emoji=config.BellCup,
            description="Bell Cup Track List"
            ),
            discord.SelectOption(
            label="Golden Dash Cup Commands",
            emoji=config.GoldenDashCup,
            description="Golden Dash Cup Track List"
            ),
            discord.SelectOption(
            label="Lucky Cat Cup Commands",
            emoji=config.LuckyCatCup,
            description="Lucky Cat Cup Track List"
            ),
            discord.SelectOption(
            label="Turnip Cup Commands",
            emoji=config.TurnipCup,
            description="Turnip Cup Track List"
            ),
            discord.SelectOption(
            label="Propeller Cup Commands",
            emoji=config.PropellerCup,
            description="Propeller Cup Track List"
            ),
            discord.SelectOption(
            label="Rock Cup Commands",
            emoji=config.RockCup,
            description="Rock Cup Track List"
            ),
            discord.SelectOption(
            label="Moon Cup Commands",
            emoji=config.MoonCup,
            description="Moon Cup Track List"
            ),
            discord.SelectOption(
            label="Fruit Cup Commands",
            emoji=config.FruitCup,
            description="Fruit Cup Track List"
            ),
            discord.SelectOption(
            label="Boomerang Cup Commands",
            emoji=config.BoomerangCup,
            description="Boomerang Cup Track List"
            ),
        ]
        super().__init__(
            placeholder=f"🤏Select some option",
            max_values=1,
            min_values=1,
            options=options
        )
    async def callback(self, int:discord.Interaction):
        if self.values[0] == "Mushroom Cup Commands":
            await int.response.edit_message(embed=config.embedMushroomcup)
        elif self.values[0] == "Flower Cup Commands":
            await int.response.edit_message(embed=config.embedFlowercup)
        elif self.values[0] == "Star Cup Commands":
            await int.response.edit_message(embed=config.embedStarcup)
        elif self.values[0] == "Special Cup Commands":
            await int.response.edit_message(embed=config.embedSpecialcup)
        elif self.values[0] == "Egg Cup Commands":
            await int.response.edit_message(embed=config.embedEggcup)
        elif self.values[0] == "Crossing Cup Commands":
            await int.response.edit_message(embed=config.embedCrossingcup)
        elif self.values[0] == "Shell Cup Commands":
            await int.response.edit_message(embed=config.embedShellcup)
        elif self.values[0] == "Banana Cup Commands":
            await int.response.edit_message(embed=config.embedBananacup)
        elif self.values[0] == "Leaf Cup Commands":
            await int.response.edit_message(embed=config.embedLeafcup)
        elif self.values[0] == "Lightning Cup Commands":
            await int.response.edit_message(embed=config.embedLightningcup)
        elif self.values[0] == "Triforce Cup Commands":
            await int.response.edit_message(embed=config.embedTriforcecup)
        elif self.values[0] == "Bell Cup Commands":
            await int.response.edit_message(embed=config.embedBellcup)
        elif self.values[0] == "Golden Dash Cup Commands":
            await int.response.edit_message(embed=config.embedGoldenDashcup)
        elif self.values[0] == "Lucky Cat Cup Commands":
            await int.response.edit_message(embed=config.embedLuckyCatcup)
        elif self.values[0] == "Turnip Cup Commands":
            await int.response.edit_message(embed=config.embedTurnipcup)
        elif self.values[0] == "Propeller Cup Commands":
            await int.response.edit_message(embed=config.embedPropellercup)
        elif self.values[0] == "Rock Cup Commands":
            await int.response.edit_message(embed=config.embedRockcup)
        elif self.values[0] == "Moon Cup Commands":
            await int.response.edit_message(embed=config.embedMooncup)
        elif self.values[0] == "Fruit Cup Commands":
            await int.response.edit_message(embed=config.embedFruitcup)
        elif self.values[0] == "Boomerang Cup Commands":
            await int.response.edit_message(embed=config.embedBoomerangcup)


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