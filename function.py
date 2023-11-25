import re
import discord
from cog import player_id
msg = None

def categorize_track(track):
            track = filtertext(match=track)
            lower_track = track.lower()
            dlc_tracks = [
                'bpp', 'btc', 'bcmo', 'bcma', 'btb', 'bsr', 'bsg', 'bnh', 'bnym',
                'bmc3', 'bkd', 'bwp', 'bss', 'bsl', 'bmg', 'bshs', 'bll', 'bbl',
                'brrm', 'bmt', 'bbb', 'bpg', 'bmm', 'brr7', 'bad', 'brp', 'bdks',
                'byi', 'bbr', 'bmc', 'bws', 'bssy', 'batd', 'bdc', 'bmh', 'bscs',
                'blal', 'bsw', 'bkc', 'bvv','bra','bdkm','bdci','bppc','bmd','briw',
                'bbc3','brrw','brr','bdct'
            ]
            
            if lower_track in dlc_tracks:
                return 'DLC'
            
            elif lower_track in [
                'mks', 'wp', 'ssc', 'tr', 'mc', 'th', 'tm', 'sgf', 'sa', 'ds',
                'ed', 'mw', 'cc', 'bdd', 'bc', 'rr', 'rmmm', 'rmc', 'rccb', 'rtt',
                'rddd', 'rdp3', 'rry', 'rdkj', 'rws', 'rsl', 'rmp', 'ryv', 'rttc',
                'rpps', 'rgv', 'rrd', 'dyc', 'dea', 'ddd', 'dmc', 'dwgm', 'drr',
                'diio', 'dhc', 'dbp', 'dcl', 'dww', 'dac', 'dnbc', 'drir', 'dsbs', 'dbb'
            ]:
            
                return 'S'
            else:
                return 'abbr not in anylist'
            
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
        return None
    

def slx_member_id(current_slx_member):
    #current slx players
    Pond = 324207503816654859
    Stan = 842403545709150268
    Robertala = 857313302203727884
    Ant = 687878207956975758
    FreeDobby = 873958010467258428
    FalseKing = 209006928272162816
    AMDX = 822687821243875378
    Vonz = 857722140006940692
    JacKo = 405275041388036106
    Rick = 696689053449322566
    Rushh = 513922747341209601
    BIGW = 951512433598541915
    BenJames = 709522824544518216
    Kaleb112 = 771019494125993985
    Torasshi = 262191669410005002

    #former slx players
    Zquka = 257332011075764224
    Xenoph = 151131182187282432
    slx_list = [Pond,Stan,Robertala,Ant,FreeDobby,FalseKing,AMDX,Vonz,JacKo,Rick,Rushh,BIGW,BenJames,Kaleb112,Torasshi]
    slx_former_list = [Zquka,Xenoph]
    return slx_list
                
#wrong def slx_id(user_id):
    if user_id.id not in player_id:
        return
    else:
        return user_id.id
            
def filterregex(match):
    pattern = r'\d+:\d+\.\d+'
    msg_content = ""
    matches = re.findall(pattern, msg_content)
    for match in matches:
        return match
    else:
        return None
    
def get_filter_content(track):
    return track


def filtertext(match):
    pattern = r'[a-zA-Z0-9]+'
    msg_content = match
    matches = re.findall(pattern, msg_content)
    for match in matches:
        return match
    else:
        return '' 
    
def check_user_id(user_id_check:int):
    list_member = slx_member_id(current_slx_member=int)
    if user_id_check not in list_member:
        return None
    else:
        for current_slx_member in list_member:
            return current_slx_member
        
def player_mii_pfp(player_name):
    if player_name=="Alberto":
        return "https://i.gyazo.com/d6ddd086e16f14b53fafcd05753f5780.png"
    elif "Army":
        return "https://i.gyazo.com/12b465eb7c0600e5452bd3885288b2a4.png"
    elif "Panda":
        return "https://i.gyazo.com/3eb3a940af6dc812c6444ab97175f8e1.jpg"
    elif "StervtL":
        return "https://i.gyazo.com/583ee34baab6131d8c4c4aaf0b32e01b.png"
    elif "Jimmy":
        return "https://gyazo.com/1d5c4ff0d1f1d4510c791c4d931e1ea2.png"
    elif "Technical":
        return "https://i.gyazo.com/63b6329a321fdc12d8fe55122d4f833f.png"
    elif "K4I":
        return "https://gyazo.com/06bdc3c68c5baf1e987e15b81a4fe980.png"
    elif "Kevin":
        return "https://gyazo.com/51dede1323d5fe7755e068afa9306c6c.png"
    elif "Shaun":
        return "https://gyazo.com/edcb7a068dee9b327580481e1650617a.png"
    elif "JenZua":
        return "https://i.gyazo.com/8749de065de445f330585667351ad555.png"
    elif "Pii":
        return "https://i.gyazo.com/ff76355cb6b1f47d9ea9d0ffbee09e68.png"
    elif "SuperFX":
        return "https://media.discordapp.net/attachments/360273303426039808/735824383016435812/image0.jpg"
    elif "おまえモナー":
        return "https://gyazo.com/43267f60c9e1b727241e12670c307b4c.png"
    elif "Vincent":
        return "https://i.gyazo.com/d565058807ffb5cb3a9665fea9612dc3.png"
    elif "しらぬい":
        return "https://i.gyazo.com/75700e32ceac6acd9984d72dc22b8ed3.png"
    elif "Lemon":
        return "https://gyazo.com/5493870e38f06133fb083cdb0a72241a.png"
    elif "TylerR":
        return "https://gyazo.com/0f8ec2c284c30d8711c081c112317b21.png"
    elif "Davi":
        return "https://gyazo.com/68501b0fb879da67355f6889970ab51a.png"
    elif "そうめん":
        return "https://i.gyazo.com/879becac3bd86c3d09c5fe8dfc5d50ea.png"
    elif "エル":
        return "https://i.gyazo.com/f1985f99b69c0b50304537170c3b2822.png"
    elif "Danny":
        return "https://gyazo.com/a6040832be242407d60f5ebbe6346193.png"
    else:
        return "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTBD-Y75x88euisalAMvdnAmutQA9ISrptQSA&usqp=CAU"