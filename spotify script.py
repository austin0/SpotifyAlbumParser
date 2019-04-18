# shows album info for a URN or URL
# Austin Bailey 19/04/19
# really poorly coded but I needed it to work
# authenticates with spotify api to pull and parse album info

import spotipy
import sys
import spotipy.util as util
import json
import pprint

artist_name = ""
addAlbum = "y"
sqlString = ""

if len(sys.argv) > 1:
    urn = sys.argv[1]
else:
    urn = 'spotify:album:2T6jeELx5BqH4GMLObBy10'

username = "evolvespotify60@grr.la"
scope = "user-library-read"

token = util.prompt_for_user_token(username,scope,client_id='c85eb119fa4c4cbd8a55fd7612c6a737',client_secret='226a8e8461eb470cbc53c0bb545a62cc',redirect_uri='http://localhost/')

while addAlbum == "y":

    sp = spotipy.Spotify(auth=token)
    album = sp.album(urn)
    #pprint.pprint(album)
    
    newdump = json.dumps(album)
    parsed_json = json.loads(newdump)
    artistdump= json.dumps(parsed_json['artists'])
    artist_json = json.loads(artistdump)
    genredump= json.dumps(parsed_json['artists'])
    genre_json = json.loads(artistdump)
    
    print(parsed_json['name'])
    print(parsed_json['album_type'])
    print(parsed_json['label'])
    print(parsed_json['release_date'])
    print(parsed_json['total_tracks'])
    for i in artist_json:
        artist_name = (i['name'])
    print(parsed_json['genres'])
    
    sqlString += ("INSERT INTO album(name, release_date, type, genre, track_count) VALUES({}, {}, {}, {}, {});\n".format(parsed_json['name'], parsed_json['release_date'], parsed_json['album_type'], parsed_json['genres'], parsed_json['total_tracks']))
    sqlString += ("INSERT INTO artist(name) VALUES({});\n".format(artist_name))
    
    addAlbum = str(input("Add another album? y/n?\n"))
    if addAlbum != "y":
        print("Exiting...")
        break
    
    urn = str(input("Enter a new spotify album URN:\n"))
    
text_file = open("albums2.txt", "w")
text_file.write(sqlString)
text_file.close()