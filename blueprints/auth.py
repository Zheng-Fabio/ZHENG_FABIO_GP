from flask import Blueprint, redirect, request, session, url_for
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIFY_CLIENT_ID = "1309983a0aef47d7bddd75184d399824"
SPOTIFY_CLIENT_SECRET = "9af4d25c0049484a8ff33a20d5127b21"
SPOTIFY_REDIRECT_URI = "https://5000-zhengfabio-zhengfabiogp-uxskculo3z7.ws-eu117.gitpod.io/callback"

auth_bp = Blueprint('auth', __name__)
sp_oauth = SpotifyOAuth(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    redirect_uri=SPOTIFY_REDIRECT_URI,
    scope="user-read-private user-library-read playlist-read-private"
)

@auth_bp.route('/')
def login():
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)

@auth_bp.route('/callback')
def callback():
    code = request.args.get('code')
    token_info = sp_oauth.get_access_token(code)
    session['token_info'] = token_info
    return redirect(url_for('home.home'))

@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))
