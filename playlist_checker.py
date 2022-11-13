from pytube import YouTube, Playlist
import pandas as pd
from utils import get_files_from_path
import multiprocessing


# get list of video names from playlist (compatible with downloaded names)
def get_files_from_url(playlist_url, typee):
    playlist = Playlist(playlist_url)    
    
    threads = []
    manager = multiprocessing.Manager()
    file_list = manager.list()
    lock = multiprocessing.Lock()
    
    for url in playlist.video_urls:
        video = YouTube(url, use_oauth=True, allow_oauth_cache=True)
        process = multiprocessing.Process(target=check_single_url, args=(video, typee, file_list,lock,))
        process.start()
        threads.append(process)
        
    for process in threads:
        process.join()
        
    return file_list  

def check_single_url(video, typee, file_list, lock):
    try:
        if typee == 'video':
            df = video.streams.filter(only_video=True).order_by('resolution').desc()[0].default_filename
        elif typee == 'audio':
            df = video.streams.filter(only_audio=True).order_by('abr').desc()[0].default_filename
            
        filename = df.split('.')[0]
        
        with lock:
            file_list.append(filename)
            
    except Exception as e:
            print('Error proccessing this video!')
            print(e)
    
    
    

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
        
        # Check only video playlists, because for now, we have video or video + audio playlists (zero only audio)
        if types[i] == 'audio':
            continue
        
        deleted = check_playlist(urls[i], paths[i], types[i])
        for x in deleted:
            missing_files.append( (names[i], x) )

    return missing_files

        