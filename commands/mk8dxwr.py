import re

import aiohttp
import discord
from bs4 import BeautifulSoup
from discord import Embed
from discord.ext import commands
from mk8dx import Track
from pytube import YouTube

from function import player_mii_pfp

class MyView(discord.ui.View):
  def __init__(self,url):
      super().__init__(timeout=600000)
      self.url = url
      button = discord.ui.Button(label=' ', style=discord.ButtonStyle.url, url=f'{self.url}',emoji="<a:youtubecafeyoutube:1175840629536870450>")
      self.add_item(button)


  @discord.ui.button(label="watch in discord", style=discord.ButtonStyle.green,emoji="<a:srt_discordloading:1175832338597429358>")
  async def youtube_discord(self, interaction:discord.Interaction,button:discord.ui.Button):
      await interaction.response.send_message(f"{self.url}",delete_after=300)

      self.stop()
class mk8dxwr(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        
    @commands.hybrid_command(name='wr')
    async def worldrecord(self,ctx:commands.Context, abbra_track):
        """display world record of anytrack for currently track from mk8dxwr.com"""
        
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
                        re.search(r"show_splits\('([^']+)', '([^']+)', '([^']+)', '([^']+)', '([^']+)'", onmouseover_attr)
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
            except TypeError:
                # Handle TypeError
                return f"Error: {trackname}'s WR video hasn't been verified yet in mkwrs.com, so no video for you"

            except AttributeError as e:
                # Print relevant information for debugging
                print(f"AttributeError: {e} ")

                return f"Error: AttributeError in get_track_url for track {trackname} \n {player_}\n   \n {e}"



        url = "https://mkwrs.com/mk8dx/wrs.php?date=0"

        trackname = result
        if trackname == "SNES Bowser's Castle 3":
            trackname = "SNES Bowser Castle 3"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                await response.text()

        result = await get_track_url(trackname, url)
        def youtube_id(url):
            try:
                video = YouTube(url)
                video_id = video.video_id
                return video_id 
            except Exception as e:
                return f"error: {e}"

        if isinstance(result, tuple):
            # Unpack tuple values
            track_url, date_, player_, nation_, full_url, time_, combo_charecter, combo_vegicle, combo_glider, combo_roller, duration_, lap1, lap2, lap3, coins, shroom, player_profile = result
            mii_pfp = player_mii_pfp(player_name=player_)
            # Get video information
            video_picture_url = track_url
            video_id = youtube_id(video_picture_url)
            thumbnail_url = f'https://img.youtube.com/vi/{video_id}/maxresdefault.jpg'

            # Format player name
            player_ = f"{player_}"
            name_parts = player_.split(" ")
            " ".join(name_parts[:-1]).rstrip()

            # Create Discord Embed
            embed = Embed()
            embed.set_thumbnail(url=mii_pfp)
            embed.set_author(name=f"{player_}'s profile", icon_url=f"{full_url}", url=f"https://mkwrs.com/mk8dx/{player_profile}")
            embed.add_field(
                name=f"Currently World Record Of **___{trackname}___** ",
                value = f"""
                    Verified Date: **{date_}**
                    Time: **{time_}**
                    WR HOLDER: **{player_}**
                    Country: **{nation_}**
                    Length Day: **{duration_}**
                    **__lap time__** :stopwatch:
                    :one: {lap1}
                    :two: {lap2}
                    :three: {lap3}
                    <:threemushrooms:1175155099971096679> **{shroom}**
                    <:item000Coin:1175154443306668192> **{coins}**

                    **___Combination___**
                    charecter: **{combo_charecter}**
                    vehicle: **{combo_vegicle}**
                    roller: **{combo_roller}**
                    glider: **{combo_glider}**
                """)
            embed.set_image(url=f"{thumbnail_url}")
            embed.set_footer(text="")
            yt_send = MyView(url=track_url)
        
            await ctx.send(embed=embed, view=yt_send)
        else:
            await ctx.send(result)


        
async def setup(bot):
    await bot.add_cog(mk8dxwr(bot))