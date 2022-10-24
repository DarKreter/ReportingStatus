from pytube import YouTube, Playlist
import pandas as pd
from utils import get_files_from_path

# get list of video names from playlist (compatible with downloaded names)
def get_files_from_url(playlist_url, typee):
    playlist = Playlist(playlist_url)    
    
    file_list = []
    for video in playlist.videos:
        if typee == 'video':
            default_filename = video.streams.filter(only_video=True).order_by('resolution').desc()[0].default_filename
        elif typee == 'audio':
            default_filename = video.streams.filter(only_audio=True).order_by('abr').desc()[0].default_filename
            
        filename = default_filename.split('.')[0]
        
        file_list.append(filename)
    
    return file_list  

def check_playlist(url, path, typee):
    local_files = get_files_from_path(path, typee)
    yt_files = get_files_from_url(url, typee)
    
    local_files.sort()
    yt_files.sort()
    
    deleted_files = []
    
    for local_file in local_files:
        if local_file not in yt_files:
            deleted_files.append(local_file)
    
    return deleted_files

def get_missing_files():
    # Read watched playlists
    df = pd.read_csv('watchlist/playlists.csv', delimiter=';')
    mydict = df.to_dict(orient='list')

    missing_files = []
    for i in range(len(mydict['name'])):
        names = mydict['name']
        paths = mydict['path']
        urls = mydict['url']
        types = mydict['type']
        
        deleted = check_playlist(urls[i], paths[i], types[i])
        for x in deleted:
            missing_files.append( (names[i], x) )

    return missing_files

        