#!/usr/bin/python3
import discord
from client import client
from TOKEN import TOKEN

from utils import run_blocking
from functions import *
import globalVar
globalVar.init()


# Called when bot is ready 
@client.event
async def on_ready():
    # Debug info
    print('We have logged in as {0.user}'.format(client))
    
    # game status
    game = discord.Game("with your mom")
    await client.change_presence(status=discord.Status.online, activity=game)
    
    # Do everything here
    
    # Checking missing files in playlist
    await run_blocking(check_zfs_pools)
    await run_blocking(check_supervisor)
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

    # exit
    await client.close()


client.run(TOKEN)

