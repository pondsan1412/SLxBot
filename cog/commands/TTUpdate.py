
import discord
from discord.ext import commands

import gspread
from oauth2client.service_account import ServiceAccountCredentials
from cog import secret
from discord import ApplicationContext,Option

import random
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
    @commands.slash_command(name="submit")
    async def _update_tt(
        self,
        ctx:ApplicationContext,
        track,
        category:Option(str,choices=['S','DLC','SL'],name='category'),
        player:Option(
            str,
            choices=
                config.player
            ,
            name='player',
        ),
        time
    ):
       

        update_row_submit = [track, category, player, time]  # กำหนดค่า update_row_submit ก่นใช้งาน
        if update_row_submit:
            file_in_sheet_testsheet.insert_row(update_row_submit, 3)
            await ctx.response.send_message(random.choice(config.Text_replying))
        else:
            await ctx.followup.send("please update with correct info")

    @commands.has_any_role('TT Updater')
    @commands.command(name="remove_tt",description="to remove tt when you failed update")
    async def _remove_tt(self,ctx:discord.Interaction):
        file_in_sheet_testsheet.delete_rows(3)
        await ctx.response.send_message(f"removed")

