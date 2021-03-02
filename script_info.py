import sys

set_language = 'RU' #'RU'
warning = 'set_language contains inappropriate symbols, it must be either \'EN\' or \'RU\''

def greetings():
    if set_language == 'EN':
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        print("    The following script is to help you transfer/copy your audio from VK")
        print("(playlists are supported) to Spotify with creating corresponding playlists.")
        print("   For more detailed information type \'help', otherwise press any button.")
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n")

    elif set_language == 'RU':     
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        print("Данный скрипт осуществляет перенос аудио из вконтакте (содержимое плейлистов")
        print(" в том числе) на платформу Spotify с созданием соответствующих плейлистов.")
        print("      Для более подробной информации о работе скрипта введите \'help'.")
        print("            В противном случае нажмите любую клавишу.")
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n")
    else:
        sys.exit(warning)

def help():
    if set_language == 'EN':
        print("You can specify the source from which to take audio:")
        print(r"    - general (audio from main page of vk.com/audio{user_name}")
        print("    - playlists (audio from all user's added playlists")
        print(r"    - {playlist name} specified playlist will be selected as source.")
        print("      (you can also use several playlists as input using")
        print("      comma and consequent space symbol, for example: ")
        print("      Music for good sleep, WorkOut, Blood on the Tracks (1975)\n")
        print("      Important: make sure there's no name conflicts and VK playlists' names")
        print("      differ from ones in Spotify!\n")
    elif set_language == 'RU':
        print("Вы можете указать источник, из которого брать аудиозапии:")
        print("    - general (аудиозаписи пользователя с главной страницы)")
        print("    - playlists (аудиозаписи всех плейлистов пользователя)")
        print(r"    - {название плейлиста} указанный плейлист будет выбран в качестве источника.")
        print("      (вы также можете указать несколько плейлистов в качестве входных данных,")
        print("      указав их через запятую с пробелом, например: ")
        print("      Музыка для сна, Для тренировок\n")
        print("      Предупреждение: Убедитесь, что названия плейлистов VK отличаются от названий")
        print("      плейлистов в Spotify, чтобы избежать конфликта имён!\n")
    else:
        sys.exit(warning)

def get_vk():
    vk_login = vk_password = source = None

    if set_language == 'EN':
        print("In the following order, enter VK login, VK password and audio source")
        vk_login = input("Your VK login: ")
        vk_password = input("Your VK password: ")
        source = list(input("Audio source: ").split(", "))
    elif set_language == 'RU':
        print("В следующем порядке введите логин VK, пароль VK и источник, из которого брать аудио")
        vk_login = input("Ваш логин VK: ")
        vk_password = input("Ваш пароль VK: ")
        source = list(input("Источник аудио: ").split(", "))
    else:
        sys.exit(warning)
    print()
    
    return vk_login, vk_password, source

def vk_wrong_password():
    if set_language == 'RU':
        return "Неверный логин или пароль!"
    elif set_language == 'EN':
        return  "Wrong login or password!"

def get_spotify():
    client_id = client_secret = None

    if set_language == 'EN':
        print("Enter your Client-ID and Client-secret of your spotfy app")
    elif set_language == 'RU':
        print("Введите Client-ID и Client-secret вашего спотифай приложения")
    else:
        sys.exit(warning)

    client_id = input("Client-ID: ")
    client_secret = input("Client-secret: ")
    print()
    return client_id, client_secret

def spotify_warnings(user_playlist='default'):
    playlist_name = None
    if user_playlist == 'default':
        playlist_name = 'General audio from VK' 
    else:
        playlist_name = user_playlist
        print(playlist_name)

    if set_language == 'EN':
        print("Playlist named '{0}' has been created before!".format(playlist_name))
    elif set_language == 'RU':
        print("Плейлист с названием '{0}' уже существует!".format(playlist_name))
    else:
        sys.exit(warning)

def script_description():
    if set_language == 'RU':
        return 'Данный плейлист был создан с использованием скрипта "VKtoSpotify"'
    else:
        return 'This playlist was created using "VKtoSpotify" script' 

def getting_vk_audio_message():
    if set_language == 'RU':
        return "Собираем информацию об аудио"
    elif set_language == 'EN':
        return "Gathering user's audio data information"
    else:
        sys.exit(warning)

def getting_vk_playlist_music_message():
    if set_language == 'RU':
        return "Собираем информацию об аудиозаписях в плейлистах" 
    elif set_language == 'EN':
        return "Gathering information about user playlists' audio"
    else:
        sys.exit(warning)

def getting_vk_albums_message():
    if set_language == 'RU':
        return "Собираем информацию о плейлистах пользователя"
    elif set_language == 'EN':
        return "Gathering information about user's playlists"
    else:
        sys.exit(warning)

def adding_music_to_sp_playlists():
    if set_language == 'RU':
        return "Создаём плейлисты в Spotify и добавляем в них аудио"
    elif set_language == 'EN':
        return "Creating Spotify playlists and adding audio to them"
    else:
        sys.exit(warning)

def animation_finihsed():
    if set_language == 'RU':
        return "Готово!"
    elif set_language == 'EN':
        return "Done!"
    else:
        sys.exit(warning)