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
    @commands.has_any_role('TT Updater')
    @commands.hybrid_command(
        name="submit",
        help="Time Trial",
        description="Time Trial Update",
        aliases=["tt"]
    )
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