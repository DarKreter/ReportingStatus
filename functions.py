import discord
from unidecode import unidecode
from client import client
import globalVar
# from globalVar import *


# Called when bot is ready 
@client.event
async def on_ready():
    # Debug info
    print('We have logged in as {0.user}'.format(client))
    
    game = discord.Game("with your mom")
    await client.change_presence(status=discord.Status.online, activity=game)
    
    
    for ch in client.get_guild(globalVar.GuildID).channels:
        if ch.id == globalVar.ChannelID:
            channel = ch



    await channel.send(embed=globalVar.report_message)

    await client.close()
