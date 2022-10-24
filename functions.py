import discord
from unidecode import unidecode
from client import client
from globalVar import *


# Called when bot is ready 
@client.event
async def on_ready():
    # Debug info
    print('We have logged in as {0.user}'.format(client))
    
    game = discord.Game("with your mom")
    await client.change_presence(status=discord.Status.online, activity=game)
    
    
    for ch in client.get_guild(GuildID).channels:
        if ch.id == ChannelID:
            channel = ch

    await channel.send("test")
    
    # embedVar = discord.Embed(title="tytul", description="123", color=0xe0a2e6)
# if source != "":
#     embedVar.add_field(name="Sosik:", value="source", inline=False)
# embedVar.set_image(url = "https://www.cukierniasamanta.pl/sklep/wp-content/uploads/2020/03/paczek.jpg")
    
# await message.channel.send(embed=embedVar)

# await message.channel.send(embed=embedVar)

    
