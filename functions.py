import discord
from unidecode import unidecode
from client import client
import globalVar
from playlist_checker import get_missing_files


def check_playlists():
    missing_files = get_missing_files()

    # missing_files = [('「KDABAMV」', 'Akame Ga Kill - Natural 「KDABAMV」'), ('「KDABAMV」', 'Anime MIX - Surrender 「KDABAMV」')]
    # missing_files = []

    if len(missing_files) == 0:
        _value = "__Everything is up to date!__ （＾ω＾）"
    else:
        _value = "Some videos are **__missing__**: (๑˃̣̣̥⌓˂̣̣̥)\n\n"
        for playlist, title in missing_files:
            _value+="'**{}**' from '**{}**'!\n".format(title,playlist)
            
        
    globalVar.report_message.add_field(name="**YOUTUBE PLAYLISTS STATUS:**", value=_value, inline=False)
    
