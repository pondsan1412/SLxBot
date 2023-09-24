import discord
from discord.ext import commands
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from cog import secret
from discord import app_commands
import random

#connect to creds 
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)
sheet = client.open("Silent Lightning's TT Leaderboard")
file_in_sheet_testsheet = sheet.worksheet("Submissions")

#Gspread pages
shroom_150cc = sheet.worksheet("150ccS")
top_ranking = sheet.worksheet("Top Ranking")
overall_s = sheet.worksheet("150ccS")
overall_dlc = sheet.worksheet("150ccDLC")

#random text 
Text_replying = [
    "Finished",
    "Done",
    "your TT has been update!",
    "thanks for submit your TT!!",
    "great job!! your TT is amazing!",
    "All good",
    "Updated!",
    "submit complete",
    "vollständig einreichen",
    "Schön!",
    "fertig!",
    "Danke!"
]
#build class
class admins(commands.Cog):
    def __init__(self,bot:commands.Bot):
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
        app_commands.Choice(name="BIGWILLI",value="BIGWILLI"),
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
        app_commands.Choice(name="Rush",value="Rush"),
        app_commands.Choice(name="Stan",value="Stan"),
        app_commands.Choice(name="Torasshi",value="Torasshi"),
        app_commands.Choice(name="Vonz",value="Vonz"),
        app_commands.Choice(name="Xenoph",value="Xenoph"),
        app_commands.Choice(name="Zquka",value="Zquka"),
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
        await ctx.send(random.choice(Text_replying))
    @commands.hybrid_command(
        name="show",
        help=".",
        description=""
    )
    async def _show(self,ctx:commands.Context):
        show_info = shroom_150cc.get("B4:E15")  
        await ctx.send("https://cdn.discordapp.com/attachments/1154810370884640833/1154810420943655094/MKS.PNG")
        for row in show_info:
            await ctx.send(row)

    @commands.hybrid_command(
        name="topranking",
        help=".",
        description=""
    )
    async def _overall(self,ctx:commands.Context):
        show_topranking = top_ranking.get("G2:J22")
        await ctx.send("https://cdn.discordapp.com/attachments/1066363054473883658/1155036284205674507/New_Project_1.png")
        for row in show_topranking:
            await ctx.send(row)

    @commands.hybrid_command(name="overall_s")
    async def _overall_s(self,ctx:commands.Context):
        show_overall_s = overall_s.get("V4:Y22")
        await ctx.send("https://cdn.discordapp.com/attachments/1155032331619405875/1155032907350552616/S.PNG")
        for row in show_overall_s:
            await ctx.send(row)

    @commands.hybrid_command(name="overall_dlc")
    async def _overall_dlc(self,ctx:commands.Context):
        show_overall_dlc = overall_dlc.get("V4:Y22")
        await ctx.send("https://cdn.discordapp.com/attachments/1155032331619405875/1155032393049194526/DLC.PNG")
        for row in show_overall_dlc:
            await ctx.send(row)
async def setup(bot):
    await bot.add_cog(admins(bot))