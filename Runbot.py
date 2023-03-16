import discord
from discord.ext import commands
import os
from cog import config
from cog import TracksList
from cog import secret
class bot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=commands.when_mentioned_or("."),
            intents=discord.Intents.all(),
            help_command= CustomHelpCommand(
            no_category = "other commands"
            )
        )
    async def on_ready(self):
        print(self.user)
        ch_ready = int(secret.ch_onready)
        print(ch_ready)
        bot = self.get_channel(ch_ready)
        await bot.send("I'm ready sir")
    async def setup_hook(self):
        await bot.load_extension("cog.TracksList")
        await bot.tree.sync()
class CustomHelpCommand(commands.DefaultHelpCommand):
    async def send_bot_help(self, mapping):
        embed = discord.Embed(
            title="Help",
            description="List of available commands:"
        )
        for cog, commands in mapping.items():
            if cog is None:
                continue
            commands_signatures = []
            for command in commands:
                commands_signatures.append(
                    f"{command.name}:{command.help}"
                )
            if commands_signatures:
                cog_name = getattr(cog, "qualified_name","Other")
                embed.add_field(
                    name="Tracks List ",
                    value="\n".join(commands_signatures),
                    inline=False,
                )
        embed.set_footer(text="Page 1/2 | Developer team")
        button = discord.ui.Button(
            style=discord.ButtonStyle.green,
            label="Next Page",
            custom_id="help_next_page",
        )
        view = discord.ui.View()
        view.add_item(button)
        await self.get_destination().send(embed=embed,view=view)

    async def send_help_page(self, interaction:discord.Interaction, page_number):
        if page_number == 1:
            await self.send_bot_help(self.context.bot.cogs)
        elif page_number == 2:
           embed = discord.Embed(title="555")
           await interaction.response.send_message(embed=embed)

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if interaction.custom_id == "help_next_page":
            await interaction.response.defer()
            await self.send_help_page(2)
            return True
        return False
    

bot = bot()
bot.run(secret.discord_token, reconnect=True)