#team SLx  Timetrials Leaderboard in mario kart games
import discord
from discord.ext import commands
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from discord import Embed

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
player_tab = sheet.worksheet("Players")
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
    "Paris Promenade":{
        "range":"B4:E15",
        "image_url":""
    },
    "Toad Circuit":{
        "range":"G4:J15",
        "image_url":""
    },
    "Choco Mountain":{
        "range":"L4:O15",
        "image_url":""
    },
    "Coconut Mall":{
        "range":"Q4:T15",
        "image_url":""
    },
    "Tokyo Blur":{
        "range":"B17:E28",
        "image_url":""
    },
    "Shroom Ridge":{
        "range":"G17:J28",
        "image_url":""
    },
    "Sky Garden":{
        
        "range":"L17:O28",
        "image_url":""
    },
    "Ninja Hideaway":{
        "range":"Q17:T28",
        "image_url":""
    },
    "New York Minute":{
        "range":"B30:E41",
        "image_url":""
    },
    "Mario Circuit 3":{
        "range":"G30:J41",
        "image_url":""
    },
    "Kalimari Desert":{
        "range":"L30:J41",
        "image_url":""
    },
    "Waluigi Pinball":{
        "range":"Q30:T41",
        "image_url":""
    },
    "Sydney Sprint":{
        "range":"B43:E54",
        "image_url":""
    },
    "Snow Land":{
        "range":"G43:J54",
        "image_url":""
    },
    "Mushroom Gorge":{
        "range":"L43:O54",
        "image_url":""
    },
    "Sky-High Sundae":{
        "range":"Q43:T54",
        "image_url":""
    },
    "London Loop":{
        "range":"B56:E67",
        "image_url":""
    },
    "Boo Lake":{
        "range":"G56:J67",
        "image_url":""
    },
    "Rock Rock Mountain":{
        "range":"L56:O67",
        "image_url":""
    },
    "Maple Treeway":{
        "range":"Q56:T67",
        "image_url":""
    },
    "Berlin Byways":{
        "range":"B69:E80",
        "image_url":""
    },
    "Peach Gardens":{
        "range":"G69:J80",
        "image_url":""
    },
    "Merry Mountain":{
        "range":"L69:O80",
        "image_url":""
    },
    "3DS Rainbow Road":{
        "range":"Q69:T80",
        "image_url":""
    },
    "Amsterdam Drift":{
        "range":"B82:E93",
        "image_url":""
    },
    "Riverside Park":{
        "range":"G82:J93",
        "image_url":""
    },
    "DK Summit":{
        "range":"L82:O93",
        "image_url":""
    },
    "Yoshi\'s Island":{
        "range":"Q82:T93",
        "image_url":""
    },
    "Bangkok Rush":{
        "range":"B95:E106",
        "image_url":""
    },
    "Mario Circuit":{
        "range":"G95:J106",
        "image_url":""
    },
    "Waluigi Stadium":{
        "range":"L95:O106",
        "image_url":""
    },
    "Singapore Speedway":{
        "range":"Q95:T106",
        "image_url":""
    },
    "Athens Dash":{
        "range":"B108:E119",
        "image_url":""
    },
    "Daisy Cruiser":{
        "range":"G108:J119",
        "image_url":""
    },
    "Moonview Highway":{
        "range":"L108:O119",
        "image_url":""
    },
    "Squeaky Clean Sprint":{
        "range":"Q108:T119",
        "image_url":""
    },
    "Los Angeles Laps":{
        "range":"B121:E132",
        "image_url":""
    },
    "Sunset Wilds":{
        "range":"G121:J132",
        "image_url":""
    },
    "Koopa Cape":{
        "range":"L121:O132",
        "image_url":""
    },
    "Vancouver Velocity":{
        "range":"Q121:T132",
        "image_url":""
    },
    
}
    
    

standard_track = {
    "Mario Kart Stadium":{
        "range":"B4:E15",
        "image_url":config.t_MKS
    },
    "Water Park":{
        "range":"G6:J15",
        "image_url":config.t_WP
    },
    "Sweet Sweet Canyon":{
        "range":"L6:O15",
        "image_url":config.t_SSC
    },
    "Thwomp Ruins":{
        "range":"Q4:T15",
        "image_url":config.t_TR 
    },
    "Mario Circuit":{
        "range":"B17:E28",
        "image_url":config.t_MC 
    },
    "Toad Harbor":{
        "range":"G17:J28",
        "image_url":config.t_TH 
    },
    "Twisted Mansion":{
        "range":"L17:O28",
        "image_url":config.t_TM 
    },
    "Shy Guy Falls":{
        "range":"Q17:T28",
        "image_url":config.t_SGF 
    },
    "Sunshine Airport":{
        "range":"B30:E41",
        "image_url":config.t_SA 
    },
    "Dolphin Shoals":{
        "range":"G30:J41",
        "image_url":config.t_DS 
    },
    "Electrodrome":{
        "range":"L30:O41",
        "image_url":config.t_Ed 
    },
    "Mount Wario":{
        "range":"Q30:T41",
        "image_url":config.t_MW
    },
    
    "Bone-Dry Dunes":{
        "range":"G43:J54",
        "image_url":config.t_BDD 
    },
    "Bowser's Castle":{
        "range":"L43:O54",
        "image_url":config.t_BC 
    },
    "Rainbow Road":{
        "range":"Q43:T54",
        "image_url":config.t_RR 
    },
    "Moo Moo Meadows":{
        "range":"B56:E67",
        "image_url":config.rMMM
    },
    "Mario Circuit":{
        "range":"G56:J67",
        "image_url":config.rMC
    },
    "Cheep Cheep Beach":{
        "range":"L56:J67",
       "image_url":config.rCCB
    },
    "Toad's Turnpike":{
        "range":"Q56:T67",
        "image_url":config.rTT
    },
    "Dry Dry Desert":{
        "range":"B69:E80",
       "image_url":config.rDDD
    },
    "Donut Plains 3":{
        "range":"G69:J80",
        "image_url":config.rDP3
    },
    "Royal Raceway":{
        "range":"L69:O80",
        "image_url":config.rRRy
    },
    "DK Jungle":{
        "range":"Q69:T80",
        "image_url":config.rDKJ
    },
    "Wario Stadium":{
        "range":"B82:E93",
        "image_url":config.rWS
    },
    "Sherbet Land":{
        "range":"G82:J93",
        "image_url":config.rSL
    },
    "Music Park":{
        "range":"L82:O93",
        "image_url":config.rMP
    },
    "Yoshi Valley":{
        "range":"Q82:T93",
        "image_url":config.rYV
    },
    "Tick-Tock Clock":{
        "range":"B95:E106",
        "image_url":config.rTTC
    },
    "Piranha Planet Slide":{
        "range":"G95:J106",
        "image_url":config.rPPS
    },
    "Grumble Volcano":{
        "range":"L95:O106",
         "image_url":config.rGV

    },
    "Rainbow Road":{
        "range":"Q95:T106",
        "image_url":config.rRRd
    },
    "Yoshi Circuit":{
        "range":"B108:E119",
        "image_url":config.t_dYC
    },
    "Excitebike Arena":{
        "range":"G108:J119",
        "image_url":config.t_dEA
    },
    "Dragon Driftway":{
        "range":"L108:O119",
        "image_url":config.t_dDD
    },
    "Mute City":{
        "range":"Q108:T119",
        "image_url":config.t_dMC
    },
    "Wario's Gold Mine":{
        "range":"B121:E132",
        "image_url":config.dWGM
    },
    "SNES Rainbow Road":{
        "range":"G121:J132",
        "image_url":config.dRR
    },
    "Ice Ice Outpost":{
        "range":"L121:O132",
        "image_url":config.dIIo
    },
    "Hyrule Circuit":{
        "range":"Q121:T132",
        "image_url":config.dHC
    },
    "Baby Park":{
        "range":"B134:E145",
        "image_url":config.dBP
    },
    "Cheese Land":{
        "range":"G134:J145",
        "image_url":config.dCL
    },
    "Wild Woods":{
        "range":"L134:O145",
        "image_url":config.dWW
    },
    "Animal Crossing":{
        "range":"Q134:T145",
        "image_url":config.dAC
    },
    "Neo Bowser City":{
        "range":"B147:E158",
        "image_url":config.dNBC
    },
    "Ribbon Road":{
        "range":"G147:J158",
        "image_url":config.dRiR
    },
    "Super Bell Subway":{
        "range":"L147:O158",
        "image_url":config.dSBS
    },
    "Big Blue":{
        "range":"Q147:T158",
         "image_url":config.dBB
    },
    "Cloudtop Cruise":{
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
    await bot.add_cog(Slxleaderboard(bot))
#import mk8dx
from mk8dx import Track
class Slxleaderboard(commands.Cog, name='leaderboard'):
    def __init__(self, bot: commands.Bot):
        self.bot: commands.Bot = bot

    @commands.command(name="show", description="to show overall and specific track")
    async def show_track(self, ctx, track: str):
        dcl = Track.from_nick(track)
        track = dcl.name
        
        valid_tracks = dlc_track.keys()
        valid2_track = standard_track.keys()
        overall_s_track = top_s.keys()
        overall_dlc_track = top_dlc.keys()
        valid_top = top_all.keys()

        embed = Embed()  # สร้าง Embed เปล่า

        if track in top_s:
            image_url = top_s[track]["image_url"]
            if image_url:
                embed.set_image(url=image_url)  # เพิ่มรูปภาพใน Embed

        # ตรวจสอบและเพิ่มรูปภาพใน Embed
        if track in top_dlc:
            image_url = top_dlc[track]["image_url"]
            if image_url:
                embed.set_image(url=image_url)

        # เริ่มสร้าง Embed สำหรับข้อมูล track
        track_embed = Embed()

        if track in dlc_track:
            image_url = dlc_track[track]["image_url"]
            if image_url:
                await ctx.send(image_url)  # ส่งรูปภาพก่อน

        elif track in standard_track:
            image_url = standard_track[track]["image_url"]
            if image_url:
                await ctx.send(image_url)  # ส่งรูปภาพก่อน

        if track in top_all:
            image_url = top_all[track]["image_url"]
            if image_url:
                await ctx.send(image_url)  # ส่งรูปภาพก่อน

        if track in valid_tracks:
            data = get_data_for_track(overall_dlc, dlc_track[track]["range"])
            formatted_data = "\n".join([" ".join(row) for row in data])
            formatted_data = formatted_data.replace("[", "").replace("]", "").replace("'", "").replace(",", "")
            track_embed.add_field(name="", value=f"**{track}**\n{formatted_data}")  # เพิ่มข้อมูลในรูปแบบ Field ใน Embed ข้อมูล track

        elif track in valid2_track:
            data2 = get_standard_track(overall_s, standard_track[track]["range"])
            format2 = "\n".join([" ".join(row) for row in data2])
            format2 = format2.replace("[", "").replace("]", "").replace("'", "").replace(",", "")
            track_embed.add_field(name="", value=f"**{track}**\n{format2}")  # เพิ่มข้อมูลในรูปแบบ Field ใน Embed ข้อมูล track

        if track in overall_s_track:
            data3 = get_data_for_track(overall_s, top_s[track]["range"])
            format3 = "\n".join([" ".join(row) for row in data3])
            format3 = format3.replace("[", "").replace("]", "").replace("'","").replace(",", "")
            track_embed.add_field(name="", value=f"**{track}**\n{format3}")  # เพิ่มข้อมูลในรูปแบบ Field ใน Embed ข้อมูล track

        elif track in overall_dlc_track:
            data4 = get_standard_track(overall_dlc, top_dlc[track]["range"])
            format4 = "\n".join([" ".join(row) for row in data4])
            format4 = format4.replace("[", "").replace("]", "").replace("'", "").replace(",", "")
            track_embed.add_field(name="", value=f"**{track}**\n{format4}")  # เพิ่มข้อมูลในรูปแบบ Field ใน Embed ข้อมูล track

        if track in valid_top:
            data5 = get_standard_track(top_ranking, top_all[track]["range"])
            format5 = "\n".join([" ".join(row) for row in data5])
            format5.replace("[", "").replace("]","").replace("'","").replace(",", "")
            track_embed.add_field(name="", value=f"**{track}**\n{format5}")  # เพิ่มข้อมูลในรูปแบบ Field ใน Embed ข้อมูล track

        await ctx.send(embed=track_embed)  # ส่ง Embed ข้อมูล track

    @commands.command(name="player")
    async def _player(self,ctx):
        worksheet = player_tab.get("A1:C24")
        data = "\n".join([" ".join(row) for row in worksheet])
        await ctx.send(data)

