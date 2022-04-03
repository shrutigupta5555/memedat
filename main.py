import discord 
from discord.embeds import Embed 
# from discord import client
from discord.ext import commands 

from dotenv import load_dotenv 
import os

from deepface import DeepFace
import numpy as np 

from PIL import Image

bot = commands.Bot(command_prefix='!!')
load_dotenv()


#detect emotions 

def detect():
    analyze = DeepFace.analyze(img_path="m.png", actions=['emotion'])  #here the first parameter is the image we want to analyze #the second one there is the action
    return analyze['dominant_emotion']


@bot.command()
async def ping(ctx):
    await ctx.send('pong pong')


@bot.command()
async def prompt(ctx):
    await ctx.send('p')





bot.run(os.getenv('BOT_TOKEN'))