import re
import discord
from new_command import player_id
msg = None

def categorize_track(track):
            track = filtertext(match="")
            lower_track = track.lower()
            dlc_tracks = [
                'bpp', 'btc', 'bcmo', 'bcma', 'btb', 'bsr', 'bsg', 'bnh', 'bnym',
                'bmc3', 'bkd', 'bwp', 'bss', 'bsl', 'bmg', 'bshs', 'bll', 'bbl',
                'brrm', 'bmt', 'bbb', 'bpg', 'bmm', 'brr7', 'bad', 'brp', 'bdks',
                'byi', 'bbr', 'bmc', 'bws', 'bssy', 'batd', 'bdc', 'bmh', 'bscs',
                'blal', 'bsw', 'bkc', 'bvv','bra','bdkm','bdci','bppc','bmd','briw',
                'bbc3','brrw',
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
                return 'wrong abbr!'
            
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
    msg_content = msg.content
    matches = re.findall(pattern, msg_content)
    for match in matches:
        return match
    else:
        return None

def filtertext(match):
    pattern = r'[a-zA-Z0-9]+'
    msg_content = msg.content
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
