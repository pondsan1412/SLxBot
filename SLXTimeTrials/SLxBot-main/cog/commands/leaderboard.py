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

#from here all of specific track             
    @commands.hybrid_command(name="show", description="to show overall and specific track")
    async def show_track(self,ctx, track:str):
        valid_tracks = dlc_track.keys()
        valid2_track = standard_track.keys()
        overall_s_track = top_s.keys()
        overall_dlc_track = top_dlc.keys()
        valid_top = top_all.keys()
        embed = discord.Embed(
        title=f"{track}",
        color=discord.Color.blue()
    )
        if track in top_s:
            image_url = top_s[track]["image_url"]
            if image_url:
                await ctx.send(image_url)
        else:
            if track in top_dlc:
                image_url = top_dlc[track]["image_url"]
                if image_url:
                    await ctx.send(image_url)

        if track in dlc_track:
                image_url = dlc_track[track]["image_url"]
                if image_url:
                    await ctx.send(image_url)
        else:
            if track in standard_track:
                image_url = standard_track[track]["image_url"]
                if image_url:
                    await ctx.send(image_url)
        if track in top_all:
            image_url = top_all[track]["image_url"]
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

        if track in overall_s_track:
            data3 = get_data_for_track(overall_s, top_s[track]["range"])

            format3 = "\n".join([" ".join(row) for row in data3])
            format3 = format3.replace("[", "").replace("]", "").replace("'", "").replace(",", "")
            await ctx.send(f"\n{format3}")
        else:
            if track in overall_dlc_track :
                data4 = get_standard_track(overall_dlc, top_dlc[track]["range"])
                format4 = "\n".join([" ".join(row) for row in data4])
                format4 = format4.replace("[", "").replace("]", "").replace("'", "").replace(",", "")
                await ctx.send(f"\n{format4}")
        if track in valid_top:
            data5 = get_standard_track(top_ranking, top_all[track]["range"])
            format5 = "\n".join([" ".join(row) for row in data5])
            format5.replace("[", "").replace("]", "").replace("'", "").replace(",", "")
            await ctx.send(f"\n{format5}")

#overall
top_all ={
    "top_all":{
        "range":"G2:J22",
        "image_url":"https://cdn.discordapp.com/attachments/1066363054473883658/1155036284205674507/New_Project_1.png?ex=65147c1d&is=65132a9d&hm=9b4aeba7711ff3f836d0286c5266b62933f6f3841c2087ca51a9df7f715f8103&"
    },
}
top_s  = {
    "top_s":{
        "range":"V4:Y22",
        "image_url":"https://media.discordapp.net/attachments/1156152527193133079/1156152806986752031/S.png?ex=6513eeb5&is=65129d35&hm=eeddfdf42a93d048b4449b8e5aa7c4802d2efe6ddd6005964537fc37f20190d0&="
    },
}     
top_dlc = {"top_dlc":{"range":"V4:Y22","image_url":"https://cdn.discordapp.com/attachments/1156152527193133079/1156287206747549806/DLC.png?ex=65146be0&is=65131a60&hm=74093c16774afa1996fc4638c0d88455972435814009bf4f5f3bdf9d1f5a00b6&"}}  
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
        "image_url":config.rMMM
    },
    "rMC":{
        "range":"G56:J67",
        "image_url":config.rMC
    },
    "rCCB":{
        "range":"L56:J67",
       "image_url":config.rCCB
    },
    "rTT":{
        "range":"Q56:T67",
        "image_url":config.rTT
    },
    "rDDD":{
        "range":"B69:E80",
       "image_url":config.rDDD
    },
    "rDP3":{
        "range":"G69:J80",
        "image_url":config.rDP3
    },
    "rRRy":{
        "range":"L69:O80",
        "image_url":config.rRRy
    },
    "rDKJ":{
        "range":"Q69:T80",
        "image_url":config.rDKJ
    },
    "rWS":{
        "range":"B82:E93",
        "image_url":config.rWS
    },
    "rSL":{
        "range":"G82:J93",
        "image_url":config.rSL
    },
    "rMP":{
        "range":"L82:O93",
        "image_url":config.rMP
    },
    "rYV":{
        "range":"Q82:T93",
        "image_url":config.rYV
    },
    "rTTC":{
        "range":"B95:E106",
        "image_url":config.rTTC
    },
    "rPPS":{
        "range":"G95:J106",
        "image_url":config.rPPS
    },
    "rGV":{
        "range":"L95:O106",
         "image_url":config.rGV

    },
    "rRRd":{
        "range":"Q95:T106",
        "image_url":config.rRRd
    },
    "dYC":{
        "range":"B108:E119",
        "image_url":config.t_dYC
    },
    "dEA":{
        "range":"G108:J119",
        "image_url":config.t_dEA
    },
    "dDD":{
        "range":"L108:O119",
        "image_url":config.t_dDD
    },
    "dMC":{
        "range":"Q108:T119",
        "image_url":config.t_dMC
    },
    "dWGM":{
        "range":"B121:E132",
        "image_url":config.dWGM
    },
    "dRR":{
        "range":"G121:J132",
        "image_url":config.dRR
    },
    "dIIO":{
        "range":"L121:O132",
        "image_url":config.dIIo
    },
    "dHC":{
        "range":"Q121:T132",
        "image_url":config.dHC
    },
    "dBP":{
        "range":"B134:E145",
        "image_url":config.dBP
    },
    "dCL":{
        "range":"G134:J145",
        "image_url":config.dCL
    },
    "dWW":{
        "range":"L134:O145",
        "image_url":config.dWW
    },
    "dAC":{
        "range":"Q134:T145",
        "image_url":config.dAC
    },
    "dNBC":{
        "range":"B147:E158",
        "image_url":config.dNBC
    },
    "dRiR":{
        "range":"G147:J158",
        "image_url":config.dRiR
    },
    "dSBS":{
        "range":"L147:O158",
        "image_url":config.dSBS
    },
    "dBB":{
        "range":"Q147:T158",
         "image_url":config.dBB
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