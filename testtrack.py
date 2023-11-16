from mk8dx import Track

def compare_track(abbreviation):
    try:
        list_track = Track.from_nick(nick=abbreviation).full_name
        track_name = list_track
        return track_name
    except AttributeError:
        return f'{abbreviation} is not in the tracks list'
    
result = compare_track(abbreviation="rgv")
print(result)