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
                'bbc3','brr',
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
            
def slxmember_id(user,user_id):
            if user == player_id.AMDX:
                return "AMDX"
            elif user == player_id.Ant:
                return "Ant"
            elif user == player_id.BenJames:
                return "Benjames"
            elif user == player_id.BIGW:
                return "BigW"
            elif user == player_id.FalseKing:
                return "FalseKing"
            elif user == player_id.FreeDobby:
                return "FreeDobby"
            elif user == player_id.Holycomb:
                return "Holycomb"
            elif user == player_id.JacKo:
                return "JacKo"
            elif user == player_id.Kaleb112:
                return "Kaleb112"
            elif user == player_id.leftyginger:
                return "leftyginger"
            elif user == player_id.Nesszomi:
                return "Nesszomi"
            elif user == player_id.Paulo22:
                return "Paulo22"
            elif user == player_id.Pond:
                return "Pond"
            elif user == player_id.Rick:
                return "Rick"
            elif user == player_id.Robertala:
                return "Robertala"
            elif user == player_id.Rushh:
                return "Rushh"
            elif user == player_id.Stan:
                return "Stan"
            elif user == player_id.SUIIced:
                return "SUIIced"
            elif user == player_id.Torasshi:
                return "Torasshi"
            elif user == player_id.Vonz:
                return "Vonz"
            else:
                return user_id

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
    