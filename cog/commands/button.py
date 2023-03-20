import discord
from discord.ui import Button, View
from discord.ext import commands
import flag
import os
class Buttons(discord.ui.View):
    def __init__(self, ctx):
        super().__init__(timeout=None)
        self.ctx = ctx
    @discord.ui.button(
        emoji="🇩🇪",
        style=discord.ButtonStyle.blurple
    )
    async def red_button(
        self,
        interaction:discord.Interaction,
        button:discord.ui.Button
    ):
        
        await interaction.response.edit_message(
            content=f"{translated_text.text}"
        )

    @discord.ui.button(
        label="Remove buttons",
        style=discord.ButtonStyle.red
    )
    async def _blue(
        self,
        interaction:discord.Interaction,
        button:discord.ui.Button
    ):
        self.clear_items()
        await interaction.response.edit_message(
            view=self
        )
    async def on_timeout(self):
        await self.message.edit(view=None)