from flask import Blueprint, render_template, redirect, session, url_for
import spotipy

home_bp = Blueprint('home', __name__)

@home_bp.route('/home')
def home():
    token_info = session.get('token_info', None)
    if not token_info:
        return redirect(url_for('auth.login'))

    sp = spotipy.Spotify(auth=token_info['access_token'])
    user_info = sp.current_user()
    playlists = sp.current_user_playlists()
    return render_template('home.html', user_info=user_info, playlists=playlists['items'])

@home_bp.route('/playlist/<playlist_id>')
def playlist_tracks(playlist_id):
    token_info = session.get('token_info', None)
    if not token_info:
        return redirect(url_for('auth.login'))

    sp = spotipy.Spotify(auth=token_info['access_token'])
    results = sp.playlist_tracks(playlist_id)
    tracks = results['items']
    return render_template('playlist_tracks.html', tracks=tracks)
