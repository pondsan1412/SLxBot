import discord
from discord.ext import commands
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from cog import secret
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)
sheet = client.open("Silent Lightning TT Leaderboard")
file_in_sheet_testsheet = sheet.worksheet("Submissions")

class admins(commands.Cog):
    def __init__(self,bot:commands.Bot):
        self.bot = bot
    @commands.hybrid_command(
        name="ttupdate",
        help="submissions update",
        description="5555555",
        aliases=["tt"]
    )
    @app_commands.choices(category=[app_commands.Choice(name="DLC",value="DLC"),app_commands.Choice(name="S",value="S")])
    @app_commands.choices(player=[
        app_commands.Choice(name="Zquka",value="Zquka"),
        app_commands.Choice(name="FalseKing",value="FalseKing")
    ])
    async def _update_tt(
        self,
        ctx,
        track,
        category,
        player,
        time,
    ):
        
        update_row_submit = [track,category,player,time]
        file_in_sheet_testsheet.insert_row(update_row_submit, 1937)
        await ctx.send("Done!")
        
async def setup(bot):
    await bot.add_cog(admins(bot))