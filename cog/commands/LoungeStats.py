#Old files for Loungestats command fetch from mk8dx api

import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup
import re
from cog import config

#url logo 
mmr_icons = {
    'Silver 1': 'https://i.imgur.com/xgFyiYa.png',
    'Silver 2': 'https://i.imgur.com/xgFyiYa.png',
    'Iron 1': 'https://i.imgur.com/AYRMVEu.png',
    'Iron 2': 'https://i.imgur.com/AYRMVEu.png',
    'Gold 1': 'https://i.imgur.com/6yAatOq.png',
    'Gold 2': 'https://i.imgur.com/6yAatOq.png',
    'Diamond 2':'https://i.imgur.com/RDlvdvA.png',
    'Bronze 1':'https://i.imgur.com/DxFLvtO.png',
    'Bronze 2':'https://i.imgur.com/DxFLvtO.png',
    'Plat 1':'https://i.imgur.com/8v8IjHE.png',
    'Plat 2':'https://i.imgur.com/8v8IjHE.png',
    'Sapphire 1':'https://i.imgur.com/bXEfUSV.png',
    'Sapphire 2':'https://i.imgur.com/bXEfUSV.png',
    'Ruby 1':'https://i.imgur.com/WU2NlJQ.png',
    'Ruby 2':'https://i.imgur.com/WU2NlJQ.png',
    'Diamond 1':'https://i.imgur.com/RDlvdvA.png',
    'Diamond 2':'https://i.imgur.com/RDlvdvA.png',
    'Master 1':'https://i.imgur.com/3yBab63.png',
    'Master 2':'https://i.imgur.com/3yBab63.png',
    'Grandmaster':'https://i.imgur.com/EWXzu2U.png'

}



class LoungeStats(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
        self.words_txt = ""
        
    def cog_unload(self):
        self.bot.help_command = self._original_help_command
    
    async def help(self, ctx):
        pass

    @commands.hybrid_command(name="stats")
    async def _stats(self, ctx, *, name=None):
        if name is None:
            name = ctx.author.display_name  
        if name == "FreeDobby":
            name = "Wednesday"
        if name == "Robala":
            name = "Robertala"
        
        url = f"https://8dxlounge-obs-overlay.vercel.app/overlay/{name}/9"
        response = requests.get(url)

        if response.status_code == 200:
            html_data = response.text
            soup = BeautifulSoup(html_data, 'html.parser')

            # Extract the relevant data
            title = soup.find('h1', class_='title').text
            items = [item.text.strip() for item in soup.find_all('div', class_='items')[0]]

            # หาข้อมูล MMR ด้วย regex
            mmr_match = re.search(r'MMR: (\d+) \(([^)]+)\)', html_data)
            if mmr_match:
                mmr_value = mmr_match.group(1)
                mmr_category = mmr_match.group(2)

                # ตรวจสอบ mmr_category และกำหนด thumbnail ตามคำศัพท์ที่ตรงกับนั้น
                thumbnail_url = mmr_icons.get(mmr_category, '')

                # Create an Embed to display the data
                embed = discord.Embed(title=title, color=discord.Color.blue())
                embed.set_thumbnail(url=thumbnail_url)
                for item in items:
                    item = item.split(': ')
                    if len(item) == 2:
                        embed.add_field(name=item[0], value=item[1], inline=True)

                await ctx.send(embed=embed)
        else:
            await ctx.send("No info")

    @commands.hybrid_command(name="mmr")
    async def _mmr(self, ctx, *, names=None):
        if names is None:
            names = [ctx.author.display_name]
        else:
            # แยกชื่อผู้เล่นโดยใช้ `,` และลบช่องว่างหลังหน้าและหลังชื่อผู้เล่น
            names = [name.strip() for name in names.split(',')]

        mmr_info = []

        for name in names:
            if name == "FreeDobby":
                name = "Wednesday"
            elif name == "Robala":
                name = "Robertala"
            
            url = f"https://8dxlounge-obs-overlay.vercel.app/overlay/{name}/9"
            response = requests.get(url)

            if response.status_code == 200:
                html_data = response.text

                mmr_match = re.search(r'MMR: (\d+)', html_data)
                if mmr_match:
                    mmr_value = mmr_match.group(1)
                    mmr_info.append(f"**{name}**\n{mmr_value}")

        if mmr_info:
            # สร้าง embed สำหรับแสดงข้อมูล MMR
            embed = discord.Embed(title=f"{config.gigachad}MMR Information{config.mariothinking}", color=discord.Color.blue())
            for info in mmr_info:
                embed.add_field(name="\u200B", value=info, inline=True)

            if len(mmr_info) > 1:
                # คำนวณค่าเฉลี่ยของ MMR และแสดงเฉพาะถ้ามีมากกว่าหนึ่งคน
                mmr_values = [int(info.split('\n')[1]) for info in mmr_info]
                mmr_avg = sum(mmr_values) / len(mmr_values)
                embed.add_field(name="\u200B", value=f"**MMR Avg.**\n{mmr_avg:.1f}", inline=False)

            await ctx.send(embed=embed)
        else:
            await ctx.send("No info")
    @commands.hybrid_command("inwardtop")
    async def _inward(self,ctx):
        # ระบุ URL ของหน้าเว็บ
        url = "https://www.mkleaderboards.com/mk8dx/charts/inward/150cc/1/full"

        # ดึงเนื้อหาจาก URL
        response = requests.get(url)
        html = response.text

        # ใช้ BeautifulSoup เพื่อแปลง HTML
        soup = BeautifulSoup(html, "html.parser")

        # ค้นหา <div> ที่มี class="panel centered"
        panel_div = soup.find("div", {"class": "panel centered"})

        if panel_div:
            # ถ้าเจอ <div> ที่ตรงตามเงื่อนไข
            # ให้ดึงข้อความภายใน <div> และส่งไปยังแชทของ Discord
            panel_info = panel_div.get_text()
            await ctx.send(f"{panel_info}")
        else:
            # ถ้าไม่พบ <div> ที่ตรงตามเงื่อนไข
            await ctx.send("ไม่พบข้อมูลใน <div class=\"panel centered\">")
    


        
async def setup(bot):
    await bot.add_cog(LoungeStats(bot))