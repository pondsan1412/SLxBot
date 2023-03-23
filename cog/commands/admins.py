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
    async def _update_tt(
        self,
        ctx:commands.Context,
        Track:str,
        Category:str,
        Player:str,
        Time:str,
    ):
        update_row_submit = [Track,Category,Player,Time]
        file_in_sheet_testsheet.insert_row(update_row_submit, 1937)
        await ctx.send("done!")
        
async def setup(bot):
    await bot.add_cog(admins(bot))