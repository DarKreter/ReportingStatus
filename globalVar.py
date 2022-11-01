import datetime
import discord
import random
from utils import executeBashCommand

GuildID = 698673052447145986
ChannelID = 1034119438577971220
BakuganID = 324627270478200832
MinetaID = 369551883817320448

_title = "**Here is report of my __current state__:**"
_footer = "Send with love to my master"
_description = ""
_mention = "Hear me out! <@{}> <@{}>\n‎".format(BakuganID, MinetaID)
_color = 0xe0a2e6


_love_gifs = [  "https://media.tenor.com/45Z2kLVzfNsAAAAM/ily-i-love-you.gif",
                "https://media.tenor.com/ZYUbvoVXwQsAAAAM/love-you.gif",
                "https://media.tenor.com/DZll3gcSP04AAAAM/love.gif",
                "https://media.tenor.com/Gf7MgJEnHsIAAAAC/anime-love.gif",
                "https://media1.giphy.com/media/FNmjncTKQvsCRiX7sH/giphy.gif?cid=790b7611e6d825571caac5a04058c82b9182627c76f753eb&rid=giphy.gif&ct=g",
                "https://media0.giphy.com/media/ChBqKOyv46K4rjjRzF/giphy.gif?cid=790b7611b85166eac1e44c57b451b60602225dd0ac5b1c02&rid=giphy.gif&ct=g",
                "https://media4.giphy.com/media/LML5ldpTKLPelFtBfY/200.gif?cid=82a1493buun1gq9vct6gpzrzmf0xqajph86el2qm2ahl333g&rid=200.gif&ct=g",
                "https://media0.giphy.com/media/jljN26bOX0EpLTCr2C/giphy.gif?cid=790b76116ef73cdf66a9f469282024a2b997b925f1508a14&rid=giphy.gif&ct=g",
                "https://media0.giphy.com/media/jA2t5eQyzgFKZnUKI9/giphy.gif?cid=790b7611cd66524ee31cfe930e4f0daa6794c554d6713983&rid=giphy.gif&ct=g",
                "https://media3.giphy.com/media/2kKsU8jKLMtFvyYOVk/giphy.gif?cid=790b761131d2f9112dd13578108c8d245d4c256a7afdfb37&rid=giphy.gif&ct=g",
                "https://media2.giphy.com/media/5XhOpxXNSU5J2oEyRO/giphy.gif?cid=790b7611ed4c2d866719e6f10c2af309e0701ba440fb3694&rid=giphy.gif&ct=g",
                "https://media0.giphy.com/media/s8Ie6HLTDgnHIzv1xU/giphy.gif?cid=790b7611dcf4928715399d43eb94c256a5ab67060f62a6ae&rid=giphy.gif&ct=g",
                "https://media0.giphy.com/media/IdAGaCAYR3UsDn3waC/giphy.gif?cid=790b761166ec7469b1d0d4e0deca6210e212ee7bf4a2546b&rid=giphy.gif&ct=g",
                "https://media4.giphy.com/media/Jool6IwWMgh6C3B0og/giphy.gif?cid=790b761168ca28871243dbce765e4b11bb7a67704f37176a&rid=giphy.gif&ct=g",
                "https://media.tenor.com/3PKwjqz9c_QAAAAM/anime-love-u-anime-girl.gif"]



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