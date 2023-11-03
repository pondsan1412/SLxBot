import discord
from discord.ext import commands
from discord import app_commands,Embed
from easygoogletranslate import EasyGoogleTranslate
import asyncio
import re
from new_command import player_id
from cog import config
from oauth2client.service_account import ServiceAccountCredentials
import gspread
import discord.utils

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

class context(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        self.ctx_menu = app_commands.ContextMenu(
            name="Translate",
            callback=self.tl,
        )
        self.ctx_menu2 = app_commands.ContextMenu(name="Submit TimeTrials",callback=self.submit,)
        self.bot.tree.add_command(self.ctx_menu)
        self.bot.tree.add_command(self.ctx_menu2)
    async def cog_unload(self) -> None:
        self.bot.tree.remove_command(self.ctx_menu.name, type=self.ctx_menu.type)
    async def tl(self,i:discord.Interaction,msg:discord.Message):
        
        flag_emoji_ger = "🇩🇪"
        flag_emoji_jp = "🇯🇵"
        flag_emoji_nl = "🇳🇱"
        flag_emoji_us = "🇺🇸"
        flag_emoji_th = "🇹🇭"
       
        translator = EasyGoogleTranslate()
        translated_text = translator.translate(f'{msg.content}', target_language='en')
        
        msg = await i.response.send_message(translated_text)
        
        await msg.add_reaction(flag_emoji_ger)
        await msg.add_reaction(flag_emoji_jp)
        await msg.add_reaction(flag_emoji_nl)
        await msg.add_reaction(flag_emoji_us)
        await msg.add_reaction(flag_emoji_th)

        def check(reaction, user):
            if str(reaction.emoji) in [
                flag_emoji_ger,flag_emoji_jp,
                flag_emoji_nl,flag_emoji_us,
                flag_emoji_th
            ]:
                if user != self.bot.user:
                    dest_lang = None
                
                    if str(reaction.emoji) == flag_emoji_ger:
                        dest_lang = "de"
                    elif str(reaction.emoji) == flag_emoji_jp:
                        dest_lang = "ja"
                    elif str(reaction.emoji) == flag_emoji_nl:
                        dest_lang = "nl"
                    elif str(reaction.emoji) == flag_emoji_us:
                        dest_lang = "en"
                    elif str(reaction.emoji) == flag_emoji_th:
                        dest_lang = "th"

                    if dest_lang is not None:
                        new_translate = translator.translate(translated_text, target_language=dest_lang)
                        asyncio.create_task(msg.edit(content=f"`{new_translate}`: {new_translate}"))
                        return True
            return False       
        
        while True:
            try:
                reaction, user = await self.bot.wait_for('reaction_add', timeout=600.0, check=check)
            except asyncio.TimeoutError:
                asyncio.create_task(msg.edit(content=f"Timeout❌"))
                break

    
    
    @app_commands.checks.has_any_role('TT Updater')
    async def submit(self, i: discord.Interaction, msg: discord.Message):
        role = discord.utils.get(i.guild.roles, name="TT Updater")
        if role in i.user.roles:
            pass
        else:
            await i.response.send_message("you do not have permission")
        def slxmember_id(user):
            if user == player_id.Pond:
                return "Pond"
            elif user == player_id.Stan:
                return "Stan"
            elif user == player_id.Robertala:
                return "Robertala"
            elif user == player_id.Ant:
                return "Ant"
            elif user == player_id.FreeDobby:
                return "FreeDobby"
            elif user == player_id.FalseKing:
                return "FalseKing"
            elif user == player_id.AMDX:
                return "AMDX"
            elif user == player_id.Vonz:
                return "Vonz"
            elif user == player_id.JacKo:
                return "JacKo"
            elif user == player_id.Rick:
                return "Rick"
            elif user == player_id.Rushh:
                return "Rushh"
            elif user == player_id.BIGW:
                return "BIGW"
            elif user == player_id.BenJames:
                return "Benjames"
            elif user == player_id.Kaleb112:
                return "Kaleb112"
            elif user ==player_id.Torasshi:
                return "Torasshi"
            else:
                return msg.author.name
            
        def filterregex(match):
            pattern = r'\d+:\d+\.\d+'
            msg_content = msg.content
            matches = re.findall(pattern, msg_content)
            for match in matches:
                return match
            else:
                return None

        def filtertext(match):
            pattern = r'[a-zA-Z]+'
            msg_content = msg.content
            matches = re.findall(pattern, msg_content)
            for match in matches:
                return match
            else:
                return '' 
            
        def categorize_track(track):
            track = filtertext(match="")
            lower_track = track.lower()
            dlc_tracks = [
                'bpp',
                'btc',
                'bcmo',
                'bcma',
                'btb',
                'bsr',
                'bsg',
                'bnh',
                'bnym',
                'bmc3',
                'bkd',
                'bwp',
                'bss',
                'bsl',
                'bmg',
                'bshs',
                'bll',
                'bbl',
                'brrm',
                'bmt',
                'bbb',
                'bpg',
                'bmm',
                'brr7',
                'bad',
                'brp',
                'bdks',
                'byi',
                'bbr',
                'bmc',
                'bws',
                'bssy',
                'batd',
                'bdc',
                'bmh',
                'bscs',
                'blal',
                'bsw',
                'bkc',
                'bvv'
            ]
            
            if lower_track in dlc_tracks:
                return 'DLC'
            elif lower_track in [
                'mks',
                'wp',
                'ssc',
                'tr',
                'mc',
                'th',
                'tm',
                'sgf',
                'sa',
                'ds',
                'ed',
                'mw',
                'cc',
                'bdd',
                'bc',
                'rr',
                'rmmm',
                'rmc',
                'rccb',
                'rtt',
                'rddd',
                'rdp3',
                'rry',
                'rdkj',
                'rws',
                'rsl',
                'rmp',
                'ryv',
                'rttc',
                'rpps',
                'rgv',
                'rrd',
                'dyc',
                'dea',
                'ddd',
                'dmc',
                'dwgm',
                'drr',
                'diio',
                'dhc',
                'dbp',
                'dcl',
                'dww',
                'dac',
                'dnbc',
                'drir',
                'dsbs',
                'dbb'
            ]:
                return 'S'
            else:
                return None


                
        author_id = msg.author.id
        player = slxmember_id(author_id)
        trackname = filtertext(msg.content)
        time = filterregex(msg.content)
        category = categorize_track(trackname)
        update_row_submit =[trackname, category, player, time]
        msg_id = msg.jump_url

        if trackname=='':
            error_message_track = f"player {msg.author.mention} didn't put **track abbr** did you forget it?. \ngo to post {msg_id} \n`error: missing **track abbr**`"
            await i.response.send_message(error_message_track)
            
        
        elif time is None:
            error_message_time = f"can't submit because {msg.author.mention}  forgor to put **time** in their post.\n go to post {msg_id} \n`error: missing **time**`"
            await i.response.send_message(error_message_time)
            return
        else:
            file_in_sheet_testsheet.insert_row(update_row_submit, 3)
            check = "<:SL:916870427232567328>"
            await msg.add_reaction(check)
            embed = Embed(title=f"Update for {msg.author.name}", colour=discord.Color.gold())
            embed.add_field(name="description",value=f"Track: **{trackname}** time: **{time}**",)
            embed.add_field(name="Proof",value=msg_id)
            embed.set_author(name=f"Verified by: {i.user.name}",icon_url=i.user.display_avatar)
            embed.set_thumbnail(url=msg.author.display_avatar)
            await i.response.send_message(embed=embed)


    



        

    
    @commands.command(name="c")
    async def c(self, ctx:commands.Context):
        await ctx.send("yo")
async def setup(bot):
    await bot.add_cog(
        context(bot)
    )