import discord
from discord.ext import commands
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from cog import secret
from discord import app_commands
import random
from cog import config
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


#build class
class leaderboard(commands.Cog):
    def __init__(self,bot:commands.Bot):
        self.bot = bot

#this command show up track leaderboard  
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

#from here all of specific track             
    @commands.hybrid_command(name="show", description="to show overall specific track")
    async def show_track(self,ctx, track):
        valid_tracks = dlc_track.keys()
        
        if track in dlc_track:
                image_url = dlc_track[track]["image_url"]
                if image_url:
                    await ctx.send(image_url)
        if track in valid_tracks:
            data = get_data_for_track(overall_dlc, dlc_track[track]["range"])

            formatted_data = "\n".join([" ".join(row) for row in data])
            formatted_data = formatted_data.replace("[", "").replace("]", "").replace("'", "").replace(",", "")
            await ctx.send(f"\n{formatted_data}")
        else:
            await ctx.send("Invalid track option. Please choose a valid track.")
        
#track variable for worksheet get value
#add anytrack here bro
dlc_track = {
    "bSCS": {
        "range": "Q108:T119",
        "image_url": config.bSCS
    },
    "bTB":{
        "range":"B17:E28",
        "image_url": config.bTB
    },
    "bBL":{
        "range":"G56:J67",
        "image_url": config.BooLake
    }
    

}
#function to get data from variable "normal_track" and return it to parameter
def get_data_for_track(worksheet, range):
    return worksheet.get(range)

async def setup(bot):
    await bot.add_cog(leaderboard(bot))