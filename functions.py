import discord
from unidecode import unidecode
from client import client


# Called when bot is ready 
@client.event
async def on_ready():
    # Debug info
    print('We have logged in as {0.user}'.format(client))
    
    game = discord.Game("with your mom")
    await client.change_presence(status=discord.Status.invisible, activity=game)


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    await message.channel.send(message.content)

    
