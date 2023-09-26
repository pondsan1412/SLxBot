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
    async def show_track(self,ctx, track:str):
        valid_tracks = dlc_track.keys()
        
        valid2_track = standard_track.keys()
        if track in dlc_track:
                image_url = dlc_track[track]["image_url"]
                if image_url:
                    await ctx.send(image_url)
        else:
            if track in standard_track:
                image_url = standard_track[track]["image_url"]
                if image_url:
                    await ctx.send(image_url)
        
        if track in valid_tracks:
            data = get_data_for_track(overall_dlc, dlc_track[track]["range"])

            formatted_data = "\n".join([" ".join(row) for row in data])
            formatted_data = formatted_data.replace("[", "").replace("]", "").replace("'", "").replace(",", "")
            await ctx.send(f"\n{formatted_data}")
        else:
            if track in valid2_track:
                data2 = get_standard_track(overall_s, standard_track[track]["range"])
                format2 = "\n".join([" ".join(row) for row in data2])
                format2 = format2.replace("[", "").replace("]", "").replace("'", "").replace(",", "")
                await ctx.send(f"\n{format2}")
        
#track variable for worksheet get value
#add anytrack here bro
dlc_track = {
    "bPP":{
        "range":"B4:E15",
        "image_url":""
    },
    "bTC":{
        "range":"G4:J15",
        "image_url":""
    },
    "bCM":{
        "range":"L4:O15",
        "image_url":""
    },
    "bCMa":{
        "range":"Q4:T15",
        "image_url":""
    },
    "bTB":{
        "range":"B17:E28",
        "image_url":""
    },
    "bSR":{
        "range":"G17:J28",
        "image_url":""
    },
    "bSG":{
        
        "range":"L17:O28",
        "image_url":""
    },
    "bNH":{
        "range":"Q17:T28",
        "image_url":""
    },
    "bNYM":{
        "range":"B30:E41",
        "image_url":""
    },
    "bMC3":{
        "range":"G30:J41",
        "image_url":""
    },
    "bKD":{
        "range":"L30:J41",
        "image_url":""
    },
    "bWP":{
        "range":"Q30:T41",
        "image_url":""
    },
    "bSS":{
        "range":"B43:E54",
        "image_url":""
    },
    "bSN":{
        "range":"G43:J54",
        "image_url":""
    },
    "bMG":{
        "range":"L43:O54",
        "image_url":""
    },
    "bSHS":{
        "range":"Q43:O54",
        "image_url":""
    },
    "bLL":{
        "range":"B56:E67",
        "image_url":""
    },
    "bBL":{
        "range":"G56:J67",
        "image_url":""
    },
    "bRRM":{
        "range":"L56:O67",
        "image_url":""
    },
    "bMT":{
        "range":"Q56:T67",
        "image_url":""
    },
    "bBB":{
        "range":"B69:E80",
        "image_url":""
    },
    "bPG":{
        "range":"G69:J80",
        "image_url":""
    },
    "bMM":{
        "range":"L69:J80",
        "image_url":""
    },
    "bRR7":{
        "range":"Q69:T80",
        "image_url":""
    },
    "bAD":{
        "range":"B82:E93",
        "image_url":""
    },
    "bRP":{
        "range":"G82:J93",
        "image_url":""
    },
    "bDKS":{
        "range":"L82:O93",
        "image_url":""
    },
    "bYI":{
        "range":"Q82:T93",
        "image_url":""
    },
    "bBR":{
        "range":"B95:E106",
        "image_url":""
    },
    "bMC":{
        "range":"G95:J106",
        "image_url":""
    },
    "bWS":{
        "range":"L95:O106",
        "image_url":""
    },
    "bSSy":{
        "range":"Q95:T106",
        "image_url":""
    },
    "bAtD":{
        "range":"B108:E119",
        "image_url":""
    },
    "bDC":{
        "range":"G108:J119",
        "image_url":""
    },
    "bMH":{
        "range":"L108:O119",
        "image_url":""
    },
    "bSCS":{
        "range":"Q108:T119",
        "image_url":""
    },
    "bLAL":{
        "range":"B121:E132",
        "image_url":""
    },
    "bSW":{
        "range":"G121:J132",
        "image_url":""
    },
    "bKC":{
        "range":"L121:O132",
        "image_url":""
    },
    "bVV":{
        "range":"Q121:T132",
        "image_url":""
    },
    
}
    
    

standard_track = {
    "MKS":{
        "range":"B4:E15",
        "image_url":config.t_MKS
    },
    "WP":{
        "range":"G6:J15",
        "image_url":config.t_WP
    },
    "SSC":{
        "range":"L6:O15",
        "image_url":config.t_SSC
    },
    "TR":{
        "range":"Q4:T15",
        "image_url":config.t_TR 
    },
    "MC":{
        "range":"B17:E28",
        "image_url":config.t_MC 
    },
    "TH":{
        "range":"G17:J28",
        "image_url":config.t_TH 
    },
    "TM":{
        "range":"L17:O28",
        "image_url":config.t_TM 
    },
    "SGF":{
        "range":"Q17:T28",
        "image_url":config.t_SGF 
    },
    "SA":{
        "range":"B30:E41",
        "image_url":config.t_SA 
    },
    "DS":{
        "range":"G30:J41",
        "image_url":config.t_DS 
    },
    "Ed":{
        "range":"L30:O41",
        "image_url":config.t_Ed 
    },
    "MW":{
        "range":"Q30:T41",
        "image_url":config.t_MW
    },
    
    "BDD":{
        "range":"G43:J54",
        "image_url":config.t_BDD 
    },
    "BC":{
        "range":"L43:O54",
        "image_url":config.t_BC 
    },
    "RR":{
        "range":"Q43:T54",
        "image_url":config.t_RR 
    },
    "rMMM":{
        "range":"B56:E67",
        "image_url":"_____________"
    },
    "rMC":{
        "range":"G56:J67",
        "image_url":"_____________"
    },
    "rCCB":{
        "range":"L56:J67",
       "image_url":"_____________"
    },
    "rTT":{
        "range":"Q56:T67",
        "image_url":"_____________"
    },
    "rDDD":{
        "range":"B69:E80",
       "image_url":"."
    },
    "rDP3":{
        "range":"G69:J80",
        "image_url":"_____________"
    },
    "rRRy":{
        "range":"L69:O80",
        "image_url":"_____________"
    },
    "rDKJ":{
        "range":"Q69:T80",
        "image_url":"_____________"
    },
    "rWS":{
        "range":"B82:E93",
        "image_url":"_____________"
    },
    "rSL":{
        "range":"G82:J93",
        "image_url":"_____________"
    },
    "rMP":{
        "range":"L82:O93",
        "image_url":"_____________"
    },
    "rYV":{
        "range":"Q82:T93",
        "image_url":"_____________"
    },
    "rTTC":{
        "range":"B95:E106",
        "image_url":"_____________"
    },
    "rPPS":{
        "range":"G95:J106",
        "image_url":"_____________"
    },
    "rGV":{
        "range":"L95:O106",
         "image_url":"_____________"

    },
    "rRRd":{
        "range":"Q95:T106",
        "image_url":"_____________"
    },
    "dYC":{
        "range":"B108:E119",
        "image_url":"_____________"
    },
    "dEA":{
        "range":"G108:J119",
        "image_url":"_____________"
    },
    "dDD":{
        "range":"L108:O119",
        "image_url":"_____________"
    },
    "dMC":{
        "range":"Q108:T119",
        "image_url":"_____________"
    },
    "dWGM":{
        "range":"B121:E132",
        "image_url":"_____________"
    },
    "dRR":{
        "range":"G121:J132",
        "image_url":"_____________"
    },
    "dIIO":{
        "range":"L121:O132",
        "image_url":"_____________"
    },
    "dHC":{
        "range":"Q121:T132",
        "image_url":"_____________"
    },
    "dBP":{
        "range":"B134:E145",
        "image_url":"_____________"
    },
    "dCL":{
        "range":"G134:J145",
        "image_url":"_____________"
    },
    "dWW":{
        "range":"L134:O145",
        "image_url":"_____________"
    },
    "dAC":{
        "range":"Q134:T145",
        "image_url":"_____________"
    },
    "dNBC":{
        "range":"B147:E158",
        "image_url":"_____________"
    },
    "dRiR":{
        "range":"G147:J158",
        "image_url":"_____________"
    },
    "dSBS":{
        "range":"L147:O158",
        "image_url":"_____________"
    },
    "dBB":{
        "range":"Q147:T158",
         "image_url":"_____________"
    },
    "CC":{
        "range":"B43:E54",
        "image_url":config.t_CC 
    },
}
#function to get data from variable "normal_track" and return it to parameter
def get_data_for_track(worksheet, range):
    return worksheet.get(range)
def get_standard_track(worksheet, range):
    return worksheet.get(range)
async def setup(bot):
    await bot.add_cog(leaderboard(bot))