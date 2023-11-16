import discord
from discord.ext import commands

class ErrorHandler(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send(error)
            return  # ไม่ต้องแสดง error หาก command ไม่ถูกพบ

        # ปรับแต่งได้ตามความต้องการ
        error_embed = discord.Embed(
            title="Error",
            description=f"An error occurred: {error}",
            color=discord.Color.red()
        )
        await ctx.send(embed=error_embed)
    @commands.Cog.listener()
    async def on_message_error(self, message, error):
        # ปรับแต่งได้ตามความต้องการ
        error_embed = discord.Embed(
            title="Error",
            description=f"An error occurred in on_message: {error}",
            color=discord.Color.red()
        )
        await message.channel.send(embed=error_embed)
async def setup(bot):
    await bot.add_cog(
        ErrorHandler(bot)
    )
