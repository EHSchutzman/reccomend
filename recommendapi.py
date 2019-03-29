import musicbrainzngs as m
from fuzzywuzzy import fuzz
import json
m.auth('ehschutzman', 'password123')
m.set_useragent("CS525App", "1.0", contact='')


def main(s):


    result = m.search_artists(artist=s)
    best_ratio = -1
    name = ''
    artist_id = ''
    for artist in result['artist-list']:
        ratio = fuzz.token_set_ratio(s, artist['name'])
        if ratio > best_ratio:
            best_ratio = ratio
            artist_id = artist['id']
            name = artist['name']
            if ratio == 100:
                break

    if(artist_id == ''):
        print("No artist by name ", s)
        return

    result = m.search_releases(arid=artist_id,
                                          limit=15)
    artist = m.get_artist_by_id(artist_id)

    print(json.dumps(artist, sort_keys = True, indent = 4))

    print("\n::::::::::::\n")
    print(json.dumps(result, sort_keys = True, indent = 4))


if __name__ == '__main__':
    main('Jon Bellion')
    # main('John Bellion')
    # main('Aerosmoth')

