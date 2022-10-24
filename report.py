#!/usr/bin/python3
import datetime
import random
from playlist_checker import check_playlists
from functions import *
from TOKEN import TOKEN
from client import client
from globalVar import *
globalVar.init()


# General config for bot message
globalVar.report_message = discord.Embed(   title=globalVar._title, 
                                            description=globalVar._description,
                                            color=globalVar._color,
                                            timestamp=datetime.datetime.now(),
                                            url = "https://www.kilimandzaro.com")
globalVar.report_message.set_image(url = random.choice(globalVar._love_gifs))
globalVar.report_message.set_footer(text = globalVar._footer)


# missing_files = check_playlists()

# missing_files = [('「KDABAMV」', 'Akame Ga Kill - Natural 「KDABAMV」'), ('「KDABAMV」', 'Anime MIX - Surrender 「KDABAMV」')]
missing_files = []


if len(missing_files) == 0:
    _value = "__Everything is up to date!__ （＾ω＾）"
else:
    _value = "Some videos are **__missing__**: (๑˃̣̣̥⌓˂̣̣̥)\n\n"
    for playlist, title in missing_files:
        _value+="'**{}**' from '**{}**'!\n".format(title,playlist)
        
    
globalVar.report_message.add_field(name="**YOUTUBE PLAYLISTS STATUS:**", value=_value, inline=False)
# globalVar.report_message.add_field(name="‎", value="", inline=False)


client.run(TOKEN)

