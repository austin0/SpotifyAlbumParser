SpotifyAlbumParser

This script uses the spotify API and spotipy repository to pull info bout a selected album from spotify servers and then parse it into PostGreSQL form for insertion into a database.

### Requirements

* Login to Spotify Developer Dashboard and create a new app to obtain the Client ID and Client Secret. Add these to CLIENT_ID and CLIENT_SECRET in the code. After this, click edit settings of the newly created app and add http://localhost/ to Redirect URIs and save.

* [Spotipy](https://spotipy.readthedocs.io/en/latest/) : Spotipy is a lightweight Python library for the Spotify Web API. With Spotipy you get full access to all of the music data provided by the Spotify platform.
