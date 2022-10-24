#!/usr/bin/python3
import discord
from client import client
from TOKEN import TOKEN

from functions import check_playlists
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
    await check_playlists()

    # globalVar.report_message.add_field(name="‎", value="", inline=False)

    # find channel to write
    for ch in client.get_guild(globalVar.GuildID).channels:
        if ch.id == globalVar.ChannelID:
            channel = ch
    # Write to channel
    await channel.send(embed=globalVar.report_message)

    # exit
    await client.close()


client.run(TOKEN)

