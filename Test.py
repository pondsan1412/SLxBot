import gspread
from oauth2client.service_account import ServiceAccountCredentials
import discord
from discord.ext import commands
from cog import secret
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)
sheet = client.open("Silent Lightning TT Leaderboard")
file_in_sheet_testsheet = sheet.worksheet("Submissions")

bot = commands.Bot(command_prefix="?",intents=discord.Intents.all())
@bot.event
async def on_ready():
    print(bot.user)
@bot.command(name="test")
async def test(ctx,a,b,c,d):
    update_row_submit = [a,b,c,d]
    file_in_sheet_testsheet.insert_row(update_row_submit, 1937)
    await ctx.send(update_row_submit)
bot.run(secret.discord_token)