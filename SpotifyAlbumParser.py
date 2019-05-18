# shows album info for a URN or URL
# Austin0 19/04/19

import spotipy
import sys
import spotipy.util as util
import json
#import pprint

addAlbum = True
sqlString = ""
userDecision = ""

username = "/*ENTER SPOTIFY USERNAME HERE*/" # your spotify username will be the email address you use to log in.
client_id="/*ENTER CLIENT ID HERE*/" # your spotify client keys can be retrieved from the developer.spotify.com page
client_secret="/*ENTER SECRET CLIENT KEY HERE*/"
scope = "user-library-read"
redirect_uri='http://localhost/'

token = util.prompt_for_user_token(username,scope,client_id,client_secret,redirect_uri)

while addAlbum:

    urn = (input("Enter a new spotify album URN:\n"))
    sp = spotipy.Spotify(auth=token)
    album = sp.album(urn)
    #pprint.pprint(album) # pprint is used to format the json returned by the spotify api, enable this to view raw data
    
    parsed_json = json.loads(json.dumps(album))
    artist_json = json.loads(json.dumps(parsed_json['artists']))
    
    print(parsed_json['name'])
    print(parsed_json['album_type'])
    print(parsed_json['label'])
    print(parsed_json['release_date'])
    print(parsed_json['total_tracks'])
    for artist in artist_json:
        artist_name = (artist['name'])
        print(artist_name)
    print(parsed_json['genres']) # if genres is empty spotify has not classified the album yet
    
    sqlString += ("INSERT INTO album(name, release_date, type, genre, track_count) VALUES('{}', '{}', '{}', '{}', {});\n".format
                    (parsed_json['name'],
                     parsed_json['release_date'], 
                     parsed_json['album_type'], 
                     parsed_json['genres'], 
                     parsed_json['total_tracks']))
                     
    sqlString += ("INSERT INTO artist(name) VALUES('{}');\n".format(artist_name))
    
    while userDecision not in {"y", "n"}:
        userDecision = str(input("Add another album? y/n?\n")).lower().strip()
        if userDecision == "n":
            print("Exiting...")
            addAlbum = False
    
    userDecision = ""
    
text_file = open("albums.txt", "w")
text_file.write(sqlString)
text_file.close()
