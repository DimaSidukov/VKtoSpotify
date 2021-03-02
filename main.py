from fetch_data import ImportFromVk
from create_playlist import LoadToSpotify
import time
import itertools
import script_info

def main():
    script_info.greetings()
    help = input()
    if help == 'help':
        script_info.help()

    vk_log, vk_pass, vk_fetch = script_info.get_vk()
    vk_audio = []
    vk_session = ImportFromVk(vk_login=vk_log, vk_password=vk_pass)

    spotify_client_id, spotify_client_secret = script_info.get_spotify()
    spotify_session = LoadToSpotify(client_id=spotify_client_id, client_secret=spotify_client_secret)

    if vk_fetch[0] == 'general':
        vk_audio = vk_session.get_audio()
        spotify_session.add_music(track_names=vk_audio)

    elif vk_fetch[0] == 'all':
        vk_audio.append(vk_session.get_audio())
        tmp_list = vk_session.get_album_audio()
        for temp in tmp_list:
            vk_audio.append(temp)
        del tmp_list

        vk_playlist_names = ['General audio from VK', *vk_session.get_albums(True)]  
        spotify_session.add_music(track_names=vk_audio, playlists=vk_playlist_names)

    elif vk_fetch[0] == 'playlists':
        vk_audio = vk_session.get_album_audio()
        vk_playlist_names = vk_session.get_albums(True)
        spotify_session.add_music(track_names=vk_audio, playlists=vk_playlist_names)

    else:
        vk_audio = vk_session.get_album_audio(vk_fetch)
        spotify_session.add_music(track_names=vk_audio, playlists=vk_fetch)

if __name__ == "__main__":
    main()