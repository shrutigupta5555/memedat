import asyncio
from email.mime import message
from random import randint
from tkinter import font
import discord 
from discord.embeds import Embed
# from discord import client
import time
from discord.ext import commands 
from PIL import Image
from PIL import ImageDraw, ImageFont

from dotenv import load_dotenv 
import os


emojis = ['1️⃣','2️⃣','3️⃣','4️⃣','5️⃣']

bot = commands.Bot(command_prefix='~')
load_dotenv()

@bot.command()
async def ping(ctx):
    await ctx.send('pong pong')



@bot.command()
async def start(ctx):
    await ctx.send('tag all the players playing the game 😏')

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel 

    members = await bot.wait_for("message", check=check)
    m = members.content.split(" ")
    captions = []
    r = randint(0,30)
    filepath = f"templates/{r}.jpg"
    await ctx.send("caption this amazing template [40 chars]\n", file=discord.File(filepath))
    i = 0 
    cap = []

    def check2(msg):
        if msg.author == bot.user:
            return False
        else:
            return True
    while i!=len(m):
        await ctx.send(f'send in your caption {m[i]}')
        lol = await bot.wait_for("message", check=check2)
        i+=1
        cap.append(lol.content)
        
    print(cap)
    s = ""
    count = 1
    for i in cap:
        s+=f"{count}: {i}\n"
        count+=1
    print(s)
    # msgid = ''
    message = await ctx.send(f'vote for your favorite caption\n{s}\n\nyouve 10 seconds')
    

    # print(f'id is {msgid}')
    for x in range(len(cap)):
        # print(f'x is {x}')
        if x>5:
            break
        await message.add_reaction(emojis[x])
    # msgid  =await  message.id
    most_voted = ""
    t = 10
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    
    # time.sleep(15)
    # msg = ctx.channel.fetch_message(msgid)
    # print(msg.reactions)
    # most_voted = max(message.reactions, key=lambda r: r.count)
    

    await ctx.send(f"The winner is caption number 2 !!")
    

    myFont = ImageFont.truetype("roboto.ttf", 40)
    im = Image.open(f'templates/{r}.jpg')
    W, H = im.size
    draw = ImageDraw.Draw(im)
    w, h = draw.textsize(cap[1], font=myFont)   
    draw.text(((W-w)/2,(H-70)), cap[1], fill="black", font=myFont)


    # myFont2 = ImageFont.truetype("roboto.ttf", 37)
    # draw = ImageDraw.Draw(im)
    # w, h = draw.textsize(cap[1], font=myFont2)   
    # draw.text(((W-w)/2,(H-60)), cap[1], fill="white", font=myFont2)
    

   
    im.save("car2.png")

    await ctx.send("the winning caption be like 😏", file=discord.File('car2.png')) 








bot.run(os.getenv('BOT_TOKEN'))