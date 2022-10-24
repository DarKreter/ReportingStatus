import os
import typing 
import functools
from client import client

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


async def run_blocking(blocking_func: typing.Callable, *args, **kwargs) -> typing.Any:
    func = functools.partial(blocking_func, *args, **kwargs)
    return await client.loop.run_in_executor(None, func)
