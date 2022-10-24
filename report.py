#!/usr/bin/python3
from playlist_checker import check_playlists
from client import client
from TOKEN import TOKEN


# missing_files = check_playlists()

missing_files = [('playlista1', 'video1'), ('playlista2', 'video2')]

for file in missing_files:
    print(file)


client.run(TOKEN)


# List all files in folder
# List all files in yt playlist

# compare

# Report on discord message