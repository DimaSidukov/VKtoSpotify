import spotipy
from spotipy.oauth2 import SpotifyOAuth
import loading_animation
import threading
import time
from script_info import spotify_warnings, script_description, adding_music_to_sp_playlists

script_description = script_description()

class LoadToSpotify:

    """
    This class is used to create new spotify playlists and upload music to these playlists.

    Attributes
    ------------
    sp      : spotify authorization to get access to the profile with a restriction of modifying solely public information
    user_id : a string storing ID of user, that is essential for script operation

    Methods
    ------------
    add_music(track_names, playlists='None')
            If playlists equals 'None' then there's new playlist created (with name of 'General audio from VK'),
            aftermath, audio data from track_names used to find corresponding tracks and add them to the fresh playlist.
            playlists argument can also recieve name of playlists to create, so then track_names of particual VK albums will be
            added to these playlists.

    get_user_playlists()
            The following method returns list of Spotify playlists to avoid name conflict with VK audio albums 
    """

    def __init__(self, client_id, client_secret):
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, 
                                                            client_secret=client_secret,
                                                            redirect_uri='http://localhost:8888/callback',
                                                            scope='playlist-modify-public'))
        self.user_id = self.sp.me()['id']
                                               
    def add_music(self, track_names, playlists='None'):

        loading_animation.done = False
        t = threading.Thread(target=loading_animation.animate, args=(adding_music_to_sp_playlists(), ))         
        t.start()

        if playlists == 'None':
            gen_playlist_name = 'General audio from VK'
            if gen_playlist_name not in self.get_user_playlists():
                playlist = self.sp.user_playlist_create(user=self.user_id, name=gen_playlist_name, public=True, collaborative=False, description=script_description)
                for track in track_names:
                    result = self.sp.search(q=track['artist'] + ' ' + track['title'], limit=1)
                    try:
                        self.sp.playlist_add_items(playlist['id'], [result['tracks']['items'][0]['id']])
                    except:
                        pass
            else:
                spotify_warnings()
        
        else:
            for user_playlist, track_list in zip(playlists, track_names):
                if user_playlist not in self.get_user_playlists():
                    spot_playlist = self.sp.user_playlist_create(user=self.user_id, name=user_playlist, public=True, collaborative=False, description=script_description)
                    for track in track_list:
                        result = self.sp.search(q=track['artist'] + ' ' + track['title'], limit=1)
                        try:
                            self.sp.playlist_add_items(spot_playlist['id'], [result['tracks']['items'][0]['id']])
                        except:
                            pass
                else:
                    spotify_warnings(user_playlist)

        time.sleep(2)
        loading_animation.done = True
        t.join()

    def get_user_playlists(self):
        playlists = self.sp.current_user_playlists()
        user_playlists = []
        while playlists:
            for playlist in playlists['items']:
                user_playlists.append(playlist['name'])
            if playlists['next']:
                playlists = self.sp.next(playlists)
            else:
                playlists = None
        return user_playlists