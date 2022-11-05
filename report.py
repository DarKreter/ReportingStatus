#!/usr/bin/python3
import discord
from client import client
from TOKEN import TOKEN

from utils import run_blocking, executeBashCommand
from functions import *
import globalVar
globalVar.init()


# Called when bot is ready 
@client.event
async def on_ready():
    # Debug info
    print('We have logged in as {0.user}'.format(client))
    
    # game status
    activity = discord.Activity(type=discord.ActivityType.watching, name="your server dying")
    await client.change_presence(status=discord.Status.online, activity=activity)    # client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='The Boys'))
    # Do everything here
    
    # Checking missing files in playlist
    await run_blocking(check_disks)
    await run_blocking(check_docker)
    await run_blocking(check_supervisor)
    await run_blocking(check_wireguard)
    await run_blocking(check_automatic_script_execution_time)
    await run_blocking(check_playlists)
    
    
    # globalVar.report_message.add_field(name="‎", value="", inline=False)

    # find channel to write
    for ch in client.get_guild(globalVar.GuildID).channels:
        if ch.id == globalVar.ChannelID:
            channel = ch
    # Write to channel

    await channel.send(content=globalVar._mention, embed=globalVar.report_message)
    if globalVar.attachment != "":
        await channel.send(file=discord.File(globalVar.attachment))
        command = ["rm", globalVar.attachment]
        executeBashCommand(command).decode("utf-8")

    # exit
    await client.close()


client.run(TOKEN)

