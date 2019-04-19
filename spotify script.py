# shows album info for a URN or URL
# Austin0 19/04/19

import spotipy
import sys
import spotipy.util as util
import json
#import pprint

artist_name = ""
addAlbum = "y"
sqlString = ""

if len(sys.argv) > 1:
    urn = sys.argv[1]
else:
    urn = 'spotify:album:2T6jeELx5BqH4GMLObBy10'

username = "*/ENTER SPOTIFY USERNAME HERE/*" # your spotify username will be the email address you use to log in.
scope = "user-library-read"

token = util.prompt_for_user_token(username,scope,client_id='*/ENTER  CLIENT ID HERE/*',client_secret='*/ENTER SECRET CLIENT KEY HERE/*',redirect_uri='http://localhost/') # your spotify client keys can be retrieved from the developer.spotify.com page

while addAlbum == "y":

    sp = spotipy.Spotify(auth=token)
    album = sp.album(urn)
    #pprint.pprint(album) #ppint is used to format the json returned by the spotify api, enable this to view raw data
    
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
    
    sqlString += ("INSERT INTO album(name, release_date, type, genre, track_count) VALUES('{}', '{}', '{}', '{}', {});\n".format(parsed_json['name'], parsed_json['release_date'], parsed_json['album_type'], parsed_json['genres'], parsed_json['total_tracks']))
    sqlString += ("INSERT INTO artist(name) VALUES('{}');\n".format(artist_name))
    
    addAlbum = str(input("Add another album? y/n?\n"))
    if addAlbum != "y":
        print("Exiting...")
        break
    
    urn = str(input("Enter a new spotify album URN:\n"))
    
text_file = open("albums2.txt", "w")
text_file.write(sqlString)
text_file.close()