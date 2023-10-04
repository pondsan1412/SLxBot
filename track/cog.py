from typing import Optional
from components import BotMessage, ColoredEmbed

from discord import Message
from discord.ext import commands
from mk8dx import Track

from track.emoji import TrackEmoji
import discord

SNEET_BOT_ID = 810319965164535848
HAM_GUILD_ID = 899957283230994442
TrackEmbed = discord.Embed
class TrackCog(commands.Cog, name='Track'):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot
    
    @commands.Cog.listener('on_ready')
    async def setup(self):
        TrackEmoji.setup(self.bot)
        # my old team BP's joke
        if self.bot.user.id == SNEET_BOT_ID:
            Track.RMP.nicks |= {'seimei'}
            Track.TH.nicks |= {'ｾｲﾒｲ'}
            Track.RMMM.nicks |= {'ﾜﾀｶﾞｼ'}
            Track.SA.nicks |= {'dra', 'ﾄﾞﾗ'}
            Track.DEA.nicks |= {'kichi', 'ｷﾁ'}
            Track.DBP.nicks |= {'kami', 'kami track', 'ｵﾐｸｼﾞｺｰｽ'}
            Track.DWGM.nicks |= {'gomi', 'gomi track'}
            Track.DBB.nicks |= {'ﾓｻﾞﾋﾞｰ'}
            Track.RDKJ.nicks |= {'jk'}
            Track.CC.nicks |= {'新潟県', 'ﾆｲｶﾞﾀｹﾝ'}

    def track_info(self, nick: str, include_joke: bool = False) -> Optional[BotMessage]:
        track = Track.from_nick(nick)
        if track is None:
            if not include_joke:
                return
            # my team HαM's joke
            elif nick == 'どかんがどっかーん':
                track = Track.BPP
            elif nick in {'きらーうらいか', 'キラー裏イカ'}:
                track = Track.DCL
            elif nick == 'いるかはいるか':
                track = Track.DS
            elif nick == 'はむで試行回数をこなしすぎるコース':
                track = Track.RMP
            else:
                return
        embed = TrackEmbed(
            title=f'{track.abbr} {track.abbr_ja}',
            description=f'{track.full_name}\n{track.full_name_ja}'
        )
        if track.id < 80:
            embed.set_image(url=f'https://raw.githubusercontent.com/sheat-git/mk8dx/main/tracks/20230713/{track.id}.jpg')
            embed.set_footer(text='Map: © Mario Kart Blog')
        else:
            embed.set_image(url=f'https://raw.githubusercontent.com/sheat-git/mk8dx/main/cups/{track.cup.id}.jpeg')
        return BotMessage(embed=embed)

    def nicks(self, nick: str) -> BotMessage:
        track = Track.from_nick(nick)
        if track is None:
            return BotMessage(f'Track Not Found: {nick}')
        return BotMessage(embed=ColoredEmbed(
            title=f'{track.abbr} {track.abbr_ja}',
            description='\n'.join(sorted(track.nicks))
        ))

    @commands.command(
        name='nicks',
        aliases=['nick'],
        brief='Shows all registered nicknames'
    )
    async def command_nicks(self, ctx: commands.Context, nick: str):
        await self.nicks(nick=nick).send(msg=ctx)

    @commands.Cog.listener(name='on_message')
    async def catch_track(self, message: Message):
        if message.author.bot:
            return
        if message.guild and message.guild.name == "Silent Lightning [MK8D Server]":
                return
        is_ham = (message.guild is not None and message.guild.id == HAM_GUILD_ID)
        msg = self.track_info(nick=message.content, include_joke=is_ham)
        if msg is not None:
            await msg.send(message.channel)