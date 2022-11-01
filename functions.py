import discord
from unidecode import unidecode
from client import client
import globalVar
from playlist_checker import get_missing_files
import utils


def check_playlists():
    missing_files = []
    # missing_files = [('「KDABAMV」', 'Akame Ga Kill - Natural 「KDABAMV」'), ('「KDABAMV」', 'Anime MIX - Surrender 「KDABAMV」')]
    # missing_files = get_missing_files()


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
    
def check_zfs_pools():
    command = ["./zpool_status.sh"]
    output = utils.executeBashCommand(command).decode("utf-8").split("\n")

    names = ""
    statuses = ""
    for i in range(0, len(output)-1, 2):
        names += "**{}**\n".format(output[i])
        statuses += "__{}__\n".format(output[i+1])

    globalVar.report_message.add_field(name="**ZFS STATUS & DISK USAGE:**", value="(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧", inline=False)
    globalVar.report_message.add_field(name="Pool name", value=names, inline=True)
    globalVar.report_message.add_field(name="Status", value=statuses, inline=True)
    globalVar.report_message.add_field(name="‎", value="‎", inline=True)
    
  
def check_diskspace():
    command = ["./disk_usage.sh"]
    output = utils.executeBashCommand(command).decode("utf-8").split("\n")
    # _value = "‎\n"
    names = ""
    sizes = ""
    useds = ""
    avails = ""
    perc_uses = ""
    for line in output[1:-1]:
        # remove empty elements of splitted string
        line = [x for x in line.split(" ") if x]
        names += "**{}**\n".format(line[0])
        sizes += "{}\n".format(line[1])
        useds += "{}\n".format(line[2])
        avails += "{}\n".format(line[3])
        perc_uses += "__{}__\n".format(line[4])
        
    names += "‎\n"
    # globalVar.report_message.add_field(name="**DISK USAGE:**", value="‎", inline=False)
    globalVar.report_message.add_field(name="Filesystem", value=names, inline=True)
    # globalVar.report_message.add_field(name="Size", value=sizes, inline=True)
    globalVar.report_message.add_field(name="Used", value=useds, inline=True)
    # globalVar.report_message.add_field(name="Avail", value="\n".join(avails), inline=True)
    globalVar.report_message.add_field(name="Use%", value=perc_uses, inline=True)
    
    
def check_disks():
    check_zfs_pools()
    check_diskspace()