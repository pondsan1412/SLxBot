import discord
from discord.ext import commands
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from discord import app_commands
from cog import config

#connect to JSON
scope = [config.feed_t,config.spread_t,config.file_t,config.drive_t]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)
sheet = client.open(config.sheet_name)
file_in_sheet_testsheet = sheet.worksheet(config.sheet_file_Submission)

#Gspread pages
shroom_150cc = sheet.worksheet("150ccS")
top_ranking = sheet.worksheet("Top Ranking")
overall_s = sheet.worksheet("150ccS")
overall_dlc = sheet.worksheet("150ccDLC")



class UpdateTimeTrials(commands.Cog, name='UpdateTT'):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    

#commands
    @commands.has_any_role('TT Updater')
    @commands.hybrid_command(
        name="submit",
        help="Submissions Update",
        description="Time Trial Update",
        aliases=["tt"]
    )
    @app_commands.choices(category=[
        app_commands.Choice(name="S",value="S"),
        app_commands.Choice(name="DLC",value="DLC")])
    @app_commands.choices(player=[
        app_commands.Choice(name="AMDX",value="AMDX"),
        app_commands.Choice(name="Ant",value="Ant"),
        app_commands.Choice(name="Benjames",value="Benjames"),
        app_commands.Choice(name="BIGW",value="BIGW"),
        app_commands.Choice(name="FalseKing",value="FalseKing"),
        app_commands.Choice(name="FreeDobby",value="FreeDobby"),
        app_commands.Choice(name="Holycomb",value="Holycomb"),
        app_commands.Choice(name="JacKo",value="JacKo"),
        app_commands.Choice(name="Kaleb112",value="Kaleb112"),
        app_commands.Choice(name="Leftyginger",value="Leftyginger"),
        app_commands.Choice(name="Ness",value="Ness"),
        app_commands.Choice(name="Ole",value="Ole"),
        app_commands.Choice(name="Paulo22",value="Paulo22"),
        app_commands.Choice(name="Pond",value="Pond"),
        app_commands.Choice(name="Rick",value="Rick"),
        app_commands.Choice(name="Robertala",value="Robertala"),
        app_commands.Choice(name="Rushh",value="Rushh"),
        app_commands.Choice(name="Stan",value="Stan"),
        app_commands.Choice(name="Torasshi",value="Torasshi"),
        app_commands.Choice(name="Vonz",value="Vonz"),
        
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
        file_in_sheet_testsheet.insert_row(update_row_submit, 3)
        await ctx.send(f"submit: `{update_row_submit}`")

    @commands.has_any_role('TT Updater')
    @commands.command(name="remove_tt",description="to remove tt when you failed update")
    async def _remove_tt(self,ctx:discord.Interaction):
        file_in_sheet_testsheet.delete_rows(3)
        await ctx.response.send_message(f"removed")

async def setup(bot):
    await bot.add_cog(
        UpdateTimeTrials(bot)
    )