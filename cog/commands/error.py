import discord
from discord.ext import commands
from cog.commands.General import General

class error(commands.Cog):
    def __init__(self,bot:commands.Context):
        self.bot = bot
    @commands.Cog.listener()
    async def on_command_error(
        self,
        ctx,
        error
    ):
        if isinstance(
            error,
            commands.MissingAnyRole
        ):
            await ctx.send("Access Denied! You does not have a [dev] role!")
        else:
            pass
        if isinstance(
            error,
            AttributeError
        ):
            await ctx.send(error,AttributeError)
    
async def setup(bot):
    await bot.add_cog(error(bot))