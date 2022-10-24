import os

def get_files_from_path(path, typee):
    if typee == 'video':
        ext = 'mkv'
    elif typee == 'audio':
        ext = 'webm'
    
    files_list = []
    with os.scandir(path) as entries:
        for entry in entries:
            if entry.name[len(entry.name) - len(ext):] == ext:
                files_list.append(entry.name[:-(len(ext)+1)])
    return files_list