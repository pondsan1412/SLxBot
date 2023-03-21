# Help command that uses discord's embed feature
# Load this file in your cogs

import discord
from discord.ext import commands
from discord.ui import Button
from discord.ui import View
from discord import app_commands
prefix = '.'
bot_title = 'Mario Kart Track List'
bot_description = ''
bottom_info = ''


class Help(commands.Cog):
    """ Help commands """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='help',
                      description='Help command',
                      aliases=['info', 'commands'],
                      case_insensitive=True)
    async def help_command(self, ctx, *commands: str):
        """ Shows this message """
        bot = ctx.bot
        embed = discord.Embed(title=bot_title, description=bot_description)
        
        def generate_usage(command_name):
            """ Generates a string of how to use a command """
            temp = f'{prefix}'
            command = bot.get_command(command_name)
            # Aliases
            if len(command.aliases) == 0:
                temp += f'{command_name}'
            elif len(command.aliases) == 1:
                temp += f'[{command.name}|{command.aliases[0]}]'
            else:
                t = '|'.join(command.aliases)
                temp += f'[{command.name}|{t}]'
            # Parameters
            params = f' '
            for param in command.clean_params:
                params += f'<{command.clean_params[param]}> '
            temp += f'{params}'
            return temp

        def generate_command_list(cog):
            """ Generates the command list with properly spaced help messages """
            # Determine longest word
            max = 0
            for command in bot.get_cog(cog).get_commands():
                if not command.hidden:
                    if len(f'{command}') > max:
                        max = len(f'{command}')
            # Build list
            temp = ""
            for command in bot.get_cog(cog).get_commands():
                if command.hidden:
                    temp += ''
                elif command.help is None:
                    temp += f'{command}\n'
                else:
                    temp += f'{command}'
                    for i in range(0, max - len(f'{command}') + 1):
                        temp += '   '
                    temp += f'{command.help}\n'
            return temp

        # Help by itself just lists our own commands.
        if len(commands) == 0:
            for cog in bot.cogs:
                temp = generate_command_list(cog)
                if temp != "":
                    embed.add_field(name=f'**{cog}**', value=temp, inline=False)
            if bottom_info != "":
                embed.add_field(name="Info", value=bottom_info, inline=False)
        elif len(commands) == 1:
            # Try to see if it is a cog name
            name = commands[0].capitalize()
            command = None

            if name in bot.cogs:
                cog = bot.get_cog(name)
                msg = generate_command_list(name)
                embed.add_field(name=name, value=msg, inline=False)
                msg = f'{cog.description}\n'
                embed.set_footer(text=msg)

            # Must be a command then
            else:
                command = bot.get_command(name)
                if command is not None:
                    help = f''
                    if command.help is not None:
                        help = command.help
                    embed.add_field(name=f'**{command}**',
                                    value=f'{command.description}```{generate_usage(name)}```\n{help}',
                                    inline=False)
                else:
                    msg = ' '.join(commands)
                    embed.add_field(name="Not found", value=f'Command/category `{msg}` not found.')
        else:
            msg = ' '.join(commands)
            embed.add_field(name="Not found", value=f'Command/category `{msg}` not found.')
#button class9o0p-[il.=;'0-p[']\
        button = discord.ui.Button(
            style=discord.ButtonStyle.red,
            label="Contact Developer",
            url="https://c4.wallpaperflare.com/wallpaper/560/855/635/spy-x-family-anya-forger-hd-wallpaper-preview.jpg",
        )
        view = discord.ui.View()
        view.add_item(button)
        await ctx.send(f'{ctx.author.mention}', embed=embed,view=view)
        
        return
# Cog setup
async def setup(bot):
    await bot.add_cog(Help(bot))