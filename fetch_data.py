import vk_api
from vk_api import audio
import loading_animation
import threading
import time
import sys
from script_info import vk_wrong_password, getting_vk_audio_message, getting_vk_playlist_music_message, getting_vk_albums_message, get_2fa_code

class ImportFromVk:

    """
    A class used to generate a VK session and gather data about user's audio from different sources,
    be it general audio or music in playlists.

    Attributes
    ------------
    vk_session: a variable used to authorize into VK via parental class' auth() method
    vk        : a variable for getting API methods available after authorizing
    vk_audio  : an instance of VkAudio class for accessing audio-related API methods


    Methods
    ------------
    get_audio() 
                getting list of user's audio on the main VK audio page with dropping out miscellanous
                information
    get_albums(target=False) 
                if target equals False, album data (such as hash_code, playlist id) will be used 
                to get list of audio of that album, otherwise, only album title saved
    get_album_audio(way='playlists')
                as mentioned in help section, there may be different arguments to be a source of audio data,
                hereby way is used as that source type
    """
    
    def __init__(self, vk_login, vk_password):
        self.vk_session = vk_api.VkApi(login=vk_login, password=vk_password, auth_handler=get_2fa_code)

        try:
            self.vk_session.auth()
        except vk_api.exceptions.BadPassword:
            sys.exit(vk_wrong_password())
            
        self.vk = self.vk_session.get_api()
        self.vk_audio = audio.VkAudio(self.vk_session)

    def get_audio(self):

        loading_animation.done = False
        t = threading.Thread(target=loading_animation.animate, args=(getting_vk_audio_message(), ))         
        t.start()

        general_audio = self.vk_audio.get()

        for list_item in general_audio:
          for i in ['url', 'track_covers', 'owner_id', 'id', 'duration']:
              del list_item[i]

        time.sleep(2)
        loading_animation.done = True
        t.join()

        return general_audio

    def get_albums(self, target=False):
        user_albums = self.vk_audio.get_albums()

        loading_animation.done = False
        t = threading.Thread(target=loading_animation.animate, args=(getting_vk_albums_message(), ))         
        t.start()

        if target == False:
            for list_item in user_albums:
                for i in ['url']:
                    del list_item[i]
        else:
            temp_albums = []
            for list_item in user_albums:
                temp_albums.append(list_item['title'])
            user_albums = temp_albums

        time.sleep(2)
        loading_animation.done = True
        t.join()
        
        return user_albums


    def get_album_audio(self, way='playlists'):
        album_audio = []
        temp_audio_list = []

        loading_animation.done = False
        t = threading.Thread(target=loading_animation.animate, args=(getting_vk_playlist_music_message(), ))         
        t.start()

        if way == 'playlists':
            for playlist in self.get_albums():
                temp_audio_list = self.vk_audio.get(owner_id=playlist['owner_id'], album_id=playlist['id'], access_hash=playlist['access_hash'])
                for track in temp_audio_list:
                    for i in ['url', 'track_covers', 'owner_id', 'id', 'duration']:
                        del track[i]
                album_audio.append(temp_audio_list)
        else:
            for playlist in self.get_albums():
                if playlist['title'] in way:                  
                    temp_audio_list = self.vk_audio.get(owner_id=playlist['owner_id'], album_id=playlist['id'], access_hash=playlist['access_hash'])
                    for track in temp_audio_list:
                        for i in ['url', 'track_covers', 'owner_id', 'id', 'duration']:
                            del track[i]                   
                    album_audio.append(temp_audio_list)

        time.sleep(2)
        loading_animation.done = True
        t.join()

        return album_audio