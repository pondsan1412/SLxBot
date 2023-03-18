# Help command that uses discord's embed feature
# Load this file in your cogs

import discord
from discord.ext import commands
class Help(commands.Cog):
    """ Help commands """
    def __init__(self, bot):
        self.bot = bot
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
                    name="cog_name",
                    value="\n".join(commands_signatures),
                    inline=False,
                )
        embed.set_footer(text="For help, contact developer team")
#this is button class i dont know why it doesn't red instead of grey wtf
        button = discord.ui.Button(
            style=discord.ButtonStyle.green,
            label="Contact Dev",
            url="https://github.com/pondsan1412"
        )
        view = discord.ui.View()
        view.add_item(button)
        await self.get_destination().send(embed=embed,view=view)

# Cog setup
async def setup(bot):
    await bot.add_cog(Help(bot))