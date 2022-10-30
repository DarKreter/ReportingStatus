import datetime
import discord
import random
from utils import executeBashCommand

GuildID = 698673052447145986
ChannelID = 1034119438577971220
BakuganID = 324627270478200832
MinetaID = 369551883817320448

_title = "**Here is report of my __current state__:**"
_footer = "Send with love to my master\n"
_description = ""
_mention = "Hear me out! <@{}> <@{}>\n‎".format(BakuganID, MinetaID)
_color = 0xe0a2e6


_love_gifs = ["https://media.tenor.com/45Z2kLVzfNsAAAAM/ily-i-love-you.gif",
              "https://media.tenor.com/rFomhnWNTYwAAAAC/i-love-you-love.gif",
              "https://i.gifer.com/6Sam.gif",
              "https://media.tenor.com/kZq4mYF5bicAAAAC/heart-anime.gif",
              "https://media.tenor.com/ZYUbvoVXwQsAAAAM/love-you.gif",
              "https://media.tenor.com/DZll3gcSP04AAAAM/love.gif",
              "https://media.tenor.com/Gf7MgJEnHsIAAAAC/anime-love.gif",
              "https://media.tenor.com/3PKwjqz9c_QAAAAM/anime-love-u-anime-girl.gif",
              "https://media.tenor.com/OV5ltVkjtooAAAAC/love-you-happy.gif",
              "https://media.tenor.com/RzmW-BtosV4AAAAC/show-by-rock-cyan-hijirikawa.gif",
              "https://pa1.narvii.com/6699/626d9360aa957f3961fc97b530cc4fb4ac3ef1dd_hq.gif",
              "https://i.pinimg.com/originals/f2/80/5f/f2805f274471676c96aff2bc9fbedd70.gif",
              "https://media4.giphy.com/media/LML5ldpTKLPelFtBfY/200.gif?cid=82a1493buun1gq9vct6gpzrzmf0xqajph86el2qm2ahl333g&rid=200.gif&ct=g",
              "https://i.imgur.com/w2AsgSW.gif?noredirect",
              "https://media.tenor.com/FSLoxixwzPkAAAAd/monika-ddlc.gif"]


def init():    
    global attachment
    attachment = ""
    global report_message
    command = ["uptime", "--pretty"]
    output = executeBashCommand(command).decode("utf-8").split("\n")[0][3:]
    _description = "With uptime: *{}*\n‎\n".format(output)
    
    report_message = discord.Embed(   title=_title, 
                                                description=_description,
                                                color=_color,
                                                timestamp=datetime.datetime.now(),
                                                url = "https://www.kilimandzaro.com")
    report_message.set_image(url = random.choice(_love_gifs))
    report_message.set_footer(text = _footer)