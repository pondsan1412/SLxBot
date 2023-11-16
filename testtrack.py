from mk8dx import Track

def compare_track(abbra):
    try:
        list_track = Track.from_nick(nick=abbra).full_name
        track_name = list_track
        return track_name
    except AttributeError:
        return f'{abbra} is not in the tracks list'
    
result = compare_track(abbra="rgv")
print(result)