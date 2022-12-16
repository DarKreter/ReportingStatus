#!/usr/bin/python3
import discord
from client import client
from TOKEN import TOKEN

from utils import executeBashCommand
from globalVar import OwnID

from datetime import datetime

# Called when bot is ready 
@client.event
async def on_ready():
    # Debug info
    print('We have logged in as {0.user}'.format(client))
    
    # game status
    game = discord.Game("with your mom")
    await client.change_presence(status=discord.Status.idle, activity=game)
  

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    originalMess = message.content # originalMessage
    messLC = originalMess.lower()  # messageLowerCase
    messWWS = messLC.replace(" ", "").replace("\t", "").replace("\n", "") # messWithoutWhiteSpaces
    
    # Check if someone tagged BOTan
    if messLC.find('kilimanjaro-chan') != -1 or originalMess.find("<@{}>".format(OwnID)) != -1:
        await message.channel.send("Don't you worry, somehow I'm still alive...")

    elif messLC == "!report":
        print("{}:".format(datetime.now()))
        print("Request to do report from {}".format(client.user))
        command = ["supervisorctl", "start", "Kilimanjaro_report"]
        output = executeBashCommand(command).decode("utf-8")
        await message.channel.send(output)
        
    elif messLC == "!youtube_autodownload":
        print("{}:".format(datetime.now()))
        print("Request to do report from {}".format(client.user))
        command = ["supervisorctl", "start", "YouTube_autodownload"]
        output = executeBashCommand(command).decode("utf-8")
        await message.channel.send(output)
        
    elif messLC == "!smart_backup":
        print("{}:".format(datetime.now()))
        print("Request to do report from {}".format(client.user))
        command = ["supervisorctl", "start", "smart_backup"]
        output = executeBashCommand(command).decode("utf-8")
        await message.channel.send(output)
        

client.run(TOKEN)

