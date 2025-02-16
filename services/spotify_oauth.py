import os
from spotipy.oauth2 import SpotifyOAuth

# Configura le credenziali Spotify
SPOTIFY_CLIENT_ID = "1309983a0aef47d7bddd75184d399824"
SPOTIFY_CLIENT_SECRET = "9af4d25c0049484a8ff33a20d5127b21"
SPOTIFY_REDIRECT_URI = "https://5000-zhengfabio-zhengfabiogp-uxskculo3z7.ws-eu117.gitpod.io/callback"

# Crea un'istanza di SpotifyOAuth
sp_oauth = SpotifyOAuth(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    redirect_uri=SPOTIFY_REDIRECT_URI,
    scope="user-read-private user-library-read playlist-read-private"
)
