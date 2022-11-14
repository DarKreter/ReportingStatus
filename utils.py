import os
import subprocess
import typing 
import functools
from client import client

def executeBashCommand(bashCommand):
    process = subprocess.Popen(bashCommand, stdout=subprocess.PIPE)
    output, error = process.communicate()
    return output

def get_files_from_path(path, typee):
    if typee == 'video':
        ext = 'mkv'
    elif typee == 'audio':
        ext = 'ogg'
    
    files_list = []
    with os.scandir(path) as entries:
        for entry in entries:
            if entry.name[len(entry.name) - len(ext):] == ext:
                files_list.append(entry.name[:-(len(ext)+1)])
                
    exclude = path + '.exclude.txt'
    if os.path.isfile(exclude):
        file = open(exclude, 'r')
        lines = file.read().splitlines()
        file.close()
        
        for line in lines:
            if line in files_list:
                files_list.remove(line)
    
    return files_list


async def run_blocking(blocking_func: typing.Callable, *args, **kwargs) -> typing.Any:
    func = functools.partial(blocking_func, *args, **kwargs)
    return await client.loop.run_in_executor(None, func)
