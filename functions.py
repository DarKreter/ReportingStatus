import discord
from unidecode import unidecode
from client import client
import globalVar
from playlist_checker import get_missing_files
import utils


def check_playlists():
    # missing_files = get_missing_files()

    # missing_files = [('「KDABAMV」', 'Akame Ga Kill - Natural 「KDABAMV」'), ('「KDABAMV」', 'Anime MIX - Surrender 「KDABAMV」')]
    missing_files = []

    if len(missing_files) == 0:
        _value = "__Everything is up to date!__ （＾ω＾）"
    else:
        _value = "Some videos are **__missing__**: (๑˃̣̣̥⌓˂̣̣̥)\n\n"
        for playlist, title in missing_files:
            _value+="'**{}**' from '**{}**'!\n".format(title,playlist)
            
    # If its too long for field content
    if len(_value) > 1024:
        # write missing amv to file
        globalVar.attachment = "missing_amv.txt"
        f = open(globalVar.attachment, "w")
        f.write(_value.replace("*", ""))
        f.close()
        _value = "Some videos are **__missing__**: (๑˃̣̣̥⌓˂̣̣̥)\n\n"
        _value+= "[[*Too many missing titles to display in one message, linking attachment...*]]"
        
    globalVar.report_message.add_field(name="**YOUTUBE PLAYLISTS STATUS:**", value=_value, inline=False)
    
def check_zfs_pools():
    command = ["./zpool_status.sh"]
    output = utils.executeBashCommand(command).decode("utf-8").split("\n")
    # _value = "‎\n"
    _value = ""
    for i in range(0, len(output)-1, 2):
        _value+="**{}**: __{}__\n".format(output[i], output[i+1])
    _value += "‎\n"
    globalVar.report_message.add_field(name="**ZFS POOLS STATUS:**", value=_value, inline=False)

def check_automatic_script_execution_time():
    scripts = [("YouTube autodownload", "k8d.server.yt_autodownload/log.txt"), 
               ("Anime smart backup", "k8d.server.smart_backup/log.txt")]
    _value = ""
    
    for name, script in scripts:
        command = "stat -c '%y' /home/kretes/{}".format(script).split(" ")
        output = utils.executeBashCommand(command).decode("utf-8").split('.')[0][1:]
        _value+="**{}**: *{}*\n".format(name, output)
        
    _value += "‎\n"
    globalVar.report_message.add_field(name="**Last execution of automatic scripts:**", value=_value, inline=False)

    
def check_supervisor():
    command = ["supervisorctl", "status"]
    output = utils.executeBashCommand(command).decode("utf-8").split("\n")
    # _value = "‎\n"
    _value = ""
    for line in output[:-1]:
        # remove empty elements of splitted string
        line = [x for x in line.split(" ") if x]
        name = line[0]
        state = line[1]
        line.pop(0)
        line.pop(0)
        
        _value+="**{}**: __{}__, {}\n".format(name, state, " ".join(line))
    _value += "‎\n"
    globalVar.report_message.add_field(name="**SUPERVISOR STATUS:**", value=_value, inline=False)
    
    