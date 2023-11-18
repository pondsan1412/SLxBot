import discord
from discord.ext import commands
from bs4 import BeautifulSoup
class mk8dxwr(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        
    @commands.hybrid_command(name='wr')
    async def worldrecord(self,ctx:commands.Context, abbra_track):
        """display world record of anytrack for currently track from mk8dxwr.com"""
        from mk8dx import Track
        from discord import Embed
        import aiohttp
        from pytube import YouTube
        from discord import Button
        import re
        def compare_track(abbra):
            try:
                list_track = Track.from_nick(nick=abbra).full_name
                track_name = list_track
                return track_name
            except AttributeError:
                return f'{abbra} is not in the tracks list'

        result = compare_track(abbra=abbra_track)

        async def get_track_url(trackname, url):
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    html_content = await response.text()

            soup = BeautifulSoup(html_content, 'html.parser')
            wr_table = soup.find('table', class_='wr')

            try:
                if wr_table:
                    for row in wr_table.find_all('tr')[1:]:
                        columns = row.find_all('td')
                        track = columns[0].a.text.strip()
                        date_ = columns[4].text.strip()
                        player_ = columns[2].text.strip()
                        img_tag = columns[3].center.img
                        nation_ = img_tag['title'] if img_tag else None
                        src_value = img_tag['src']
                        combo_charecter = columns[6].text.strip()
                        combo_vehicle = columns[7].text.strip()
                        combo_roller = columns[8].text.strip()
                        combo_glider = columns[9].text.strip()
                        # Provide a default value if columns[10] is None
                        duration_ = columns[5].text.strip()
                        full_url = f'https://mkwrs.com/mk8dx/{src_value}'
                        onmouseover_attr = columns[10].img.get('onmouseover', '')
                        splits_values = [value.strip() for value in onmouseover_attr[15:-2].split("', '")]
                        matches = re.search(r"show_splits\('([^']+)', '([^']+)', '([^']+)', '([^']+)', '([^']+)'", onmouseover_attr)
                        player_profile = columns[2].a['href']
                        # Check if columns[1].a is not None before accessing its text attribute
                        time_ = columns[1].a.text.strip() if columns[1].a else None

                        if splits_values:
                            lap1, lap2, lap3, coins, shroom = splits_values[1:6]
                        else:
                            lap1, lap2, lap3, coins, shroom = '', '', '', '', ''
                        
                        if track.lower() == trackname.lower():
                            return columns[1].a['href'], date_, player_, nation_, full_url, time_, combo_charecter, combo_vehicle, combo_glider, combo_roller, duration_, lap1, lap2, lap3, coins, shroom,player_profile

                    # Track not found
                    return None
                else:
                    # No World Records table found
                    return None
            except TypeError as e:
                # Handle TypeError
                return f"Error: {trackname}'s WR video hasn't been verified yet in mkwrs.com, so no video for you"

            except AttributeError as e:
                # Print relevant information for debugging
                print(f"AttributeError: {e} ")
                print(f"columns[0]: {columns[0] if columns else None}")
                print(f"columns[0].a: {columns[0].a if columns and columns[0] else None}")
                return f"Error: AttributeError in get_track_url for track {trackname} \n {e}"



        url = "https://mkwrs.com/mk8dx/wrs.php?date=0"
        trackname = result
        if trackname == "SNES Bowser's Castle 3":
            trackname = "SNES Bowser Castle 3"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                html_content = await response.text()

        result = await get_track_url(trackname, url)
        def youtube_id(url):
            try:
                video = YouTube(url)
                video_id = video.video_id
                return video_id 
            except Exception as e:
                return f"error: {e}"

        if isinstance(result, tuple):
            track_url, date_, player_, nation_, full_url, time_,combo_charecter,combo_vegicle,combo_glider,combo_roller,duration_,lap1,lap2,lap3,coins,shroom,player_profile = result
            video_picture_url = track_url
            video_id = youtube_id(video_picture_url)
            thumbnail_url = f'https://img.youtube.com/vi/{video_id}/maxresdefault.jpg'
            player_ = f"{player_}"
            name_parts = player_.split(" ")
            cleaned_player = " ".join(name_parts[:-1]).rstrip()

            embed = Embed()
            
            embed.set_author(name=f"{player_}'s profile", icon_url=f"{full_url}",
                    url=f"https://mkwrs.com/mk8dx/{player_profile}")
            embed.add_field(name=f"Currently World Record Of **___{trackname}___** ",
                            value=f" \n Verified Date: **{date_}** \n Time: **{time_}** \n WR HOLDER: **{player_}**\n Country: **{nation_}**\nLength Day: **{duration_}** \n **__lap time__** :stopwatch: \n :one: {lap1}, \n:two: {lap2}, \n:three: {lap3} \n <:threemushrooms:1175155099971096679> **{shroom}** \n <:item000Coin:1175154443306668192> **{coins}** \n\n **___Combination___** \n charecter: **{combo_charecter}**\n vehicle: **{combo_vegicle}** \n roller: **{combo_roller}**\n glider: **{combo_glider}** ")
            embed.set_image(url=f"{thumbnail_url}").video
            embed.set_footer(text="")
            view = discord.ui.View()
            style = discord.ButtonStyle.blurple
            button = discord.ui.Button(style=style, url=track_url, label=f"Watch {player_}'s video")
            view.add_item(item=button)
            await ctx.send(embed=embed,view=view)
            
        else:
            await ctx.send(result)
async def setup(bot):
    await bot.add_cog(mk8dxwr(bot))